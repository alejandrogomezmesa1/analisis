"""Arma el visor interactivo del modelo y el diagrama ER (SVG) a partir del bd.uml.

REGLA DE ORO: cada vez que se toca un bd.uml se corre este script. Así el visor y el diagrama ER
nunca quedan desactualizados (el hook pre-commit del repo lo corre solo).

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
    04_Modelado_DB/Diagramas/vN_AAAA-MM-DD/LaCocaDiagramDB.svg      diagrama ER: versión nueva si el bd.uml cambió
Requisito para el SVG: `npm install` una vez en esta carpeta (instala @viz-js/viz).
"""
import datetime, html as H, json, os, re, subprocess, sys

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


DG = os.path.join(ROOT, "04_Modelado_DB", "Diagramas")
COLORES = ["#EEF2FA", "#F1ECF8", "#E6F4F1", "#FBF3E4", "#FBEFF0", "#F0F5F2", "#FBEDE8", "#EAF3FB", "#F6F1E7", "#EEF6EC", "#F8ECF3"]


def dot_er(version, tablas, refs, procesos):
    fk = {(r["from"], r["fc"]) for r in refs}
    L = ['digraph ER {', 'graph [rankdir=LR, newrank=true, splines=true, fontname="Helvetica", fontsize=22, labelloc=t, '
         'nodesep=0.3, ranksep=1.0, pad=0.4,',
         f' label=<<B>JackSoft - Modelo Relacional bd.uml v{version} ({len(tablas)} tablas, {len(refs)} relaciones, '
         f'{len(procesos)} procesos en orden del flujo)</B><BR/> >];',
         'node [shape=plain, fontname="Helvetica"]; edge [fontname="Helvetica", fontsize=8, color="#6B7280", arrowtail=tee, dir=both];']
    for k, p in enumerate(procesos):
        L.append(f'subgraph cluster_{k} {{ label=<<B>{H.escape(p["code"] + ". " + p["name"])}</B>>; style="rounded,filled"; '
                 f'fillcolor="{COLORES[k % len(COLORES)]}"; color="#B8C0CC"; fontsize=13;')
        for t in p["tables"]:
            filas = "".join(
                f'<TR><TD ALIGN="LEFT"><FONT POINT-SIZE="9">{"<B>PK</B>&#160;" if c["pk"] else ("<I>FK</I>&#160;" if (t, c["n"]) in fk else "")}'
                f'{H.escape(c["n"])}</FONT></TD><TD ALIGN="LEFT"><FONT POINT-SIZE="9" COLOR="#6B7280">{H.escape(c["t"])}</FONT></TD></TR>'
                for c in tablas[t]["cols"])
            L.append(f'{t} [label=<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="2" BGCOLOR="#FFFFFF" COLOR="#5B6573">'
                     f'<TR><TD COLSPAN="2" BGCOLOR="#1E293B"><FONT COLOR="#FFFFFF"><B>{t}</B></FONT></TD></TR>{filas}</TABLE>>];')
        L.append("}")
    for r in refs:
        L.append(f'{r["to"]} -> {r["from"]} [label="{r["fc"]}", arrowhead={"tee" if r["k"] == "-" else "crow"}];')
    L.append("}")
    return "\n".join(L)


def diagrama_er(version, tablas, refs, procesos):
    """Crea una versión nueva del diagrama ER si la última no corresponde a esta versión del bd.uml."""
    vs = sorted((int(m.group(1)), d) for d in os.listdir(DG) if (m := VER.match(d)))
    ultima = os.path.join(DG, vs[-1][1], "LaCocaDiagramDB.svg") if vs else None
    if ultima and os.path.exists(ultima) and f"bd.uml v{version} (" in open(ultima, encoding="utf-8").read():
        return f"Diagrama ER: {vs[-1][1]} ya es de bd.uml v{version}"
    if not os.path.isdir(os.path.join(AQUI, "node_modules", "@viz-js")):
        return "Diagrama ER: falta 'npm install' en 04_Modelado_DB/Visor_Modelo (no se generó el SVG)"
    destino = os.path.join(DG, f"v{(vs[-1][0] if vs else 0) + 1}_{datetime.date.today().isoformat()}")
    os.makedirs(destino, exist_ok=True)
    dot = os.path.join(AQUI, "salida", "er.dot")
    open(dot, "w", encoding="utf-8").write(dot_er(version, tablas, refs, procesos))
    subprocess.run(["node", os.path.join(AQUI, "render_svg.mjs"), dot, os.path.join(destino, "LaCocaDiagramDB.svg")], check=True)
    return f"Diagrama ER: versión nueva {os.path.basename(destino)} (bd.uml v{version}) — anótala en el CHANGELOG"


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
    if not any(v.get("version") == version for v in hist["versiones"]):
        print(f"AVISO: historial_cambios.json no tiene una entrada para la v{version}: agrégala (versión, fecha y cambios).")
    print(diagrama_er(version, tablas, refs, procesos))


if __name__ == "__main__":
    main()
