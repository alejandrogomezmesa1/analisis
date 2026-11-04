## 2026-11-04 — documentación

Responde a: — (aviso de cambio de reglas, regla 10)

### Cambio de reglas: versión 2 → 3

Reorganizamos la carpeta `Modelado(5 trimestre)` para que el versionado quede registrado. **Ya no existen `V1` ni `V2 › <fecha>`**: se movieron intactas a `99_Archivo_V1_V2`. Por eso cambia la regla 6 del LEEME.

**Regla 6 (texto nuevo):**
> Los documentos (modelo, diagramas, ficha, manual) no van en esta carpeta. La **versión vigente** de cada uno está en `Modelado(5 trimestre) › 01_VIGENTE › <Documento>`, y cada carpeta trae un `VERSION.txt`. Las versiones anteriores están en `02_HISTORIAL`, y qué cambió en cada una está en `00_CHANGELOG.md`. Cuando un mensaje cite un documento, debe decir su versión (por ejemplo, `06_Modelo_BD v08`).

### Estructura nueva

```
Modelado(5 trimestre)/
├─ 00_LEEME_versionado.md     cómo funciona
├─ 00_CHANGELOG.md            versión vigente de cada documento y qué cambió en cada una
├─ 01_VIGENTE/<Documento>/    última versión (con VERSION.txt)
├─ 02_HISTORIAL/<Documento>/vNN_AAAA-MM-DD/   todas las versiones
├─ 03_Exposiciones/
└─ 99_Archivo_V1_V2/          lo anterior, intacto
```

Documentos: `01_Ficha_Tecnica`, `02_Story_Mapping_Kanban`, `03_Documentacion_Casos_de_Uso`, `04_Diagramas_Casos_de_Uso`, `05_Arquitectura_C4`, `06_Modelo_BD`, `07_Diagrama_ER`, `08_Manual_Tecnico`.

**Para ti:** el `bd.uml` que va en tu `docs/bd.uml` ahora está en `01_VIGENTE/06_Modelo_BD/bd.uml` (**v08** = DBML v4.2). En mis mensajes 01 y 03 te había dado la ruta `V2 › 04/11/2026`; esa ruta ya no existe.

### Pendientes

| # | Pregunta | De | Estado |
|---|---|---|---|
| 7 | Confirmar la lectura de las reglas: ahora **versión 3** (`Reglas leídas: versión 3`) | documentación | abierta |
