---
title: "Contexto de entregables e incongruencias — JackSoft"
type: tracker
tags:
  - incongruencias
  - trazabilidad
  - cascada
related:
  - "[[00_INDICE_GENERAL]]"
  - "[[00_MOC_Manual_Tecnico]]"
  - "[[Correcciones_Manual_Tecnico_v1]]"
---

# Contexto de entregables e incongruencias — JackSoft

> Complemento de [[Correcciones_Manual_Tecnico_v1]]. Aquí se registra **qué dice cada entregable** (fuente de lo entregado y revisado) y **dónde se contradicen**. Revisado el 2026-09-25.

---

## 1. Inventario de fuentes (versión vigente de cada entregable)

| Entregable | Archivo vigente (Módulo Oficial) | Fecha | Contenido | Versiones anteriores |
|---|---|---|---|---|
| Ficha de proyecto | `06_Gestion_de_Proyecto_Scrum/Fichas_Tecnicas/v6_2026-09-13/Ficha_3agosto Jacksoft CF.docx` (+ PDF) | 13 sep | Alcance: 8 procesos, 26 subprocesos web + 5 mobile. **VoBo Requisitos 10/09/2026** (Newton Pomare) | 24jul, 30jul, 3ago, 14ago |
| Kanban + Backlog + Story Mapping + Matriz HU | `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Tablero_Kanban/v3_2026-09-13/Tablero Kanban 13_09.xlsx` | 24 sep | Story Mapping v03: **22 módulos / 135 historias**. Matriz HU: **22 subprocesos / 186 HU** | Agosto 21, Agosto 10 |
| Matriz HU (independiente) | `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/Matriz_HU/v1_2026-08-12/Matriz_Historias_de_Usuario_actualizada.xlsx` | 12 ago | 159 HU, taxonomía vieja (7 procesos / 25 subprocesos) | — (superada por la matriz del Kanban 13_09) |
| Diagramas de casos de uso | `05_Casos_de_Uso/Diagramas_DrawIO/Casos_de_usos.drawio` | 24 sep | 22 diagramas (sin Permisos), solo actor Admin. = imágenes del Manual v2 | `mapa_interactivo.svg` (26 ago, versión vieja) |
| Documentación de casos de uso | `05_Casos_de_Uso/Especificaciones/Documentacion_Word/v2_2026-09-14/Documentacion_Casos_de_Uso_JackSoft.docx` | 14 sep | **243 fichas HU_001–HU_243** = mismas fichas del Manual v1/v2 | 31 de agosto (`_31ago.docx`) |
| Modelo de BD | `04_Modelado_DB/Modelo_Relacional/v3_2026-10-30/bd.uml` (DBML **v3.5**) | 30 oct | 35 tablas, 53 relaciones, 22 TableGroups = 22 subprocesos. Acceso único por `usuarios` (→ clientes / empleados), kardex, cocas, alergias, producto terminado | DBML V2 (24 ago, 33 tablas, vigente hasta el 30 oct), DBML v1 (13 ago), `LaCocaDiagramDB.svg` (21 ago, 37 tablas) |
| Manual técnico | `10_Manual_Tecnico/Documentos_Word/v2_2026-09-25/Manual_Tecnico_v2_septiembre_25.docx` | 24 sep | Diagramas v2 + fichas v1. Trabajo en curso / Fuente de verdad: `Manual_Tecnico_v2.1_Jacksoft.docx` | v1 (con comentarios de evaluadora) |

---

## 2. Comparación por módulo

Cantidad de casos de uso / historias en cada entregable. **SM** = Story Mapping v03 · **MHU** = Matriz HU 13_09 · **Drawio** = diagramas v2 · **Fichas** = Documentación CU / Manual (v1=v2).

