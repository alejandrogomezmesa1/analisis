---
title: "Estado actual — versión vigente de cada documento"
type: tracker
tags:
  - versiones
  - head
related:
  - "[[00_MOC_Versiones]]"
  - "[[CHANGELOG]]"
---

# Estado actual (HEAD de cada documento)

Última actualización: **2026-11-17** (commit C-089). Copia de todas las versiones vigentes en `00_Documentacion_Vigente/`. Al crear una versión nueva, actualizar su fila aquí y agregar el commit en [[CHANGELOG]]. Para publicarla en Google Drive (Modelado(5 trimestre)): `python3 00_Contexto_Versiones/publicar_drive.py`.

| Módulo | Documento | Vigente | Versiones | Ruta de la versión vigente | Último commit |
|---|---|:---:|:---:|---|---|
| 01 Investigación | Árbol de problemas | **v1** | 1 | `01_Investigacion_y_Analisis/Diagramas/Arbol_de_Problemas/v1_2026-08-11/` | C-012 |
| 01 Investigación | Árbol de objetivos | **v1** | 1 | `01_Investigacion_y_Analisis/Diagramas/Arbol_de_Objetivos/v1_2026-08-25/` | C-023 |
| 01 Investigación | Mapa mental | **v2** | 2 | `01_Investigacion_y_Analisis/Diagramas/Mapa_Mental/v2_2026-08-25/` | C-024 |
| 01 Investigación | Análisis 5W1H (slide) | **v2** | 2 | `01_Investigacion_y_Analisis/Diagramas/Analisis_5W1H/v2_2026-08-11/` | C-014 |
| 03 Procesos | Aplicativo web mapa de procesos | **v2** | 2 | `03_Procesos/App_Mapa_Procesos/v2_2026-09-28/` | C-035 |
| 04 Modelo BD | Modelo relacional (DBML) | **v12** (DBML v4.6, entregable) | 12 | `04_Modelado_DB/Modelo_Relacional/v12_2026-11-13/bd.uml` | C-079 |
| 04 Modelo BD | Diagrama ER (SVG) | **v10** | 10 | `04_Modelado_DB/Diagramas/v10_2026-11-13/` | C-080 |
| 04 Modelo BD | Diccionario de datos (Word) | **v1** (v4.6) | 1 | `04_Modelado_DB/Diccionario_y_Tablas/Documento_Word/v1_2026-11-13/` | C-081 |
| 05 Casos de uso | Diagrama de despliegue | **v1** | 1 | `05_Casos_de_Uso/Diagrama_Despliegue/v1_2026-11-10/` | C-081 |
| 05 Casos de uso | Arquitectura C4 | **v5** (bd.uml v4.6, con permisos) | 5 | `05_Casos_de_Uso/Arquitectura_C4/v5_2026-11-17/` | C-086 |
| 05 Casos de uso | Documentación de casos de uso (Word) | **v5** (253 fichas, Permisos HU_246–HU_253) | 5 | `05_Casos_de_Uso/Especificaciones/Documentacion_Word/v5_2026-11-17/` | C-087 |
| 05 Casos de uso | Diagramas, visor y scripts (sistema generado) | 24 subprocesos (con Permisos) | repo git | `05_Casos_de_Uso/` (repo `CasosDeUsoJackSoft`) | C-085 |
| 06 Scrum | Ficha de proyecto | **v10** (oficial, con permisos) | 10 | `06_Gestion_de_Proyecto_Scrum/Fichas_Tecnicas/v10_2026-11-17/` | C-083 |
| 06 Scrum | Tablero Kanban + Story Mapping + Matriz HU | **v8** (24 subprocesos, 165 historias, 510 puntos) | 8 | `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Tablero_Kanban/v8_2026-11-17/` | C-084 |
| 06 Scrum | Matriz HU (independiente) | **v1** — superada por el Tablero Kanban v3+ | 1 | `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Matriz_HU/v1_2026-08-12/` | C-016 |
| 06 Scrum | Presentación de artefactos Scrum | **v1** | 1 | `06_Gestion_de_Proyecto_Scrum/Presentacion_Artefactos/v1_2026-07-27/` | C-006 |
| 07 Diseño | Mockups | **v1** | 1 | `07_Diseno_y_Mockups/Mockups/v1_2026-08-09/` | C-010 |
| 07 Diseño | Facilitación gráfica | **v1** | 1 | `07_Diseno_y_Mockups/Facilitacion_Grafica/v1_2026-08-24/` | C-022 |
| 08 Entregables | Plantilla de informe | **v2** | 2 | `08_Entregables_e_Informes/Informes_Academicos/Plantilla_Informe/v2_2026-09-01/` | C-027 |
| 08 Entregables | Rúbrica de investigación | **v1** | 1 | `08_Entregables_e_Informes/Informes_Academicos/Rubrica_Investigacion/v1_2026-08-25/` | C-025 |
| 08 Entregables | Ensayo: Por qué es importante conocer en detalle | **v1** | 1 | `08_Entregables_e_Informes/Ensayos_y_Monografias/Importancia_Conocer_en_Detalle/v1_2026-06-16/` | C-002 |
| 08 Entregables | Ensayo: ¿Qué son los requisitos? | **v1** | 1 | `08_Entregables_e_Informes/Ensayos_y_Monografias/Que_Son_Los_Requisitos/v1_2026-06-16/` | C-003 |
| 10 Manual técnico | Manual técnico (Word) | **v7** (archivo "v2.4": Permisos, C4 v5, diccionario y despliegue de Omar, imágenes originales) | 7 | `10_Manual_Tecnico/Documentos_Word/v7_2026-11-17/` | C-088 |

## Pendientes detectados al reorganizar

- **Tablero Kanban v4 (C-036):** no se sabe qué cambió frente a la v3. Conviene anotarlo en el commit.
- **Mockups de Configuraciones del sistema y Menú:** faltan en Figma; el manual v4 tiene la sección con la nota de pendiente.
- **Tablero Kanban v5:** ábrelo en Excel una vez para que recalcule el Backlog, el Tablero y el Avance (está marcado para recalcular al abrir).
- **Ficha v8:** es la versión oficial vigente.
- **Frontend:** los cambios que debe hacer están en el chat con Claude Omar: `chat/00_CHAT.txt` (copia de Google Drive › JackSoft › JackSoft › chat; reglas en `00_LEEME_reglas_del_chat.md`).
