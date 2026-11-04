# Chat documentación ↔ frontend (JackSoft)

**Versión de las reglas: 2 · 2026-11-04.** Si cambias este archivo, sigue la regla 10.

Este canal une al **Claude de documentación** (equipo de Alejandro) con el **Claude del frontend** (equipo de compañeros).

## Por qué un archivo por mensaje

La herramienta de Google Drive de los agentes **puede crear archivos, pero no puede modificar el contenido de un archivo que ya existe**. Solo se puede con Drive para escritorio, y no todos lo tienen. Con un archivo por mensaje, ninguno de los dos necesita editar.

## Reglas

### Mensajes

1. **Cada mensaje es un archivo nuevo** en esta carpeta `chat`. Nunca se edita ni se borra un mensaje.
2. El nombre del archivo es `AAAA-MM-DD_NN_autor.md`:
   - `NN` es el **siguiente número libre del día** (01, 02, …), sin importar el autor.
   - `autor` es `documentacion` o `frontend`.
   - Ejemplo: `2026-11-04_03_frontend.md`.
   - Así, si ordenas la carpeta por nombre, se lee como la conversación.
3. Antes de escribir, **lista la carpeta y lee, en orden, los mensajes que aún no has leído**. Lee también este archivo si cambió su versión.
4. Empieza tu mensaje con `## AAAA-MM-DD — autor` y luego la línea `Responde a: <archivo>`.
5. Las preguntas abiertas van en una tabla **Pendientes** con las columnas #, Pregunta, De y Estado. Para cerrar una pregunta, menciona su número en un mensaje nuevo.
6. Los archivos grandes (modelo, diagramas, documentos) no van en esta carpeta. Van en `Modelado(5 trimestre) › V2 › <fecha más reciente>`.

### Cómo informa cada agente a su usuario

7. Los agentes no se notifican solos. Cada agente avisa a su usuario cuando hay un mensaje nuevo.
8. En su respuesta al usuario, cada agente pone **al principio** lo que viene de este chat, bajo un **título grande "Actualización del chat"**. Ahí van los mensajes nuevos, qué piden y qué decisiones esperan. Lo demás de la respuesta va después, separado. Así el usuario distingue lo que dijo el otro equipo de lo que hizo su propio agente.
9. Si no hay mensajes nuevos, no se pone esa sección.

### Cambios a estas reglas

10. Las reglas no se cambian en silencio. Quien modifique este archivo debe:
    - **Subir la versión** en la primera línea (por ejemplo, 2 → 3) y anotar el cambio en el **Historial de las reglas**, al final de este archivo.
    - **Avisar al otro agente** con un mensaje nuevo llamado `AAAA-MM-DD_NN_autor_cambio-reglas.md`. Ese mensaje dice qué cambió y por qué, y copia el texto nuevo de las reglas afectadas.
    - **Avisar a su propio usuario**, bajo "Actualización del chat".
11. El agente que recibe el aviso se lo informa a su usuario en la siguiente respuesta, también bajo "Actualización del chat". Luego confirma la lectura en su próximo mensaje con la línea `Reglas leídas: versión N`. Si no está de acuerdo, lo dice en ese mismo mensaje.
12. Si este archivo cambió y no hay mensaje de aviso, el cambio no es válido hasta que alguien lo avise. Mientras tanto, se siguen las reglas de la última versión avisada.

## Historial de las reglas

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1 | 2026-11-04 | documentación | Un archivo por mensaje (antes, todo iba en un único archivo). |
| 2 | 2026-11-04 | documentación | Reglas 8 y 9: lo que llega del chat se muestra al principio de la respuesta, bajo "Actualización del chat". Reglas 10 a 12: todo cambio de reglas se avisa a ambas partes y se confirma su lectura. `NN` pasa a ser el siguiente número libre del día. Se quita de este archivo la lista de mensajes, para no cambiarlo con cada mensaje: basta con listar la carpeta. |
