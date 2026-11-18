# Grill G3, ronda G3-1 (complemento): ingreso con Google y Apple

Claude Omar · 2026-11-15 · base `06_Modelo_BD v12` (DBML v4.6). Sigue a `adjuntos/022_grill-G3.md` (Q1 a Q10).

## El flujo que propone Omar (web y app iguales)

1. Una sola pantalla de acceso, para "Ingresar" y para el paso de cuenta del asistente, con tres opciones:
   - Continuar con Google;
   - Continuar con Apple;
   - Continuar con correo: primero el correo; si la cuenta existe pide la contraseña, y si no, la crea.
2. El asistente queda así: Tu plan → Tu cuenta → Tus datos → Entrega → Pago.
   - El paso de cuenta y el de datos son un mismo paso con dos vistas, así que siguen siendo 4 pasos.
   - Con Google o Apple, el nombre y el correo llegan verificados y no se crea contraseña. Solo se piden documento, celular y alergias.
3. La cuenta se crea en el paso 2 (antes que el pago). El borrador del asistente ya no guarda la contraseña en el navegador.
4. Si alguien entra con Google o Apple y no tiene cuenta, se crea y sigue al asistente. Ya no hay ACCOUNT_NOT_FOUND.
5. El personal (administrador, cocina, domiciliario) sigue con correo y contraseña creados en el panel.

Técnica:
- OpenID Connect (Authorization Code + PKCE en la web).
- El backend verifica el id_token: firma, iss, aud, exp y nonce.
- La cuenta se reconoce por el `sub` del proveedor, no por el correo: Apple puede dar un correo de relevo y solo manda el nombre la primera vez.

## Preguntas

Q11 | Social | Para entrar con Google o Apple hay que guardar qué proveedor y qué identificador (`sub`) tiene cada cuenta, y quien entra así no tiene contraseña. ¿Cómo queda en el modelo?
  * Tabla identidades | Nueva tabla identidades_externas (usuario_id, proveedor enum proveedor_identidad: google | apple, sub, correo, fecha_vinculo), unique (proveedor, sub). usuarios.password pasa a ser opcional, y accesos gana metodo (correo | google | apple) para la bitácora.
  - Columnas en usuarios | usuarios.google_sub y usuarios.apple_sub (opcionales y únicos), password opcional. Agregar otro proveedor obliga a cambiar la tabla.

Q12 | Vincular | Una persona con cuenta de correo (creada en el panel o en el asistente) entra un día con Google usando ese mismo correo. ¿Qué pasa?
  * Vincular si verificado | Si Google o Apple confirman el correo (email_verified), se vincula a la cuenta existente. Si no, se le pide su contraseña antes de vincular.
  - Cuenta aparte | Se crea otra cuenta. Quedan dos clientes con el mismo correo, y el correo deja de ser único.

Q13 | Equipo | ¿El personal (administrador, cocina, domiciliario) también puede entrar con Google o Apple?
  * Solo correo | El personal entra con el correo y la contraseña que crea el administrador en Usuarios. Así el panel controla quién entra.
  - También Google | El personal puede vincular su Google a la cuenta que le creó el administrador.
