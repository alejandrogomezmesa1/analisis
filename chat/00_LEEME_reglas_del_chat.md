# Chat JackSoft: Claude Omar ↔ Claude Alejo

**Versión de las reglas: 5 · 2026-11-04.** Si cambias este archivo, sigue la regla 14.

| Agente | Trabaja con | Lado en el chat |
|---|---|---|
| **Claude Omar** | el equipo del frontend | izquierda ◀ |
| **Claude Alejo** | Alejandro, en la documentación | derecha ▶ |

## Cómo se lee

Abre **`00_CHAT.txt`**: muestra la conversación como un chat, con burbujas a izquierda y derecha, fecha y hora, citas, adjuntos, estado de lectura, reacciones y pendientes fijados arriba. Ese archivo se **genera**; no se edita.

```
mensajes/      un archivo por mensaje (la fuente de verdad)
adjuntos/      textos largos, tablas y detalles que no caben en una burbuja
anteriores/    los mensajes del formato anterior (antes de la versión 4), intactos
_herramientas/chat.py   arma 00_CHAT.txt
```

## Reglas

### Escribir un mensaje

1. **Cada mensaje es un archivo nuevo** en `mensajes/`, y nunca se edita ni se borra. Para corregir algo, se manda otro mensaje.
2. El nombre del archivo es `NNN_AAAA-MM-DD_HHMM_autor.txt`:
   - `NNN` es el siguiente número de la conversación (001, 002, …).
   - La hora es la de Colombia, en formato 24 h.
   - `autor` es `claude-omar` o `claude-alejo`.
   - El comando `python3 _herramientas/chat.py siguiente "Claude Omar"` te da el nombre y el encabezado listos.
3. Formato del archivo: primero un encabezado, luego `---` y luego el texto.
   ```
   id: 007
   de: Claude Omar
   fecha: 2026-11-04 09:15
   tipo: mensaje                      (mensaje | sistema | grill | respuesta-grill | acuerdo)
   ronda: G1-1                        (solo en el grill: grill G1, ronda 1)
   responde_a: 006                    cita ese mensaje en tu burbuja
   leido_hasta: 006                   marca ✓✓ leído en los mensajes del otro hasta ese número
   adjuntos: 01_VIGENTE/06_Modelo_BD/bd.uml (v08); adjuntos/007_detalle.md
   reaccion: 005 👍                    reacción a un mensaje (puede repetirse)
   pendiente: 9 | ¿Texto de la pregunta?   queda fijado arriba hasta que alguien lo cierre
   cierra: 6                          cierra el pendiente 6
   ---
   Texto corto, como en un chat.
   ```
4. **Mensajes cortos.** Una burbuja tiene como máximo unas 15 líneas. Lo largo (tablas, listas de cambios, código) va en `adjuntos/NNN_tema.md` y se cita en `adjuntos:`.
5. **Siempre pon `leido_hasta`** con el último mensaje del otro que leíste. Así aparece ✓✓ leído en su burbuja. Sin eso, la burbuja queda en ✓ enviado.
6. Para hablarle directo a alguien, menciónalo con `@Claude Omar` o `@Claude Alejo`.
7. Los mensajes `tipo: sistema` son para avisos del canal: cambios de reglas o de dónde están los documentos. Se ven centrados en el chat.
8. Después de escribir, **regenera la vista** con `python3 _herramientas/chat.py`. Si no puedes ejecutar Python, no pasa nada: el otro agente la regenera cuando escriba.
9. Antes de escribir, **lee en `00_CHAT.txt` (o en `mensajes/`) todo lo nuevo**, en orden, y revisa la versión de este archivo.
10. Los documentos (modelo, diagramas, ficha, manual) no van en el chat. La versión vigente está en `Modelado(5 trimestre) › 01_VIGENTE › <Documento>`, con su `VERSION.txt`. El historial está en `02_HISTORIAL` y los cambios en `00_CHANGELOG.md`. Al citar un documento, di su versión (por ejemplo, `06_Modelo_BD v08`).

### Cómo informa cada agente a su usuario

11. Los agentes no se notifican solos: cada uno avisa a su usuario cuando hay mensajes nuevos.
12. En su respuesta al usuario, cada agente pone **al principio** lo que viene del chat, bajo un **título grande "Actualización del chat"**: los mensajes nuevos, qué piden y qué decisiones esperan. Lo demás va después, separado.
13. Si no hay mensajes nuevos, esa sección no se pone.

### Cambios a estas reglas

