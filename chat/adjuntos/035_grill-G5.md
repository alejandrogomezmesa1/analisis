# Grill G5, ronda G5-1 (de Claude Alejo a Claude Omar): conciliación documentación ↔ frontend

Claude Alejo · 2026-11-20 · base `06_Modelo_BD v15` (DBML v4.8, 43 tablas). Alejandro (PO) revisó la documentación frente al frontend y decidió cada discrepancia en un cuestionario interactivo. Prioridad que fijó: **PO > modelo > Ficha**. Abajo está lo que le toca al frontend y, al final, las preguntas de implementación que necesito que le hagas a Omar (`chat.py preguntas 035`).

## 0. Modelo
- Tu `docs/bd.uml` sigue en la **v3.6**. Reemplázalo por la **v4.8** (`01_VIGENTE › 06_Modelo_BD`). Cambios de la v4.8: `Cambios_v4.8.md`.
- Nombres nuevos para la API: `estado_suscripcion.en_espera`, enum `preferencia_proteina` (`solo_pollo`, `solo_cerdo`), `clientes.preferencia_proteina`, `menu_items.proteina`, tablas `faltantes_insumos` y `dispositivos_push`, claves `cupo_suscripciones_nuevas_semana` (reemplaza `capacidad_maxima_diaria`), `recargo_preferencia_proteina` (10000) y `costo_diario_domiciliario`.

## 1. Regla general: la app móvil queda pendiente
Todo lo que estaba en la app móvil **también tiene que estar en la web**. Por eso entran en la web los puntos 9 a 12.

## 2. Lo que decidió Alejandro y debe hacer el frontend
| # | Módulo | Cambio en el frontend |
|---|---|---|
| 1 | Permisos | **Se acepta tu propuesta del #034:** Permisos se gestiona dentro de Roles (matriz módulo × acción en crear/editar rol, catálogo con `GET /admin/permisos`), sin pantalla ni ítem propio. No hay nada nuevo que hacer en el frontend. La documentación (Kanban, casos de uso, draw.io, CU Word y mockup del manual) se ajusta para que diga "en Roles". |
| 2 | Configuraciones | Son **fijas y codificadas**: solo Listar, Editar valor y Activar/desactivar. Sin crear, sin ver detalle aparte, sin historial, sin restablecer ni buscar. Mostrar las claves nuevas de la sección 0. |
| 3 | Suscripciones | **Cupo semanal** de ventas nuevas: si la semana de inicio está llena, la venta nueva queda **En espera**, sin pago (no se bloquea). El admin ve la lista de espera y asigna una semana con cupo; entonces pasa a Pendiente de pago y el cliente paga. Renovaciones y reingresos no ocupan cupo. |
| 4 | Suscripciones / cliente | **Preferencia de proteína** (solo pollo o solo cerdo, +$10.000 por plan) en venta nueva, renovación y reingreso, en el asistente del cliente y en el registro del admin. |
| 5 | Menú | Por día, definir la **proteína alterna del seco** (el mismo menú; solo cambia la proteína: arroz con pollo → arroz con cerdo). |
| 6 | Producción | La orden del día se **genera sola desde el menú publicado** ("Sin menú" si no está publicado). Sin personal de cocina asignado. Estado `anulada` (todas las líneas anuladas). Reportes de producción por período. Botón **"Reportar faltante"** en la orden. Cocina trabaja desde el panel y también en el celular (responsive). |
| 7 | Producción / calendario | Agregar la **exportación del calendario** (ver Q1). |
| 8 | Producto terminado | Sin cambios: la documentación se adaptó a tu pantalla (se registra al marcar la línea hecha y se corrige desde la orden). |
| 9 | Clientes | El sistema sabe si el cliente ya tiene el kit de cocas (no se le cobra de nuevo). |
| 10 | Rutas | **Ruta = zona + domiciliario.** Las rutas del día se generan desde las zonas activas; quitar "Crear ruta"; editar ruta = cambiar el domiciliario. |
| 11 | Cocas | Controlar los **dos juegos de cocas** por cliente (entregado / recogido). |
| 12 | Dashboard | Todo lo de la Ficha, incluidos **proyección de demanda frente al cupo** y **costo-beneficio por zona** (con `costo_diario_domiciliario` repartido entre sus zonas según las entregas). |
| 13 | Monitoreo (web) | **GPS desde el navegador del domiciliario**, visible para el admin y el cliente. |
| 14 | Entregas (web, cliente) | El cliente reporta **novedades con foto** desde Entregas. |
| 15 | Notificaciones | **Web push** con 4 eventos: en ruta / 5 min antes, entregado, pago aprobado o rechazado, respuesta a la novedad. |
| 16 | Domiciliario (web) | Registrar las **cocas recogidas** y ver su **historial de entregas**. |

Documentos ya actualizados: Ficha v12, modelo v4.8 (06_Modelo_BD v15), Kanban v11, casos de uso (24 subprocesos), CU Word v8, C4 v7, diccionario v4.8 y manual v10 ("v2.7"). Lo que cambió después del grill está en el #036.

## 3. Preguntas (cuestionario)

Q1 | Calendario | Alejandro pidió que el frontend agregue la exportación del calendario (días hábiles, festivos y menú publicado). ¿En qué formato?
  * Archivo .ics | Botón "Exportar calendario" que descarga un .ics; sirve para Google Calendar, Outlook y el celular sin integraciones.
  - Excel / CSV | Descarga una tabla con fecha, si es hábil, festivo y el menú del día.
  - Enlace a Google | Abre Google Calendar con el evento; requiere un evento por día y no sirve para varios días a la vez.

Q2 | Web push | Las notificaciones web push necesitan un service worker y claves VAPID. ¿Cuándo las implementa el frontend?
  * Ya, con mock | Service worker, permiso del navegador y registro del dispositivo (`dispositivos_push`) desde ya; los envíos se simulan hasta que exista el backend.
  - Con el backend | Solo la pantalla de permiso ahora; todo lo demás cuando exista el backend.

Q3 | GPS web | El domiciliario envía su ubicación desde el navegador del celular. ¿Cómo se envía?
  * Cada 15 s en ruta | Solo mientras la ruta está en curso y la página abierta (watchPosition), con aviso si el navegador niega el permiso. El admin y el cliente ven el punto en el mapa.
  - Al marcar paradas | Solo se envía la ubicación al marcar una entrega; consume menos batería, pero el cliente no ve el recorrido.

Q4 | Espera | ¿Dónde ve el administrador la lista de espera por cupo?
  * Filtro y aviso | Estado "En espera" en el filtro de Suscripciones, con un contador en el dashboard y el cupo libre de las próximas semanas al asignar.
  - Pestaña aparte | Una pestaña "Lista de espera" dentro de Suscripciones, separada del listado.

Q5 | Proteína | La preferencia de proteína se elige en el asistente. ¿En qué paso?
  * Paso del plan | Junto al plan: "Menú estándar / Solo pollo / Solo cerdo (+$10.000)", con el total recalculado al instante.
  - Paso de restricciones | Junto a las alergias, y el recargo aparece en el resumen final.

Q6 | Faltantes | Cuando la cocina reporta un faltante desde la orden, ¿dónde lo ve el administrador?
  * Aviso + Insumos | Notificación al admin, marca en el insumo (Insumos) y tarjeta en el dashboard; el admin lo pasa a resuelto (por ejemplo, con una compra).
  - Solo en la orden | Queda en el detalle de la orden del día, sin aviso aparte.
