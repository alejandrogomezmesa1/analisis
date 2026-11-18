# Acuerdo G2: notas de Alejandro del 11-nov frente al frontend

Claude Alejo · 2026-11-17 · base `06_Modelo_BD v12` (DBML v4.6). Ronda G2-1 (#017 → #021).

## Decisiones

| # | Tema | Decisión | Decidió |
|---|---|---|---|
| G2-1 Q1 | Permisos | Matriz módulo × acción en Roles; el menú y los botones salen de los permisos que manda el servidor (`user.permissions`), no del mapa fijo del frontend | Omar (delegada) |
| G2-1 Q2 | Imagen | `productos.imagen_url`; el archivo se guarda en el mismo almacenamiento que los comprobantes | Omar (delegada) |
| G2-1 Q3 | Planificada | `ordenes_produccion.cantidad_planificada` (total de almuerzos); cada línea muestra la cantidad calculada y la producida | Omar (delegada) |
| G2-1 Q4 | Renombres | `contiene` → `alergenos` y `movimientos_inventario` → `movimientos_insumos` en el modelo, la API y el frontend | Omar (delegada) |

## Qué hace cada lado

**Modelo (Claude Alejo):**
- Ya en la v4.6: `permisos` y `rol_permisos`.
- En la v4.7: `productos.imagen_url`, el renombre `alergenos`, `cantidad_planificada` pasa a `ordenes_produccion` y sale de `producto_terminado`, y `movimientos_inventario` → `movimientos_insumos`.

**Frontend (Claude Omar), al confirmarse:**
- Roles: la matriz módulo × acción (ver, crear, editar, cambiar_estado; según G3-Q6 no hay eliminar ni exportar).
- El menú y los botones se calculan con `user.permissions`; `roles.js` queda solo como respaldo sin conexión.
- Productos: subir la foto del plato.
- Producción: el total arriba, y en cada línea la cantidad calculada y la producida.
- Los nombres `alergenos` y `movimientos_insumos` en la API y en las pantallas.
