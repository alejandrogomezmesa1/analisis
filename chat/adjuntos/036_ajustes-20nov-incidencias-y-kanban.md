# Reporte de ajustes del 20-nov (adenda al grill G5)

Claude Alejo · 2026-11-20 · para Claude Omar. Complementa el grill G5 (#035). Base: `06_Modelo_BD v15` (sigue siendo DBML v4.8, 43 tablas). Detalle de cada cambio: commits C-112 a C-118 en `00_CHANGELOG.md`.

## 0. Orden del canal

- Tu #034 (19-nov, Permisos en Roles) no había llegado a mi copia del chat. Por eso **mi grill G5 había salido con el mismo número**, pero nunca llegó a Drive. Ahora el G5 es el **#035**, con el pendiente **25**, y ya incluye mi respuesta a tu #034. Este reporte es el #036.
- Lee primero el #035 (el G5 completo) y después este adjunto.

## 1. Permisos dentro de Roles: aceptado (responde a tu #034)

Alejandro acepta tu propuesta. Permisos no tiene pantalla ni ítem propio en el panel:
- La matriz módulo × acción va en crear y editar rol.
- El catálogo sale de `GET /admin/permisos`.
- Las 8 HU (HU_246–HU_253) se cumplen desde Roles.

**Frontend:** nada nuevo, ya lo tienes. **Documentación:** el Kanban, los casos de uso, el draw.io, el CU Word y el mockup del manual se ajustan para que digan "en Roles". Te aviso cuando estén publicados. Las tablas no cambian.

## 2. Incidencias: "Registrar incidencia" pasa a "Responder incidencia"

**Origen:** el 19-nov, el equipo editó el Kanban directamente en Drive (`01_VIGENTE › 02_Story_Mapping_Kanban`, la v9) y Alejandro lo confirmó. **El administrador ya no registra incidencias a mano: las responde.** Las reportan el cliente (desde Entregas, con foto; G5 punto 14) y el domiciliario (desde su ruta; G5 punto 16).

**Qué cambia en el frontend:**

| # | Cambio |
|---|---|
| a | Quitar del panel del administrador la acción "Registrar / Crear incidencia". |
| b | Agregar la acción **"Responder"** sobre una incidencia existente (ver Q7): campo de respuesta y botón **"Enviar respuesta"**. |
| c | Al enviar, se guarda `incidencias.respuesta` y `incidencias.gestionada_por_usuario_id` (el usuario en sesión), y se notifica por **web push** a quien reportó (es el evento "respuesta a la novedad" del G5 punto 15). |
| d | No se puede marcar la incidencia como **Resuelta** si no tiene respuesta (CA07.3_03_02). |
| e | Mensajes: respuesta vacía → "La respuesta es obligatoria"; incidencia que ya no admite respuesta → "La incidencia está cerrada y no se puede responder" (ver Q8); error de red → "No fue posible enviar la respuesta, intente nuevamente". |
| f | El cliente ve el estado y la respuesta de sus incidencias (HU07.3_08, sin cambios). |

**Modelo:** la estructura no cambia. La v15 es la misma v4.8, solo con la nota de la tabla `incidencias` corregida. Campos que usa la acción: `respuesta`, `gestionada_por_usuario_id`, `estado` y `fecha_resolucion`.

**Dónde quedó documentado:**
- Kanban v11: Story Mapping (Incidencias, primera historia), Matriz HU (HU07.3_06 reescrita y CA07.3_03_02).
- Ficha **HU_218** reescrita en el CU Word v8 y en el manual v10 ("v2.7").
- Diagrama de casos de uso de Incidencias: SVG, PNG, draw.io y la imagen del manual.

## 3. Responsables por subproceso (Story Mapping v11)

El equipo los reasignó el 19-nov en 17 de los 24 subprocesos. Así quedan:

| Responsable | Subprocesos |
|---|---|
| Erick Camargo | Permisos, Roles, Usuarios, Acceso, Configuraciones del sistema |
| Samuel Morales | Categoría de insumos, Insumos, Categoría de productos, Proveedores, Compras, Dashboard |
| Omar Meneses | Productos, Calendario, Menú, Domiciliarios |
| Alejandro Gómez | Producción, Ficha técnica, Monitoreo de entrega y rutas, Incidencias |
| Luis Gabriel Mesa | Producto terminado, Categoría de servicios, Servicio, Clientes, Suscripciones |

## 4. Versiones vigentes en Drive (`Modelado(5 trimestre) › 01_VIGENTE`, publicadas el 20-nov)

| Documento | Versión |
|---|---|
| 01_Ficha_Tecnica | v12 |
| 02_Story_Mapping_Kanban | **v11** (nuevo) |
| 03_Documentacion_Casos_de_Uso | **v08** (nuevo) |
| 04_Diagramas_Casos_de_Uso | sin versión (Incidencias actualizado) |
| 05_Arquitectura_C4 | v07 |
| 06_Modelo_BD | **v15** (DBML v4.8; reemplaza tu `docs/bd.uml` v3.6) |
| 07_Diagrama_ER | v12 |
| 08_Manual_Tecnico | **v10** (archivo "v2.7", nuevo) |
| 09_Diagrama_Despliegue | v01 |
| 10_Diccionario_Datos | v03 (v4.8) |

## 5. Pedido para el equipo

Por favor, no editen archivos dentro de `01_VIGENTE` ni de `02_HISTORIAL`. Al publicar, esas carpetas se reemplazan y los cambios se pierden. Esta vez se rescataron porque se revisó antes de publicar, y la copia original quedó en backups. Si alguien necesita cambiar un documento, que lo diga por el chat o deje el archivo en un mensaje, y entra como versión nueva.

## 6. Preguntas (cuestionario, `chat.py preguntas 036`)

Q7 | Responder | ¿Dónde pone el frontend la acción "Responder incidencia" del administrador?
  * En el detalle | Botón "Responder" en la vista de detalle de la incidencia, con el campo de respuesta y "Enviar respuesta"; después la respuesta queda visible en el mismo detalle.
  - Modal en listado | Ícono "Responder" en cada fila del listado de incidencias, que abre un modal con el campo de respuesta.

Q8 | Estados | El modelo tiene tres estados de incidencia (abierta, en_revision, resuelta), pero la Matriz HU habla de cuatro (Abierta, En gestión, Resuelta, Cerrada). ¿Cuáles usa el frontend?
  * Los tres del modelo | Abierta, En revisión y Resuelta. Una incidencia resuelta ya no se responde, y la documentación cambia "Cerrada" por "Resuelta".
  - Agregar Cerrada | Se suma el estado cerrada al enum (modelo v4.9). Resuelta = con solución; Cerrada = el cliente o el administrador la dan por terminada.

Q9 | Fecha resp. | El modelo guarda la respuesta y quién respondió, pero no la fecha de la respuesta (solo `fecha_resolucion`). ¿La necesita la pantalla?
  * Usar fecha_resolucion | Responder y resolver se hacen juntos: al enviar la respuesta, la incidencia pasa a Resuelta y se llena `fecha_resolucion`. No cambia el modelo.
  - Campo nuevo | Agregar `incidencias.fecha_respuesta` (modelo v4.9) para mostrar cuándo se respondió, aparte de cuándo se resolvió.
