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

### C-124 · 2026-11-20 · docs(drive+chat) · publicación y aviso #037 a Claude Omar
- **Ruta:** `00_Contexto_Versiones/publicar_drive.py`, `chat/mensajes/037_…`, carpeta chat de Drive
- **Mensaje:** Se publican el Kanban v12, el CU Word v9, el manual v11 y los diagramas de casos de uso. El #037 le avisa a Omar que la documentación de Permisos dentro de Roles quedó lista y cierra su pendiente 24.

### C-123 · 2026-11-20 · docs(notas) · Permisos dentro de Roles en estado, índice y cascada
- **Ruta:** `00_Contexto_Versiones/ESTADO_ACTUAL.md`, `CASCADA_DOCUMENTAL.md`, `00_INDICE_GENERAL.md`, `10_Manual_Tecnico/Auditoria_y_Control_Calidad/Faltantes_Manual_v6.md`
- **Mensaje:** Vigentes al día (Kanban v12, CU Word v9, manual v11) y se cierra el pendiente de Permisos.

### C-122 · 2026-11-20 · fix(manual-tecnico) · v10 → v11 (archivo "v2.8")
- **Ruta:** `10_Manual_Tecnico/Documentos_Word/v11_2026-11-20/` — `Manual_Tecnico_v2.8_Jacksoft.docx`; fuente del mockup en `07_Diseno_y_Mockups/Mockups_Fuente/mock_roles_permisos.html`
- **Mensaje:** Mockup nuevo de Permisos: pantalla "Editar rol: Cocina" con el nombre, el estado y la matriz de permisos en el mismo formulario, sin ítem Permisos en el menú, y botón "Guardar rol" (mismo estilo y tamaño, 2048×964). Sección "Permisos (dentro de Roles)" y pie de figura reescritos. Diagrama de casos de uso de Permisos: el caso central pasa a "Permisos en Roles". Las mismas fichas que el CU Word v9. Portada "Versión 2.8" y fila nueva en el control de cambios.

### C-121 · 2026-11-20 · fix(documentacion-cu) · v8 → v9 (repo 05)
- **Ruta:** `05_Casos_de_Uso/Especificaciones/Documentacion_Word/v9_2026-11-20/`
- **Mensaje:** Las fichas HU_246 a HU_253 se usan desde el formulario de crear o editar rol (ya no desde la opción "Permisos" del menú). La precondición pide el permiso sobre el módulo Roles. El rol Administrador no se edita, y Guardar rol guarda el nombre y los permisos juntos. HU_001 (Crear rol) y HU_004 (Editar rol) incluyen la matriz. La sección pasa a llamarse "Permisos (en Roles)". Siguen siendo 250 fichas.

