"""Arma el visor interactivo del modelo (diagrama animado por procesos, notas y últimos cambios).

Uso (desde la raíz del vault):
    python3 04_Modelado_DB/Visor_Modelo/construir_visor.py            # usa el bd.uml de la versión vigente
    python3 04_Modelado_DB/Visor_Modelo/construir_visor.py ruta/bd.uml

Entradas (todas en esta carpeta, salvo el bd.uml):
    template.html           la página (HTML, CSS y JS) con el marcador __DATA__
    visor_config.json       procesos, subprocesos y campos/tablas eliminados con su motivo
    historial_cambios.json  resumen de cambios por versión (lo muestra el botón "Cambios")
Salidas:
    salida/modelo_la_coca.html                     contenido para publicar el artifact (sin <html>/<head>)
    <versión vigente>/Visor_Interactivo/modelo_la_coca_v4.html   página completa para abrir sin conexión
"""
import json, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(AQUI))
MR = os.path.join(ROOT, "04_Modelado_DB", "Modelo_Relacional")
VER = re.compile(r"^v(\d+)_(\d{4}-\d{2}-\d{2})$")
ESQ = ('<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,'
       'initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0;font:14px system-ui}'
       '[hidden]{display:none!important}</style></head><body>')


def vigente():
    vs = sorted((int(m.group(1)), d) for d in os.listdir(MR) if (m := VER.match(d)))
    return os.path.join(MR, vs[-1][1])


def parsear(uml):
    s = open(uml, encoding="utf-8").read()
    s = re.sub(r"^Records[^{]*\{.*?^\}", "", s, flags=re.M | re.S)
    ver = re.search(r"Modelo Relacional \(v([\d.]+)", s)
    tablas, refs = {}, []
    for m in re.finditer(r"^Table (\w+) \{(.*?)^\}", s, re.M | re.S):
        name, body = m.group(1), m.group(2)
        note = re.search(r"\n  Note: '(.*)'", body)
        pkcomp = re.search(r"\((\w+), (\w+)\) \[pk\]", body)
        cols = []
        for line in body.split("\n"):
            mm = re.match(r"  (\w+) (\"[^\"]+\"|\w+)\s*(\[(.*)\])?\s*$", line)
            if not mm or mm.group(1) in ("Note", "indexes"):
                continue
            attrs = mm.group(4) or ""
            sin_nota = re.sub(r"note: '[^']*'", "", attrs)
            cnote = re.search(r"note: '([^']*)'", attrs)
            cols.append({"n": mm.group(1), "t": mm.group(2).strip('"'),
                         "pk": "pk" in sin_nota or bool(pkcomp and mm.group(1) in pkcomp.groups()),
                         "nn": "not null" in attrs, "u": bool(re.search(r"\bunique\b", sin_nota)),
                         "note": cnote.group(1) if cnote else ""})
        tablas[name] = {"cols": cols, "note": note.group(1) if note else ""}
    for m in re.finditer(r"^Ref: (\w+)\.(\w+) ([<>-]) (\w+)\.(\w+)", s, re.M):
        refs.append({"from": m.group(1), "fc": m.group(2), "k": m.group(3), "to": m.group(4), "tc": m.group(5)})
    for t in tablas:
        for c in tablas[t]["cols"]:
            c["fk"] = any(r["from"] == t and r["fc"] == c["n"] for r in refs)
    enums = {m.group(1): re.findall(r"^\s+(\w+)", m.group(2), re.M)
             for m in re.finditer(r"^Enum (\w+) \{(.*?)^\}", s, re.M | re.S)}
    grupos = [(m.group(1), m.group(2).split()) for m in re.finditer(r"^TableGroup (\w+) \{(.*?)^\}", s, re.M | re.S)]
    return (ver.group(1) if ver else "?"), tablas, refs, enums, grupos


def main():
    uml = sys.argv[1] if len(sys.argv) > 1 else os.path.join(vigente(), "bd.uml")
    version, tablas, refs, enums, grupos = parsear(uml)
    cfg = json.load(open(os.path.join(AQUI, "visor_config.json"), encoding="utf-8"))
    hist = json.load(open(os.path.join(AQUI, "historial_cambios.json"), encoding="utf-8"))
    nombres = {p["code"]: p for p in cfg["procesos"]}
    procesos = []
    for g, ts in grupos:
        code = g.split("_")[0]
        p = nombres.get(code, {"name": g, "desc": ""})
        procesos.append({"code": code, "name": p["name"], "desc": p["desc"], "tables": ts})
    faltan = set(tablas) - {t for _, ts in grupos for t in ts}
    if faltan:
        raise SystemExit(f"Tablas sin proceso (TableGroup): {sorted(faltan)}")
    for t, v in tablas.items():
        v["sub"] = cfg["subprocesos"].get(t, "—")
        v["removed"] = cfg["campos_eliminados"].get(t, [])
    M = {"version": version, "procesos": procesos, "tables": tablas, "refs": refs, "enums": enums,
         "tablas_eliminadas": cfg.get("tablas_eliminadas", []), "cambios": hist["versiones"]}
    tpl = open(os.path.join(AQUI, "template.html"), encoding="utf-8").read()
    html = tpl.replace("__DATA__", json.dumps(M, ensure_ascii=False))
    os.makedirs(os.path.join(AQUI, "salida"), exist_ok=True)
    open(os.path.join(AQUI, "salida", "modelo_la_coca.html"), "w", encoding="utf-8").write(html)
    destino = os.path.join(os.path.dirname(uml), "Visor_Interactivo")
    os.makedirs(destino, exist_ok=True)
    open(os.path.join(destino, "modelo_la_coca_v4.html"), "w", encoding="utf-8").write(ESQ + html + "</body></html>")
    print(f"Visor v{version}: {len(tablas)} tablas, {len(refs)} relaciones, {len(procesos)} procesos, "
          f"{len(hist['versiones'])} versiones en el historial de cambios.")


if __name__ == "__main__":
    main()
