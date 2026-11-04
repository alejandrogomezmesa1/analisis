# Modelo relacional v4.0 — modelo entregable (2026-11-04)

Revisión campo por campo de las 41 tablas. Reglas aplicadas:

1. **Máximo 12 columnas por tabla.**
2. Se quita lo **técnico** (`created_at`, `updated_at`) cuando ninguna historia de usuario lo usa.
3. Se quita lo **redundante**: un dato que ya vive en otra tabla (fecha y domiciliario de la ruta, estado de la cuenta en `usuarios`).
4. Se quita lo **calculado**: totales y conteos que salen de otros campos (`subtotal`, `valor_total`, `dias_facturables`, `pago_pendiente`).
5. Las tablas puente usan **llave compuesta** en vez de `id`.

Resultado: **41 tablas, 60 relaciones, 46 campos eliminados, 1 campo nuevo** (`incidencias.reportado_por_usuario_id`). Máximo 12 columnas por tabla.

Visor interactivo (relaciones animadas y notas por tabla): https://claude.ai/artifact/61mqHjLZm1YSZAVvvoqy8t — copia sin notas en `Visor_Interactivo/`.

## Procesos en orden del flujo de trabajo

1. **Acceso y seguridad**: Antes de operar: quién entra y con qué rol. — `roles`, `usuarios`, `tokens_restablecimiento`, `accesos`, `consentimientos`
2. **Configuración y calendario**: Reglas del negocio y días hábiles que usan todos los procesos. — `configuraciones_sistema`, `historial_configuraciones`, `calendario`
3. **Abastecimiento**: Insumos, proveedores y compras que alimentan el inventario. — `categorias_insumos`, `insumos`, `proveedores`, `proveedor_categorias`, `compras`, `compra_detalle`, `movimientos_inventario`
4. **Catálogo de cocina**: Platos, recetas (fichas técnicas) y tipos de coca. — `tipos_recipiente`, `categorias_productos`, `productos`, `fichas_tecnicas`, `ficha_tecnica_detalle`
5. **Oferta de planes**: Planes que se venden (semanal, quincenal, mensual). — `categorias_servicios`, `servicios`
6. **Registro de clientes**: El cliente, sus direcciones por día y sus juegos de cocas. — `clientes`, `direcciones_cliente`, `direccion_dias`, `juegos_cocas`, `recipientes`
7. **Venta y pagos**: Suscripción, comprobantes y pausas de entrega. — `suscripciones`, `pagos`, `suspensiones_entrega`
8. **Menú semanal**: Se publica el menú de la semana con alternativas por restricción. — `menus_semana`, `menus_diarios`, `menu_items`, `menu_alternativas`
9. **Producción**: Orden del día y líneas de producto terminado. — `ordenes_produccion`, `producto_terminado`
10. **Despacho y rutas**: Zonas, rutas del día, entregas y ubicación en tiempo real. — `zonas_cobertura`, `rutas`, `ruta_clientes`, `geolocalizacion_domiciliarios`
11. **Incidencias**: Novedades de la entrega y su solución. — `incidencias`

Domiciliarios no tiene tabla (es un usuario con rol Domiciliario). Dashboard no tiene tablas (vistas y consultas).

## Campos eliminados y motivo

### P1. Acceso y seguridad

| Tabla | Campo | Motivo |
| :--- | :--- | :--- |
| `usuarios` | `creado_por_usuario_id` | Auditoría que ninguna HU consulta; el alta la hace siempre el administrador. |
| `usuarios` | `acceso_enviado_en` | Solo informativo; el envío del correo de acceso no cambia el estado de la cuenta. |
| `usuarios` | `created_at` | Campo técnico de auditoría; el ORM lo puede manejar sin estar en el modelo entregable. |
| `tokens_restablecimiento` | `created_at` | Redundante: expira_en ya fija la vigencia del token. |
| `accesos` | `ip` | Ninguna HU filtra ni reporta por IP; fecha_hora, resultado y detalle bastan para la bitácora. |
| `consentimientos` | `ip` | Dato técnico; la evidencia de Ley 1581 queda con usuario, versión, fecha y canal. |
| `consentimientos` | `navegador` | Dato técnico sin uso en HU. |