### C-120 · 2026-11-20 · fix(tablero-kanban + casos-uso) · Kanban v11 → v12 y diagrama de Permisos
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Tablero_Kanban/v12_2026-11-20/`, `05_Casos_de_Uso/scripts/actualizar_casos_uso_canonicos.py`, diagramas PUML/SVG/PNG de PERMISOS, visor y `Diagramas_DrawIO/Casos_de_usos.drawio`
- **Mensaje:** Acuerdo con Claude Omar (#034/#036): Permisos se gestiona dentro de Roles, sin pantalla propia. En el Story Mapping, la columna pasa a "PERMISOS (EN ROLES)", con las mismas 8 historias. En la Matriz HU, la épica 01.3 y 11 criterios dicen "en el formulario de crear y editar rol", y HU01.1_01 y HU01.1_03 incluyen la matriz. Los conteos no cambian. En los casos de uso, el caso central pasa de "Gestión de permisos" a "Permisos en Roles" (también en el draw.io).

### C-119 · 2026-11-20 · docs(chat) · G5 pasa a #035; reporte #036 a Claude Omar
- **Ruta:** `chat/` (#034 de Claude Omar, #035, #036, `adjuntos/035_grill-G5.md`, `adjuntos/036_ajustes-20nov-incidencias-y-kanban.md`) y la carpeta chat de Drive
- **Mensaje:** El #034 de Claude Omar (19-nov: Permisos se gestiona dentro de Roles) estaba en Drive y no en el repo, y el grill G5 había salido local con el mismo número sin llegar a Drive. Se trajo su #034, el G5 pasó a #035 (pendiente 25) y su punto 1 dice ahora que Alejandro acepta Permisos dentro de Roles. El #036 le informa a Omar los ajustes C-112 a C-118 (Responder incidencia, responsables, versiones vigentes) y le pregunta Q7 a Q9 (dónde va "Responder", estados de incidencia y fecha de respuesta). Chat sincronizado con Drive. **Pendiente:** ajustar la documentación de Permisos "en Roles" (Kanban, casos de uso, draw.io, CU Word, mockup del manual).

### C-118 · 2026-11-20 · docs(drive) · se publican en Drive los vigentes del 20-nov
- **Ruta:** `00_Contexto_Versiones/publicar_drive.py` → Drive › JackSoft › JackSoft › Modelado(5 trimestre)
- **Mensaje:** Antes de publicar se revisó `01_VIGENTE`: el equipo había editado en Drive el `Tablero Kanban 18_11 v9.xlsx` el 19-nov (responsables y "Responder incidencia"). Esos cambios se pasaron al repo (C-112 a C-117) y luego se publicaron la ficha v12, el Kanban v11, el CU Word v8, la C4 v7, el modelo v15, el ER v12, el manual v10 y el diccionario v3. La copia editada de la v9 sale de `01_VIGENTE` (Drive la guarda en la papelera); su contenido quedó en la v11 y el archivo original en `09_Backups_y_Archivos_Zips/Drive_GoogleSheets/Tablero Kanban 18_11 v9 (editado en Drive 2026-11-19).xlsx`.

### C-117 · 2026-11-20 · docs(notas) · índice general al día
- **Ruta:** `00_INDICE_GENERAL.md`
- **Mensaje:** Las líneas "⭐ vigente" del modelo, el ER, el CU Word, la C4, la ficha, el Kanban y el manual estaban atrasadas (algunas seguían en las versiones del 3-nov). Ahora apuntan a las vigentes de [[ESTADO_ACTUAL]].

### C-116 · 2026-11-20 · fix(modelo-relacional) · v14 → v15 (sigue siendo DBML v4.8)
- **Ruta:** `04_Modelado_DB/Modelo_Relacional/v15_2026-11-20/` — `bd.uml`, `Cambios_v4.8.md`, `Visor_Interactivo/`
- **Mensaje:** Sin cambios de estructura. La nota de `incidencias` dice "Responder incidencia" en lugar de "Registrar incidencia" (la reportan el cliente y el domiciliario). Se conserva la etiqueta v4.8 para no mover las referencias del diccionario, la C4 y el manual; el ER v12 sigue siendo válido (no muestra notas). Visor regenerado.

### C-115 · 2026-11-20 · fix(manual-tecnico) · v9 → v10 (archivo "v2.7")
- **Ruta:** `10_Manual_Tecnico/Documentos_Word/v10_2026-11-20/` — `Manual_Tecnico_v2.7_Jacksoft.docx`
- **Mensaje:** Ficha HU_218 reescrita como "Responder incidencia" (objetivo, precondiciones, flujo, excepciones; incluye Ver detalle de incidencia). En el diagrama de casos de uso de Incidencias, "Crear incidencias" pasa a "Responder incidencia" (se corrigió el texto en la imagen, igual al draw.io). Descripción del módulo: consultar, clasificar, responder y resolver; reportan el cliente y el domiciliario. Portada "Versión 2.7" y fila nueva en el control de cambios.

### C-114 · 2026-11-20 · fix(documentacion-cu) · v7 → v8 (repo 05)
- **Ruta:** `05_Casos_de_Uso/Especificaciones/Documentacion_Word/v8_2026-11-20/`
- **Mensaje:** HU_218 "Registrar incidencia" → "Responder incidencia", con la ficha reescrita (el administrador responde la incidencia que reportó un cliente o un domiciliario; se guarda quién respondió y se notifica por web push). Siguen siendo 250 fichas.

### C-113 · 2026-11-20 · fix(casos-uso) · Incidencias: Responder incidencia (repo 05)
- **Ruta:** `05_Casos_de_Uso/scripts/actualizar_casos_uso_canonicos.py`, `Diagramas_PUML/INCIDENCIAS.puml`, `Diagramas_SVG/INCIDENCIAS.svg`, `Diagramas_PNG/INCIDENCIAS.png`, MD, visor y `Diagramas_DrawIO/Casos_de_usos.drawio`
- **Mensaje:** Lista canónica igual al Story Mapping v11. "Responder incidencia" queda como extensión de Listar incidencias. En el draw.io, la elipse "Crear incidencias" pasa a "Responder incidencia". PNG capturado del SVG a 1050×750.

### C-112 · 2026-11-20 · fix(tablero-kanban) · v10 → v11
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Tablero_Kanban/v11_2026-11-20/` — `Tablero Kanban 20_11 v11.xlsx`
- **Mensaje:** Se pasan al repo los cambios que el equipo hizo en Drive el 19-nov sobre la v9: responsables reasignados en 17 de los 24 subprocesos (fila 21 del Story Mapping) y "Registrar incidencia" → "Responder incidencia". En la Matriz HU, HU07.3_06 se reescribe como responder incidencia (CA07.3_06_01 y _02) y CA07.3_03_02 pide una respuesta antes de marcar Resuelta. Mismos conteos (159 historias, 515 puntos, 190 HU, 500 criterios). Editado sobre el XML para conservar los gráficos; recalcula al abrir en Excel.

