"""Publica en Google Drive la documentación del trimestre de modelado, con su versionado.

Uso (desde la raíz del vault):
    python3 00_Contexto_Versiones/publicar_drive.py            # publica
    python3 00_Contexto_Versiones/publicar_drive.py --simular  # muestra qué haría, sin copiar

Estructura que mantiene en  Drive › JackSoft › JackSoft › Modelado(5 trimestre):

    00_LEEME_versionado.md      cómo funciona (lo escribe este script)
    00_CHANGELOG.md             versión vigente de cada documento + historial de cambios (lo escribe este script)
    01_VIGENTE/<Documento>/     última versión de cada documento, con VERSION.txt
    02_HISTORIAL/<Documento>/vNN_AAAA-MM-DD/   todas las versiones (no se borran)
    03_Exposiciones/            presentaciones del trimestre (no tienen versiones; no las toca)

Reglas:
- La fuente de verdad es el repo: cada documento tiene carpetas vN_AAAA-MM-DD y la vigente es la de N más alto.
- En Drive se usa el mismo número que en el repo, con dos dígitos (v8 → v08) para que ordene bien.
- 02_HISTORIAL solo crece: una versión publicada no se borra. Si un archivo de una versión cambió en el repo,
  se reemplaza y se avisa.
- 01_VIGENTE se actualiza por documento: solo se reemplaza la carpeta del documento que cambió de versión
  (así no se vuelven a subir los archivos grandes que no cambiaron).
"""
import filecmp, os, re, shutil, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRIVE = os.environ.get("JACKSOFT_DRIVE", os.path.expanduser(
    "~/Library/CloudStorage/GoogleDrive-alejandrogomezmesa1@gmail.com/Mi unidad/JackSoft/JackSoft/Modelado(5 trimestre)"))
SIMULAR = "--simular" in sys.argv

# Documentos del trimestre, en el orden de la cascada documental (la ficha manda).
DOCS = [
    ("01_Ficha_Tecnica",          "06_Gestion_de_Proyecto_Scrum/Fichas_Tecnicas"),
    ("02_Story_Mapping_Kanban",   "06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Tablero_Kanban"),
    ("03_Documentacion_Casos_de_Uso", "05_Casos_de_Uso/Especificaciones/Documentacion_Word"),
    ("05_Arquitectura_C4",        "05_Casos_de_Uso/Arquitectura_C4"),
    ("06_Modelo_BD",              "04_Modelado_DB/Modelo_Relacional"),
    ("07_Diagrama_ER",            "04_Modelado_DB/Diagramas"),
    ("08_Manual_Tecnico",         "10_Manual_Tecnico/Documentos_Word"),
]
# Sin carpetas de versión en el repo (sistema generado): solo van a 01_VIGENTE.
SIN_VERSION = [
    ("04_Diagramas_Casos_de_Uso", [("05_Casos_de_Uso/Diagramas_DrawIO/Casos_de_usos.drawio", "Casos_de_usos.drawio"),
                                   ("05_Casos_de_Uso/Diagramas_PNG", "PNG")]),
]
VER = re.compile(r"^v(\d+)_(\d{4}-\d{2}-\d{2})$")
BASURA = {".DS_Store", "desktop.ini", ".git"}
log = []

def say(msg):
    log.append(msg); print(msg)

def versiones(rel):
    base = os.path.join(ROOT, rel)
    vs = [(int(m.group(1)), m.group(2), d) for d in os.listdir(base)
          if (m := VER.match(d)) and os.path.isdir(os.path.join(base, d))]
    return sorted(vs)

def nombre_drive(n, fecha):
    return f"v{n:02d}_{fecha}"

def sincronizar(src, dst):
    """Copia src → dst archivo por archivo; devuelve (nuevos, cambiados). No borra nada en dst."""
    nuevos = cambiados = 0
    for dirpath, dirnames, files in os.walk(src):
        dirnames[:] = [d for d in dirnames if d not in BASURA]
        rel = os.path.relpath(dirpath, src)
        for f in files:
            if f in BASURA: continue
            a = os.path.join(dirpath, f); b = os.path.normpath(os.path.join(dst, rel, f))
            if not os.path.exists(b): nuevos += 1
            elif not filecmp.cmp(a, b, shallow=False): cambiados += 1
            else: continue
            if not SIMULAR:
                os.makedirs(os.path.dirname(b), exist_ok=True); shutil.copy2(a, b)
    return nuevos, cambiados

