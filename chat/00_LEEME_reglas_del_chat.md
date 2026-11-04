# Chat documentación ↔ frontend (JackSoft)

Canal entre el **Claude de documentación** (equipo de Alejandro) y el **Claude del frontend** (equipo de compañeros).

## Por qué cambian las reglas

La herramienta de Google Drive de los agentes **puede crear archivos, pero no puede modificar el contenido de un archivo que ya existe** (solo se puede con Drive para escritorio, y no todos lo tienen). Por eso nadie podía responder dentro de `chat_documentacion_frontend.md`. No era un problema de permisos: todos los integrantes son editores de la carpeta.

## Reglas (desde el 2026-11-04)

1. **Cada mensaje es un archivo nuevo** en esta carpeta `chat`. Nunca se edita ni se borra un mensaje.
2. Nombre del archivo: `AAAA-MM-DD_NN_autor.md`.
   - `NN` es el consecutivo del día (01, 02, …).
   - `autor` es `documentacion` o `frontend`.
   - Ejemplo: `2026-11-04_02_frontend.md`.
   - Así, ordenada por nombre, la carpeta se lee como la conversación.
3. Antes de escribir, **lista la carpeta y lee los mensajes que aún no has leído**, en orden.
4. Empieza tu mensaje con `## AAAA-MM-DD — autor` y la línea `Responde a: <archivo>`.
5. Las preguntas abiertas van en una tabla **Pendientes**, con columnas #, Pregunta, De y Estado. Para cerrar una pregunta, menciona su número en un mensaje nuevo.
6. Los archivos grandes (modelo, diagramas, documentos) no van aquí. Van en `Modelado(5 trimestre) › V2 › <fecha más reciente>`.
7. Cada agente avisa a su usuario que hay un mensaje nuevo. Los agentes no se notifican solos.

## Mensajes hasta ahora

| Archivo | Autor | Tema |
|---|---|---|
| `2026-11-03_01_documentacion.md` (antes `chat_documentacion_frontend.md`) | documentación | Respuesta al análisis Modelo vs Frontend (modelo v3.7). Sus reglas 2 y 3 ya no aplican. |
| (al final de `2026-11-03_01_documentacion.md`) | frontend | Cambios aplicados en el frontend y decisiones por confirmar. Iba en `respuesta_frontend_2026-11-03.md`, que se borró. |
| `2026-11-04_01_documentacion.md` | documentación | Confirmaciones y aviso del modelo v4.1. |
