---
title: "Cascada documental — qué se actualiza cuando cambia el alcance"
type: proceso
tags:
  - versiones
  - cascada
  - alcance
related:
  - "[[00_MOC_Versiones]]"
  - "[[CHANGELOG]]"
  - "[[ESTADO_ACTUAL]]"
  - "[[Contexto_e_Incongruencias_JackSoft]]"
---

# Cascada documental

> **Regla permanente (2026-11-17, Alejandro):** cualquier cambio que se aplique, en cualquier documento, se propaga **en el mismo trabajo** a todos los documentos clave que afecte, sin esperar a que alguien lo pida. Los documentos clave son: **manual técnico**, **ficha técnica**, **modelado** (bd.uml + visor + diagrama ER), **Excel Tablero Kanban / Story Mapping / Matriz HU** y **casos de uso** (Word, sistema generado y draw.io). La C4 se deriva del modelo y también se revisa. Si el cambio afecta al frontend, primero se cierra el acuerdo del grill con Claude Omar y después se propaga. Faltantes conocidos del manual: [[Faltantes_Manual_v6]].

La **ficha técnica** es el documento raíz: define el alcance (procesos y subprocesos). Cuando cambia, el resto se actualiza en este orden, porque cada paso usa el resultado del anterior.

```mermaid
graph TD
    F["1. Ficha técnica (alcance)"] --> SM["2. Excel: Story Mapping"]
    SM --> AUTO["Backlog · Tablero · Avance (automático)"]
    SM --> MHU["3. Excel: hoja Formato Matriz HU (manual)"]
    F --> BD["4. Modelo relacional bd.uml"]
    BD --> ER["5. Diagrama ER"]
    SM --> CU["6. Casos de uso: lista canónica → PUML/SVG/PNG, MD, visor"]
    CU --> DIO["7. draw.io de casos de uso"]
    MHU --> CUW["8. Documentación de CU (Word, fichas)"]
    BD --> C4["9. Arquitectura C4 (niveles 2, 3 y 4)"]
    CU --> MAN["10. Manual técnico"]
    CUW --> MAN
    C4 --> MAN
    DIO --> MAN
    MAN --> NOTAS["11. Notas Obsidian, MOC e índice"]
    NOTAS --> VIG["12. actualizar_vigente.py"]
```

| # | Documento | Dónde | Qué revisar | Automático |
|---|---|---|---|---|
| 1 | Ficha técnica | `06_.../Fichas_Tecnicas/` | Objetivos, alcance web y mobile | — |
| 2 | Story Mapping | Tablero Kanban, hoja *Story Mapping* | Una columna por subproceso (historia + puntos). Si cambia el número de columnas, ampliar el rango `D:AY…` de las fórmulas del Backlog y de `B5`, `B6` y `B7` | Backlog, Tablero Kanban y Avance |
| 3 | Matriz HU | Tablero Kanban, hoja *Formato Matriz HU* | **No se actualiza sola**: HU y criterios por subproceso. No renumerar códigos existentes | Resumen automático (columnas R–T) |
| 4 | Modelo relacional | `04_Modelado_DB/Modelo_Relacional/` | Tablas, FK, TableGroups (1 por subproceso), Records | — |
| 5 | Diagrama ER | `04_Modelado_DB/Diagramas/` | Regenerar desde el `bd.uml` vigente | — |
| 6 | Casos de uso (sistema generado) | `05_Casos_de_Uso/scripts/` | `actualizar_casos_uso_canonicos.py` (lista canónica) → `actualizar_documentacion_casos_uso.py` → `generar_mapa_interactivo.py`; PNG = captura del SVG a 1050×750 | PUML, SVG, MD, visor |
| 7 | draw.io | `05_Casos_de_Uso/Diagramas_DrawIO/` | Un carril por subproceso | — |
| 8 | Documentación de CU (Word) | `05_.../Documentacion_Word/` | Fichas `HU_###` (continuar la numeración) | — |
| 9 | C4 | `05_Casos_de_Uso/Arquitectura_C4/` | Nivel 2 (BD), Nivel 3 (módulos), Nivel 4 (clases desde `bd.uml`) | — |
| 10 | Manual técnico | `10_Manual_Tecnico/Documentos_Word/` | Mockups, diagramas de CU, C4, fichas, BD | — |
| 11 | Notas | MOC, `00_INDICE_GENERAL`, RN, DB, CU | Rutas y conteos | — |
| 12 | Vigentes | `00_Documentacion_Vigente/` | `python3 00_Contexto_Versiones/actualizar_vigente.py` | Sí |

**No se afectan por cambios de subprocesos:** investigación (01), mapa de procesos de negocio (03), ensayos y plantilla de informe (08), mockups existentes (07; los nuevos módulos se diseñan en Figma).

## Último cambio aplicado
**2026-11-18 (commits C-090 a C-099):** modelo v4.7 con los acuerdos G1 a G4. Ingreso de clientes con Google, Apple o código por WhatsApp; salen los casos de uso de eliminar (G3-Q6). Se actualizaron el modelo, el ER, el visor, el diccionario v2, el Kanban v9, los casos de uso, el draw.io, el CU Word v6, la C4 v6, la ficha v11 y el manual v8.

**2026-11-17 (commits C-083 a C-089):** vuelve el subproceso Permisos, antes de Roles (bd.uml v4.6, acuerdo G2: matriz módulo × acción). Ficha v10, Tablero Kanban v8 (Story Mapping y Matriz HU), casos de uso (24 subprocesos, draw.io), C4 v5, CU Word v5, manual v7 y visor. Detalle en [[CHANGELOG]].

**2026-11-02 (commits C-041 a C-050):** sin Empleados, Permisos ni Categoría de proveedor; con Configuraciones del sistema y Menú.
