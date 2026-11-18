# Acuerdo G1: modelos v4.3 a v4.5 frente al frontend

Claude Omar · 2026-11-14 · base `06_Modelo_BD v12` (DBML v4.6). Rondas G1-1 (#014 → #015) y G1-2 (#016 → #019).

## Decisiones

| # | Tema | Decisión | Decidió |
|---|---|---|---|
| G1-1 Q1 | Alergias | Lista de componentes del modelo; "vegetariano" y "bajo en sal" dejan de ser opciones | Alejandro |
| G1-1 Q2 | Otras alergias | Se amplía `componente_alimento` con `frutos_secos` y `huevo`; lo demás se coordina por WhatsApp | Alejandro |
| G1-1 Q3 | Varias alergias | La primera alternativa del plato que no tenga ninguna de sus alergias; si no hay, "sin alternativa" y la orden lo avisa | Alejandro |
| G1-1 Q4 | Calificación | Se quita (cuenta, panel y dashboard) | Alejandro |
| G1-1 Q5 | Bloqueo | Solo en el backend (`intentos_maximos_acceso`, `minutos_bloqueo_acceso`); el frontend solo muestra el mensaje | Alejandro |
| G1-1 Q6 | Acceso | Sale `accesos.detalle`; la IP tampoco queda | Alejandro |
| G1-1 Q7 | Existencia | Editar la existencia a mano registra un movimiento de ajuste | Alejandro |
| G1-2 Q1 | Vegetariano | Al migrar se le marcan carne, cerdo y mariscos; el cliente lo corrige en su perfil | Omar (delegada) |
| G1-2 Q2 | Bajo en sal | Se quita la marca y se avisa por WhatsApp | Omar (delegada) |
| G1-2 Q3 | Orden de alternativas | Por orden de creación, sin campo nuevo | Omar (delegada) |
| G1-2 Q4 | Ajuste | Un solo movimiento por la diferencia: entrada si sube, salida si baja | Omar (delegada) |

## Qué hace cada lado

**Modelo (Claude Alejo), en la v4.7:**
- `componente_alimento` + `frutos_secos`, `huevo`.
- Nada más de G1: lo demás ya está en v4.3 a v4.6.

**Frontend (Claude Omar), al confirmarse:**
- Alergias en el asistente, el perfil y Clientes: casillas con las 7 del enum (sin texto libre, sin "vegetariano", sin "bajo en sal"). Migración de la base de prueba según Q1 y Q2.
- Tipo de incidencia `restriccion_no_atendida` → `alergia_no_atendida` (como en el modelo desde v4.3).
- Alternativa del menú: la primera que sirva, en orden de creación.
- Se quita la calificación de la cuenta, del panel y del dashboard.
- Bitácora de acceso: fecha, correo, usuario y resultado (sin motivo ni IP). Se quita el bloqueo local del frontend.
- Insumos: editar la existencia crea el movimiento de ajuste por la diferencia.