| # | Módulo | Ficha (alcance) | SM | MHU | Drawio | Fichas | Tablas BD V2 |
|---|---|---|---|---|---|---|---|
| 1 | Roles | ✔ | 7 | 7 | 6 (sin Asignar permisos) | 7 | roles, rol_permisos |
| — | **Permisos** | ✔ **subproceso propio** | — | — | — | 6 (0 en v2.1) | permisos |
| 2 | Usuarios | ✔ | 6 | 7 | 7 | 7 | usuarios |
| 3 | Acceso | ✔ | 4 | 10 (3 actores) | 3 (**log de acceso**) | 5 | accesos |
| 4 | Categoría de insumos | ✔ | 6 | 6 | 6 | 7 | categorias_insumos |
| 5 | Insumos | ✔ | 8 (Kardex) | 9 | 7 | 12 | insumos, insumo_proveedores (**sin movimientos/kardex**) |
| 6 | Categoría de productos | ✔ | 6 | 6 | 6 | 6 | **categorias_preparaciones** |
| 7 | Productos | ✔ | 7 | 9 | 6 | 10 | **preparaciones**, menus, menu_preparaciones |
| — | **Categoría de proveedor** | ✔ **subproceso propio** | — | — | — | — | — (existía en DBML v1) |
| 8 | Proveedores | ✔ | 7 | 9 | 6 | 9 | proveedores |
| 9 | Compras | ✔ | 7 (Anular) | 8 (Anular) | 7 (**Eliminar**) | 10 (Anular) | compras, compra_detalle |
| 10 | Empleados | ✔ | 6 | 9 (+ móvil) | 7 | 7 | empleados |
| 11 | Producción (orden) | ✔ | 6 | 11 (+ móvil) | 4 (**sin Crear orden**) | 7 | ordenes_produccion, orden_produccion_detalle |
| 12 | Ficha técnica | ✔ | 7 | 9 | 6 | 14 | fichas_tecnicas, ficha_tecnica_detalle |
| 13 | Producto terminado | ✔ | 6 | 8 | 5 | 10 | **ninguna** (solo `cantidad_producida` en orden_produccion_detalle) |
| 14 | Categoría de servicios | ✔ | 5 (sin Ver detalle) | 5 | 6 | 6 | categorias_servicios |
| 15 | Servicio | ✔ | 7 | 8 | 6 | 11 (6 en v2.1) | servicios |
| 16 | Calendario / Agenda | ✔ "agenda" | 4 | 4 | 4 | 10 | calendario |
| 17 | Clientes | ✔ | 6 | 12 (+ móvil) | 6 | 16 (6 en v2.1) | clientes, direcciones_cliente |
| 18 | Suscripciones | ✔ + renovación/reingreso | 8 | 13 (+ móvil) | 4 | 30 | suscripciones, pagos, suspensiones_entrega |
| 19 | Domiciliarios / **Rutas** | ✔ "asignación de **rutas** y domiciliarios" | 5 | 9 (son **rutas**) | 3 | 14 | rutas, ruta_clientes, zonas_cobertura (domiciliario = empleado) |
| 20 | Monitoreo tiempo real | ✔ | 7 (+ zonas) | 10 (+ móvil) | 4 | 10 | geolocalizacion_domiciliarios |
| 21 | Incidencias | ✔ | 6 | 9 (+ móvil) | 6 (sin Gestionar) | 9 | incidencias |
| 22 | Dashboard | ✔ | 4 | 8 | 6 | 20 | — (consultas) |
| | **Total** | 26 web + 5 mobile | **135** | **186** | **124** | **243** | 33 |

---

## 3. Incongruencias detectadas

Severidad: 🔴 bloquea la entrega / la evaluadora lo detecta · 🟠 inconsistencia entre entregables · 🟡 forma / detalle

### 3.1 Trazabilidad y archivos

