# Respuestas de Omar a G5 (#035), #036 y G6 (#038)

Claude Omar · 2026-11-21 · Omar confirmó todas las opciones recomendadas; abajo va el porqué de cada una. Todavía no aplico nada en el frontend hasta el acuerdo de cada grill (regla 21).

## G5, ronda G5-1 (#035)

R1 | Archivo .ics | decidió Omar
- Además del Excel que ya tiene el calendario del panel (fecha, hábil, festivo, almuerzos y el plato de cada menú). El .ics sirve para Google Calendar, Outlook y el celular sin integraciones.

R2 | Ya, con mock | decidió Omar
- Con la app móvil en pausa, la web tiene que cubrir sus avisos. Service worker, permiso del navegador y registro en `dispositivos_push` desde ya; los envíos se simulan hasta que exista el backend.

R3 | Cada 15 s en ruta | decidió Omar
- Solo así el cliente ve el recorrido. Se envía mientras la ruta está en curso y la página abierta, con aviso si el navegador niega el permiso.

R4 | Filtro y aviso | decidió Omar
- Estado "En espera" en el filtro de Suscripciones, contador en el dashboard y el cupo libre de las próximas semanas al asignar. Sin pantalla nueva.

R5 | Paso del plan | decidió Omar
- La preferencia cambia el precio: va donde se ve el total y se recalcula al instante.

R6 | Aviso + Insumos | decidió Omar
- Un faltante se resuelve con una compra: debe verse en el insumo, con aviso al admin y su paso a resuelto.

## #036 (Incidencias)

R7 | En el detalle | decidió Omar
- Estándar del panel (20-nov): el detalle abre en el panel lateral y nunca se abre un modal sobre otro. La respuesta queda visible en el mismo detalle.

R8 | Los tres del modelo | decidió Omar
- Abierta, En revisión y Resuelta bastan; una resuelta ya no se responde. La documentación cambia "Cerrada" por "Resuelta" y no hace falta un modelo v4.9.

R9 | Usar fecha_resolucion | decidió Omar
- Responder y resolver van juntos: al enviar la respuesta, la incidencia pasa a Resuelta con su fecha. Sin campo nuevo.

## G6, ronda G6-1 (#038), las que seguían abiertas

R2 | Solo en Servicios | decidió Omar
- Los precios Gourmet son filas de `servicios` que edita el admin. En el panel de prueba son un 35 % más que los Estándar, pero la Ficha no fija cifras.

R4 | No se agrega | decidió Omar
- De acuerdo: sin Corporativo, `menu_propio` no distingue nada. En el frontend toda categoría activa tendrá su menú.

R6 | Sí, como propones | decidió Omar
- Es lo que ya funciona en el panel (commit aa9986e): `menus` con código ME-001, categoría, `semana` (lunes o null) y estado; `menus_diarios` por `dia_semana`; único (`categoria_servicio_id`, `semana`) publicado. Un menú se reutiliza duplicándolo.

R7 | Sí, se guarda | decidió Omar
- El plato del festivo sigue en el menú: solo no se produce ni se muestra esa semana. Al duplicar el menú para otra semana, vuelve.

R8 | Sí, mismas reglas | decidió Omar
- Una sola lógica para cualquier categoría: alternativas por alergia y proteína alterna (con su recargo) también en Gourmet.

R9 | Elige al cotizar | decidió Omar
- El asistente pregunta primero Estándar o Gourmet; "Mi menú" muestra el de su categoría y `GET /menu?categoria=` da el de cada una.

R10 | Sí, se acepta | decidió Omar
- La persona natural (p. ej. el de la plaza) y la empresa piden datos distintos: CC, CE, PPT o PA para la persona y NIT para la empresa.

R11 | 4 campos en proveedores | decidió Omar
- Un contacto por proveedor, obligatorio solo para empresas y vacío para persona natural. Reemplaza G3-Q10. Es lo que muestra el panel.

R12 | Todo junto | decidió Omar
- El dígito de verificación se calcula del número (algoritmo DIAN): guardarlo aparte duplica un dato derivable. `documento` guarda número y DV sin guion; la API lo valida.

## Lo que haré en el frontend cuando se cierren los acuerdos
- G6-R5 (decidió Alejandro): quito la categoría guardada en la suscripción de la API simulada; sale de `servicio_id → servicios.categoria_id`.
- Reemplazo `docs/bd.uml` (v3.6) por la v4.8.
- Los 16 cambios del G5 y los de Incidencias, por partes; aviso en el chat con cada entrega.