### C-111 · 2026-11-20 · docs(chat) · grill G5 a Claude Omar: cambios del frontend
- **Ruta:** `chat/` (#034 y `adjuntos/034_grill-G5.md`)
- **Mensaje:** Lista de los cambios que el frontend debe hacer tras el grill de discrepancias del 20-nov, y aviso del modelo v4.8 (reemplazar su `docs/bd.uml` v3.6).

### C-110 · 2026-11-20 · docs(notas) · reglas, índice y DB al día con la v4.8
- **Ruta:** `00_INDICE_GENERAL.md`, `02_Reglas_de_Negocio/` (RN_Limite_Suscripcion_Semanal, RN_Suscripciones_y_Menus, RN_Domiciliarios_y_Rutas, RN_Pagos_y_Comprobantes, MOC, QA), `03_Procesos/Documentos/`, `01_Investigacion_y_Analisis/Documentos/` (requisitos), `04_Modelado_DB/Diccionario_y_Tablas/` (Esquema, Configuraciones, Suscripciones, MOC)
- **Mensaje:** Kit de cocas $70.000 → $80.000 donde quedaba. Solo Bancolombia (sale Nequi). Cupo semanal con lista de espera, preferencia de proteína (+$10.000 por plan), rutas = zonas y configuraciones fijas. El índice y el MOC del modelo apuntan a bd.uml v4.8. El "157 vs 192" no se cambia: son historias del Story Mapping frente a filas de la matriz.

### C-109 · 2026-11-20 · fix(manual-tecnico) · v8 → v9 (archivo "v2.6")
- **Ruta:** `10_Manual_Tecnico/Documentos_Word/v9_2026-11-20/` — `Manual_Tecnico_v2.6_Jacksoft.docx`
- **Mensaje:** Modelo v4.8 y diccionario de 43 tablas. Los 6 diagramas de casos de uso que cambiaron se redibujaron desde el draw.io (Configuraciones, Producción, Producto terminado, Suscripciones, Menú y Dashboard); en el lugar de Producción había por error un diagrama viejo de ficha técnica. C4 v7 (contexto, contenedores, componentes y clases). Fichas: salen HU_019, 021, 024, 025 y 026; se reescriben 10 y entran HU_256 a HU_259 (234 fichas). Textos de los módulos al día. Portada "Versión 2.6" y fila nueva en el control de cambios.

### C-108 · 2026-11-20 · fix(diccionario-datos) · v2 → v3 (v4.8)
- **Ruta:** `04_Modelado_DB/Diccionario_y_Tablas/Documento_Word/v3_2026-11-20/` — `Diccionario_de_Datos_JackSoft_v4.8.docx`
- **Mensaje:** Tablas nuevas faltantes_insumos y dispositivos_push (43 tablas). Campos clientes.preferencia_proteina y menu_items.proteina; estado en_espera; valor_plan con el recargo. Descripciones de configuraciones (fijas), ordenes_produccion (generada desde el menú, anulada), producto_terminado y rutas (= zonas). Relaciones nuevas en usuarios, insumos y ordenes_produccion.

### C-107 · 2026-11-20 · fix(arquitectura-c4) · v6 → v7 (repo 05)
- **Ruta:** `05_Casos_de_Uso/Arquitectura_C4/v7_2026-11-20/`
- **Mensaje:** App móvil pendiente: el domiciliario y el cliente usan la web (GPS desde el navegador). Sistema externo nuevo: Servicios Web Push (VAPID); Firebase queda para la app. BD bd.uml v4.8 con 43 tablas. N3: producción generada desde el menú con faltantes, cupo semanal y lista de espera, proteína, rutas = zonas, dashboard con proyección y costo por zona. N4: 43 clases (FaltanteInsumo, DispositivoPush). PNG redibujados con Graphviz.

### C-106 · 2026-11-20 · fix(documentacion-cu) · v6 → v7 (repo 05)
- **Ruta:** `05_Casos_de_Uso/Especificaciones/Documentacion_Word/v7_2026-11-20/`
- **Mensaje:** Salen 5 fichas de Configuraciones (HU_019, 021, 024, 025 y 026). Se reescriben HU_081 (orden desde el menú publicado), 084, 102, 165, 183 (cupo semanal), 197 (rutas desde las zonas), 200, 241, 242 y 243. Entran HU_256 Gestionar lista de espera por cupo, HU_257 Elegir preferencia de proteína, HU_258 Definir proteína alterna del seco y HU_259 Reportar faltantes de insumos. Quedan 250 fichas.

### C-105 · 2026-11-20 · feat(casos-uso) · conciliación con el frontend (repo 05)
- **Ruta:** `05_Casos_de_Uso/scripts/actualizar_casos_uso_canonicos.py`, diagramas PUML/SVG/PNG, MD, visor y `Diagramas_DrawIO/Casos_de_usos.drawio`
- **Mensaje:** Lista canónica igual al Story Mapping v10. Configuraciones queda con Listar, Editar y Activar/desactivar. Producción suma Reportar faltantes y Reporte por período; Producto terminado se registra y corrige desde la orden; Suscripciones suma lista de espera y preferencia de proteína; Menú suma proteína alterna; Dashboard suma proyección y costo-beneficio por zona. En el draw.io salen 5 elipses de configuración con 7 conectores y entran 7 casos "Extends"; los 6 carriles se revisaron a ojo.

### C-104 · 2026-11-20 · fix(tablero-kanban) · v9 → v10
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Tablero_Kanban/v10_2026-11-20/` — `Tablero Kanban 20_11 v10.xlsx`
- **Mensaje:** Matriz HU: salen HU01.2_01, 03, 06, 07 y 08; se reescriben las HU de producción, producto terminado, cupo, rutas y dashboard (cocina "desde el panel, también en el celular"); entran HU06.2_15 (lista de espera), HU06.2_16 (preferencia de proteína) y HU06.3_10 (proteína alterna del seco). Quedan 190 HU y 500 criterios. Story Mapping: 159 historias y 515 puntos. Recalcula al abrir en Excel.

### C-103 · 2026-11-20 · fix(diagrama-er) · v11 → v12
- **Ruta:** `04_Modelado_DB/Diagramas/v12_2026-11-20/` — `LaCocaDiagramDB.svg`
- **Mensaje:** Diagrama ER de bd.uml v4.8 (43 tablas, 59 relaciones), generado por `construir_visor.py`. Visor v4.8 regenerado.

### C-102 · 2026-11-20 · fix(modelo-relacional) · v13 → v14 (DBML v4.8)
- **Ruta:** `04_Modelado_DB/Modelo_Relacional/v14_2026-11-20/` — `bd.uml`, `Cambios_v4.8.md`, `Visor_Interactivo/`
- **Mensaje:** Decisiones del grill de discrepancias con el frontend: cupo semanal de ventas nuevas con estado en_espera, preferencia de proteína (enum, clientes y menu_items, recargo de $10.000), configuraciones fijas con claves nuevas (cupo, recargo, costo diario del domiciliario), tablas faltantes_insumos y dispositivos_push, notas de orden anulada, producto terminado, rutas = zonas y dashboard. 43 tablas y 59 relaciones, ninguna con más de 12 columnas.

### C-101 · 2026-11-20 · fix(ficha-proyecto) · v11 → v12
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Fichas_Tecnicas/v12_2026-11-20/` — `Ficha_Jacksoft_CF_v12.docx`
- **Mensaje:** La app móvil queda pendiente y todo lo suyo también se ofrece en la web. Solo Bancolombia. Cupo semanal con lista de espera y preferencia de proteína. Configuraciones fijas (sin historial). Órdenes generadas desde el menú, sin personal asignado, faltantes y reportes por período. Rutas = zonas, dos juegos de cocas, dashboard con demanda frente al cupo y costo logístico. Fila nueva en el control de cambios.

### C-100 · 2026-11-20 · docs(grill) · discrepancias documentación ↔ frontend
- **Ruta:** (decisiones en cuestionarios interactivos con Alejandro)
- **Mensaje:** Revisión de la documentación frente al frontend de Omar y grill para corregir las discrepancias: móvil pendiente (todo en la web), cupo semanal con lista de espera, proteína, configuraciones fijas, producción desde el menú, rutas = zonas, web push, GPS desde el navegador, novedades con foto y faltantes. Prioridad PO > modelo > Ficha. Lo del frontend va al chat (grill G5).

### C-099 · 2026-11-18 · fix(manual-tecnico) · v7 → v8 (archivo "v2.5")
- **Ruta:** `10_Manual_Tecnico/Documentos_Word/v8_2026-11-18/` — `Manual_Tecnico_v2.5_Jacksoft.docx`
- **Mensaje:** Modelo v4.7 en todo el manual. El diccionario de datos queda con 41 tablas (identidades_externas, codigos_acceso, movimientos_insumos y los campos nuevos). Mockup de Permisos (antes estaba pendiente). Los 12 diagramas de casos de uso que cambiaron se redibujaron desde el draw.io: sin "Eliminar", y Acceso con Google/Apple y WhatsApp. C4 v6. Fichas: salen las 4 de eliminar y entran HU_254 y HU_255 (235 fichas). Portada "Versión 2.5" y fila nueva en el control de cambios.

### C-098 · 2026-11-18 · fix(diccionario-datos) · v1 → v2 (v4.7)
- **Ruta:** `04_Modelado_DB/Diccionario_y_Tablas/Documento_Word/v2_2026-11-18/` — `Diccionario_de_Datos_JackSoft_v4.7.docx`
- **Mensaje:** Sobre el diccionario de Omar (mismo formato): tablas nuevas identidades_externas y codigos_acceso, renombres (movimientos_insumos, alergenos) y los campos de G1 a G4. Se verificó tabla por tabla contra bd.uml v4.7: 41 de 41 iguales.

### C-097 · 2026-11-18 · fix(ficha-proyecto) · v10 → v11
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Fichas_Tecnicas/v11_2026-11-18/` — `Ficha_Jacksoft_CF_v11.docx`
- **Mensaje:** Acceso web y móvil: el personal entra solo con correo y contraseña; los clientes también con Google, Apple o un código por WhatsApp. La bitácora registra el método de ingreso.

### C-096 · 2026-11-18 · fix(arquitectura-c4) · v5 → v6 (repo 05)
- **Ruta:** `05_Casos_de_Uso/Arquitectura_C4/v6_2026-11-18/`
- **Mensaje:** Sistemas externos nuevos en N1, N2 y N3: Google y Apple (OpenID Connect + PKCE) y WhatsApp Business API (código de acceso). La BD pasa a bd.uml v4.7 con 41 tablas. N4 regenerado: 41 clases (con IdentidadExterna, CodigoAcceso y MovimientoInsumo), 55 relaciones.

### C-095 · 2026-11-18 · fix(documentacion-cu) · v5 → v6 (repo 05)
- **Ruta:** `05_Casos_de_Uso/Especificaciones/Documentacion_Word/v6_2026-11-18/`
- **Mensaje:** Salen las 4 fichas de eliminar (rol, usuario, categoría de insumos y ruta: G3-Q6). En Acceso entran HU_254 "Iniciar sesión con Google o Apple" y HU_255 "Iniciar sesión con código por WhatsApp". Quedan 251 fichas.

### C-094 · 2026-11-18 · feat(casos-uso) · sin "Eliminar"; Acceso con Google, Apple y WhatsApp (repo 05)
- **Ruta:** `05_Casos_de_Uso/scripts/actualizar_casos_uso_canonicos.py`, diagramas PUML/SVG/PNG, MD, visor y `Diagramas_DrawIO/Casos_de_usos.drawio`
- **Mensaje:** Salen los 10 casos de uso "Eliminar …" de la lista canónica (G3-Q6). Acceso suma "Iniciar sesión con Google o Apple" e "Iniciar sesión con código por WhatsApp" (extienden "Iniciar sesión"). En el draw.io salen 11 elipses de eliminar con sus conectores (33 celdas), y el carril de Acceso suma al actor Cliente con las dos formas nuevas de ingreso.

### C-093 · 2026-11-18 · fix(tablero-kanban) · v8 → v9
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Tablero_Kanban/v9_2026-11-18/` — `Tablero Kanban 18_11 v9.xlsx`
- **Mensaje:** Story Mapping: salen las 10 historias "Eliminar …" (20 puntos) y ACCESO suma "Iniciar sesión con Google o Apple" y "Iniciar sesión con código por WhatsApp" (5 puntos cada una): quedan 157 historias y 500 puntos. Matriz HU: salen 12 HU de eliminar (26 filas) y entran HU02.2_11 y HU02.2_12 (6 criterios). Los códigos existentes no se renumeran. Recalcula al abrir en Excel.

### C-092 · 2026-11-18 · docs(chat) · acuerdo G3 confirmado; aviso del modelo v4.7 y de Permisos
- **Ruta:** `chat/` (#031 a #033)
- **Mensaje:** Omar confirmó G2 y respondió G4 (#031, modelado delegado) y publicó el acuerdo G3 (#032). Claude Alejo confirmó G3 en el #033, que cierra los pendientes 20, 22 y 23, y avisó del modelo v4.7 y de que Permisos volvió a ser un subproceso.

### C-091 · 2026-11-18 · fix(diagrama-er) · v10 → v11
- **Ruta:** `04_Modelado_DB/Diagramas/v11_2026-11-18/` — `LaCocaDiagramDB.svg`
- **Mensaje:** Diagrama ER de bd.uml v4.7 (41 tablas, 55 relaciones), generado por `construir_visor.py` (regla de oro). El visor se republicó en el mismo enlace.

### C-090 · 2026-11-18 · fix(modelo-relacional) · v12 → v13 (DBML v4.7)
- **Ruta:** `04_Modelado_DB/Modelo_Relacional/v13_2026-11-18/` — `bd.uml`, `Cambios_v4.7.md`, `Visor_Interactivo/`
- **Mensaje:** Aplica los acuerdos G1, G2, G3 y G4 con Claude Omar y la foto del menú. Tablas nuevas identidades_externas y codigos_acceso. Renombres: movimientos_insumos y productos.alergenos. Campos nuevos: tipo_documento, telefono único, password opcional, accesos.metodo, imagen_url, cantidad_planificada en la orden, rendimiento_porciones, dias_habiles, beneficios, municipio, nombre_publico y foto_url. Claves nuevas de pago y de horario. Salen clientes.franja_horaria y las claves de bloqueo. La nota de roles se corrige. Quedan 41 tablas y 55 relaciones.

### C-089 · 2026-11-17 · feat(visor-modelo) · Permisos como proceso propio en el visor
- **Ruta:** `04_Modelado_DB/Visor_Modelo/visor_config.json`, `salida/modelo_la_coca.html`, `Modelo_Relacional/v12_2026-11-13/Visor_Interactivo/`
- **Mensaje:** `permisos` y `rol_permisos` quedan en el subproceso Permisos (antes Roles). Visor regenerado con `construir_visor.py` y republicado en el mismo enlace. El bd.uml no cambia: la nota de `roles` que aún dice "Asignar permisos al rol" se corrige en la v4.7.

### C-088 · 2026-11-17 · fix(manual-tecnico) · v6 → v7 (archivo "v2.4")
- **Ruta:** `10_Manual_Tecnico/Documentos_Word/v7_2026-11-17/` — `Manual_Tecnico_v2.4_Jacksoft.docx`
- **Mensaje:** Parte de la v6 de Omar (diccionario v4.6 y despliegue) y recupera las imágenes originales de la v5. Agrega Permisos antes de Roles: mockup (pendiente en Figma), diagrama de casos de uso y fichas HU_246 a HU_253 (237 fichas). C4 v5 en contenedores, componentes y clases. Portada "Versión 2.4" y fila nueva en el control de cambios.

### C-087 · 2026-11-17 · fix(documentacion-cu) · v4 → v5 (repo 05)
- **Ruta:** `05_Casos_de_Uso/Especificaciones/Documentacion_Word/v5_2026-11-17/`
- **Mensaje:** Sección "Permisos:" antes de Roles con 8 fichas HU_246 a HU_253 (253 fichas): listar, ver detalle, asignar, consultar los del rol, quitar, cambiar estado, buscar/filtrar y reporte por rol.

### C-086 · 2026-11-17 · fix(arquitectura-c4) · v4 → v5 (repo 05)
- **Ruta:** `05_Casos_de_Uso/Arquitectura_C4/v5_2026-11-17/`
- **Mensaje:** Nivel 2: la BD es bd.uml v4.6 (39 tablas) y la web arma menú y botones con los permisos. Nivel 3: el componente de acceso cubre la matriz módulo × acción y envía `user.permissions`. Nivel 4 regenerado desde bd.uml v4.6: 39 clases con Permiso y RolPermiso, 53 relaciones. PNG nuevos de N2, N3 y N4.

### C-085 · 2026-11-17 · feat(casos-uso) · vuelve el subproceso Permisos (repo 05)
- **Ruta:** `05_Casos_de_Uso/scripts/`, `Diagramas_PUML|SVG|PNG/PERMISOS.*`, `Diagramas_DrawIO/Casos_de_usos.drawio`, MD y visor
- **Mensaje:** Permisos entra en la lista canónica antes de Roles (Configuración y Seguridad, 8 casos de uso): 24 subprocesos, 163 CU. Carril nuevo en el draw.io.

### C-084 · 2026-11-17 · fix(tablero-kanban) · v7 → v8
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Tablero_Kanban/v8_2026-11-17/` — `Tablero Kanban 17_11 v8.xlsx`
- **Mensaje:** Story Mapping: columna PERMISOS (D:E) antes de ROLES, 8 historias y 22 puntos; las columnas siguientes se corren 2 (hasta AY) y las fórmulas del Backlog, B5:B7 y las filas 19 y 20 se ampliaron a `D:AY` (24 subprocesos, 165 historias, 510 puntos). Matriz HU: bloque "01.3 Gestión de permisos" (HU01.3_01 a HU01.3_08, 21 criterios) antes de Usuarios. Recalcula al abrir en Excel.

### C-083 · 2026-11-17 · fix(ficha-proyecto) · v9 → v10
- **Ruta:** `06_Gestion_de_Proyecto_Scrum/Fichas_Tecnicas/v10_2026-11-17/` — `Ficha_Jacksoft_CF_v10.docx`
- **Mensaje:** Vuelve el subproceso de permisos (antes de roles): el rol se define con los permisos que se le asignan, y el acceso web y móvil depende del rol y sus permisos.

### C-082 · 2026-11-17 · docs(drive) · se publican en Drive todos los vigentes
- **Ruta:** `00_Contexto_Versiones/publicar_drive.py`, `00_Contexto_Versiones/ESTADO_ACTUAL.md`
- **Mensaje:** `publicar_drive.py` ahora también publica `09_Diagrama_Despliegue` y `10_Diccionario_Datos` (mismos nombres de carpeta que usó Omar en 01_VIGENTE). Se publicó el manual v6 como vigente; la v5, con las imágenes en buena calidad, queda en 02_HISTORIAL. ESTADO_ACTUAL al día con el manual v6, el diccionario y el despliegue.

### C-081 · 2026-11-17 · docs(drive) · se baja lo nuevo de Drive (manual v6, diccionario, despliegue, exposiciones)
- **Ruta:** `10_Manual_Tecnico/Documentos_Word/v6_2026-11-17/`, `04_Modelado_DB/Diccionario_y_Tablas/Documento_Word/v1_2026-11-13/`, `05_Casos_de_Uso/Diagrama_Despliegue/v1_2026-11-10/` (repo propio de 05), `08_Entregables_e_Informes/Exposiciones/`, `09_Backups_y_Archivos_Zips/Drive_GoogleSheets/`
- **Mensaje:** Se comparó Drive contra el repo por contenido (hash) y en el servidor por fecha y autor. Se bajó lo que el equipo subió o editó y el repo no tenía: (1) el manual vigente que Omar re-guardó el 17-nov, con el diccionario de datos v4.6 en lugar del ejemplo "IdVenta" y el diagrama de despliegue. El texto restante es igual a la v5, pero las imágenes quedaron recomprimidas: la mayor bajó de 11,7 a 2,3 MP (mismo problema del 12-nov, ver C-078). (2) `Diccionario_de_Datos_JackSoft_v4.6.docx` (Omar, 13-nov, carpeta 10_Diccionario_Datos de Drive, que no bajó al Drive local). (3) `Diagrama De Despliegue.jpg` (Omar, 10-nov, 01_VIGENTE/09_Diagrama_Despliegue). (4) Las exposiciones "Bocetos a Código" y "Topologías de Redes" de 03_Exposiciones. (5) Una exportación del Google Sheets "Tablero Kanban + Matriz HU (Agosto 21))" que mega2808 editó el 21-oct; es la línea vieja del tablero (la vigente es la v7), por eso va a backups.

### C-080 · 2026-11-13 · fix(diagrama-er) · v9 → v10
- **Ruta:** `04_Modelado_DB/Diagramas/v10_2026-11-13/` — `LaCocaDiagramDB.svg`
- **Mensaje:** Diagrama ER de bd.uml v4.6 (39 tablas, 53 relaciones), generado por `construir_visor.py` (regla de oro).

### C-079 · 2026-11-13 · fix(modelo-relacional) · v11 → v12 (DBML v4.6)
- **Ruta:** `04_Modelado_DB/Modelo_Relacional/v12_2026-11-13/` — `bd.uml`, `Cambios_v4.6.md`, `Visor_Interactivo/`
- **Mensaje:** Vuelven los permisos: tablas permisos (módulo + acción, enum accion_permiso) y rol_permisos (llave compuesta), en P1. Se aplicó sin esperar el acuerdo G2 porque la respuesta del frontend no cambia las tablas. Lo demás de G1/G2 pasa a la v4.7. Nuevo `validar_dbml.mjs` en Visor_Modelo.

### C-078 · 2026-11-13 · feat(visor-modelo) · regla de oro: bd.uml → visor + diagrama ER; manual restaurado
- **Ruta:** `04_Modelado_DB/Visor_Modelo/` (construir_visor.py, render_svg.mjs, package.json), `00_Contexto_Versiones/hooks/pre-commit`, `00_Contexto_Versiones/publicar_drive.py`
- **Mensaje:** Regla de oro: siempre que se toca un bd.uml se regeneran el visor y el diagrama ER. `construir_visor.py` crea una versión nueva de `04_Modelado_DB/Diagramas` cuando el SVG no corresponde a la versión del bd.uml. `publicar_drive.py` lo corre antes de publicar, y el hook `pre-commit` (para instalar en `.git/hooks`) lo corre en cada commit que toca un bd.uml. Drive: alguien re-guardó el manual vigente desde Drive el 12-nov (mismo texto y figuras, imágenes recomprimidas, 3 con menos resolución). Se restauró la v5 en `01_VIGENTE` desde `02_HISTORIAL`, y la copia re-guardada quedó en la papelera de Drive.

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
