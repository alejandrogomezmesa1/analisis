#!/usr/bin/env python3
"""Chat entre Claude Omar (frontend) y Claude Alejo (documentación).

Los mensajes viven en  mensajes/NNN_AAAA-MM-DD_HHMM_<autor>.txt  (uno por archivo, nunca se editan).
Este script arma la vista  00_CHAT.txt  con burbujas: Claude Omar a la izquierda, Claude Alejo a la derecha.

Uso (desde cualquier carpeta):
    python3 _herramientas/chat.py              regenera 00_CHAT.txt
    python3 _herramientas/chat.py siguiente "Claude Alejo"
                                               imprime el nombre y el encabezado del próximo mensaje

Formato de un mensaje (encabezado, una línea en blanco o '---', y el texto):

    id: 008
    de: Claude Alejo                 (Claude Omar | Claude Alejo)
    fecha: 2026-11-04 03:20          (hora de Colombia, 24 h)
    tipo: mensaje                    (mensaje | sistema | grill | respuesta-grill | acuerdo)
    ronda: G1-1                      (solo en grill y respuesta-grill: grill G1, ronda 1)
    responde_a: 006                  (opcional: cita ese mensaje)
    leido_hasta: 006                 (opcional: último mensaje del otro que ya leíste → ✓✓)
    adjuntos: 01_VIGENTE/06_Modelo_BD/bd.uml (v08); adjuntos/008_detalle.md
    reaccion: 006 👍                  (opcional, se puede repetir)
    pendiente: 8 | ¿Texto de la pregunta?    (opcional, se puede repetir: queda fijado arriba)
    cierra: 7                        (opcional, se puede repetir: quita el pendiente fijado)
    ---
    Texto del mensaje. Corto, como en un chat; lo largo va en adjuntos/.
"""
import os, re, sys, textwrap, unicodedata, datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MSG = os.path.join(BASE, "mensajes")
OUT = os.path.join(BASE, "00_CHAT.txt")
IZQ, DER = "Claude Omar", "Claude Alejo"
ANCHO, BURBUJA, SANGRIA = 104, 66, 38          # ancho total, ancho de burbuja, sangría de la derecha
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
         "septiembre", "octubre", "noviembre", "diciembre"]

def w(s):  # ancho visible (emojis y similares ocupan 2)
    n = 0
    for ch in s:
        if unicodedata.combining(ch) or ch in "‍️": continue
        n += 2 if unicodedata.east_asian_width(ch) in "WF" or ord(ch) >= 0x1F000 else 1
    return n

def pad(s, n):
    return s + " " * max(0, n - w(s))

def leer(path):
    txt = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    head, _, body = txt.partition("\n---\n")
    if not _:
        head, _, body = txt.partition("\n\n")
    m = {"reaccion": [], "pendiente": [], "cierra": [], "adjuntos": [], "archivo": os.path.basename(path)}
    for line in head.splitlines():
        if ":" not in line: continue
        k, v = (x.strip() for x in line.split(":", 1))
        if k in ("reaccion", "pendiente", "cierra"): m[k].append(v)
        elif k == "adjuntos": m[k] += [a.strip() for a in v.split(";") if a.strip()]
        else: m[k] = v
    m["id"] = int(m.get("id", re.match(r"(\d+)", m["archivo"]).group(1)))
    m["dt"] = datetime.datetime.strptime(m["fecha"], "%Y-%m-%d %H:%M")
    m["tipo"] = m.get("tipo", "mensaje")
    m["cuerpo"] = body.strip("\n")
    return m

def envolver(texto, ancho):
    out = []
    for par in texto.split("\n"):
        if not par.strip(): out.append(""); continue
        sang = re.match(r"\s*([-*•]|\d+[.)])?\s*", par).group(0)
        cuerpo = par[len(sang):]
        extra = w(cuerpo) - len(cuerpo)          # emojis: ocupan más de lo que cuenta len()
        lines = textwrap.wrap(cuerpo, width=max(10, ancho - len(sang) - extra), break_long_words=True) or [""]
        out.append(sang + lines[0]); out += [" " * len(sang) + l for l in lines[1:]]
    # ajuste fino por emojis anchos
    res = []
    for l in out:
        while w(l) > ancho:
            corte = ancho
            while w(l[:corte]) > ancho: corte -= 1
            res.append(l[:corte]); l = l[corte:]
        res.append(l)
    return res

def resumen(m, n=50):
    t = re.sub(r"\s+", " ", m["cuerpo"]).strip()
    if len(t) <= n: return t
    corte = t.rfind(" ", 0, n)
    return t[:corte if corte > 20 else n].rstrip(",.;:") + "…"

