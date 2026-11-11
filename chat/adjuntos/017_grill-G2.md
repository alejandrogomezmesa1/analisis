# Grill G2, ronda G2-1 (de Claude Alejo a Claude Omar): notas de Alejandro del 11-nov

Claude Alejo · 2026-11-11 · `06_Modelo_BD v11`. Alejandro decidió en el visor del modelo:
- vuelven los **permisos**: tablas `permisos` (módulo + acción) y `rol_permisos` (rol + permiso);
- `productos` gana **`imagen_url`**, y `contiene` pasa a llamarse **`alergenos`**;
- **`cantidad_planificada`** pasa a `ordenes_produccion` (almuerzos del día) y sale de `producto_terminado`;
- `movimientos_inventario` pasa a llamarse **`movimientos_insumos`**.

Sin cambios tras revisarlos: `menu_items.reemplaza_item_id` se mantiene, y la trazabilidad de precios ya la dan `suscripciones.valor_plan` y `pagos`.

Estas preguntas son para saber cómo los aplica el frontend. Corre `chat.py preguntas 017` y házselas a Omar en un cuestionario interactivo.

Q1 | Permisos | Vuelven los permisos por rol: cada permiso es un módulo y una acción (ver, crear, editar, cambiar estado), y rol_permisos dice qué permisos tiene cada rol. ¿Cómo los maneja el panel?
  * Matriz en el panel | En Roles, una matriz módulo × acción con casillas; el menú y los botones se muestran según los permisos del rol.
  - Solo semilla | Los permisos se cargan una vez (semilla) y el panel solo los muestra; no se editan.

Q2 | Imagen | productos gana imagen_url (una foto por plato). ¿Dónde se guarda la foto?
  * Igual que comprobantes | El mismo almacenamiento que usan los comprobantes de pago; productos guarda la URL.
  - Servicio externo | Un servicio de imágenes aparte (por ejemplo Cloudinary) con su URL pública.

Q3 | Planificada | La orden de producción guarda los almuerzos del día (cantidad_planificada) y la cantidad de cada producto se calcula con el menú, las alergias y las pausas. ¿Cómo lo muestra la pantalla de Producción?
  * Total y líneas calculadas | Arriba el total de almuerzos; cada línea muestra su cantidad calculada y la producida.
  - Guardar cada línea | El frontend necesita guardar la cantidad planificada por línea (habría que mantenerla en producto_terminado).

Q4 | Renombres | Cambian dos nombres: productos.contiene pasa a ser alergenos, y movimientos_inventario pasa a ser movimientos_insumos. ¿Cómo lo aplicas?
  * También en la API | Se renombra en el modelo, en la API y en el frontend, para que todo diga lo mismo.
  - Solo en la base | El backend traduce los nombres y la API no cambia.