def reemplazar(src_items, dst, version_txt):
    """Deja dst con exactamente src_items (lista de (origen, nombre)) y VERSION.txt."""
    marca = os.path.join(dst, "VERSION.txt")
    if os.path.exists(marca) and open(marca, encoding="utf-8").read().splitlines()[0] == version_txt.splitlines()[0]:
        n = c = 0
        for s, name in src_items:
            if os.path.isdir(s): a, b = sincronizar(s, os.path.join(dst, name))
            else:
                t = os.path.join(dst, name)
                a, b = (0, 0) if os.path.exists(t) and filecmp.cmp(s, t, shallow=False) else ((0, 1) if os.path.exists(t) else (1, 0))
                if (a or b) and not SIMULAR: shutil.copy2(s, t)
            n += a; c += b
        return "igual" if not (n or c) else f"actualizada ({n} nuevos, {c} cambiados)"
    if not SIMULAR:
        if os.path.exists(dst): shutil.rmtree(dst)
        os.makedirs(dst)
        for s, name in src_items:
            t = os.path.join(dst, name)
            if os.path.isdir(s): shutil.copytree(s, t, ignore=shutil.ignore_patterns(*BASURA))
            else: shutil.copy2(s, t)
        open(marca, "w", encoding="utf-8").write(version_txt)
    return "reemplazada"

def changelog_repo():
    """Entradas del CHANGELOG del repo que tocan los documentos del trimestre."""
    txt = open(os.path.join(ROOT, "00_Contexto_Versiones/CHANGELOG.md"), encoding="utf-8").read()
    bloques = re.split(r"\n(?=### C-\d+)", txt)
    rutas = [r for _, r in DOCS] + ["05_Casos_de_Uso/Diagramas", "chat/"]
    out = []
    for b in bloques:
        if not b.startswith("### C-"): continue
        if any(r in b for r in rutas): out.append(b.strip())
    return out

def main():
    # Regla de oro: el visor y el diagrama ER se regeneran desde el bd.uml vigente antes de publicar.
    import subprocess
    subprocess.run([sys.executable, os.path.join(ROOT, "04_Modelado_DB", "Visor_Modelo", "construir_visor.py")], check=True)
    if not os.path.isdir(DRIVE):
        raise SystemExit(f"No encuentro la carpeta de Drive: {DRIVE}\n¿Está abierto Google Drive para escritorio?")
    hoy = datetime.date.today().isoformat()
    estado = []
    for nombre, rel in DOCS:
        vs = versiones(rel)
        for n, fecha, d in vs:
            dst = os.path.join(DRIVE, "02_HISTORIAL", nombre, nombre_drive(n, fecha))
            existia = os.path.exists(dst)
            a, b = sincronizar(os.path.join(ROOT, rel, d), dst)
            if not existia: say(f"  + historial  {nombre}/{nombre_drive(n, fecha)}  ({a} archivos)")
            elif a or b: say(f"  ! historial  {nombre}/{nombre_drive(n, fecha)} cambió en el repo: {a} nuevos, {b} reemplazados")
        n, fecha, d = vs[-1]
        src = os.path.join(ROOT, rel, d)
        items = [(os.path.join(src, f), f) for f in sorted(os.listdir(src)) if f not in BASURA]
        vtxt = (f"{nombre_drive(n, fecha)}\nDocumento: {nombre}\nVersión del repo: {d} ({rel})\n"
                f"Publicado: {hoy}\nHistorial: 02_HISTORIAL/{nombre}/\n")
        r = reemplazar(items, os.path.join(DRIVE, "01_VIGENTE", nombre), vtxt)
        if r != "igual": say(f"  * vigente    {nombre} → {nombre_drive(n, fecha)} ({r})")
        estado.append((nombre, nombre_drive(n, fecha), len(vs), files_of(src)))
    for nombre, items in SIN_VERSION:
        its = [(os.path.join(ROOT, s), name) for s, name in items]
        vtxt = f"sin_version\nDocumento: {nombre}\nSe genera en el repo CasosDeUsoJackSoft (sin carpetas de versión).\nPublicado: {hoy}\n"
        r = reemplazar(its, os.path.join(DRIVE, "01_VIGENTE", nombre), vtxt)
        if r != "igual": say(f"  * vigente    {nombre} ({r})")
        estado.append((nombre, "sin versión", 0, ", ".join(n for _, n in items)))
    estado.sort()
    escribir_leeme(); escribir_changelog(estado, hoy)
    print("Simulación: no se copió nada." if SIMULAR else "Listo.", "Sin cambios." if not log else f"{len(log)} cambios.")