### P2. Configuración y calendario

| Tabla | Campo | Motivo |
| :--- | :--- | :--- |
| `configuraciones_sistema` | `valor_minimo` | La validación de rango vive en la aplicación por clave (son pocas claves). |
| `configuraciones_sistema` | `valor_maximo` | Ídem valor_minimo. |
| `configuraciones_sistema` | `estado` | Una configuración no se desactiva: las funcionalidades se apagan con su propio valor booleano. |
| `configuraciones_sistema` | `updated_at` | Redundante: el último cambio está en historial_configuraciones.fecha. |
| `configuraciones_sistema` | `updated_by_usuario_id` | Redundante: el autor del cambio está en historial_configuraciones.usuario_id. |
| `calendario` | `es_festivo` | Redundante con es_habil = false + descripcion (el festivo es un día no hábil). |

### P3. Abastecimiento

| Tabla | Campo | Motivo |
| :--- | :--- | :--- |
| `insumos` | `created_at` | Campo técnico de auditoría. |
| `insumos` | `updated_at` | Campo técnico; los cambios de existencia ya quedan en movimientos_inventario. |
| `proveedores` | `created_at` | Campo técnico de auditoría. |
| `proveedor_categorias` | `id` | Tabla puente: la llave primaria es (proveedor_id, categoria_insumo_id). |
| `compras` | `created_at` | Redundante con fecha_compra. |
| `compra_detalle` | `subtotal` | Calculado: cantidad × precio_unitario. |
| `movimientos_inventario` | `usuario_id` | Ninguna HU consulta quién registró el movimiento; el origen ya está en compra u orden de producción. |

### P5. Oferta de planes

| Tabla | Campo | Motivo |
| :--- | :--- | :--- |
| `servicios` | `duracion_dias` | Redundante con tipo_plan (semanal = 5, quincenal = 10, mensual = 20 días hábiles, RN). |

### P6. Registro de clientes

| Tabla | Campo | Motivo |
| :--- | :--- | :--- |
| `clientes` | `notas_entrega` | Redundante con direcciones_cliente.notas (las indicaciones dependen de la dirección). |
| `clientes` | `estado` | Redundante con usuarios.estado (la cuenta del cliente). |
| `direcciones_cliente` | `municipio` | Lo determina la zona de cobertura. |
| `direcciones_cliente` | `detalle` | Torre/apto se escribe en la misma dirección o en notas. |
| `direccion_dias` | `id` | Tabla puente: la llave primaria es (direccion_cliente_id, dia_semana). |
| `juegos_cocas` | `estado` | Redundante con ubicacion (extraviado) y con el estado de la suscripción. |
| `recipientes` | `estado` | Redundante con estado_fisico (perdido / dañado). |

### P7. Venta y pagos

| Tabla | Campo | Motivo |
| :--- | :--- | :--- |
| `suscripciones` | `dias_facturables` | Calculado con el calendario entre fecha_inicio y fecha_vencimiento. |
| `suscripciones` | `valor_total` | Calculado: valor_plan − descuento_festivos + cobro_cocas. |
| `suscripciones` | `inicio_sin_pago` | Redundante: inició sin pagar ⇔ fecha_limite_pago tiene valor. |
| `suscripciones` | `pago_pendiente` | Calculado: no existe un pago aprobado para la suscripción. |
| `pagos` | `subido_por_usuario_id` | El canal ya dice si lo subió el cliente (web/app) o el administrador (panel_admin). |
| `pagos` | `fecha_validacion` | Sin uso en HU; el validador queda en validado_por_usuario_id. |

### P8. Menú semanal

| Tabla | Campo | Motivo |
| :--- | :--- | :--- |
| `menus_semana` | `created_at` | Campo técnico de auditoría. |
| `menus_diarios` | `nombre` | Redundante: el menú se identifica por su fecha (calendario). |
| `menus_diarios` | `created_at` | Campo técnico de auditoría. |
| `menu_alternativas` | `orden` | Una alternativa por restricción y plato; no hace falta prioridad. |

### P9. Producción

