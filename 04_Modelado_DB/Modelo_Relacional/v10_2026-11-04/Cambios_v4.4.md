# Modelo relacional v4.4: respuesta al mensaje #008 de Claude Omar (2026-11-04)

Antes: [Cambios_v4.3.md](../v9_2026-11-04/Cambios_v4.3.md).

Resultado: 37 tablas y 52 relaciones.

Claude Omar revisó la v4.2 contra el frontend y encontró campos eliminados que una pantalla usa o que pidió el PO (puntos A a I del adjunto `chat/adjuntos/008_modelo-v4.2-frontend.md`). Alejandro decidió así:

| # | Tema | Decisión | Cambio en el modelo |
| :--- | :--- | :--- | :--- |
| A | Responsable y motivo en producción | Vuelven en la línea, porque los pidió el PO el 2-nov. | `producto_terminado.responsable_id` (FK a usuarios) y `motivo` (obligatorio al anular). La orden sigue sin responsable. |
| B | Apartamento, torre o piso | Va en el campo de notas de la dirección, que sí o sí se queda. | Se precisa la descripción de `direcciones_cliente.notas`. |
| C | Etiqueta Casa / Oficina | Sigue fuera: se muestra el barrio. | — |
| D | Porción servida (g) | Sigue fuera. Hay que avisar al PO. | — |
| E | Precio de referencia del insumo | Sigue fuera: se usa el precio de la última compra o se muestra "costo pendiente". | — |
| F | Nombre del almuerzo del día | Sale de los platos del menú (el producto principal). | — |
| G | Fecha de los ingresos en el dashboard | Se usa `pagos.fecha_pago` de los pagos aprobados. | — |
| H | "Creado el…" y clientes nuevos | Se calcula: un cliente nuevo es el que tiene su primera suscripción en el periodo. Se quita "Creado el" de las pantallas. | — |
| I | Alternativas del menú | Una alternativa por alergia (`menu_items.alergia` + `reemplaza_item_id`). El frontend se adapta. | — |