| ID | Sev. | Incongruencia | Dónde |
|---|---|---|---|
| I-01 | 🔴 | **Tres sistemas de numeración sin tabla de equivalencia:** `HU_001–243` (fichas CU / manual), `HU01.1_01` (Matriz HU, 186), IDs `1…135` (Backlog). No se puede trazar una ficha a su HU ni al backlog | Documentación CU, Manual, Kanban |
| I-02 | 🔴 | **Kanban 13_09 roto:** la hoja Backlog tiene solo 7 historias reales (Roles); el resto repite "Crear rol" y muestra `#REF!`. Tablero Kanban con 3 tarjetas; Avance dice "ROLES 341 historias", "% cobertura 137 %"; Story Mapping "Posición inicial #REF!" | `Tablero Kanban 13_09.xlsx` |
| I-03 | 🟠 | La nota de la hoja Avance dice que la Matriz HU usa "7 procesos / 25 subprocesos", pero la matriz del mismo archivo ya tiene 22 subprocesos | `Tablero Kanban 13_09.xlsx` (Avance) |
| I-04 | 🟠 | La Documentación de CU (14 sep) duplica las 243 fichas del manual: cada corrección hay que hacerla dos veces | `Documentacion_Casos_de_Uso_JackSoft.docx` |
| I-05 | 🟡 | Nombres del equipo: Ficha/Kanban = "Omar David **Meneses Verona**", "Samuel **Morales Marin**"; Manual = "Omar David **Verona Meneses**", "Samuel **Marin Marin**" | Ficha vs Manual |

### 3.2 Alcance (Ficha aprobada vs resto)

| ID | Sev. | Incongruencia | Dónde |
|---|---|---|---|
| I-06 | 🔴 | **Permisos** es subproceso aprobado en la Ficha (con VoBo 10/09) pero se eliminó de Story Mapping, Matriz y diagramas. La Ficha dice que los cambios de alcance requieren autorización del cliente → **registrar el cambio (control de cambios + acta)**. 2026-10-30: el equipo lo retira por ahora (D-E); **⏳ pendiente: acta del cliente** | Ficha vs SM/MHU/Drawio |
| I-07 | 🟠 | **Categoría de proveedor** es subproceso aprobado en la Ficha, pero no existe en ningún otro entregable (DBML V2 también quitó la tabla) | Ficha vs todo |
| I-08 | 🟠 | Ficha: subproceso "**seguimiento, renovación y reingreso**" de suscripción; la Matriz tiene HU de renovar/reingreso, pero Story Mapping y diagramas no | Ficha/MHU vs SM/Drawio |
| I-09 | 🟠 | Ficha: 5 subprocesos **mobile** (Cliente, Domiciliario, Empleado); la Matriz tiene sus HU, pero Story Mapping, Backlog, diagramas y fichas CU solo modelan al **Admin** | Ficha/MHU vs SM/Drawio/Fichas |

### 3.3 Casos de uso por módulo (Story Mapping vs Drawio vs Matriz)

| ID | Sev. | Módulo | Incongruencia |
|---|---|---|---|
| I-10 | 🔴 | Rutas / Domiciliarios | Ficha, Matriz (07.1: crear/editar/asignar **rutas**) y BD (`rutas`, `ruta_clientes`) hablan de **rutas**. Story Mapping lo convirtió en "DOMICILIARIOS" (Listar domiciliarios ×2, "Dominiciliarios" con error, "Crear asignación de zonas", "Ver estado") y movió Crear/Editar zonas a Monitoreo. Drawio: "Asignar zonas a domiciliarios". **Nadie crea rutas** fuera de la Matriz |
| I-11 | 🔴 | Acceso | SM y Matriz: iniciar sesión, recuperar contraseña, estado de la cuenta, cerrar sesión. Drawio: Listar log de acceso, Ver acceso, Reporte (corresponde a la tabla `accesos`, no a las HU) |
| I-12 | 🔴 | Producción | SM y Matriz tienen Crear orden y Programar producción; el drawio no tiene "Crear orden de producción" y usa "Filtrar", "Ver estado" |
| I-13 | 🔴 | Suscripciones | SM: 8 (cotizar, registrar, editar, cambiar estado, subir/consultar comprobante). Matriz: 13 (+ aprobar comprobante, renovar, reingreso). Drawio: 4 (Crear, Listar, Ver, Reporte) |
| I-14 | 🟠 | Roles | SM y Matriz: "Asignar permisos"; drawio no |
| I-15 | 🟠 | Incidencias | SM: Registrar, Gestionar, Filtrar. Drawio: Crear, Ver estado, **Eliminar**, reporte "Generar reporte de" (texto cortado); falta Gestionar |
| I-16 | 🟠 | Calendario | SM: Parametrizar, Listar, Ver detalle, Exportar. Drawio: Parametrizar, Visualizar, Ver, **Editar** (no está en SM); falta Exportar |
| I-17 | 🟠 | Ficha técnica | SM: Buscar, Exportar, Eliminar (sin Cambiar estado). Drawio: Cambiar estado, Eliminar (sin Buscar ni Exportar) |
| I-18 | 🟠 | Servicio | SM: Filtrar + **Eliminar servicio**. Drawio: "Ver servicios activos", sin Eliminar |
| I-19 | 🟠 | Clientes | SM: Exportar clientes; Matriz: + Eliminar cliente. Drawio: "Generar reporte", sin Filtrar ni Exportar |
| I-20 | 🟠 | Compras | SM y Matriz: **Anular** compra. Drawio: **Eliminar** compra |
| I-21 | 🟠 | Categoría de servicios | Drawio tiene "Ver categoría"; SM y Matriz no tienen Ver detalle |
| I-22 | 🟡 | Todos | Reportes: SM usa "Exportar X"; drawio "Generar reporte de X"; Matriz tiene ambos → unificar el término |
| I-23 | 🟡 | Todos | Búsqueda: "Buscar" (SM ficha técnica / producto terminado / monitoreo) vs "Filtrar" (SM servicio / incidencias) vs "Filtrar / consultar" (fichas) → unificar |

