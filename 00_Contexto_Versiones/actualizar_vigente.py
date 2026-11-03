"""Copia la versión más reciente de cada documento a 00_Documentacion_Vigente/.

Uso (desde la raíz del vault):  python3 00_Contexto_Versiones/actualizar_vigente.py

Regla: en cada carpeta que tenga subcarpetas vN_AAAA-MM-DD, la vigente es la de N más alto.
La carpeta 00_Documentacion_Vigente se regenera completa en cada ejecución (no edites nada ahí:
es solo una copia de acceso directo; los cambios se hacen en la carpeta del documento).
"""
import os, re, shutil, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(ROOT, "00_Documentacion_Vigente")
MARK = os.path.join(DEST, ".carpeta_generada")
VER = re.compile(r"^v(\d+)_(\d{4}-\d{2}-\d{2})$")
SKIP_DIRS = {".git", "00_Documentacion_Vigente", "09_Backups_y_Archivos_Zips", "_Historial", ".obsidian", ".playwright-mcp", "node_modules"}
IGNORE = shutil.ignore_patterns(".git", ".DS_Store", "desktop.ini")

# Elementos sin carpetas de versión que también conviene tener a mano (se copian tal cual).
EXTRA = [
    ("05_Casos_de_Uso/Diagramas_DrawIO/Casos_de_usos.drawio", "05_Casos_de_Uso/Diagramas_Casos_de_Uso/Casos_de_usos.drawio"),
    ("05_Casos_de_Uso/Diagramas_PNG", "05_Casos_de_Uso/Diagramas_Casos_de_Uso/PNG"),
]

def families():
    for dirpath, dirnames, _ in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not VER.match(d)]
        try:
            subs = [d for d in os.listdir(dirpath) if VER.match(d) and os.path.isdir(os.path.join(dirpath, d))]
        except OSError:
            continue
        if subs:
            best = max(subs, key=lambda d: int(VER.match(d).group(1)))
            yield os.path.relpath(dirpath, ROOT), best, len(subs)

def main():
    if os.path.exists(DEST):
        if not os.path.exists(MARK):
            raise SystemExit(f"{DEST} existe pero no fue creada por este script; revísala antes de continuar.")
        shutil.rmtree(DEST)
    os.makedirs(DEST)
    open(MARK, "w").write("Carpeta generada por 00_Contexto_Versiones/actualizar_vigente.py\n")
    rows = []
    for rel, best, n in sorted(families()):
        src = os.path.join(ROOT, rel, best)
        dst = os.path.join(DEST, rel)
        shutil.copytree(src, dst, ignore=IGNORE)
        files = sorted(f for f in os.listdir(dst) if not f.startswith("."))
        rows.append((rel, best, n, files))
    for src, dst in EXTRA:
        s, d = os.path.join(ROOT, src), os.path.join(DEST, dst)
        if os.path.isdir(s): shutil.copytree(s, d, ignore=IGNORE)
        elif os.path.exists(s): os.makedirs(os.path.dirname(d), exist_ok=True); shutil.copy2(s, d)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = ["---", 'title: "Documentación vigente (copia automática)"', "type: MOC", "tags:", "  - versiones", "  - vigente",
             "related:", '  - "[[00_MOC_Versiones]]"', '  - "[[ESTADO_ACTUAL]]"', "---", "",
             "# 📦 Documentación vigente", "",
             f"Copia automática de la **última versión** de cada documento. Generada el **{now}** con `00_Contexto_Versiones/actualizar_vigente.py`.", "",
             "> No edites aquí: esta carpeta se borra y se vuelve a crear en cada ejecución. Los cambios se hacen creando una nueva versión en la carpeta del documento (ver [[00_MOC_Versiones]]).", "",
             "| Documento (carpeta de origen) | Versión copiada | Versiones existentes | Archivos |", "|---|:---:|:---:|---|"]
    for rel, best, n, files in rows:
        lines.append(f"| `{rel}` | **{best}** | {n} | {', '.join('`' + f + '`' for f in files)} |")
    lines += ["", "Además se copian el draw.io de casos de uso y sus PNG (`05_Casos_de_Uso/Diagramas_Casos_de_Uso/`), que se versionan en el repo git de `05_Casos_de_Uso`."]
    open(os.path.join(DEST, "00_LEEME_Vigente.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"{len(rows)} documentos copiados a {os.path.relpath(DEST, ROOT)}/")
    for rel, best, n, _ in rows:
        print(f"  {best:16} {rel}")

if __name__ == "__main__":
    main()
