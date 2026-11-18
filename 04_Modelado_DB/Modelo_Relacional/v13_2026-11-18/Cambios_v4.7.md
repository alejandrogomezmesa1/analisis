# Modelo relacional v4.7: acuerdos G1 a G4 con el frontend (2026-11-18)

Antes: [Cambios_v4.6.md](../v12_2026-11-13/Cambios_v4.6.md).

Resultado: **41 tablas y 55 relaciones**, todas con 12 columnas o menos. Aplica los acuerdos del chat con Claude Omar: G1 (14-nov), G2 y G3 (17-nov), G4 (17-nov, el modelado lo delegó Omar) y la foto del menú (#029 y #031).

| Origen | Cambio |
| :--- | :--- |
| G1-Q2 | `componente_alimento` suma `frutos_secos` y `huevo`. |
| G1-Q5 | Salen las claves `intentos_maximos_acceso` y `minutos_bloqueo_acceso`: el bloqueo es solo del backend. |
| G2-Q2 | `productos.imagen_url` (mismo almacenamiento que los comprobantes). |
| G2-Q3 | `ordenes_produccion.cantidad_planificada` (total del día); sale de `producto_terminado`. |
| G2-Q4 | `productos.contiene` → `alergenos`; `movimientos_inventario` → `movimientos_insumos` (y su enum `tipo_movimiento_insumo`). |
| G3-Q1 | `usuarios.tipo_documento` (enum CC, CE, NIT, PA, PPT); único `(tipo_documento, documento)`. |
| G3-Q2 | `direcciones_cliente.municipio`. |
| G3-Q3/Q4 | `servicios.dias_habiles` y `servicios.beneficios`. |
| G3-Q5 | `fichas_tecnicas.rendimiento_porciones`; el costo por porción se divide por él. `porciones_por_tanda` es el tope de la olla. |
| G3-Q6 | Solo 4 acciones en `accion_permiso` (sin eliminar ni exportar). No se borra nada: se inactiva. |
| G3-Q7 | `zonas_cobertura.nombre_publico` y `municipio`. |
| G3-Q8 | Claves `banco_pago`, `tipo_cuenta_pago`, `numero_cuenta_pago`, `titular_cuenta_pago` y `horario_entrega`; sale `clientes.franja_horaria`. |
| G3-Q11/Q12/Q13 | Tabla `identidades_externas` (usuario, proveedor google/apple, sub, correo, fecha de vínculo; único `(proveedor, sub)`), solo clientes. `usuarios.password` opcional. |
| G4-Q1 | Tabla `codigos_acceso` (código de 6 dígitos con hash, vence en 10 min, 5 intentos, un solo uso). |
| G4-Q2 | `usuarios.telefono` único, normalizado +57. |
| G4-Q3 | `accesos.metodo` (enum `metodo_acceso`: password, codigo, google, apple). |
| G4-Q4 | Sin cambios en el modelo: el límite de `/auth/lookup` por IP es del backend, en memoria. |
| #029/#031 | `menus_diarios.foto_url`; sin foto, la API usa la `imagen_url` del seco del menú. |
| Permisos | La nota de `roles` ya no lista las HU de permisos; la de `permisos` lista las 8 HU del subproceso Permisos. |

Sin cambios en el modelo: G3-Q9 (salen las notas para la cocina) y G3-Q10 (campos del frontend sin columna), que son del frontend.
