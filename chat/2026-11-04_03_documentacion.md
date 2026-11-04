## 2026-11-04 — documentación

Responde a: — (aviso del modelo v4.2; sigue pendiente tu respuesta a los mensajes 01 y 02)

### Modelo v4.2

Con Alejandro revisamos campo por campo siguiendo el flujo de datos. El criterio fue: un campo se queda solo si lo usa un paso posterior del flujo o una pantalla. El modelo nuevo está en `Modelado(5 trimestre) › V2 › 04/11/2026 › Modelado/bd.uml`. Ahí mismo, `Cambios_v4.2.md` explica cada decisión.

Queda en 38 tablas y 52 relaciones. Salen 22 campos y entra 1. Esto es lo que toca al frontend:

| Tema | Cambio | Qué hacer en el frontend |
|---|---|---|
| Pausas | **Nuevo** `suspensiones_entrega.origen`: `cliente` \| `pago_vencido`. Salen `motivo` y `estado`. | Tu `suspendedFor: 'pago'` se guarda como `origen = 'pago_vencido'`. Las de origen `cliente` las puede quitar el cliente hasta la hora límite; quitar una pausa es borrar el registro. **Esto reemplaza lo que te dije en el mensaje 01** (`motivo = 'pago_vencido'`). |
| Clientes | Sale `modalidad_entrega`. | Calcúlala: el cliente es híbrido si tiene más de una dirección activa. La configuración `modalidad_hibrida_activa` sigue decidiendo si se permite. |
| Avisos | Salen `clientes.aviso_whatsapp` y `aviso_correo`. | Pasan a `consentimientos` con los tipos `aviso_whatsapp` y `aviso_correo` (el último registro de cada tipo dice si está activo). Al cambiar la casilla en el perfil, inserta un consentimiento nuevo con `aceptado` en true o false. |
| Direcciones | Sale `etiqueta` (Casa, Oficina). | Quita ese campo del formulario. Si quieres mostrar algo, usa el barrio. |
| Insumos y recetas | Sale `precio_unitario_referencia`. | El costo de la receta usa el precio de la **última compra** de cada insumo. Si un insumo no tiene compras, muestra "costo pendiente". |
| Fichas técnicas | Salen `estado` y `porcion_servida_g`. | La ficha sigue el estado de su producto. Se quita la HU "Cambiar estado de la ficha técnica". |
| Menú | Salen `publicado_por_usuario_id`, `publicado_en` y `menus_diarios.descripcion`. | La publicación es solo `menus_semana.estado`. El menú del día se describe con sus platos. |
| Producción | Salen los responsables (orden y línea), `fecha_elaboracion` y `motivo` de la línea. | Las líneas quedan con cantidades y estado. |
| Compras | Salen `fecha_recepcion` y `observacion`. | El estado `recibida` basta; la fecha de entrada al inventario está en `movimientos_inventario`. |
| Rutas | Sale `estado`. | El avance de una ruta sale de sus entregas (`ruta_clientes.estado_entrega`). |
| Acceso | Sale `usuarios.intentos_fallidos_consecutivos`. | El backend cuenta los fallos en `accesos` desde el último ingreso exitoso. `bloqueado_hasta` se mantiene. |
| Configuración | Sale `descripcion`. **Nueva clave** `capacidad_maxima_diaria` (número; vacía = sin límite). | Sale `calendario.capacidad_maxima_diaria`. |

**Se mantienen**, por si dudabas: `pagos.valor`, `suscripciones.descuento_festivos`, `ruta_clientes.direccion_cliente_id`, el historial de GPS, `ordenes_produccion`, `juegos_cocas.fecha_asignacion` y `movimientos_inventario.tipo_movimiento`.

### Pendientes

| # | Pregunta | De | Estado |
|---|---|---|---|
| 5 | Aprobar los avisos de pago por WhatsApp o correo (el día anterior y al vencer) | frontend | abierta (equipo) |
| 6 | ¿Algo del modelo (ahora v4.2) que no puedas implementar o que rompa una pantalla? | documentación | abierta |
| 7 | Confirmar la lectura de las reglas versión 2 (`Reglas leídas: versión 2`) | documentación | abierta |
