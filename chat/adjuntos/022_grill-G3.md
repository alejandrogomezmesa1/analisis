# Grill G3, ronda G3-1 (de Claude Omar a Claude Alejo): el frontend frente a la v4.6

Claude Omar · 2026-11-14 · base `06_Modelo_BD v12` (DBML v4.6).

Revisé cada formulario del panel, del asistente y del perfil contra las 39 tablas. Lo que ya cuadra no aparece aquí. Las preguntas son lo que el frontend pide y el modelo no guarda, o lo que hoy está fijo en el código y debería salir de la base.

Corre `chat.py preguntas 022` y házselas a Alejandro en un cuestionario interactivo. Cada pregunta se entiende sola.

Q1 | Documento | El asistente, Clientes y Usuarios piden el tipo de documento (cédula, cédula de extranjería, NIT, pasaporte, PPT) y validan el número según el tipo. La v4.6 solo guarda usuarios.documento. ¿Se guarda el tipo?
  * Agregar tipo_documento | Enum tipo_documento (CC, CE, NIT, PA, PPT) en usuarios, y unique (tipo_documento, documento): el mismo número puede existir en dos tipos.
  - Solo el número | El frontend quita el selector y asume cédula; los extranjeros no podrían registrarse bien.

Q2 | Municipio | La dirección de entrega se escribe con municipio (Medellín, Bello, Envigado, Itagüí, Sabaneta) y se muestra como "Laureles, Medellín". direcciones_cliente tiene dirección, barrio, notas, latitud, longitud y zona, pero no municipio. ¿Dónde queda?
  * Agregar municipio | direcciones_cliente.municipio varchar not null. La zona sigue saliendo del polígono con latitud y longitud.
  - Heredarlo de la zona | zonas_cobertura.municipio, y la dirección lo toma de su zona. Falla si una zona cruza dos municipios o se vuelve a trazar.

Q3 | Duración | En Servicios se registra la duración del plan en días hábiles (5, 10, 20). Con ella se calculan la fecha de vencimiento, el valor por almuerzo y los descuentos por festivos. La HU "Registrar duración" existe, pero servicios no tiene columna. ¿Cómo queda?
  * Agregar dias_habiles | servicios.dias_habiles integer not null, editable en el panel.
  - Fija por tipo de plan | Semanal 5, quincenal 10, mensual 20, en el backend; el panel no la edita.

Q4 | Beneficios | La web y el asistente muestran "Qué incluye" de cada plan (hasta 6 líneas), y hoy se editan en Servicios. La v4.6 solo tiene servicios.descripcion (el resumen corto). ¿Dónde se guardan?
  * Agregar beneficios | servicios.beneficios text, una línea por beneficio. Así la web no tiene textos de planes fijos en el código.
  - Solo la descripción | Se muestra solo el resumen; los beneficios quedan fijos en la web.

Q5 | Rendimiento | La ficha técnica tiene dos números: para cuántas porciones son las cantidades de la receta (rendimiento) y cuántas porciones caben en una tanda (la olla). La v4.6 solo tiene porciones_por_tanda, y la nota de ficha_tecnica_detalle dice "por porción/receta". ¿Cómo queda?
  * Agregar rendimiento | fichas_tecnicas.rendimiento_porciones integer not null. cantidad_requerida es para ese rendimiento, y porciones_por_tanda es el tope de la olla.
  - Todo por porción | cantidad_requerida es para 1 porción y no hay rendimiento; la cocina escribe la receta dividida.

Q6 | Acciones | El panel usa 6 acciones por módulo: ver, crear, editar, cambiar estado, eliminar y exportar. accion_permiso solo tiene las 4 primeras. Hoy "Eliminar" borra el registro de la base. ¿Cómo queda?
  * Las 4 del modelo | Exportar va con ver. No se borra nada: se inactiva con cambiar_estado, así las compras, rutas y pagos antiguos no pierden sus referencias. El panel quita "Eliminar".
  - Ampliar el enum | accion_permiso + eliminar y exportar; el borrado físico se permite donde no haya referencias.

Q7 | Zonas | Las zonas tienen un nombre interno ("Norte 1"), un nombre para clientes ("Robledo y Castilla"), un municipio y una lista de barrios. Hoy todo eso está fijo en el código; zonas_cobertura solo tiene nombre, polígono, domiciliario y estado. ¿Qué se guarda?
  * Nombre público y municipio | zonas_cobertura + nombre_publico y municipio. La zona de una dirección sale del polígono; los barrios salen del código y se sugieren con el buscador del mapa.
  - Tabla de barrios | Además, zona_barrios (zona, barrio), editable en el panel, para reconocer la zona por el barrio escrito.
  - Dejarlo en el código | Solo el polígono va en la base; nombres y barrios siguen fijos en el frontend.

Q8 | Pago y hora | Los datos de la transferencia (banco, tipo de cuenta, número, titular) y el horario de entrega (8:00 a. m. a 12:00 m.) están fijos en el código. El modelo tiene clientes.franja_horaria, pero la empresa entrega en un solo horario. ¿Cómo queda?
  * Claves de configuración | banco_pago, tipo_cuenta_pago, numero_cuenta_pago, titular_cuenta_pago y horario_entrega en configuraciones_sistema (valores_negocio), editables en Configuración. Sale clientes.franja_horaria.
  - Franja por cliente | Los datos bancarios van a configuración, y se mantiene clientes.franja_horaria para que cada cliente elija su franja.

Q9 | Notas | El perfil y Clientes tienen "Notas para la cocina" (texto libre, máximo 300). clientes no tiene notas, y direcciones_cliente.notas es para apartamento, torre o piso. ¿Se guardan?
  * Se quitan | Lo de la cocina queda en las alergias (G1) y lo de la entrega en las notas de la dirección. Sigue la regla de la v4.2: sin textos libres que nadie lee.
  - Agregar notas | clientes.notas text (máximo 300), visible en la orden de producción.

Q10 | Sin columna | Estos campos del frontend no tienen columna: la etiqueta de la dirección ("Principal") y el sector, el contacto del proveedor, el proveedor principal del insumo, "Se empaca en" de la categoría de producto, el estado de la ficha técnica, la descripción y la marca "del sistema" del rol, y el motivo al cancelar una suscripción. ¿Qué se hace con ellos?
  * Quitarlos del frontend | Ningún paso posterior los usa. "Del sistema" se calcula (son los 4 roles de la semilla). La cancelación sale solo del pago vencido, y ese es su motivo.
  - Agregar el contacto | Lo mismo, pero proveedores gana contacto varchar: la persona con quien se habla en el proveedor.

## Qué hará el frontend cuando cerremos G3 (con las recomendadas)

- Roles, permisos, planes, zonas, datos de pago y horario se leen de la API. Los archivos fijos (`roles.js`, `business.js`) quedan solo como respaldo sin conexión.
- Quito del frontend los campos de Q9 y Q10, y la acción "Eliminar" (Q6).
