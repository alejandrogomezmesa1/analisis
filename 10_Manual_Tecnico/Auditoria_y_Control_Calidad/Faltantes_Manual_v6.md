---
title: "Faltantes del manual técnico v6 (2026-11-17)"
type: auditoria
tags:
  - manual-tecnico
  - auditoria
  - cascada
related:
  - "[[00_MOC_Manual_Tecnico]]"
  - "[[CASCADA_DOCUMENTAL]]"
---

# Faltantes del manual técnico v6

Revisión de `Documentos_Word/v6_2026-11-17/Manual_Tecnico_v2.3_Jacksoft.docx`, la copia que Omar re-guardó en Drive el 17-nov, frente a los documentos vigentes: bd.uml v4.6, CU Word v4, Story Mapping v7, ficha v9 y C4 v4. Por ahora es solo una lista: nada se ha corregido. Cada punto se cierra cuando se aplique (ver la regla permanente en [[CASCADA_DOCUMENTAL]]).

## Lo que está al día
- El diccionario de datos tiene las 39 tablas de la v4.6, igual que `Diccionario_de_Datos_JackSoft_v4.6.docx`.
- Los 24 diagramas de casos de uso (23 subprocesos + el mapa general), la C4 (contexto, contenedor, componentes, clases) y el diagrama de despliegue.
- 21 mockups con figura numerada.

## Contenido que falta

| # | Sección | Qué falta | Fuente para completarlo |
|---|---|---|---|
| 1 | Documentación de CU | Faltan **16 fichas** del CU Word v4: HU_123 a HU_127 (Servicio: nombre, tipo, descripción, valor, duración del plan), HU_143 a HU_150 (Clientes: dirección, modalidad, teléfono, correo, restricciones, alergias, suscripciones asociadas, historial de pagos) y HU_153 a HU_155 (reportes de clientes). El manual tiene 229 fichas y el CU Word, 245. | CU Word v4 |
| 2 | Permisos | El modelo v4.6 devolvió `permisos` y `rol_permisos`, pero el manual no tiene módulo de Permisos: ni mockup, ni CU, ni diagrama. Tampoco lo tienen la ficha v9, el Story Mapping v7, los CU ni la C4 nivel 4. | bd.uml v4.6, acuerdo G2 (matriz módulo × acción) |
| 3 | Modelo de BD › Estructura (Modelado) | Vacía: falta la imagen del diagrama ER. | `04_Modelado_DB/Diagramas/v10_2026-11-13/LaCocaDiagramDB.svg` |
| 4 | Modelo de BD › Script | Vacío: falta el script SQL (o un enlace al bd.uml / DBML). | bd.uml v4.6 |
| 5 | Prototipo (React) | Vacío: tiene solo el texto de la plantilla. Faltan pantallazos o el enlace del frontend y la página de aterrizaje. | Frontend de Omar |
| 6 | Seguridad (5 subsecciones) | Vacías: encriptación, tokens, OAuth 2, CSP/XSS, inyección SQL. Ya hay decisiones para llenarlas: bloqueo por intentos en el backend (G1), ingreso con Google y Apple por OpenID Connect + PKCE (G3-Q11 a Q13), código por WhatsApp (G4). | Chat G1, G3, G4 |
| 7 | Requerimientos mínimos (hardware, software, configuraciones) | Vacíos. | Diagrama de despliegue, stack del frontend y backend |
| 8 | Mockups de Configuraciones del sistema y Menú | Siguen con "Pendiente: agregar la vista del mockup en Figma". | Figma |
| 9 | Diagrama de despliegue | Solo está la imagen, sin descripción ni figura numerada. | — |
| 10 | Bibliografía | Solo el texto de la plantilla ("<Colocar la referencia…>"). | — |
| 11 | Anexos › Actas de reunión | Vacío. | — |

## Forma y datos desactualizados

| # | Dónde | Problema |
|---|---|---|
| 12 | Tabla de contenido | Desactualizada: todavía dice "CU02 xxxxx", "Modelo No Relacional", "Técnicas de recolección". Hay que actualizar el campo en Word. |
| 13 | Lista de figuras | Vacía (el campo no está actualizado). |
| 14 | Figuras | Solo los mockups tienen pie de figura. Los diagramas de CU, la C4, el despliegue y el ER no tienen. |
| 15 | Anexos | Citan documentos viejos: "formato ficha proyecto 14agosto" (la vigente es la v9) y "Tablero Kanban 13/09" (el vigente es el v7). |
| 16 | Control del documento | Sigue con datos de la plantilla: autores vacíos, "Abril 2021"; firmas y fechas vacías. |
| 17 | Control de cambios y portada | La edición de Omar del 17-nov (diccionario v4.6 + despliegue) no tiene fila en el control de cambios. La portada sigue en "Versión 2.3": debería ser la 2.4. |
| 18 | Textos de plantilla | Quedan instrucciones de la plantilla: "Herramienta Figma u otro del mismo nivel…", "Aquí deben ir los pantallazos…", "Nota: Si para el proyecto no aplica…". |
| 19 | Imágenes | Al re-guardarlo en Drive se recomprimieron: la mayor bajó de 11,7 a 2,3 MP. La próxima versión debe recuperar las imágenes de la v5 (o de sus fuentes). |
| 20 | Eliminar | Hay 4 CU de borrado (rol, usuario, categoría de insumos, ruta). En G3-Q6 se decidió no borrar sino inactivar, así que salen cuando se aplique la v4.7. |

## Inconsistencias entre documentos clave (no solo del manual)
- **Story Mapping v7 (182 historias) frente al CU Word v4 y el manual (245 y 229 casos):** cambian los nombres y el número de historias por módulo. Por ejemplo, el Dashboard tiene 5 historias en el SM y 19 casos en el manual, y Suscripciones tiene 11 y 29. Hay que decidir cuál es la lista canónica.
- **Ficha v9:** no menciona permisos ni el ingreso con Google y Apple.
- **C4 v4 (03-nov):** es anterior a la v4.6; el nivel 4 (clases) no tiene permisos.

## Lo que entra con la v4.7 (cuando cierren G2, G3 y G4)
Diccionario y ER: `alergenos`, `movimientos_insumos`, `imagen_url`, `cantidad_planificada`, `tipo_documento`, `municipio`, `dias_habiles`, `beneficios`, `rendimiento_porciones`, `nombre_publico`, `foto_url` del menú, `identidades_externas`, password opcional y las claves de pago y horario. CU de Acceso con Google, Apple y código por WhatsApp. Salen los CU de Eliminar, las notas para la cocina y `franja_horaria`.