### 3.4 Eliminar vs borrado lógico

| ID | Sev. | Incongruencia |
|---|---|---|
| I-24 | 🔴 | El encabezado del DBML V2 dice: *"ningún subproceso permite eliminar, solo inactivar"*, y RN-07 exige borrado lógico. Pero SM, Matriz y drawio tienen **"Eliminar"** en ~14 módulos (roles, usuarios, categorías, insumos, productos, proveedores, empleados, ficha técnica, servicio, incidencias, clientes…) y además "Cambiar estado" |

### 3.5 Base de datos

| ID | Sev. | Incongruencia |
|---|---|---|
| I-25 | 🔴 | **Tres modelos distintos:** DBML v1 (13 ago), SVG (21 ago, 37 tablas con `juegos_cocas`, `recipientes`, `movimientos_inventario`, `producto_terminado`, `menus_diarios`) y DBML V2 (24 ago, 33 tablas con `preparaciones`, `menus`). El diagrama SVG **no corresponde** al DBML vigente |
| I-26 | 🟠 | DBML V2 renombró productos → `preparaciones` y categorías → `categorias_preparaciones`, pero todos los demás entregables dicen "Productos" / "Categoría de productos" |
| I-27 | 🟠 | Producto terminado es un módulo con 6–10 CU, pero en V2 **no tiene tabla** |
| I-28 | 🟠 | "Consultar Kardex de insumos" (SM, Matriz) no tiene tabla de movimientos en V2 (sí estaba en el SVG) |
| I-29 | 🟠 | Cocas (RN-01): el SVG tenía `juegos_cocas` / `recipientes`; V2 solo guarda conteos (`ruta_clientes.cocas_*`, `suscripciones.cobro_cocas`, `clientes.tiene_cocas_propias`). El monitoreo "estado de cocas" y la HU móvil de tenencia de cocas dependen de esto |
| I-30 | 🟡 | La ficha de alcance de Clientes y el Manual v2.1 mencionan **alergias**; V2 no tiene columna de alergias (el SVG sí: `alergias_alimentarias`) |
| I-31 | 🟡 | El domiciliario es un `empleado` con cargo = domiciliario (nota en V2), pero SM y drawio lo tratan como un módulo con entidad propia |
| I-32 | 🟡 | La sección "Modelo de Base de Datos" del manual está vacía (el diccionario tiene el ejemplo `IdVenta` de la plantilla) |

