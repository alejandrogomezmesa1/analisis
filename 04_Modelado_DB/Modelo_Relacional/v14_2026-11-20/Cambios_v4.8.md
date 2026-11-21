# Modelo relacional v4.8: conciliación con el frontend (2026-11-20)

Antes: [Cambios_v4.7.md](../v13_2026-11-18/Cambios_v4.7.md).

Resultado: **43 tablas y 59 relaciones**, todas con 12 columnas o menos. Aplica las decisiones de Alejandro en el grill del 20-nov (cuestionarios interactivos) para corregir las discrepancias entre la documentación y el frontend. Lo que toca al frontend se acuerda con Claude Omar en el grill G5.

| Decisión | Cambio |
| :--- | :--- |
| Cupo de cocina con lista de espera | La clave `capacidad_maxima_diaria` pasa a `cupo_suscripciones_nuevas_semana` (suscripciones nuevas por semana). `estado_suscripcion` suma `en_espera`: venta nueva por encima del cupo, sin pago, hasta que el administrador le asigna una semana; entonces pasa a `pendiente_pago`. Renovaciones y reingresos no ocupan cupo. |
| Preferencia de proteína | Enum `preferencia_proteina` (`solo_pollo`, `solo_cerdo`). `clientes.preferencia_proteina` (se elige en venta nueva, renovación o reingreso). `menu_items.proteina`: el mismo seco con la otra proteína; único `(menu_id, producto_id, alergia, proteina)`. Clave `recargo_preferencia_proteina` ($10.000 por plan), que se suma a `suscripciones.valor_plan` al vender (sin columna nueva, para no pasar de 12). |
| Configuraciones fijas y codificadas | La nota de `configuraciones_sistema` deja solo Listar, Editar y Activar/desactivar: el administrador no crea claves. Clave nueva `costo_diario_domiciliario` para el costo-beneficio por zona. El historial sigue fuera (tabla eliminada). |
| Faltantes de insumos | Tabla nueva `faltantes_insumos` (orden, insumo, cantidad, quién reporta, estado, fecha). |
| Orden anulada | La nota de `ordenes_produccion` incluye `anulada` como estado calculado (todas las líneas anuladas) y la generación automática desde el menú publicado. |
| Producto terminado | La nota dice que el registro se crea al marcar la línea como hecha y que la cantidad se corrige desde la orden. |
| Rutas = zonas | La nota de `rutas`: zona activa + domiciliario (`zonas_cobertura.domiciliario_id` por defecto); las rutas del día se generan solas. Sale la HU Crear ruta. |
| Web push | Tabla nueva `dispositivos_push` (usuario, endpoint, claves, fecha, estado). |

Sin cambios: `juegos_cocas`, `geolocalizacion_domiciliarios` e `incidencias.foto_url` ya cubrían el control de cocas, el GPS y las novedades con foto; ahora el frontend tiene que implementarlos (G5).