def burbuja(m, msgs, todos):
    interno = BURBUJA - 4
    lineas = []
    if m.get("responde_a"):
        r = todos.get(int(m["responde_a"]))
        if r: lineas += envolver(f"↪ #{r['id']:03d} {r['de']}: {resumen(r)}", interno) + [""]
    lineas += envolver(m["cuerpo"], interno)
    for a in m["adjuntos"]:
        lineas += envolver(f"📎 {a}", interno)
    for p in m["pendiente"]:
        num, _, txt = p.partition("|")
        lineas += envolver(f"📌 Pendiente #{num.strip()}: {txt.strip()}", interno)
    for c in m["cierra"]:
        lineas += envolver(f"✅ Cierra el pendiente #{c.strip()}", interno)
    # estado de lectura
    otro = DER if m["de"] == IZQ else IZQ
    lec = [x for x in msgs if x["de"] == otro and x.get("leido_hasta") and int(x["leido_hasta"]) >= m["id"]]
    estado = f"✓✓ leído {lec[0]['dt']:%H:%M}" if lec else "✓ enviado"
    etiqueta = {"grill": " · ❓ GRILL", "respuesta-grill": " · 💬 RESPUESTA"}.get(m["tipo"], "")
    if etiqueta and m.get("ronda"): etiqueta += f" {m['ronda']}"
    titulo = f"─ {m['de']}{etiqueta} "
    num = f" #{m['id']:03d} ─"
    top = "╭" + titulo + "─" * (BURBUJA - 2 - w(titulo) - w(num)) + num + "╮"
    pie_i, pie_d = f"─ {m['dt']:%H:%M} ", f" {estado} ─"
    bot = "╰" + pie_i + "─" * (BURBUJA - 2 - w(pie_i) - w(pie_d)) + pie_d + "╯"
    filas = [top] + ["│ " + pad(l, interno) + " │" for l in lineas] + [bot]
    reac = [x for x in msgs for r in x["reaccion"] if int(r.split()[0]) == m["id"]]
    for x in reac:
        for r in x["reaccion"]:
            k, _, emo = r.partition(" ")
            if int(k) == m["id"]: filas.append(f"   {emo.strip()} {x['de']}")
    s = " " * SANGRIA if m["de"] == DER else ""
    return [s + f for f in filas]

def sistema(m):
    icono = "🤝 ACUERDO" if m["tipo"] == "acuerdo" else "⚙"
    t = f" {icono} {m['de']} · {m['dt']:%H:%M} · #{m['id']:03d} "
    out = [("─" * ((ANCHO - w(t)) // 2) + t).ljust(0) + "─" * (ANCHO - (ANCHO - w(t)) // 2 - w(t))]
    for l in envolver(m["cuerpo"], ANCHO - 20):
        out.append(" " * max(0, (ANCHO - w(l)) // 2) + l)
    for a in m["adjuntos"]:
        l = f"📎 {a}"; out.append(" " * max(0, (ANCHO - w(l)) // 2) + l)
    for p in m["pendiente"]:
        num, _, txt = p.partition("|"); l = f"📌 Pendiente #{num.strip()}: {txt.strip()}"
        for x in envolver(l, ANCHO - 20): out.append(" " * max(0, (ANCHO - w(x)) // 2) + x)
    for c in m["cierra"]:
        l = f"✅ Cierra el pendiente #{c.strip()}"; out.append(" " * max(0, (ANCHO - w(l)) // 2) + l)
    out.append("─" * ANCHO)
    return out

def generar():
    msgs = sorted((leer(os.path.join(MSG, f)) for f in os.listdir(MSG) if f.endswith(".txt")), key=lambda m: m["id"])
    todos = {m["id"]: m for m in msgs}
    abiertos = {}
    for m in msgs:
        for p in m["pendiente"]:
            n, _, t = p.partition("|"); abiertos[n.strip()] = (t.strip(), m["de"], m["id"])
        for c in m["cierra"]: abiertos.pop(c.strip(), None)
    leeme = open(os.path.join(BASE, "00_LEEME_reglas_del_chat.md"), encoding="utf-8").read()
    ver = re.search(r"Versión de las reglas: (\d+)", leeme)
    L = ["═" * ANCHO,
         "  CHAT JACKSOFT   ·   Claude Omar (frontend)  ◀──────────▶  Claude Alejo (documentación)",
         f"  Reglas: versión {ver.group(1) if ver else '?'} (00_LEEME_reglas_del_chat.md)   ·   "
         f"{len(msgs)} mensajes   ·   generado {datetime.datetime.now():%Y-%m-%d %H:%M}",
         "  Vista generada por _herramientas/chat.py — no se edita. Los mensajes están en mensajes/.",
         "═" * ANCHO, ""]
    if abiertos:
        L.append("  📌 FIJADOS — pendientes abiertos")
        for n, (t, de, i) in sorted(abiertos.items(), key=lambda x: int(x[0])):
            for k, l in enumerate(envolver(f"#{n} {t}  (de {de}, en #{i:03d})", ANCHO - 6)):
                L.append(("   • " if k == 0 else "     ") + l)
        L += ["", "─" * ANCHO, ""]
    dia = None
    for m in msgs:
        if m["dt"].date() != dia:
            dia = m["dt"].date()
            t = f" {DIAS[dia.weekday()]} {dia.day} de {MESES[dia.month - 1]} de {dia.year} "
            L += ["", t.center(ANCHO, "·"), ""]
        L += (sistema(m) if m["tipo"] in ("sistema", "acuerdo") else burbuja(m, msgs, todos)) + [""]
    ult = msgs[-1] if msgs else None
    if ult:
        espera = IZQ if ult["de"] == DER else DER
        L += ["", f"  … turno de {espera} (último mensaje: #{ult['id']:03d} de {ult['de']}, {ult['dt']:%d/%m %H:%M})"]
    open(OUT, "w", encoding="utf-8").write("\n".join(L).rstrip() + "\n")
    print(f"00_CHAT.txt: {len(msgs)} mensajes, {len(abiertos)} pendientes abiertos.")

def siguiente(autor):
    ids = [int(re.match(r"(\d+)", f).group(1)) for f in os.listdir(MSG) if re.match(r"\d+_", f)]
    n = max(ids, default=0) + 1
    ahora = datetime.datetime.utcnow() - datetime.timedelta(hours=5)   # Colombia (UTC-5, sin horario de verano)
    slug = autor.lower().replace(" ", "-")
    print(f"mensajes/{n:03d}_{ahora:%Y-%m-%d_%H%M}_{slug}.txt\n")
    print(f"id: {n:03d}\nde: {autor}\nfecha: {ahora:%Y-%m-%d %H:%M}\ntipo: mensaje\nresponde_a: \nleido_hasta: \n---\n")

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "siguiente": siguiente(sys.argv[2])
    else: generar()
