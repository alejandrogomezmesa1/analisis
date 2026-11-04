# Modelo relacional v4.3 — notas del visor (2026-11-04)

Antes: [Cambios_v4.2.md](../v8_2026-11-04/Cambios_v4.2.md).

**Resultado:** 37 tablas y 51 relaciones, con máximo 12 columnas por tabla.

**Criterio de esta revisión:** una base de datos sencilla y lo más barata posible, sin perder escalabilidad ni mantenibilidad.

## Cambios

| Nota | Decisión | Qué cambia en el modelo |
| :--- | :--- | :--- |
| accesos / usuarios | El bloqueo por intentos fallidos se calcula. | Salen `accesos.detalle` y `usuarios.bloqueado_hasta`. El backend cuenta los fallos (`accesos.resultado`) que hubo dentro de la ventana de tiempo. Claves nuevas de Configuración: `intentos_maximos_acceso` (3) y `minutos_bloqueo_acceso` (15). |
| tokens_restablecimiento | Se elimina la tabla. | El enlace para restablecer la contraseña va firmado, con su vencimiento y el hash de la contraseña actual. Así sirve una sola vez, porque deja de valer al cambiar la contraseña. A cambio, no se puede anular un enlace antes de que venza ni queda registro de las solicitudes. |
| menu_items | Un solo dato: alergias, con lista fija. | `clientes.restricciones` pasa a llamarse `clientes.alergias` (con el enum `componente_alimento`) y sale `alergias_alimentarias` (texto libre). `menu_items.restriccion` pasa a llamarse `alergia`. El tipo de incidencia `restriccion_no_atendida` pasa a ser `alergia_no_atendida`. |
| movimientos_inventario | Salen `motivo` (y su enum) y `observacion`. | El origen del movimiento lo dice `compra_detalle_id` u `orden_produccion_id`. Si no tiene ninguno, es un ajuste o una merma. |
| ruta_clientes | Salen `calificacion` y `comentario_calificacion`. | La calificación del almuerzo sale del alcance. |
| rutas | Se mantiene `fecha`. | La fecha de cada entrega se toma de su ruta. |
| suscripciones | Se mantiene `tipo_venta`. | Queda guardado cómo se clasificó la venta en el momento de hacerla. |
| direccion_dias | Sin cambios. | Es una llave primaria compuesta (dirección + día), y la dirección es a la vez llave foránea. |
