# Grill G1, ronda G1-1: modelos v4.3 a v4.5 frente al frontend

Claude Omar · 2026-11-07 · `06_Modelo_BD v11`. Ya apliqué A a H (commit `d1056e1`). Estas preguntas son lo que falta para aplicar el punto I y los cambios del v4.3 sin romper pantallas. Cada una se entiende sola.

Q1 | Alergias | Hoy el cliente marca 6 restricciones: sin gluten, sin lácteos, sin mariscos, sin cerdo, vegetariano y bajo en sal. El v4.3 las cambia por 5 alergias fijas (carne, cerdo, mariscos, gluten, lácteos). ¿Cómo queda la lista que ve el cliente?
  * Las 5 del modelo | Carne (sirve para quien es vegetariano), cerdo, mariscos, gluten y lácteos. "Bajo en sal" sale: no excluye ningún producto y la cocina lo hacía aparte.
  - 5 más "bajo en sal" | Se agrega `bajo_en_sal` al enum `componente_alimento`, aunque ningún producto lo "contenga".
  - Volver a restricciones | Se mantienen las 6 restricciones del frontend y el modelo las traduce a componentes.

Q2 | Otras alerg. | El v4.3 quita el texto libre de alergias. Una alergia que no está en la lista (maní, nueces, huevo) ya no se puede registrar, y el PO pidió pedirlas al registrarse por la seguridad de la cocina. ¿Qué hacemos?
  * Ampliar la lista | Se agregan `frutos_secos` y `huevo` al enum (y se marcan en los productos). Lo demás se coordina por WhatsApp antes del primer almuerzo, como dicen los términos.
  - Solo la lista | Se quedan las 5. Cualquier otra alergia se avisa por WhatsApp.
  - Volver al texto | Se mantiene `alergias_alimentarias` como texto libre además de la lista.

Q3 | Varias alerg. | Con una alternativa por alergia (punto I), el cliente con dos alergias, por ejemplo gluten y lácteos, puede no poder comer la alternativa de una de ellas. ¿Qué recibe?
  * La primera que sirva | De las alternativas del plato, la primera que no tenga ninguna de sus alergias. Si ninguna sirve, queda "sin alternativa" y la orden lo avisa, como hoy.
  - La de su 1.ª alergia | Siempre la de su primera alergia, aunque tenga la otra. La cocina la ajusta a mano.
  - Una por combinación | Se define una alternativa por cada combinación de alergias.

Q4 | Calificación | El v4.3 quita la calificación del almuerzo. Hoy el cliente califica de 1 a 5 desde su cuenta, y el dashboard muestra el promedio. ¿Se quita del frontend?
  * Sí, se quita | Sale de la cuenta, del panel y del dashboard.
  - Se mantiene | Vuelven `calificacion` y `comentario_calificacion` al modelo.

Q5 | Bloqueo | El bloqueo de acceso usa las claves nuevas `intentos_maximos_acceso` (3) y `minutos_bloqueo_acceso` (15). Hoy el frontend bloquea con 5 intentos y 5 minutos, fijos. ¿Se editan en el panel?
  * En Configuración | Dos campos en Panel › Configuración, con esos valores por defecto.
  - Solo en el backend | El frontend solo muestra el mensaje de bloqueo.

Q6 | Acceso | Sale `accesos.detalle`. Hoy la bitácora de Acceso muestra el motivo de cada fallo: contraseña incorrecta, correo desconocido o bloqueado por intentos. ¿Se quita esa columna?
  * Sí, se quita | Queda la fecha, el correo, la IP y el resultado (exitoso o fallido).
  - Se mantiene | Vuelve `detalle` al modelo.

Q7 | Existencia | Sin motivo en `movimientos_inventario`, un movimiento sin compra ni orden de producción es un ajuste o una merma. Hoy en Insumos se edita la existencia a mano. ¿Se mantiene?
  * Sí, como ajuste | Cambiar la existencia a mano registra un movimiento de ajuste, sin motivo.
  - No | La existencia solo cambia con compras recibidas y producción.
