# Grill G1, ronda G1-2 (de Claude Alejo a Claude Omar)

Claude Alejo · 2026-11-11 · `06_Modelo_BD v11`. Surgen de las respuestas R1 a R7. Responde con `chat.py preguntas 016` en un cuestionario interactivo con Omar.

Q1 | Vegetariano | Con R1, la lista del cliente queda en carne, cerdo, mariscos, gluten, lácteos, frutos secos y huevo, y "vegetariano" deja de existir. Un cliente que hoy tiene marcado "vegetariano", ¿cómo queda al migrarlo?
  * Carne, cerdo y mariscos | Se le marcan las tres, porque un vegetariano no come ninguna. El cliente puede corregirlo en su perfil.
  - Solo carne | Se le marca solo "carne", y cerdo y mariscos quedan a su criterio.
  - Preguntarle | No se migra: se le pide que vuelva a elegir sus alergias en su próximo ingreso.

Q2 | Bajo en sal | Con R1 sale "bajo en sal". Los clientes que hoy lo tienen marcado pierden ese dato. ¿Qué se hace con ellos?
  * Avisar por WhatsApp | Se les avisa que la cocina ya no lo maneja como opción del sistema y se quita la marca.
  - Pasarlo a las notas | Se copia "bajo en sal" a las notas de su dirección para que el domiciliario y la cocina lo vean.

Q3 | Orden altern. | Con R3, el cliente recibe la primera alternativa del plato que no tenga ninguna de sus alergias. El modelo no tiene un campo de orden: "la primera" sería la que se creó primero en el menú. ¿Te sirve así?
  * Por orden de creación | Sin campo nuevo. En el editor del menú, las alternativas se muestran en el orden en que se crearon.
  - Agregar campo orden | menu_items vuelve a tener 'orden' para poder reordenar las alternativas.

Q4 | Ajuste | Con R7, editar la existencia a mano crea un movimiento de ajuste. ¿Cómo lo registra el frontend?
  * Por la diferencia | Un solo movimiento: entrada si la existencia sube, salida si baja, por la diferencia.
  - Pedir la cantidad | El usuario escribe cuánto entra o sale, en lugar de editar el total.
