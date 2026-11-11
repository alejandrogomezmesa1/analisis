---
title: "CHANGELOG — Historial de versiones de la documentación JackSoft"
type: changelog
tags:
  - versiones
  - changelog
related:
  - "[[00_MOC_Versiones]]"
  - "[[ESTADO_ACTUAL]]"
---

# CHANGELOG — Historial de versiones

Un commit por cambio, **el más reciente arriba**. Convención y plantilla en [[00_MOC_Versiones]].

> Los commits **C-001 a C-039** se reconstruyeron el 2026-11-02 a partir de las fechas de los archivos, sus nombres y el registro de [[Contexto_e_Incongruencias_JackSoft]]. Desde **C-040** se anotan en el momento del cambio.

---

### C-077 · 2026-11-11 · feat(visor-modelo) · resumen de últimos cambios y grills G1/G2
- **Ruta:** `04_Modelado_DB/Visor_Modelo/` (template.html, construir_visor.py, visor_config.json, historial_cambios.json); `chat/` (#013 a #017)
- **Mensaje:** El visor muestra "Últimos cambios": cada versión del modelo con su fecha, su estado (vigente, anterior, en revisión), su origen y sus cambios, con enlaces a las tablas. El visor ahora se arma desde el bd.uml con `construir_visor.py`, que está en el repo (antes dependía de scripts temporales). En el chat: respuesta al grill G1 de Claude Omar (#015, decisiones de Alejandro por cuestionario interactivo), grill G1-2 de vuelta (#016) y grill G2 con 6 notas nuevas del visor (#017). La v4.6 queda en revisión hasta los acuerdos.

### C-076 · 2026-11-04 · docs(chat) · reglas v6: grill interactivo
- **Ruta:** `chat/` (copia de Drive › JackSoft › JackSoft › chat)
- **Mensaje:** Las preguntas del grill van en formato de cuestionario (`Qn | título | pregunta`, de 2 a 4 opciones, la recomendada con `*`). `chat.py preguntas <id>` las convierte en JSON para AskUserQuestion, y quien recibe el grill se las muestra a su usuario como preguntas interactivas, nunca en texto plano. Las respuestas se escriben `Rn | opción | decidió <persona>`. Aviso de sistema #012.

### C-075 · 2026-11-04 · docs(chat) · reglas v5: grill-me cruzado
- **Ruta:** `chat/` (copia de Drive › JackSoft › JackSoft › chat)
- **Mensaje:** Reglas 17 a 22: todo cambio que afecte al otro lado (modelo, reglas de negocio, alcance, decisiones del frontend, reglas del chat) se alinea con un grill en rondas por parte y parte (`grill` → `respuesta-grill` → grill de vuelta → `acuerdo` confirmado por los dos) antes de aplicarse. Las decisiones las toma el usuario de cada agente. `chat.py` muestra ❓ GRILL, 💬 RESPUESTA y 🤝 ACUERDO. Aviso de sistema #011.

### C-074 · 2026-11-04 · fix(diagrama-er) · v8 → v9
- **Ruta:** `04_Modelado_DB/Diagramas/v9_2026-11-04/` — `LaCocaDiagramDB.svg`
- **Mensaje:** Diagrama ER de bd.uml v4.5 (37 tablas, 51 relaciones).

### C-073 · 2026-11-04 · fix(modelo-relacional) · v10 → v11 (DBML v4.5)
- **Ruta:** `04_Modelado_DB/Modelo_Relacional/v11_2026-11-04/` — `bd.uml`, `Cambios_v4.5.md`, `Visor_Interactivo/`
- **Mensaje:** Sale producto_terminado.responsable_id (no lo usa ningún reporte; regla Q1). Se mantiene motivo para anular.

### C-072 · 2026-11-04 · fix(diagrama-er) · v7 → v8
- **Ruta:** `04_Modelado_DB/Diagramas/v8_2026-11-04/` — `LaCocaDiagramDB.svg`
- **Mensaje:** Diagrama ER de bd.uml v4.4 (37 tablas, 52 relaciones).

### C-071 · 2026-11-04 · fix(modelo-relacional) · v9 → v10 (DBML v4.4)
- **Ruta:** `04_Modelado_DB/Modelo_Relacional/v10_2026-11-04/` — `bd.uml`, `Cambios_v4.4.md`, `Visor_Interactivo/`
- **Mensaje:** Respuesta al mensaje #008 de Claude Omar (puntos A a I): vuelven producto_terminado.responsable_id y motivo (pedido del PO); direcciones_cliente.notas guarda apto/torre/piso; se confirman las demás eliminaciones.

### C-070 · 2026-11-04 · fix(diagrama-er) · v6 → v7
- **Ruta:** `04_Modelado_DB/Diagramas/v7_2026-11-04/` — `LaCocaDiagramDB.svg`
- **Mensaje:** Diagrama ER de bd.uml v4.3 (37 tablas, 51 relaciones).

### C-069 · 2026-11-04 · fix(modelo-relacional) · v8 → v9 (DBML v4.3)
- **Ruta:** `04_Modelado_DB/Modelo_Relacional/v9_2026-11-04/` — `bd.uml`, `Cambios_v4.3.md`, `Visor_Interactivo/`
- **Mensaje:** Notas del visor: bloqueo calculado desde accesos (sin detalle ni bloqueado_hasta), sin tokens_restablecimiento (enlace firmado), alergias con lista fija en lugar de restricciones, sin motivo/observación en movimientos ni calificación en entregas. Se mantienen rutas.fecha y tipo_venta.

### C-068 · 2026-11-04 · feat(chat) · formato de chat (reglas v4) y limpieza de Drive
- **Ruta:** `chat/` (copia de Drive › JackSoft › JackSoft › chat); Drive › Modelado(5 trimestre)
- **Mensaje:** El canal pasa a ser un chat entre **Claude Omar** (izquierda) y **Claude Alejo** (derecha). Cada mensaje es un `mensajes/NNN_AAAA-MM-DD_HHMM_autor.txt` con encabezado (fecha y hora, cita, leído hasta, adjuntos, reacciones, pendientes fijados); `_herramientas/chat.py` genera la vista `00_CHAT.txt` con burbujas; los textos largos van en `adjuntos/` y los mensajes anteriores en `anteriores/` (migrados como 001 a 006). Aviso de sistema #007. En Drive se borraron V1, V2 y `99_Archivo_V1_V2` (todo su contenido tenía copia idéntica en 02_HISTORIAL, 01_VIGENTE o el repo).

### C-067 · 2026-11-04 · feat(drive) · versionado de Modelado(5 trimestre)
- **Ruta:** Drive › JackSoft › JackSoft › Modelado(5 trimestre); script `00_Contexto_Versiones/publicar_drive.py`; `chat/` (reglas v3)
- **Mensaje:** Drive pasa de carpetas por fecha (V1, V2) a la estructura del repo: `01_VIGENTE/<Documento>` (con VERSION.txt), `02_HISTORIAL/<Documento>/vNN_AAAA-MM-DD` con todas las versiones del repo (misma numeración), `00_CHANGELOG.md` y `00_LEEME_versionado.md` generados por el script, `03_Exposiciones`, y V1/V2 archivadas intactas en `99_Archivo_V1_V2`. Las reglas del chat pasan a la versión 3 (regla 6), con su aviso al frontend.

### C-066 · 2026-11-04 · fix(diagrama-er) · v5 → v6
- **Ruta:** `04_Modelado_DB/Diagramas/v6_2026-11-04/` — `LaCocaDiagramDB.svg`
- **Mensaje:** Diagrama ER de bd.uml v4.2 (38 tablas, 52 relaciones).

### C-065 · 2026-11-04 · fix(modelo-relacional) · v7 → v8 (DBML v4.2)
- **Ruta:** `04_Modelado_DB/Modelo_Relacional/v8_2026-11-04/` — `bd.uml`, `Cambios_v4.2.md`, `Visor_Interactivo/`
- **Mensaje:** Grilling del flujo de datos (19 decisiones): salen 22 campos que ningún paso posterior usa; nuevo `suspensiones_entrega.origen`; capacidad diaria a Configuración; avisos a consentimientos. Aviso al frontend en `chat/2026-11-04_03_documentacion.md`.

### C-064 · 2026-11-04 · docs(chat) · canal con el frontend: un archivo por mensaje
- **Ruta:** `chat/` (copia oficial en Google Drive › JackSoft › JackSoft › chat)
- **Mensaje:** El conector de Drive no puede modificar archivos existentes: cada mensaje pasa a ser un archivo `AAAA-MM-DD_NN_autor.md` (reglas en `00_LEEME_reglas_del_chat.md`). Se guarda la respuesta del frontend y se responde: pausas confirmadas, plazo de pago configurable (`plazo_pago_cuenta_dia_inicio`, agregado a bd.uml v4.1) y aviso del modelo v4.1.

### C-063 · 2026-11-04 · fix(diagrama-er) · v4 → v5
- **Ruta:** `04_Modelado_DB/Diagramas/v5_2026-11-04/` — `LaCocaDiagramDB.svg`
- **Mensaje:** Diagrama ER de bd.uml v4.1 (38 tablas, 55 relaciones).

### C-062 · 2026-11-04 · fix(modelo-relacional) · v6 → v7 (DBML v4.1)
- **Ruta:** `04_Modelado_DB/Modelo_Relacional/v7_2026-11-04/` — `bd.uml`, `Cambios_v4.1.md`, `Visor_Interactivo/`
- **Mensaje:** Notas de revisión del visor: se eliminan historial_configuraciones, tipos_recipiente (la categoría del producto es la coca) y menu_alternativas (integrada en menu_items con restriccion y reemplaza_item_id). Se mantienen juegos_cocas y recipientes.

### C-061 · 2026-11-04 · fix(diagrama-er) · v3 → v4
- **Ruta:** `04_Modelado_DB/Diagramas/v4_2026-11-04/` — `LaCocaDiagramDB.svg`
- **Mensaje:** Diagrama ER de bd.uml v4.0 agrupado por los 11 procesos en orden del flujo.

### C-060 · 2026-11-04 · fix(modelo-relacional) · v5 → v6 (DBML v4.0, entregable)
- **Ruta:** `04_Modelado_DB/Modelo_Relacional/v6_2026-11-04/` — `bd.uml`, `Cambios_v4.0.md`, `Visor_Interactivo/modelo_la_coca_v4.html`
- **Mensaje:** Máximo 12 columnas por tabla: 46 campos eliminados (técnicos, redundantes o calculados) con su motivo en `Cambios_v4.0.md`. Incidencias con un solo `reportado_por_usuario_id`. TableGroups por proceso en orden del flujo. Visor interactivo con relaciones animadas y notas por tabla: https://claude.ai/artifact/61mqHjLZm1YSZAVvvoqy8t

### C-059 · 2026-11-03 · docs(notas+chat) · ajuste con el frontend
- **Ruta:** notas de Obsidian (RN, diccionario, MOC, índice) y `chat/chat_documentacion_frontend.md (copia oficial en Google Drive › JackSoft › JackSoft › chat)`
- **Mensaje:** RN-05 y RN de corte semanal reescritas; precios, kit, pagos, pausas y zonas actualizados. Nueva carpeta `chat/` con el mensaje para el agente del frontend: decisiones, estados, campos nuevos, claves de configuración y checklist de cambios.

### C-058 · 2026-11-03 · fix(manual-tecnico) · v4 → v5
- **Ruta:** `10_Manual_Tecnico/Documentos_Word/v5_2026-11-03/` — `Manual_Tecnico_v2.3_Jacksoft.docx`
- **Mensaje:** Portada 2.3 y fila en control de cambios. Sin fichas de menú personalizado; "Gestionar suscripciones con pago vencido" y "Publicar menú semanal"; estados Pendiente de pago y Finalizada; C4 v4; numeración igual a la Documentación de CU v4 (229 fichas).

### C-057 · 2026-11-03 · fix(documentacion-casos-uso) · v3 → v4
- **Ruta:** `05_Casos_de_Uso/Especificaciones/Documentacion_Word/v4_2026-11-03/`
- **Mensaje:** 245 fichas renumeradas HU_001–HU_245. Se retiran Seleccionar menú personalizado, Aplicar recargo por menú personalizado y Consultar impacto del menú personalizado; renombres por las reglas nuevas. Repo 05: canónicos, SVG/PNG, MD, visor y draw.io actualizados.

### C-056 · 2026-11-03 · fix(tablero-kanban) · v6 → v7
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Tablero_Kanban/v7_2026-11-03/` — `Tablero Kanban 03_11 v7.xlsx`
- **Mensaje:** "Gestionar suscripciones con pago vencido" (reemplaza Aprobar solicitud fuera de límite) y "Publicar menú semanal". Matriz HU sin menú personalizado, kit de $80.000 y estados nuevos. Responsables y carga equitativa sin cambios (97–98 pts).

### C-055 · 2026-11-03 · fix(ficha-proyecto) · v8 → v9
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Fichas_Tecnicas/v9_2026-11-03/` — `Ficha_Jacksoft_CF_v9.docx`
- **Mensaje:** Kit $80.000 configurable; sin menú personalizado (alternativas por restricción); menú publicado por semana; corte sábado 12:00 m; inicio sin pago para renovación y reingreso (3 días hábiles); estados nuevos de la suscripción; capacidad sin límite por ahora.

### C-054 · 2026-11-03 · fix(arquitectura-c4) · v3 → v4
- **Ruta:** `05_Casos_de_Uso/Arquitectura_C4/v4_2026-11-03/`
- **Mensaje:** Alineado con bd.uml v3.7 (41 clases en el Nivel 4). Módulos 1 y 5 y detalle de suscripciones actualizados (consentimientos, menú semanal y alternativas, corte e inicio sin pago).

### C-053 · 2026-11-03 · fix(diagrama-er) · v2 → v3
- **Ruta:** `04_Modelado_DB/Diagramas/v3_2026-11-03/LaCocaDiagramDB.svg`
- **Mensaje:** Regenerado desde bd.uml v3.7 (41 tablas, 68 relaciones).

### C-052 · 2026-11-03 · fix(modelo-relacional) · v4 → v5
- **Ruta:** `04_Modelado_DB/Modelo_Relacional/v5_2026-11-03/bd.uml` (DBML v3.7)
- **Mensaje:** Ajuste con el frontend según `Analisis_Modelo_vs_Frontend_La_Coca.docx` y las decisiones del equipo: reglas (festivos, corte, inicio sin pago, pausas, precios, sin menú personalizado, capacidad opcional, proveedores por categoría), estados alineados, producción por líneas, publicación semanal del menú y tablas nuevas (consentimientos, tokens_restablecimiento, proveedor_categorias, menus_semana, menu_alternativas, direccion_dias). 41 tablas y 68 relaciones; validado con @dbml/core.

### C-051 · 2026-11-03 · fix(tablero-kanban) · v5 → v6
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Tablero_Kanban/v6_2026-11-03/`
- **Archivos:** `Tablero Kanban 03_11.xlsx`
- **Mensaje:** Responsable por módulo con carga equitativa (97–98 puntos y 31–32 historias por integrante), en la fila 21 del Story Mapping, con un cuadro "Carga por integrante" calculado en vivo (filas 27–34). La columna Responsable del Backlog se llena sola desde esa fila.
  - Alejandro Gómez: Usuarios, Clientes, Suscripciones, Incidencias (4 módulos · 31 historias · 98 pts)
  - Omar Meneses: Producción (orden), Ficha técnica, Servicio, Menú (4 · 31 · 98)
  - Erick Camargo: Roles, Configuraciones del sistema, Insumos, Producto terminado, Dashboard (5 · 32 · 98)
  - Luis Gabriel Mesa: Categoría productos, Proveedores, Categoría de servicios, Domiciliarios, Monitoreo y rutas (5 · 32 · 97)
  - Samuel Morales: Acceso, Categoría de insumos, Productos, Compras, Calendario (5 · 31 · 97)

### C-050 · 2026-11-02 · feat(documentacion-vigente) · v1
- **Ruta:** `00_Documentacion_Vigente/` (generada) y `00_Contexto_Versiones/actualizar_vigente.py`
- **Mensaje:** Carpeta con una copia de la última versión de cada documento (20 documentos más el draw.io y los PNG de casos de uso). Se regenera con `python3 00_Contexto_Versiones/actualizar_vigente.py` después de cada cambio.

### C-049 · 2026-11-02 · docs(notas) · cambio de alcance
- **Ruta:** notas de Obsidian de 00, 02, 04, 05, 06 y 10
- **Mensaje:** Notas y MOC actualizados al alcance de la Ficha v8. Nuevas notas [[DB_Tabla_Configuraciones_Sistema]] y [[DB_Tablas_Menu]]. Las RN de cocas, suscripciones, suspensiones y domiciliarios indican qué valores pasan a ser configurables. Decisión D-F registrada en [[Contexto_e_Incongruencias_JackSoft]] (sección 9).

### C-048 · 2026-11-02 · fix(manual-tecnico) · v3 → v4
- **Ruta:** `10_Manual_Tecnico/Documentos_Word/v4_2026-11-02/`
- **Archivos:** `Manual_Tecnico_v2.2_Jacksoft.docx` (el equipo lo llamaría "v2.2")
- **Mensaje:** Portada "Versión 2.2" y fila en el control de cambios. Mockups sin Empleados (figuras renumeradas 14–21) y con Configuraciones del sistema y Menú (pendiente la vista en Figma); diagramas de casos de uso sin Empleados y con los dos nuevos; imágenes C4 de la v3; fichas sin Empleados ni Asignar permisos, con las nuevas y con la misma numeración de la Documentación de CU v3; descripciones de los macroprocesos actualizadas. Los comentarios de la evaluadora se conservan.

### C-047 · 2026-11-02 · fix(arquitectura-c4) · v2 → v3
- **Ruta:** `05_Casos_de_Uso/Arquitectura_C4/v3_2026-11-02/`
- **Mensaje:** Alineado con `bd.uml` v3.6. Módulo 1 → "Acceso y configuración" (sin empleados, con configuraciones del sistema); módulo 5 → "Clientes, suscripciones y menú" (con MenuController/Service/Repository en el detalle). Nivel 4 regenerado desde v3.6 (36 clases). PNG redibujados con Graphviz (viz.js); el Nivel 1 no cambia.

### C-046 · 2026-11-02 · fix(documentacion-casos-uso) · v2 → v3
- **Ruta:** `05_Casos_de_Uso/Especificaciones/Documentacion_Word/v3_2026-11-02/`
- **Mensaje:** 248 fichas renumeradas HU_001–HU_248 en orden del documento. Retiradas Permisos, Asignar permisos al rol y Empleados. Nuevas Configuraciones del sistema, Menú y Aprobar solicitud fuera de límite. Se agregó "Generar reporte de clientes", que solo estaba en el manual.

### C-045 · 2026-11-02 · fix(casos-de-uso) · repo `05_Casos_de_Uso`
- **Ruta:** `05_Casos_de_Uso/` (sistema generado, versionado por su propio git)
- **Mensaje:** Lista canónica de 23 subprocesos (−EMPLEADOS, +CONFIGURACIONES DEL SISTEMA, +MENU). Regenerados PUML/SVG, PNG nuevos (captura del SVG, igual que los existentes), CU_01/03/05 en MD, `casos_de_uso_v3/`, visor web y draw.io (nuevos diagramas con el estilo del equipo). Lo anterior quedó respaldado en `05_Casos_de_Uso/_Historial/`. El SVG multifase obsoleto del visor (aún con Permisos y Empleados) pasó a `_Historial/Obsoletos/`.

### C-044 · 2026-11-02 · fix(diagrama-er) · v1 → v2
- **Ruta:** `04_Modelado_DB/Diagramas/v2_2026-11-02/`
- **Archivos:** `LaCocaDiagramDB.svg`
- **Mensaje:** Generado desde `bd.uml` v3.6 (36 tablas, 56 relaciones), agrupado por subproceso. Reemplaza al de 37 tablas del 21 de agosto.

### C-043 · 2026-11-02 · fix(modelo-relacional) · v3 → v4
- **Ruta:** `04_Modelado_DB/Modelo_Relacional/v4_2026-11-02/`
- **Archivos:** `bd.uml` (DBML v3.6)
- **Mensaje:** Se elimina `empleados`; sus FK pasan a `usuarios`; cierre semanal de suscripciones (4 configuraciones y campos `fecha_solicitud`, `fuera_de_limite`, `aprobacion_fuera_limite`, `aprobada_por_usuario_id`) (`ordenes_produccion.usuario_responsable_id`, domiciliario en rutas, entregas, GPS e incidencias). Nuevas `configuraciones_sistema` e `historial_configuraciones` (enum `tipo_valor_configuracion`). `menus_diarios` y `menu_items` pasan al grupo Menú; `menus_diarios.semana_inicio`. 23 subprocesos. Validado con @dbml/core.

### C-042 · 2026-11-02 · fix(tablero-kanban) · v4 → v5
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Tablero_Kanban/v5_2026-11-02/`
- **Archivos:** `Tablero Kanban 02_11.xlsx`
- **Mensaje:** Story Mapping de 23 subprocesos y 157 historias, hasta 12 por subproceso (−EMPLEADOS; +CONFIGURACIONES DEL SISTEMA; +MENU; −Asignar permisos; +Aprobar solicitud fuera de límite; "No coincide con el MockUp" pasa a comentario). Fórmulas del Backlog ampliadas a D:AW y filas 7–18 (acumulado en la fila 20). Formato Matriz HU reconstruida y renumerada: 194 HU, actores por rol, rangos hasta la fila 700.

### C-041 · 2026-11-02 · fix(ficha-proyecto) · v7 → v8
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Fichas_Tecnicas/v8_2026-11-02/`
- **Archivos:** `Ficha_Jacksoft_CF_v8_alcance.docx`
- **Mensaje:** Documento raíz de la cascada (versión oficial). Roles sin permisos; Configuraciones del sistema incluye el cierre semanal de suscripciones. Se quitan los subprocesos Empleados, Permisos y Categoría de proveedor; se agregan Configuraciones del sistema (Configuración), Menú (Ventas) y Consulta de menú (Mobile). Objetivos 1, 5 y 6 ajustados; Usuarios aclara que el personal es un usuario con rol.
- **Origen:** decisión del equipo (D-F): Empleados no tenía impacto real en el sistema.

### C-040 · 2026-11-02 · refactor(estructura) · reorganización por versiones
- **Ruta:** toda la documentación
- **Mensaje:** Cada documento queda en carpetas `vN_AAAA-MM-DD`. Se crea `00_Contexto_Versiones/` (este historial, el estado actual y la convención). No se modificó el contenido de ningún documento; solo se movieron archivos y se actualizaron las rutas citadas en las notas y MOCs.
- **Detalle:**
  - `04_Modelado_DB/DBML/` y `04_Modelado_DB/modelo 5 trimestre/` → `04_Modelado_DB/Modelo_Relacional/v1…v3`.
  - `05_Casos_de_Uso/Arquitectura_C4/Version_V2/` → `Arquitectura_C4/v1_2026-09-14/`; los archivos C4 de la raíz → `v2_2026-10-30/`. La guía `Diagramas C4.pptx.txt` (estaba suelta en la raíz) → `Arquitectura_C4/Referencia/`.
  - `Tablero Kanban 13_09.xlsx` de la raíz (editado el 23 oct, distinto del de `06`) → `Tablero_Kanban/v4_2026-10-23/`.
  - `DocumentacionPrimerosPrototipos/` (repo `Mapa-procesos-`) → completo con su `.git` en `03_Procesos/App_Mapa_Procesos/v1_2026-06-16/`.
  - `Presentacion_Artefactos/Artefactos/` (repo `artefactos`) → completo con su `.git` en `Presentacion_Artefactos/v1_2026-07-27/`.
  - `08_Entregables_e_Informes/Versiones_Anteriores/` se eliminó; su contenido pasó a `Plantilla_Informe/v1_2026-08-11/`.
  - Duplicado exacto `jacksoft_modelo_relacional.dbml` (idéntico a la v2) → `09_Backups_y_Archivos_Zips/Duplicados_Reorganizacion_2026-11-02/`.

### C-039 · 2026-10-30 · fix(ficha-proyecto) · v6 → v7
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Fichas_Tecnicas/v7_2026-10-30/`
- **Archivos:** `Ficha_3agosto Jacksoft CF_v2_festivos.docx`
- **Mensaje:** Copia de la ficha aprobada con las dos frases de festivos corregidas según RN-02 (el festivo se descuenta del precio y el vencimiento no se mueve). La v6 con VoBo no se tocó.

### C-038 · 2026-10-30 · fix(arquitectura-c4) · v1 → v2
- **Ruta:** `05_Casos_de_Uso/Arquitectura_C4/v2_2026-10-30/`
- **Archivos:** `Arquitectura_C4_JackSoft.md`, `C4_Nivel1…4*.puml` (5), `Evidencia_C4_PNG/` (5 PNG)
- **Mensaje:** C4 rehecho según la guía (niveles 1 a 4), alineado con `bd.uml` v3.5. Se agrega el detalle de suscripciones en el nivel 3. PNG dibujados con Graphviz como evidencia.

### C-037 · 2026-10-30 · fix(modelo-relacional) · v2 → v3
- **Ruta:** `04_Modelado_DB/Modelo_Relacional/v3_2026-10-30/`
- **Archivos:** `bd.uml` (DBML v3.5)
- **Mensaje:** Pasa a ser el modelo vigente: 35 tablas, 53 relaciones, 22 TableGroups (= 22 subprocesos). Acceso único por `usuarios`, sin tablas de permisos, el domiciliario como rol, kardex con motivo controlado, cocas, alergias, producto terminado y festivos según RN-02 (`dias_facturables`, `descuento_festivos`).

### C-036 · 2026-10-23 · fix(tablero-kanban) · v3 → v4
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Tablero_Kanban/v4_2026-10-23/`
- **Archivos:** `Tablero Kanban 13_09.xlsx`
- **Mensaje:** Edición posterior del tablero 13_09, con el mismo nombre y las mismas hojas (452 KB contra 398 KB de la v3). Estaba suelto en la raíz. **Cambios sin documentar:** falta anotar qué se modificó.

### C-035 · 2026-09-28 · fix(app-mapa-procesos) · v1 → v2
- **Ruta:** `03_Procesos/App_Mapa_Procesos/v2_2026-09-28/`
- **Archivos:** `index.html`, `index.css`, `main.js`, `la-coca-de-jack-pitch.html`, `mapa_procesos_lacoca_v2.svg`
- **Mensaje:** Copia del aplicativo de procesos dentro del vault, con `index.html` ajustado. CSS, JS, pitch y SVG son iguales a la v1.

### C-034 · 2026-09-25 · fix(manual-tecnico) · v2 → v3
- **Ruta:** `10_Manual_Tecnico/Documentos_Word/v3_2026-09-25/`
- **Archivos:** `Manual_Tecnico_v2.1_Jacksoft.docx` (el equipo lo llama "v2.1")
- **Mensaje:** Fichas de casos de uso corregidas y conciliadas con los diagramas. ⭐ Fuente de verdad del manual. Bitácora en [[Correcciones_Manual_Tecnico_v1]].

### C-033 · 2026-09-25 · fix(manual-tecnico) · v1 → v2
- **Ruta:** `10_Manual_Tecnico/Documentos_Word/v2_2026-09-25/`
- **Archivos:** `Manual_Tecnico_v2_septiembre_25.docx`
- **Mensaje:** Los 22 diagramas de casos de uso rehechos en draw.io, mockups descritos y figuras numeradas (1–22). Se quitan los comentarios C9–C14.

### C-032 · 2026-09-23 · feat(manual-tecnico) · v1
- **Ruta:** `10_Manual_Tecnico/Documentos_Word/v1_2026-09-23/`
- **Archivos:** `Manual_Tecnico_v1_Jacksoft.docx`
- **Mensaje:** Versión entregada, con los comentarios de la instructora y de la evaluadora (C4, C9–C14, C40–C41).

### C-031 · 2026-09-14 · feat(arquitectura-c4) · v1
- **Ruta:** `05_Casos_de_Uso/Arquitectura_C4/v1_2026-09-14/`
- **Archivos:** `Arquitectura_C4_JackSoft.md` y niveles 1–4 en `.puml` / `.svg` / `.png`
- **Mensaje:** Primera arquitectura C4, basada en el modelo de BD V2 (antes estaba en la carpeta `Version_V2/`).

### C-030 · 2026-09-14 · fix(documentacion-casos-uso) · v1 → v2
- **Ruta:** `05_Casos_de_Uso/Especificaciones/Documentacion_Word/v2_2026-09-14/`
- **Archivos:** `Documentacion_Casos_de_Uso_JackSoft.docx`
- **Mensaje:** 243 fichas HU_001–HU_243 (las mismas del Manual v1/v2).

### C-029 · 2026-09-13 · fix(tablero-kanban) · v2 → v3
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Tablero_Kanban/v3_2026-09-13/`
- **Archivos:** `Tablero Kanban 13_09.xlsx`
- **Mensaje:** Backlog, Kanban, Avance, Story Mapping v03 (22 módulos / 135 historias) y Matriz HU (22 subprocesos / 186 HU). Revisado el 24 sep. Reemplaza a la Matriz HU independiente.

### C-028 · 2026-09-13 · fix(ficha-proyecto) · v5 → v6
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Fichas_Tecnicas/v6_2026-09-13/`
- **Archivos:** `Ficha_3agosto Jacksoft CF.docx`, `Ficha_3agosto Jacksoft CF.pdf`
- **Mensaje:** Ficha con **VoBo de requisitos del 10/09/2026** (Newton Pomare). Alcance: 8 procesos, 26 subprocesos web y 5 mobile.

### C-027 · 2026-09-01 · fix(plantilla-informe) · v1 → v2
- **Ruta:** `08_Entregables_e_Informes/Informes_Academicos/Plantilla_Informe/v2_2026-09-01/`
- **Archivos:** `PlantillaInforme.docx`

### C-026 · 2026-08-31 · feat(documentacion-casos-uso) · v1
- **Ruta:** `05_Casos_de_Uso/Especificaciones/Documentacion_Word/v1_2026-08-31/`
- **Archivos:** `Documentacion_Casos_de_Uso_JackSoft_31ago.docx`

### C-025 · 2026-08-25 · feat(rubrica-investigacion) · v1
- **Ruta:** `08_Entregables_e_Informes/Informes_Academicos/Rubrica_Investigacion/v1_2026-08-25/`
- **Archivos:** `rubrica_investigacion_objetivos.txt`

### C-024 · 2026-08-25 · fix(mapa-mental) · v1 → v2
- **Ruta:** `01_Investigacion_y_Analisis/Diagramas/Mapa_Mental/v2_2026-08-25/`
- **Archivos:** `mapa_mental_1.svg`, `mapa_mental.png`
- **Mensaje:** Mapa mental ampliado (30 KB contra 12 KB de la v1), con exportación a PNG.

### C-023 · 2026-08-25 · feat(arbol-objetivos) · v1
- **Ruta:** `01_Investigacion_y_Analisis/Diagramas/Arbol_de_Objetivos/v1_2026-08-25/`
- **Archivos:** `arbol_objetivos.svg`, `arbol_objetivos.png`
- **Mensaje:** Generado con `01_Investigacion_y_Analisis/scripts/generar_arbol_objetivos.py` a partir del árbol de problemas.

### C-022 · 2026-08-24 · feat(facilitacion-grafica) · v1
- **Ruta:** `07_Diseno_y_Mockups/Facilitacion_Grafica/v1_2026-08-24/`
- **Archivos:** `FacilitacionGrafica.jpeg` (9 jul), `tablero_ajedrez.svg`, `image.png`

### C-021 · 2026-08-24 · fix(modelo-relacional) · v1 → v2
- **Ruta:** `04_Modelado_DB/Modelo_Relacional/v2_2026-08-24/`
- **Archivos:** `jacksoft_modelo_relacional_v2.dbml`
- **Mensaje:** Versión consolidada: 33 tablas adaptadas a los módulos vigentes. Fue el modelo vigente hasta el 30 oct.

### C-020 · 2026-08-21 · feat(diagrama-er) · v1
- **Ruta:** `04_Modelado_DB/Diagramas/v1_2026-08-21/`
- **Archivos:** `LaCocaDiagramDB.svg`
- **Mensaje:** Diagrama relacional completo (37 tablas). No coincide del todo con ningún DBML (ver incongruencias I-25 a I-31).

### C-019 · 2026-08-21 · fix(tablero-kanban) · v1 → v2
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Tablero_Kanban/v2_2026-08-21/`
- **Archivos:** `Tablero Kanban + Matriz HU (Agosto 21)).xlsx`, `… - Story Mapping.numbers`, `… - Story Mapping.csv`
- **Mensaje:** Integra la Matriz HU y el Story Mapping en el tablero.

### C-018 · 2026-08-14 · fix(ficha-proyecto) · v4 → v5
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Fichas_Tecnicas/v5_2026-08-14/`
- **Archivos:** `formato ficha proyecto  14agosto.docx`, `formato ficha proyecto  14agosto.md` (conversión del 24 ago)

### C-017 · 2026-08-13 · feat(modelo-relacional) · v1
- **Ruta:** `04_Modelado_DB/Modelo_Relacional/v1_2026-08-13/`
- **Archivos:** `jacksoft_modelo_relacional_v1.dbml`
- **Mensaje:** Versión inicial (33 tablas).

### C-016 · 2026-08-12 · feat(matriz-hu) · v1
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Matriz_HU/v1_2026-08-12/`
- **Archivos:** `Matriz_Historias_de_Usuario_actualizada.xlsx`
- **Mensaje:** 159 HU, con la taxonomía vieja (7 procesos / 25 subprocesos). Desde C-029 la reemplaza la Matriz HU del Tablero Kanban.

### C-015 · 2026-08-11 · feat(plantilla-informe) · v1
- **Ruta:** `08_Entregables_e_Informes/Informes_Academicos/Plantilla_Informe/v1_2026-08-11/`
- **Archivos:** `PlantillaInforme_v1_11ago.docx`, `PlantillaInforme.docx.md` (conversión), `informe.txt` (texto plano)

### C-014 · 2026-08-11 · fix(analisis-5w1h) · v1 → v2
- **Ruta:** `01_Investigacion_y_Analisis/Diagramas/Analisis_5W1H/v2_2026-08-11/`
- **Archivos:** `slide_5w1h.svg`

### C-013 · 2026-08-11 · feat(mapa-mental) · v1
- **Ruta:** `01_Investigacion_y_Analisis/Diagramas/Mapa_Mental/v1_2026-08-11/`
- **Archivos:** `mapa_mental.svg`

### C-012 · 2026-08-11 · feat(arbol-problemas) · v1
- **Ruta:** `01_Investigacion_y_Analisis/Diagramas/Arbol_de_Problemas/v1_2026-08-11/`
- **Archivos:** `arbol_problemas.svg`, `arbol_problemas.png` (exportado el 25 ago)

### C-011 · 2026-08-10 · feat(tablero-kanban) · v1
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Tablero_Kanban/v1_2026-08-10/`
- **Archivos:** `Tablero kanban Agosto 10.xlsx`

### C-010 · 2026-08-09 · feat(mockups) · v1
- **Ruta:** `07_Diseno_y_Mockups/Mockups/v1_2026-08-09/`
- **Archivos:** `Mokup url.docx`, `headerGoogleForms.png`, `headerGoogleForms.svg`

### C-009 · 2026-08-04 · feat(analisis-5w1h) · v1
- **Ruta:** `01_Investigacion_y_Analisis/Diagramas/Analisis_5W1H/v1_2026-08-04/`
- **Archivos:** `slide_5w1h_1.svg`

### C-008 · 2026-08-03 · fix(ficha-proyecto) · v3 → v4
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Fichas_Tecnicas/v4_2026-08-03/`
- **Archivos:** `Copia de Ficha_3agosto.docx`, `Copia de Ficha_3agosto.docx.md` (conversión del 13 ago)

### C-007 · 2026-07-30 · fix(ficha-proyecto) · v2 → v3
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Fichas_Tecnicas/v3_2026-07-30/`
- **Archivos:** `Copia de JackSoft_Ficha_Proyecto_30julio.docx`

### C-006 · 2026-07-27 · feat(presentacion-artefactos-scrum) · v1
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Presentacion_Artefactos/v1_2026-07-27/`
- **Archivos:** `index.html`, `URL.txt`, `assets/` (4 PNG). Tiene su propio repo git (`artefactos`).

### C-005 · 2026-07-24 · fix(ficha-proyecto) · v1 → v2
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Fichas_Tecnicas/v2_2026-07-24/`
- **Archivos:** `Formato_Ficha_Proyecto_jackSoft_24julio.docx`

### C-004 · 2026-06-16 · feat(app-mapa-procesos) · v1
- **Ruta:** `03_Procesos/App_Mapa_Procesos/v1_2026-06-16/`
- **Archivos:** sitio completo (`index.html`, `index.css`, `main.js`, pitch, SVG) más los entregables que enlaza (ficha v1, ensayos). Es el repo git `Mapa-procesos-` (antes `DocumentacionPrimerosPrototipos/`).

### C-003 · 2026-06-16 · feat(ensayo-que-son-los-requisitos) · v1
- **Ruta:** `08_Entregables_e_Informes/Ensayos_y_Monografias/Que_Son_Los_Requisitos/v1_2026-06-16/`
- **Archivos:** `¿Qué son los requisitos_.docx`, `.docx.pdf`

### C-002 · 2026-06-16 · feat(ensayo-importancia-conocer-en-detalle) · v1
- **Ruta:** `08_Entregables_e_Informes/Ensayos_y_Monografias/Importancia_Conocer_en_Detalle/v1_2026-06-16/`
- **Archivos:** `Por qué es importante conocer en detalle.docx`, `.docx.pdf`

### C-001 · 2026-06-16 · feat(ficha-proyecto) · v1
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Fichas_Tecnicas/v1_2026-06-16/`
- **Archivos:** `Formato_Ficha_Proyecto_jackSoft.docx`, `Formato_Ficha_Proyecto_jackSoft.docx.pdf`
- **Mensaje:** Primer formato de ficha de proyecto.