> **Estado 2026-10-30 (bd.uml v3.5, ver D-B):** I-25 resuelta (un solo modelo vigente) · I-26 resuelta (`productos` / `categorias_productos`) · I-27 resuelta (`producto_terminado`) · I-28 resuelta (`movimientos_inventario` con motivo controlado) · I-29 resuelta (`juegos_cocas`, `recipientes`) · I-30 resuelta (`clientes.alergias_alimentarias`) · I-31 decidida: el domiciliario es un **rol**, sin tabla propia · I-32 en curso (Manual v2.2: imagen del modelo + diccionario).

### 3.6 Decisiones de revisión del modelo (2026-10-30)

Aplicadas en `bd.uml` v3.5 y en el mapa interactivo del modelo:

| Tema | Decisión |
|---|---|
| Acceso | Acceso único: `accesos → usuarios → clientes / empleados` (1:1). Datos de la persona solo en `usuarios`; se quitan `clientes.password` y `accesos.cliente_id`; rol "Cliente". Todo empleado tiene usuario (inactivo si no usa el sistema) |
| Permisos / Categoría de proveedor | Fuera del alcance por ahora (D-E). Se elimina `rol_permisos`; lo que puede hacer cada rol se define en la aplicación |
| Domiciliario | Es un rol. La aplicación valida el rol en rutas, entregas, geolocalización e incidencias. `empleados.cargo` = puesto de trabajo (texto libre) |
| Producción | 1 menú del día = 1 orden (`menu_id` único); la fecha de la orden es la del menú |
| Calendario | Fuente de días hábiles: menú y suspensiones con `calendario_id` |
| Festivos | Sigue RN-02: el festivo se descuenta del precio y el vencimiento no se mueve. `suscripciones` agrega `dias_facturables` y `descuento_festivos`. **Contradice la Ficha aprobada** (VoBo 10/09), que dice que el festivo no descuenta y desplaza el vencimiento. El equipo eligió RN-02 y corrigió las dos frases en la copia `Ficha_3agosto Jacksoft CF_v2_festivos.docx`; el original no se tocó. **⏳ Requiere autorización del cliente** |
| Direcciones | Una dirección base por cliente + excepciones por día (híbridos); índice único parcial en SQL |
| Entregas | `ruta_clientes` guarda fecha (única con la suscripción), dirección usada y domiciliario que entregó; la ruta puede reasignarse a mitad del recorrido |
| Inventario | Kardex con motivo enum (compra / produccion / merma / ajuste) y FK obligatoria según motivo; compras con estado `recibida` (entrega completa) |
| Valores calculados | Se guardan precios del momento y existencia del insumo; `compras.valor_total` y el costo por porción de la ficha técnica son vistas |
| Incidencias | Tipo enum, `gestionada_por_usuario_id`, campo obligatorio según quién reporta |
| Borrado | Solo cambio de estado (D-C); las notas de HU ya no dicen "Eliminar" |

**⏳ Pendientes:** acta del cliente por Permisos (I-06) · autorización del cliente para el cambio de festivos (la Ficha aprobada dice lo contrario) · validaciones de aplicación (rol Domiciliario, dirección del día, motivo del kardex, quién reporta, juegos del mismo cliente) · al exportar a SQL: vistas `v_compras_total` y `v_costo_ficha_tecnica`, índice parcial de dirección base y trigger del kardex.

---

## 4. Propuesta de fuente maestra

Para cortar la cascada, cada nivel se deriva del anterior:

1. **Ficha de proyecto** (alcance aprobado) → solo se cambia con control de cambios (Permisos, Categoría de proveedor).
2. **Matriz HU 13_09** (186 HU, códigos `HUxx.x_xx`) → **catálogo maestro de historias** (tiene criterios de aceptación y actores).
3. **Story Mapping v03** → vista de las historias del **Admin (web)**; el Backlog se regenera desde aquí.
4. **Casos de uso (drawio + fichas)** → un CU por historia del SM (+ móvil si se decide), **usando el código de la Matriz** en vez de `HU_001–243`.
5. **BD (`bd.uml` v3.5)** → cada CU que registre datos debe tener tabla o columna; las imágenes del modelo se regeneran desde el DBML.

---

## 5. Decisiones pendientes

