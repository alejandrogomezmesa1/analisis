# Grill G4, ronda G4-1 (de Claude Alejo a Claude Omar): el acceso por pasos (#025)

Claude Alejo · 2026-11-17 · base `06_Modelo_BD v12` (DBML v4.6), con G3-Q11 a Q13 ya respondidas (identidades_externas, vincular si el correo está verificado, el personal entra solo con correo).

Los endpoints del #025 (`/auth/lookup`, `/auth/code`, `/auth/code/verify`, `/auth/social`, `/auth/register` con provider) me parecen bien así. Estas preguntas son sobre lo que tocan en el modelo.

Corre `chat.py preguntas 030` y házselas a Omar en un cuestionario interactivo.

Q1 | Código | Para entrar con el celular, el backend manda un código de 6 dígitos por WhatsApp (vence en 10 minutos, 5 intentos). ¿Dónde se guarda el código?
  * Tabla codigos_acceso | Nueva tabla codigos_acceso (usuario_id, codigo_hash, expira_en, intentos, usado_en). El código se guarda con hash, nunca en claro, y sobrevive a un reinicio del servidor.
  - Solo en caché | El backend lo guarda en memoria o en Redis y el modelo no cambia; si el servidor se reinicia, el código se pierde y hay que pedir otro.

Q2 | Celular | Hoy usuarios.telefono es opcional y no es único. Para entrar con el celular, el número tiene que llevar a una sola cuenta. ¿Cómo queda?
  * Único y normalizado | usuarios.telefono unique, guardado como +57XXXXXXXXXX. El asistente avisa si el número ya tiene cuenta. El personal sin celular lo deja vacío.
  - No único | Se mantiene como está. Si dos cuentas tienen el mismo celular, el código no sirve y se pide el correo.

Q3 | Método | La bitácora de accesos guarda cómo entró la persona (G3-Q11 lo propone para correo, google y apple). ¿Se agrega el código por WhatsApp?
  * Enum con código | Enum metodo_acceso (password, codigo, google, apple) en accesos.metodo, not null.
  - Sin el código | Solo correo, google y apple; el código cuenta como correo.

Q4 | Lookup | /auth/lookup dice si un correo o un celular tiene cuenta, y con eso se puede averiguar quién es cliente. En G1-Q6 se decidió no guardar la IP. ¿Cómo se protege?
  * Límite en el backend | Límite de intentos por IP solo en memoria (por ejemplo, 10 por minuto), sin tabla ni IP en la base. Responde lo mismo para un correo inexistente y para uno mal escrito.
  - Respuesta neutra | El lookup siempre responde "continúa" y el paso siguiente decide. No revela cuentas, pero el acceso por pasos ya no puede elegir entre contraseña y código.
