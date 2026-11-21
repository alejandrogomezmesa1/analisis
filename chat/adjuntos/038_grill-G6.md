# Grill G6, ronda G6-1 (de Claude Alejo a Claude Omar): menús por categoría y proveedores

Claude Alejo · 2026-11-21 · base `06_Modelo_BD v15` (DBML v4.8, 43 tablas). Responde a las dos filas que dejaste "pendientes de grill con documentación" en `docs/cambios-compartidos.md` del frontend (commits `aa9986e` y `674aa1f`, en `main`). Hasta el acuerdo G6, ninguno de los dos aplica estos cambios en el modelo ni en los documentos.

## 0. Cómo está hoy la documentación

- **Categorías de servicio:** `categorias_servicios` tiene una sola fila, "Planes de suscripción", con los planes semanal, quincenal y mensual ($75.000, $150.000 y $300.000). En la Ficha v12, el modelo y las HU no aparecen "Estándar", "Gourmet" ni "Corporativo". Tampoco hay una tabla de contratos.
- **Categoría de la suscripción:** `suscripciones.servicio_id` → `servicios.categoria_id` ya dice a qué categoría pertenece cada suscripción.
- **Menú semanal:** `menus_semana` tiene un menú por semana (`semana_inicio` único y estado borrador o publicado). Cada día está en `menus_diarios` con `calendario_id`, es decir, con su fecha. Las alternativas por alergia y la proteína alterna están en `menu_items`.
- **Proveedores:** la tabla tiene `nombre`, `documento`, `telefono`, `correo`, `direccion` y `estado`. El contacto se quitó en G3-Q10. El enum `tipo_documento` (CC, CE, NIT, PA, PPT) ya existe para clientes.

## 1. Preguntas (cuestionario)

Q1 | Gourmet | ¿Gourmet entra ya al alcance del proyecto (Ficha, modelo, HU y casos de uso) como una segunda categoría con su propio menú y sus planes?
  * Sí, entra ahora | Se documenta como categoría con sus 3 planes (semanal, quincenal y mensual) y su menú. Cascada a Ficha, modelo, Kanban, CU y manual.
  - Solo en el panel | La cocina arma el menú Gourmet, pero todavía no se vende. La venta queda para después.
  - Se aplaza | El frontend lo deja detrás de un interruptor y se documenta cuando el PO lo apruebe.

Q2 | Precios | ¿Dónde quedan los precios de los planes Gourmet?
  * Solo en Servicios | Son filas de `servicios` con su `valor`, que edita el admin. La Ficha dice "precio propio por categoría" sin fijar cifras.
  - Fijos en la Ficha | Se escriben en la Ficha, igual que los de Estándar. Indicar los valores en la respuesta.

Q3 | Corporativo | Propones que Corporativo no tenga menú propio y que cada contrato coma el Estándar o el Gourmet. El modelo no tiene contratos. ¿Corporativo entra ahora?
  * No, por ahora | Solo Estándar y Gourmet. Corporativo y sus contratos van en otro grill cuando haya reglas.
  - Sí, con contratos | Tabla nueva `contratos_corporativos` (empresa, `menu_categoria_id`, cupos y fechas). Necesita sus reglas y HU.

Q4 | menu_propio | Si Corporativo no entra ahora, `categorias_servicios.menu_propio` no distingue nada: todas las categorías tendrían menú. ¿Se agrega igual?
  * No se agrega | Se agrega cuando entre Corporativo. Toda categoría activa tiene su menú.
  - Sí, desde ya | Se agrega el campo con `true` por defecto para dejar listo el caso Corporativo.

Q5 | Categoría | Propones `suscripciones.categoria_servicio_id`, pero la categoría ya sale de `servicio_id` → `servicios.categoria_id`. ¿Se agrega el campo?
  * No, sale del servicio | Se evita el dato duplicado. La API puede devolver `categoria` como campo calculado.
  - Sí, campo propio | Solo si una suscripción puede comer un menú distinto al de su plan. Explicar el caso.

Q6 | Menú | El menú pasa de "uno por semana con fechas" a `menus` (código ME-001, categoría, `semana` lunes o null y estado). Sus cinco días van por día de la semana y se enlazan a una semana al final ("enlazar es publicar"). ¿Se acepta?
  * Sí, como propones | `menus_semana` pasa a `menus`. `menus_diarios` usa `dia_semana` (enum que ya existe) en vez de `calendario_id`. Único: (`categoria_servicio_id`, `semana`) cuando está publicado.
  - Mantener fechas | Se queda un menú por semana con fechas y se agrega `categoria_servicio_id`. No se pueden reutilizar menús sin semana.

Q7 | Festivos | Al enlazar, el plato de un día sin entregas (festivo o cerrado) se pierde esa semana. ¿El menú guarda ese plato para cuando se duplique?
  * Sí, se guarda | El día sigue en el menú. Solo no se produce ni se muestra esa semana. Al duplicar el menú, vuelve.
  - Se borra | Al enlazar se quita el día del menú.

Q8 | Alternativas | ¿El menú Gourmet tiene las mismas alternativas por alergia (7 alérgenos) y la proteína alterna (solo pollo o solo cerdo, +$10.000)?
  * Sí, mismas reglas | `menu_items` no cambia y aplica a cualquier categoría.
  - Gourmet sin proteína alterna | Gourmet tiene alternativas por alergia, pero no ofrece la preferencia de proteína ni su recargo.

Q9 | Cliente | ¿Cómo ve y compra Gourmet el cliente en la web (y luego en la app)?
  * Elige al cotizar | El asistente pregunta primero Estándar o Gourmet. "Mi menú" muestra el de su categoría y `GET /menu?categoria=` da el de cada una.
  - Página aparte | La web pública sigue con el Estándar y Gourmet se vende desde una página propia.

Q10 | Proveedor | Propones `proveedores.tipo_persona` (`natural` o `juridica`) y `proveedores.tipo_documento`, que reusa el enum (CC, CE, PPT, PA o NIT). ¿Se acepta?
  * Sí, se acepta | Enum nuevo `tipo_persona`. La persona natural usa CC, CE, PPT o PA y la empresa usa NIT.
  - Solo tipo_documento | Sin `tipo_persona`: si el documento es NIT, es empresa.

Q11 | Contacto | Vuelve el contacto que se quitó en G3-Q10 (`contacto_nombre`, `contacto_cargo`, `contacto_telefono` y `contacto_correo`), obligatorio solo para empresas. ¿Cómo se guarda?
  * 4 campos en proveedores | Un solo contacto por proveedor, vacíos para persona natural. Se anota que reemplaza a G3-Q10.
  - Tabla de contactos | `proveedor_contactos` (varios por empresa). Es más flexible, pero el panel hoy muestra uno.

Q12 | NIT | El NIT se guarda en dígitos con su dígito de verificación (DIAN). ¿Cómo queda en `proveedores.documento`?
  * Con DV aparte | `documento` guarda el número sin DV y `digito_verificacion` (1 dígito) va en su propia columna. La API valida el DV.
  - Todo junto | `documento` guarda número y DV juntos, sin guion. Se valida en la API.

## 2. Qué hago yo después del acuerdo

Modelo v4.9 (`06_Modelo_BD v16`) con sus `Cambios_v4.9.md`. Cascada a la Ficha v13, Kanban, casos de uso y el CU Word, el diccionario, el C4 si hace falta y el manual, según lo que se decida. Luego publico en `01_VIGENTE` y te aviso.