def files_of(path):
    fs = [f for f in sorted(os.listdir(path)) if f not in BASURA]
    return ", ".join(fs[:4]) + (f" (+{len(fs) - 4})" if len(fs) > 4 else "")

def escribir(nombre, texto):
    p = os.path.join(DRIVE, nombre)
    if os.path.exists(p) and open(p, encoding="utf-8").read() == texto: return
    say(f"  * {nombre}")
    if not SIMULAR: open(p, "w", encoding="utf-8").write(texto)

def escribir_changelog(estado, hoy):
    L = ["# Registro de versiones — Modelado (5.º trimestre)", "",
         f"Generado por `publicar_drive.py` el {hoy}. No lo edites a mano: se reescribe en cada publicación.", "",
         "## Versión vigente de cada documento", "",
         "| Documento | Vigente | Versiones | Archivos |", "| :--- | :--- | ---: | :--- |"]
    L += [f"| {n} | **{v}** | {c or '—'} | {f} |" for n, v, c, f in estado]
    L += ["", "La copia de la versión vigente está en `01_VIGENTE/<Documento>/`; todas las versiones, en `02_HISTORIAL/<Documento>/`.", "",
          "## Historial de cambios (más reciente primero)", "",
          "Cada entrada es un commit del repo de documentación (C-NNN). La versión vN del repo es la carpeta vNN de Drive.", ""]
    L += [b.replace("### ", "### ", 1) + "\n" for b in changelog_repo()]
    escribir("00_CHANGELOG.md", "\n".join(L).rstrip() + "\n")

def escribir_leeme():
    escribir("00_LEEME_versionado.md", """# Cómo está organizada esta carpeta

| Carpeta | Qué tiene | ¿Se edita a mano? |
| :--- | :--- | :--- |
| `00_CHANGELOG.md` | Versión vigente de cada documento y todo lo que cambió, con fecha y motivo. | No (lo genera el script) |
| `01_VIGENTE/` | **La última versión de cada documento.** Es la que se abre, se entrega y se usa en el frontend. Cada documento trae `VERSION.txt`. | No |
| `02_HISTORIAL/` | Todas las versiones de cada documento: `vNN_AAAA-MM-DD`. Nunca se borran. | No |
| `03_Exposiciones/` | Presentaciones del trimestre (no tienen versiones). | Sí |

## Documentos (en el orden en que se actualizan: la ficha manda)

1. Ficha técnica → 2. Story Mapping / Kanban → 3. Documentación de casos de uso → 4. Diagramas de casos de uso →
5. Arquitectura C4 → 6. Modelo de base de datos → 7. Diagrama ER → 8. Manual técnico

## Reglas del versionado

- **Una versión nueva = una carpeta nueva** `vNN_AAAA-MM-DD` en `02_HISTORIAL/<Documento>/`. El número más alto es la vigente.
- El número es el mismo del repo de documentación (`v08` en Drive = `v8_…` en el repo), y cada cambio tiene su commit `C-NNN` en el CHANGELOG.
- No se suben archivos sueltos ni carpetas por fecha: todo se publica con `python3 00_Contexto_Versiones/publicar_drive.py`, que copia las versiones nuevas, actualiza `01_VIGENTE` y reescribe el CHANGELOG.
- Si alguien del equipo necesita cambiar un documento, deja el archivo nuevo en el chat o se lo pasa al equipo de documentación para que entre como versión nueva; no se reemplazan archivos dentro de `01_VIGENTE` ni de `02_HISTORIAL`.
""")

if __name__ == "__main__":
    main()
