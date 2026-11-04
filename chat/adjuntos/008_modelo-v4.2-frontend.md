# Modelo v4.1 y v4.2 frente al frontend (respuesta al pendiente #6)

Claude Omar · 2026-11-04 · `06_Modelo_BD v08`

## 1. Ya aplicado

| Tema | Cómo quedó |
|---|---|
| `plazo_pago_cuenta_dia_inicio` | Clave nueva en Configuración (`inicioSinPago.cuentaDiaInicio`, por defecto `true`). Con `false` el plazo empieza al día hábil siguiente: un plan que inicia el lunes vence el jueves. Commit `2a28ae4`, con prueba. |
| Decisiones 3, 4 y 5 | Sin cambios: quedan como estaban. |

## 2. Se resuelve en el backend, sin tocar pantallas

El frontend puede seguir recibiendo estos campos calculados en la API.

| Modelo | El backend lo calcula o lo mapea así |
|---|---|
| Sin `pago_pendiente`, `valor_total`, `dias_facturables` | `pagoPendiente` = no hay pago aprobado; `amount` = plan − festivos + kit; `billableDays` sale del calendario. |
| `suspensiones_entrega.origen` | El `suspendedFor: 'pago'` del frontend se guarda como `origen = 'pago_vencido'`, y una pausa del cliente como `origen = 'cliente'`. Reanudar una pausa borra el registro. Así ya funciona. |
| Sin `modalidad_entrega` | El frontend manda las direcciones con sus días; es híbrida si hay más de una. |
| Avisos en `consentimientos` | El perfil sigue mostrando las casillas de WhatsApp y correo; cada cambio inserta un consentimiento (`aviso_whatsapp` o `aviso_correo`). |
| Incidencias con un solo `reportado_por_usuario_id` | Sin cambios en pantalla: el rol de quien reporta ya se muestra. |
| Pagos sin `subido_por_usuario_id` | `canal` (web o WhatsApp) dice quién lo subió. |
| `capacidad_maxima_diaria` en Configuración | Sin validar por ahora (vacía = sin límite). |
| Intentos fallidos desde `accesos` | Es del backend. |
| Menú: alternativa = `menu_item` con `reemplaza_item_id` | Se puede mapear. **Ojo:** en el frontend las alternativas son una lista **en orden** por plato (el cliente recibe la primera que puede comer), no una por restricción. Hace falta un `orden` o aceptar una alternativa por cada restricción. |

## 3. Choca con algo que pidió el PO o que usa una pantalla (decidir)

| # | Campo que sale | Qué rompe | Propuesta |
|---|---|---|---|
| A | `producto_terminado.responsable_id` y `motivo`, `ordenes_produccion.usuario_responsable_id` | El PO pidió "Marcar hecho" con quién lo hizo y "Anular" con motivo (2-nov). Hoy la pantalla de Producción los pide y los muestra. | Mantener los dos, o confirmar con el PO que se quitan. |
| B | `direcciones_cliente.detalle` (v4.1) | Es el apartamento, la torre o el piso ("Apto 501"). Sin él, el domiciliario no encuentra al cliente en un edificio. | Mantenerlo, o unirlo a la línea de la dirección (el frontend ya sabe mostrar "Carrera 76 # 33 - 20, Apto 501"). |
| C | `direcciones_cliente.etiqueta` | Con dos direcciones, el cliente ve "Casa" y "Oficina" en sus entregas y en el perfil. | Sin etiqueta, mostrar el barrio. Puedo hacerlo si lo confirman. |
| D | `fichas_tecnicas.porcion_servida_g` | La ficha industrial muestra la porción servida en gramos (pedido del PO, 1-nov). | Quitarla de la pantalla si se confirma. |
| E | `insumos.precio_unitario_referencia` | Insumos tiene la columna "Precio ref." y el costo por porción de la ficha la usa. | Pasar al precio de la última compra y mostrar "costo pendiente" si no hay compras. Puedo hacerlo. |
| F | `compras.observacion`, `menus_semana.publicado_por/en`, `menus_diarios.descripcion` | Se ven en el formulario de compra y en el aviso "Publicado el … por …". | Quitarlos. Pregunta: ¿se mantiene el **nombre del plato del día** que ve la web ("Ajiaco santafereño")? |
| G | `pagos.fecha_validacion` | El dashboard suma el ingreso del mes por la fecha de aprobación del pago. | ¿Con qué fecha se cuenta el ingreso: la del pago o la del inicio del plan? |
| H | Campos `created_at` | Usuarios y clientes muestran "Creado el …", y el dashboard cuenta los clientes nuevos por fecha. | Mantener `usuarios.created_at`, o aceptar que esos datos salen de la pantalla. |

Cuando decidan A a H, aplico en el frontend lo que corresponda.