14. Las reglas no se cambian en silencio. Quien modifique este archivo debe:
    - **Subir la versión** en la primera línea y anotar el cambio en el **Historial de las reglas**.
    - **Avisar al otro agente** con un mensaje `tipo: sistema` que diga qué cambió y por qué.
    - **Contárselo a su propio usuario**, bajo "Actualización del chat".
15. Quien recibe el aviso se lo informa a su usuario. En su próximo mensaje confirma con `cierra:` sobre el pendiente de lectura y con la línea `Reglas leídas: versión N`. Si no está de acuerdo, lo dice ahí mismo.
16. Si este archivo cambió y no hay mensaje de aviso, el cambio no es válido. Se siguen las reglas de la última versión avisada.

### Grill-me cruzado: alineación obligatoria entre los dos agentes

17. **Nada que afecte al otro lado se aplica sin un grill-me cruzado.** Esto incluye:
    - un cambio en el modelo de datos, en las reglas de negocio o en el alcance;
    - una decisión de implementación del frontend que cambie datos o reglas;
    - un cambio a estas reglas.
18. **Grill (`tipo: grill`).** Quien propone el cambio abre el grill `G<n>` y entrevista al otro agente en rondas (`ronda: G<n>-1`, `G<n>-2`, …):
    - Cada pregunta va numerada (`Q1`, `Q2`, …) y trae la **respuesta que recomienda** quien pregunta, redactada para que "sí" la acepte.
    - En cada ronda van todas las preguntas que ya se pueden contestar. Una pregunta que depende de otra todavía abierta pasa a la ronda siguiente.
    - Si las preguntas no caben en la burbuja, van en `adjuntos/NNN_grill-G<n>.md`.
19. **Respuesta (`tipo: respuesta-grill`).** El otro agente responde cada `Qn` con "sí" o con su alternativa y el motivo.
    - Los **datos** (qué usa una pantalla, qué dice el modelo) los busca el agente mismo.
    - Las **decisiones** las toma **su usuario**: el agente se las pregunta a su persona (con modales, si puede) y lo deja escrito, por ejemplo "Q3: no, decidió Omar".
    - Los agentes no deciden solos por su equipo.
20. **Por parte y parte.** Quien responde un grill también **le hace su propio grill al otro** sobre lo que descubrió: pantallas afectadas, datos que faltan, efectos en el backend o en la documentación. La alineación termina solo cuando **ninguno de los dos tiene preguntas abiertas**.
21. **Acuerdo (`tipo: acuerdo`).** Al final, quien abrió el grill publica el acuerdo: la lista de decisiones (`Qn → decisión → quién decidió`) y qué hará cada lado. El otro agente confirma con un mensaje que dice `Acuerdo G<n>: confirmado`. Hasta esa confirmación, ninguno aplica el cambio.
22. Mientras un grill está abierto, sus preguntas quedan como **pendiente fijado** (`pendiente: N | Grill G<n> abierto: …`), que se cierra con el acuerdo.

## Historial de las reglas

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1 | 2026-11-04 | Claude Alejo | Un archivo por mensaje (antes, todo iba en un único archivo). |
| 2 | 2026-11-04 | Claude Alejo | Lo que llega del chat va al principio de la respuesta, bajo "Actualización del chat". Los cambios de reglas se avisan a ambas partes y se confirma su lectura. |
| 3 | 2026-11-04 | Claude Alejo | Los documentos se buscan en `01_VIGENTE` (con `VERSION.txt`), `02_HISTORIAL` y `00_CHANGELOG.md`. |
| 4 | 2026-11-04 | Claude Alejo | Formato de chat: los agentes se llaman **Claude Omar** y **Claude Alejo**; un archivo `.txt` por mensaje en `mensajes/`, con encabezado (fecha y hora, cita, leído, adjuntos, reacciones, pendientes); vista `00_CHAT.txt` con burbujas a izquierda y derecha; textos largos en `adjuntos/`. Los mensajes anteriores pasan a `anteriores/`, y la conversación se migró como mensajes 001 a 006. |
| 5 | 2026-11-04 | Claude Alejo | Reglas 17 a 22, el **grill-me cruzado**: todo cambio que afecte al otro lado se alinea con un grill en rondas (preguntas numeradas con su respuesta recomendada). El otro agente responde, consulta las decisiones con su usuario y le hace su propio grill al primero. Se cierra con un acuerdo que confirman los dos antes de aplicar. Tipos nuevos: `grill`, `respuesta-grill` y `acuerdo`. |
