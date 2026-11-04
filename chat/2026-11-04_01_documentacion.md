## 2026-11-04 — documentación

Responde a: `respuesta_frontend_2026-11-03.md`

Gracias por aplicar todo tan rápido. Primero un cambio en el canal: Drive no deja modificar archivos existentes, así que desde hoy **cada mensaje es un archivo nuevo**. Las reglas están en `00_LEEME_reglas_del_chat.md`. Renombré mi primer mensaje a `2026-11-03_01_documentacion.md`; el tuyo queda como está.

### 1. Tus decisiones (sección 2)

| # | Decisión | Respuesta |
|---|---|---|
| 1 | Las pausas no mueven la fecha final | **Confirmado.** El día pausado no se devuelve ni se corre. |
| 2 | El plazo de pago cuenta el primer almuerzo | **Pasa a ser configurable.** Nueva clave `plazo_pago_cuenta_dia_inicio` (booleano, por defecto `true`, que es como lo hiciste). Con `true`, un plan que inicia el lunes vence el miércoles al final del día. Con `false`, el plazo empieza al día hábil siguiente y vence el jueves. Por favor, léela de Configuración en vez de dejarla fija en el código. |
| 3 | Si se aprueba tarde, pasa al ciclo siguiente | Queda como la aplicaste. |
| 4 | Suspender por pago no cuenta como pausa del cliente | Queda así. En el modelo se registra en `suspensiones_entrega` con `motivo = 'pago_vencido'`. |
| 5 | El servidor calcula `tipo_venta` | Queda así. El modelo lo sigue guardando en `suscripciones.tipo_venta`. |

### 2. Tus respuestas a mis preguntas

- **Geocodificación:** anotado que la decide el backend. La opción de Mapbox permanente queda como candidata.
- **Aviso de pago:** tu propuesta (un aviso el día anterior al vencimiento y otro al vencer) queda como pendiente #5 hasta que el equipo la apruebe.

### 3. Pendiente #3: modelo nuevo (bd.uml v4.1)

El modelo cambió dos veces desde el v3.7 para dejarlo entregable. Tienes que copiar a `docs/bd.uml` el archivo de `Modelado(5 trimestre) › V2 › 04/11/2026 › Modelado/bd.uml`. En esa carpeta también están `Cambios_v4.0.md` y `Cambios_v4.1.md`, con cada campo eliminado y su motivo.

Queda en **38 tablas y 55 relaciones**, con máximo 12 columnas por tabla. Esto es lo que toca al frontend:

| Tema | Antes | Ahora |
|---|---|---|
| Suscripción | `pago_pendiente`, `inicio_sin_pago`, `valor_total`, `dias_facturables` | Ya no se guardan; se calculan. **Pago pendiente** = no hay pago aprobado. **Inició sin pagar** = `fecha_limite_pago` tiene valor. **Total** = `valor_plan − descuento_festivos + cobro_cocas`. **Días facturables** salen del calendario. Puedes seguir mostrando `pagoPendiente` en la API como campo calculado. |
| Pagos | `subido_por_usuario_id`, `fecha_validacion` | Se eliminan. El `canal` dice quién lo subió. |
| Incidencias | `tipo_reportante`, `cliente_id`, `domiciliario_id`, `registrada_por_usuario_id` | Un solo `reportado_por_usuario_id`; su rol dice si es cliente, domiciliario o administrador. El cliente y el domiciliario salen de la entrega (`ruta_cliente_id`). |
| Entregas y GPS | `ruta_clientes.fecha`, `domiciliario_entrega_id`, `geolocalizacion_domiciliarios.domiciliario_id` | La fecha y el domiciliario se leen de `rutas`. |
| Clientes | `estado`, `notas_entrega` | Usar `usuarios.estado` y `direcciones_cliente.notas`. |
| Direcciones | `municipio`, `detalle` | Se eliminan; la zona define el municipio. |
| Menú | 4 tablas | 3 tablas: `menus_semana` → `menus_diarios` → `menu_items`. `menu_alternativas` ya no existe: la alternativa es un `menu_item` con `restriccion` y `reemplaza_item_id` (el plato base que reemplaza). |
| Cocas | `tipos_recipiente` | Se elimina. La **categoría del producto es la coca** (Seco, Sopa, Ensalada, Bebida). `recipientes.categoria_producto_id` dice qué pieza es. `juegos_cocas` y `recipientes` se mantienen. |
| Configuración | `historial_configuraciones`, `estado`, rangos min/max | Se elimina la tabla del historial y la HU "Consultar historial de cambios". Clave nueva: `plazo_pago_cuenta_dia_inicio`. |
| Otros | `servicios.duracion_dias`, `calendario.es_festivo`, `compra_detalle.subtotal`, `created_at` / `updated_at` | `duracion_dias` sale de `tipo_plan` (5, 10 o 20 días). Un festivo es un día no hábil con su descripción. El subtotal se calcula. Los campos técnicos de fecha se quitan. |

### Pendientes

| # | Pregunta | De | Estado |
|---|---|---|---|
| 1 | Servicio de geocodificación | documentación | lo decide el backend |
| 2 | Avisar al cliente antes del vencimiento | documentación | cerrada, ver #5 |
| 3 | Subir el bd.uml actualizado | frontend | cerrada: v4.1 en `V2 › 04/11/2026 › Modelado` |
| 4 | Confirmar las decisiones 1 y 2 | frontend | cerrada, ver sección 1 |
| 5 | Aprobar los avisos de pago por WhatsApp o correo (el día anterior y al vencer) | frontend | abierta (equipo) |
| 6 | ¿Algo del modelo v4.1 que no puedas implementar o que rompa una pantalla? | documentación | abierta |
