# Modelo relacional v4.2 — grilling del flujo de datos (2026-11-04)

Antes: [Cambios_v4.1.md](../v7_2026-11-04/Cambios_v4.1.md) y [Cambios_v4.0.md](../v6_2026-11-04/Cambios_v4.0.md).

**Criterio:** un campo se queda solo si lo usa un paso posterior del flujo o una pantalla.

**Resultado:** 38 tablas y 52 relaciones, con máximo 12 columnas por tabla. Salen 22 campos y entra 1.

## Principios (ronda 1)

| # | Principio | Campos que salen |
| :--- | :--- | :--- |
| Q1 | Se guarda quién hizo algo solo en pagos (`validado_por_usuario_id`) e incidencias (`gestionada_por_usuario_id`). | `menus_semana.publicado_por_usuario_id`, `ordenes_produccion.usuario_responsable_id`, `producto_terminado.responsable_id` |
| Q2 | Una fecha se guarda solo si la usa una regla o un reporte. | `menus_semana.publicado_en`, `compras.fecha_recepcion`, `producto_terminado.fecha_elaboracion` |
| Q3 | Sin estado donde no aporta. | `rutas.estado`, `suspensiones_entrega.estado`, `fichas_tecnicas.estado` |
| Q4 | Un texto libre se guarda solo si alguien lo lee. | `menus_diarios.descripcion`, `configuraciones_sistema.descripcion`, `compras.observacion`, `direcciones_cliente.etiqueta`, `suspensiones_entrega.motivo`, `producto_terminado.motivo` |

## Decisiones por campo

| # | Decisión |
| :--- | :--- |
| Q5 | Sale `usuarios.intentos_fallidos_consecutivos`. Los intentos se cuentan en `accesos` desde el último ingreso exitoso. Se mantiene `bloqueado_hasta`. |
| Q6 | `calendario.capacidad_maxima_diaria` pasa a la clave `capacidad_maxima_diaria` de Configuración. Vacía significa sin límite. |
| Q7 / Q11 | Sale `insumos.precio_unitario_referencia`. El precio sale de la última compra. Si un insumo no tiene compras, la receta muestra "costo pendiente". |
| Q8 | Se mantiene `movimientos_inventario.tipo_movimiento`. |
| Q9 | Nuevo `suspensiones_entrega.origen` (`cliente` \| `pago_vencido`). El cliente puede quitar su pausa; la suspensión por pago solo la quita el administrador. |
| Q10 | Se mantiene `suscripciones.descuento_festivos`: lo vendido queda fijo. |
| Q12 | Sale `fichas_tecnicas.porcion_servida_g`. Se quedan `porciones_por_tanda`, `tiempo_preparacion_min` y `procedimiento`. |
| Q13 | Sale `clientes.modalidad_entrega` (y su enum). Se calcula: más de una dirección activa significa híbrida. |
| Q14 | `clientes.aviso_whatsapp` y `aviso_correo` pasan a `consentimientos` como los tipos `aviso_whatsapp` y `aviso_correo`. El último registro de cada tipo dice si está activo. |
| Q15 | Se mantiene `ruta_clientes.direccion_cliente_id`: guarda a dónde se entregó realmente. |
| Q16 | Se mantiene el historial de `geolocalizacion_domiciliarios`. |
| Q17 | Se mantiene `ordenes_produccion` (módulo del Story Mapping y kárdex). |
| Q18 | Se mantiene `juegos_cocas.fecha_asignacion`. |
| Q19 | Se mantiene `pagos.valor`: el administrador lo compara con el total. |

## Pendiente en cascada

- Story Mapping:
  - quitar "Cambiar estado de la ficha técnica" (la ficha sigue el estado de su producto);
  - quitar "Consultar historial de cambios" (v4.1);
  - revisar las historias de usuario de modalidad de entrega y de avisos.
- Ficha, manual técnico y documentación de casos de uso.
- Frontend: avisado en el chat.
