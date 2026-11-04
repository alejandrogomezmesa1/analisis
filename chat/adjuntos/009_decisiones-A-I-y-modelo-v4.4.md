# Decisiones sobre tu adjunto 008 y modelo v4.4

Claude Alejo · 2026-11-04 · `06_Modelo_BD v10` (DBML v4.4) en `Modelado(5 trimestre) › 01_VIGENTE › 06_Modelo_BD`

## 1. Puntos A a I (decidió Alejandro)

| # | Decisión | Qué haces en el frontend |
|---|---|---|
| A | **Vuelven** `producto_terminado.responsable_id` y `motivo`, como pidió el PO. La orden **no** tiene responsable. | Mantén "Marcar hecho" con responsable y "Anular" con motivo en la línea; quita el responsable de la orden. |
| B | El apartamento, la torre o el piso van en **`direcciones_cliente.notas`**, que es obligatorio en edificios. No hay campo aparte. | Usa `notas` para "Apto 501, torre 2…" y muéstralo junto a la dirección. |
| C | Sin etiqueta Casa / Oficina. | Muestra el **barrio** en su lugar, como propusiste. |
| D | Sin `porcion_servida_g`. | Quítala de la ficha industrial. Alejandro se lo comenta al PO. |
| E | El precio del insumo es el de su **última compra**. | Columna "Precio (última compra)" y "costo pendiente" en las fichas cuyos insumos no se han comprado. |
| F | El nombre del almuerzo del día sale de **los platos del menú** (el producto principal). Salen la observación de compras y "Publicado por/el". | Arma el nombre con `menu_items → productos`. |
| G | Los ingresos del dashboard se cuentan por **`pagos.fecha_pago`** de los pagos aprobados. | Cambia la fecha de la suma mensual. |
| H | Sin `created_at`. **Un cliente nuevo** es el que tiene su primera suscripción en el periodo. | Quita "Creado el…" de usuarios y clientes, y calcula los clientes nuevos con la primera `fecha_solicitud`. |
| I | **Una alternativa por alergia**: `menu_items.alergia` + `reemplaza_item_id`, no una lista en orden. | Adapta el editor del menú: cada alternativa dice a qué plato reemplaza y para qué alergia. |

## 2. Lo que cambió en v4.3 (por notas de Alejandro en el visor)

| Tema | Cambio |
|---|---|
| Acceso | Salen `accesos.detalle` y `usuarios.bloqueado_hasta`. El bloqueo se calcula contando los fallos (`accesos.resultado`) dentro de la ventana. Claves nuevas: `intentos_maximos_acceso` (3) y `minutos_bloqueo_acceso` (15). |
| Restablecer contraseña | Se elimina la tabla `tokens_restablecimiento`. El backend envía un **enlace firmado** con su vencimiento y el hash de la contraseña actual (sirve una sola vez y no se guarda). |
| Alergias | `clientes.restricciones` pasa a ser **`clientes.alergias`** (misma lista fija: carne, cerdo, mariscos, gluten, lácteos) y **sale** el texto libre `alergias_alimentarias`. `menu_items.restriccion` pasa a ser `alergia`. El tipo de incidencia `restriccion_no_atendida` pasa a ser **`alergia_no_atendida`**. En el registro, un solo campo de alergias con la lista fija. |
| Inventario | Salen `movimientos_inventario.motivo` (y su enum) y `observacion`. El origen se sabe por `compra_detalle_id` u `orden_produccion_id`; si no tiene ninguno, es un ajuste o una merma. |
| Entregas | Salen `ruta_clientes.calificacion` y `comentario_calificacion`: quita la calificación del almuerzo. |
| Se mantienen | `rutas.fecha` y `suscripciones.tipo_venta`. |

Detalle de cada versión: `01_VIGENTE/06_Modelo_BD/Cambios_v4.4.md`; las anteriores están en `02_HISTORIAL/06_Modelo_BD/`.
