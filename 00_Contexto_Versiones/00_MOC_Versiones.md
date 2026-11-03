---
title: "Control de versiones de la documentación — JackSoft"
type: MOC
tags:
  - versiones
  - changelog
  - contexto
related:
  - "[[00_INDICE_GENERAL]]"
  - "[[CHANGELOG]]"
  - "[[ESTADO_ACTUAL]]"
---

# Control de versiones de la documentación

Esta carpeta funciona como el `git log` de la documentación: cada cambio en un documento es una **nueva versión** y queda anotado como un **commit** en [[CHANGELOG]].

| Archivo | Para qué sirve |
|---|---|
| [[CHANGELOG]] | Historial completo, un commit por cambio (el más reciente arriba). |
| [[ESTADO_ACTUAL]] | La versión vigente de cada documento y dónde está (el `HEAD` de cada uno). |
| [[CASCADA_DOCUMENTAL]] | Orden en que se actualizan los documentos cuando cambia la ficha (alcance). |
| `actualizar_vigente.py` | Copia la última versión de cada documento a `00_Documentacion_Vigente/`. |

---

## 1. Cómo están organizadas las versiones

Dentro de la carpeta de cada documento hay una subcarpeta por versión:

```
06_Gestion_de_Proyecto_Scrum/Fichas_Tecnicas/
├── Ficha_de_Proyecto.md        ← nota de Obsidian (resumen vivo)
├── v1_2026-06-16/
├── v2_2026-07-24/
├── ...
└── v7_2026-10-30/              ← la más reciente = la vigente
```

- **Nombre:** `vN_AAAA-MM-DD` → número de versión + fecha del cambio.
- **La vigente es siempre el número más alto.** No se marca con "final", "último" ni "actual".
- **Las versiones anteriores no se borran ni se editan.** Son el historial.
- **Los archivos conservan su nombre original** dentro de cada versión, para no romper referencias.

### Qué NO se versiona en carpetas

| Elemento | Por qué | Cómo se registra |
|---|---|---|
| Notas de Obsidian (`00_MOC_*`, `RN_*`, `PROC_*`, `DB_*`, `CU_*`, `Ficha_de_Proyecto.md`, etc.) | Son la versión viva del conocimiento. Duplicarlas rompe los `[[wikilinks]]`. | Commit en el CHANGELOG. Si el cambio es grande, la versión anterior se guarda como `_Historial/Nombre__vN.md` en la misma carpeta. |
| Sistema generado de casos de uso (`05_Casos_de_Uso/Diagramas_PUML`, `Diagramas_SVG`, `Diagramas_PNG`, `Visor_Interactivo`, `scripts`, `casos_de_uso_v3`, `index.html`) | Los scripts y GitHub Pages dependen de esas rutas. | Tiene su propio repo git (`CasosDeUsoJackSoft`). Se anota un commit aquí cuando cambie. |
| `09_Backups_y_Archivos_Zips/` | Es el respaldo crudo. | No aplica. |

> **Repos git internos.** Tres carpetas tienen su propio `.git` con remoto en GitHub: `05_Casos_de_Uso/` (CasosDeUsoJackSoft), `03_Procesos/App_Mapa_Procesos/v1_2026-06-16/` (Mapa-procesos-) y `06_Gestion_de_Proyecto_Scrum/Presentacion_Artefactos/v1_2026-07-27/` (artefactos). Se movieron completos, con su `.git`.

---

## 2. Cómo registrar un cambio (hacer un "commit")

Ejemplo: se corrige la ficha de proyecto, cuya versión vigente es la `v7`.

1. **Crear la carpeta nueva:** `Fichas_Tecnicas/v8_AAAA-MM-DD/`.
2. **Guardar ahí el archivo corregido.** No sobrescribir la `v7`.
3. **Agregar un commit arriba del todo en [[CHANGELOG]]** con la plantilla de abajo (el número de commit es el siguiente al último).
4. **Actualizar la fila del documento en [[ESTADO_ACTUAL]]** (versión y ruta).
5. Si alguna nota o MOC cita la ruta del archivo vigente, actualizarla.
6. **Actualizar la carpeta de vigentes:** `python3 00_Contexto_Versiones/actualizar_vigente.py` (regenera `00_Documentacion_Vigente/` con la última versión de cada documento).

Si el cambio altera el alcance, sigue el orden de [[CASCADA_DOCUMENTAL]].

### Plantilla de commit

```markdown
### C-0XX · AAAA-MM-DD · tipo(artefacto) · vA → vB
- **Ruta:** `carpeta/vB_AAAA-MM-DD/`
- **Archivos:** `nombre.docx`
- **Autor:** Nombre
- **Mensaje:** Qué cambió y por qué (1–3 líneas).
- **Origen:** comentario de instructor / revisión / decisión del equipo (opcional)
```

### Tipos de commit

| Tipo | Uso |
|---|---|
| `feat` | Documento nuevo (su `v1`). |
| `fix` | Corrección o actualización de un documento existente (nueva versión). |
| `docs` | Cambio en notas de Obsidian o MOCs (sin carpeta de versión). |
| `refactor` | Reorganización de carpetas o rutas sin cambiar contenido. |