| Tabla | Campo | Motivo |
| :--- | :--- | :--- |
| `ordenes_produccion` | `created_at` | Redundante: la fecha de la orden es la del menú del día (calendario). |

### P10. Despacho y rutas

| Tabla | Campo | Motivo |
| :--- | :--- | :--- |
| `ruta_clientes` | `fecha` | Redundante: es rutas.fecha. |
| `ruta_clientes` | `domiciliario_entrega_id` | Redundante: es rutas.domiciliario_id (si se reasigna, se actualiza la ruta). |
| `geolocalizacion_domiciliarios` | `domiciliario_id` | Redundante: es rutas.domiciliario_id. |

### P11. Incidencias

| Tabla | Campo | Motivo |
| :--- | :--- | :--- |
| `incidencias` | `tipo_reportante` | Se deduce del rol de reportado_por_usuario_id. |
| `incidencias` | `cliente_id` | Se obtiene de la entrega (ruta_cliente) o del usuario que reporta. |
| `incidencias` | `domiciliario_id` | Se obtiene de la ruta de la entrega. |
| `incidencias` | `registrada_por_usuario_id` | Reemplazado por reportado_por_usuario_id (un solo campo para quien reporta). |

## Columnas por tabla

| Proceso | Tabla | Columnas |
| :--- | :--- | ---: |
| P1 | `roles` | 3 |
| P1 | `usuarios` | 10 |
| P1 | `tokens_restablecimiento` | 5 |
| P1 | `accesos` | 6 |
| P1 | `consentimientos` | 7 |
| P2 | `configuraciones_sistema` | 8 |
| P2 | `historial_configuraciones` | 6 |
| P2 | `calendario` | 5 |
| P3 | `categorias_insumos` | 3 |
| P3 | `insumos` | 8 |
| P3 | `proveedores` | 7 |
| P3 | `proveedor_categorias` | 2 |
| P3 | `compras` | 6 |
| P3 | `compra_detalle` | 5 |
| P3 | `movimientos_inventario` | 9 |
| P4 | `tipos_recipiente` | 3 |
| P4 | `categorias_productos` | 4 |
| P4 | `productos` | 6 |
| P4 | `fichas_tecnicas` | 7 |
| P4 | `ficha_tecnica_detalle` | 4 |
| P5 | `categorias_servicios` | 3 |
| P5 | `servicios` | 7 |
| P6 | `clientes` | 8 |
| P6 | `direcciones_cliente` | 10 |
| P6 | `direccion_dias` | 2 |
| P6 | `juegos_cocas` | 5 |
| P6 | `recipientes` | 4 |
| P7 | `suscripciones` | 12 |
| P7 | `pagos` | 9 |
| P7 | `suspensiones_entrega` | 6 |
| P8 | `menus_semana` | 5 |
| P8 | `menus_diarios` | 4 |
| P8 | `menu_items` | 4 |
| P8 | `menu_alternativas` | 4 |
| P9 | `ordenes_produccion` | 3 |
| P9 | `producto_terminado` | 9 |
| P10 | `zonas_cobertura` | 5 |
| P10 | `rutas` | 5 |
| P10 | `ruta_clientes` | 11 |
| P10 | `geolocalizacion_domiciliarios` | 5 |
| P11 | `incidencias` | 12 |

## Impacto en el frontend

- `suscripciones`: ya no hay `pago_pendiente`, `inicio_sin_pago`, `valor_total` ni `dias_facturables`. Pago pendiente = no hay pago aprobado; inició sin pagar = `fecha_limite_pago` tiene valor; total = `valor_plan − descuento_festivos + cobro_cocas`.
- `incidencias`: un solo `reportado_por_usuario_id`; el tipo de reportante sale de su rol. Cliente y domiciliario se obtienen de la entrega (`ruta_cliente_id`).
- `ruta_clientes` y `geolocalizacion_domiciliarios`: la fecha y el domiciliario se leen de `rutas`.
- `clientes`: sin `estado` (usar `usuarios.estado`) ni `notas_entrega` (usar `direcciones_cliente.notas`).
- `servicios`: sin `duracion_dias` (sale de `tipo_plan`). `calendario`: sin `es_festivo` (no hábil + descripción).