| # | Decisión | Estado |
|---|---|---|
| D-A | ¿Story Mapping v03 / Matriz 13_09 es la lista maestra de CU? | ✅ 2026-09-25: **Sí.** SM v03 define los CU del Admin; fichas y diagramas usan los códigos `HUxx.x_xx` de la Matriz 13_09. Se retira `HU_001–243` (queda solo en la tabla de equivalencias) |
| D-B | ¿Qué modelo de BD es el vigente (DBML V2 vs SVG)? | ✅ 2026-09-25: **DBML V2.** El SVG se regenera desde V2; los módulos que no tienen tabla (producto terminado, kardex, cocas, alergias) se resuelven ajustando el CU o agregando la tabla al V2. **Actualizada 2026-10-30:** el modelo vigente es `04_Modelado_DB/Modelo_Relacional/v3_2026-10-30/bd.uml` **v3.5**, que ya incluye esas tablas (ver 3.6); V2 queda como versión anterior |
| D-C | ¿"Eliminar" o solo "Cambiar estado" (RN-07 / nota del DBML)? | ✅ 2026-09-25: **Solo cambiar estado.** Se quitan los "Eliminar" de SM, Matriz, drawio y fichas (Compras usa "Anular") |
| D-D | ¿Los CU móviles (Cliente, Domiciliario, Empleado) entran en los diagramas de esta fase? | ✅ 2026-09-25: **No.** Diagramas y fichas solo con Admin; las HU móviles siguen en la Matriz para otra fase |
| D-E | Permisos y Categoría de proveedor: ¿se retiran del alcance con acta del cliente? | ✅ 2026-10-30: **Se retiran por ahora** (ninguno está en la lista de 22 subprocesos). Se elimina `rol_permisos` del modelo y "Asignar permisos" de las fichas. **⏳ Pendiente: acta del cliente** (I-06) |
| D-F | Rutas vs Domiciliarios: ¿el módulo es "Rutas y domiciliarios" (Ficha / Matriz / BD)? | 🔲 |

## 9. Cambio de alcance 2026-11-02

Decisión **D-F** (equipo, 2026-11-02): se elimina el subproceso **Empleados** (no tenía impacto real en el sistema) y se agregan **Configuraciones del sistema** (proceso Configuración) y **Menú** (proceso Ventas). También se retiran de la Ficha Permisos y Categoría de proveedor (D-E). Cascada aplicada:

| # | Entregable | Versión nueva | Cambio |
|---|---|---|---|
| 1 | Ficha de proyecto | v8 | Alcance de 23 subprocesos web + 7 mobile |
| 2 | Tablero Kanban / Story Mapping / Matriz HU | v5 | 157 historias · 194 HU renumeradas |
| 3 | Modelo relacional `bd.uml` | v4 (DBML v3.6) | 36 tablas · 56 relaciones; sin `empleados`; cierre semanal de suscripciones |
| 4 | Diagrama ER | v2 | Regenerado desde v3.6 |
| 5 | Casos de uso (PUML/SVG/PNG, drawio, visor, CU md) | repo `05_Casos_de_Uso` | −EMPLEADOS, +CONFIGURACIONES DEL SISTEMA, +MENU |
| 6 | Documentación de CU (Word) | v3 | 248 fichas renumeradas HU_001–HU_248 en orden del documento |
| 7 | Arquitectura C4 | v3 | Módulos 1 y 5 renombrados; Nivel 4 desde v3.6 |
| 8 | Manual técnico | v4 (archivo v2.2) | Mockups, diagramas, C4 y fichas |

Pendientes: mockups en Figma de Configuraciones del sistema y Menú; las incongruencias I-31 y la fila 10 (Empleados) de la sección 2 quedan cerradas por esta decisión.

Ajustes del 2026-11-03 (mismas versiones): códigos renumerados (Matriz HU y fichas `HU_###`); se retira también "Asignar permisos"; el actor "Empleado" pasa a su rol; nueva regla [[RN_Limite_Suscripcion_Semanal]]; la ficha v8 queda como **oficial**. El manual numera sus fichas con los mismos números del Word de CU (la ficha "Generar reporte de clientes", que solo estaba en el manual, se agregó al Word).
