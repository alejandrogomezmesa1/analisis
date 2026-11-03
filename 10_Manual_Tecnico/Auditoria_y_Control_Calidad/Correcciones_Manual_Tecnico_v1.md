---
title: "Correcciones Manual Técnico v1 — Seguimiento y cascada"
type: tracker
tags:
  - correcciones
  - manual-tecnico
  - casos-de-uso
  - cascada
related:
  - "[[00_INDICE_GENERAL]]"
  - "[[00_MOC_Manual_Tecnico]]"
  - "[[00_MOC_Casos_de_Uso]]"
  - "[[00_MOC_Reglas_Negocio]]"
  - "[[Contexto_e_Incongruencias_JackSoft]]"
---

# Correcciones Manual Técnico v1 — JackSoft

> **Fuente de verdad:** `Manual_Tecnico_v2.1_Jacksoft.docx` (ubicado en `10_Manual_Tecnico/Documentos_Word/v3_2026-09-25/`). Historial: v1 = con comentarios de la evaluadora · v2 (septiembre 25) = diagramas rehechos por el compañero · v2.1 = fichas corregidas (ver bitácora). Todo lo que se corrige termina ahí. Ver sección 9 para el estado de la v2. Las incongruencias **entre entregables** (Ficha, Kanban/Matriz HU, drawio, BD) están en [[Contexto_e_Incongruencias_JackSoft]].
> Este documento registra **qué se decidió, por qué y qué otros documentos hay que actualizar en cascada**. Antes de tocar cualquier documento del vault, revisar aquí la decisión vigente.

---

## 1. Comentarios recibidos

| ID | Autor | Ubicación en el manual | Comentario | Estado |
|---|---|---|---|---|
| C4 | Liliana Galeano (instructora) | Introducción | "Se construye en 7mo trimestre." | ⏸ Informativo — se deja el borrador actual |
| C9 | Evaluadora (isabel0540) | Diagrama **Suscripciones** | "Hay que evaluar este caso de uso, está pésimo, hay que considerar si son casos de uso o validaciones en el registro." | 🟡 v2: diagrama rehecho pero recortado de más; fichas sin cambiar |
| C10 | Evaluadora | Diagrama **Servicio** | "Los registros son parte de crear el servicio y no casos de uso independientes." | 🟡 v2: diagrama OK; fichas sin cambiar |
| C11 | Evaluadora | Diagrama **Ruta y Domiciliarios** | "Reasignar domiciliario no sería seleccionar domiciliario y uniría asignar y consultar." | 🟡 v2: se eliminaron las rutas por completo; fichas sin cambiar |
| C12 | Evaluadora | Diagrama **Ficha Técnica** | "Pilas, otro caso de uso: cosas que son del registro de la ficha técnica." | 🟡 v2: diagrama OK; fichas sin cambiar |
| C13 | Evaluadora | Diagrama **Clientes** | "Al igual que anteriores, hay casos de uso que son partes del registro." | 🟡 v2: diagrama OK; fichas sin cambiar |
| C14 | Evaluadora | Diagrama **Calendario** | "Al igual que en otros diagramas, colocan casos de uso que serían parte de parametrizar." | 🟡 v2: diagrama OK; fichas sin cambiar |
| C40 | Liliana Galeano | Anexos → Actas de reunión | "Firmadas por el cliente y aprendices." | 🔲 Pendiente (equipo) |
| C41 | Liliana Galeano | Anexos → Evidencias | "Videos, entrevistas, fotos, etc." | 🔲 Pendiente (equipo) |

Estados: 🔲 Pendiente · 🟡 En curso · ✅ Corregido en el manual · ⏸ Sin acción

---

## 2. Causa raíz

Los diagramas se generaron automáticamente desde la matriz de HU (`05_Casos_de_Uso/scripts/generar_svg_casos_uso.py` lee el CSV del Kanban): **cada HU se convirtió en un caso de uso** colgado de "Listar X" con `<<extends>>`. Muchas HU describen **campos de un formulario, validaciones, reglas de negocio o cálculos del sistema**, no objetivos del actor.

---

## 3. Criterio acordado (aplicar a TODOS los módulos)

**Prueba:** *¿El actor entraría al sistema solo para lograr esto y obtiene un resultado con valor?* Si no → no es caso de uso.

| Si la HU es… | Ejemplo | Destino |
|---|---|---|
| Objetivo del actor | Crear servicio, Renovar suscripción | **Caso de uso** (se mantiene) |
| Dato que se diligencia | Registrar teléfono, Registrar valor | **Campo** en el paso "Ingresa los datos…" de Crear/Editar |
| Validación | Validar cobertura, Validar capacidad | **Situación excepcional / validación** dentro del flujo |
| Regla o cálculo automático | Calcular vencimiento, Aplicar recargo, Cobro de cocas | **Regla de negocio (RN-xx)** referenciada desde el CU; respuesta del sistema en el flujo |
| Información que se consulta de un registro | Consultar historial de pagos del cliente | Parte de **Ver detalle** |
| Variante de estado | Gestionar estado Activa / Cancelada | Valores de **Cambiar estado** (transiciones en la RN) |
| Varios reportes del mismo módulo | Reporte por zona, por plan, activos | **Un solo "Generar reporte de X"** con filtros |

**Relaciones:**
- `<<include>>`: el caso base **siempre** ejecuta el incluido (flecha base → incluido). Solo si se reutiliza en varios CU.
- `<<extend>>`: comportamiento **opcional** (flecha extensión → base).
- Se elimina "Crear X `<<include>>` Listar X" (crear no ejecuta el listado). "Filtrar" pasa a `<<extend>>` de Listar.

---

## 4. Decisiones por módulo (comentados)

Leyenda de destino: **CU** = se mantiene · **→ HU_xxx (campo)** · **→ HU_xxx (detalle)** · **→ RN-xx** · **→ validación en HU_xxx** · **→ fusionada en HU_xxx**

### 4.1 Servicio (C10)

| HU | Nombre actual | Destino |
|---|---|---|
| HU_124 | Crear servicio | **CU** |
| HU_125 | Listar servicios | **CU** |
| HU_126 | Ver detalle del servicio | **CU** (extend de Listar) |
| HU_127 | Editar servicio | **CU** (extend de Listar) |
| HU_128 | Cambiar el estado del servicio | **CU** (extend de Listar) |
| HU_129 | Registrar nombre del plan | → HU_124 / HU_127 (campo) |
| HU_130 | Registrar tipo de plan | → HU_124 / HU_127 (campo) |
| HU_131 | Registrar descripción | → HU_124 / HU_127 (campo) |
| HU_132 | Registrar valor | → HU_124 / HU_127 (campo) |
| HU_133 | Registrar duración en días | → HU_124 / HU_127 (campo) |
| HU_134 | Filtrar / consultar servicios | **CU** (extend de Listar) |

Resultado: 11 → **6 CU**.

### 4.2 Suscripciones (C9)

| HU | Nombre actual | Destino |
|---|---|---|
| HU_161 | Cotizar suscripción | **CU** |
| HU_162 | Registrar suscripción | **CU** (tipo de venta: nueva / reingreso) |
| HU_163 | Listar suscripciones | **CU** |
| HU_164 | Ver detalle de suscripción | **CU** |
| HU_165 | Editar suscripción | **CU** |
| HU_166 | Administrar estado de suscripción | **CU** → renombrar "Cambiar estado de suscripción" |
| HU_167 / 168 / 169 | Registrar plan semanal / quincenal / mensual | → HU_162 (campo "Plan") |
| HU_170 / 171 | Seleccionar menú estándar / personalizado | → HU_162 (campo "Tipo de menú") |
| HU_172 | Aplicar recargo por menú personalizado | → RN-05 (cálculo en HU_162) |
| HU_173 / 174 | Calcular fecha de inicio / vencimiento | → RN-02 + RN-05 (cálculo en HU_162 y HU_183) |
| HU_175 | Registrar comprobante de transferencia | **CU** (puede ocurrir después de crear; activa la suscripción — RN-06) |
| HU_176 | Consultar comprobante de pago | → HU_164 (detalle) |
| HU_177–180 | Gestionar estado Pendiente / Activa / Cancelada / Vencida | → HU_166 (valores de estado; transiciones en RN-06) |
| HU_181 | Registrar venta nueva | → fusionada en HU_162 |
| HU_182 | Aplicar cobro de cocas en venta nueva | → RN-01 (en HU_162) |
| HU_183 | Registrar renovación | **CU** → renombrar "Renovar suscripción" |
| HU_184 | Registrar reingreso | → HU_162 (flujo alterno "reingreso") |
| HU_185 / 186 | Recuperar historial / restricciones del cliente | → respuesta del sistema en HU_162 (reingreso) y HU_183 |
| HU_187 / 188 | Exonerar cobro de cocas en renovación / reingreso | → RN-01 (en HU_183 / HU_162) |
| HU_189 | Validar cobertura de la dirección | → validación en HU_162 (RN-04) |
| HU_190 | Validar capacidad de producción | → validación en HU_162 |

Resultado: 30 → **8 CU**.

### 4.3 Ruta y Domiciliarios (C11)

| HU | Nombre actual | Destino |
|---|---|---|
| HU_194 | Crear ruta | **CU** |
| HU_191 / 192 / 193 | Consultar clientes georreferenciados / Visualizar zonas / Agrupar clientes por zona | → pasos del flujo de HU_194 (mapa al crear la ruta) |
| HU_195 | Listar rutas | **CU** |
| HU_196 | Ver detalle de ruta | **CU** |
| HU_197 | Editar ruta | **CU** |
| HU_198 | Eliminar ruta | **CU** → ⚠ revisar vs RN-07 (borrado lógico → "Cambiar estado de ruta") |
| HU_199 | Asignar domiciliario a ruta | **CU** → "Asignar domiciliario a ruta" (cubre asignar y reasignar: se selecciona el domiciliario) |
| HU_200 | Asignar / Reasignar domiciliario | → fusionada en HU_199 |
| HU_201 / 202 | Consultar clientes asociados / domiciliario asociado | → HU_196 (detalle) |
| HU_203 | Filtrar / consultar rutas | **CU** |
| HU_204 | Habilitar y deshabilitar entregas híbridas | → HU_194 / HU_197 (campo de la ruta) |

Resultado: 14 → **7 CU**.

### 4.4 Ficha Técnica de Producto (C12)

| HU | Nombre actual | Destino |
|---|---|---|
| HU_094 | Crear ficha técnica | **CU** |
| HU_095 | Listar fichas técnicas | **CU** |
| HU_096 | Ver detalle de ficha técnica | **CU** (muestra costo unitario) |
| HU_097 | Editar ficha técnica | **CU** |
| HU_098 | Cambiar estado de la ficha técnica | **CU** |
| HU_099 / 100 | Registrar insumos requeridos / cantidades | → HU_094 / HU_097 (detalle de insumos de la ficha) |
| HU_101 / 102 / 103 | Registrar tiempo / procedimiento / porciones | → HU_094 / HU_097 (campos) |
| HU_104 | Consultar costo unitario estimado | → HU_096 (dato calculado) |
| HU_105 | Filtrar / consultar fichas | **CU** |
| HU_106 | Generar reporte de fichas técnicas | **CU** (con filtros; incluye costo) |
| HU_107 | Generar reporte de costo unitario | → fusionada en HU_106 |

Resultado: 14 → **7 CU**.

### 4.5 Clientes (C13)

| HU | Nombre actual | Destino |
|---|---|---|
| HU_145 | Crear cliente | **CU** |
| HU_146 | Listar clientes | **CU** |
| HU_147 | Ver detalle del cliente | **CU** |
| HU_148 | Editar cliente | **CU** |
| HU_149–154 | Registrar dirección / modalidad / teléfono / correo / restricciones / alergias | → HU_145 / HU_148 (campos; dirección valida cobertura RN-04) |
| HU_155 / 156 | Consultar suscripciones asociadas / historial de pagos | → HU_147 (detalle) |
| HU_157 | Filtrar / consultar clientes | **CU** |
| HU_158 | Generar reporte de clientes activos | **CU** → "Generar reporte de clientes" (filtros: estado, zona, plan) |
| HU_159 / 160 | Reporte por zona / por tipo de plan | → fusionadas en HU_158 |

Resultado: 16 → **6 CU**.

### 4.6 Calendario (C14)

| HU | Nombre actual | Destino |
|---|---|---|
| HU_135 | Parametrizar calendario operativo | **CU** |
| HU_137 / 138 / 139 | Identificar días hábiles / Registrar festivos / Jornadas no operativas | → pasos de HU_135 |
| HU_136 | Listar calendario operativo | **CU** → "Consultar calendario operativo" |
| HU_140 | Cruzar agenda con suscripciones activas | → RN-02 (cálculo del sistema) |
| HU_141 | Programar producción diaria | → módulo Producción (fusionar con HU_087 Crear orden de producción) |
| HU_142 / 143 / 144 | Calcular días de servicio / fechas de vencimiento / liquidación proporcional | → RN-02 (usadas por Suscripciones HU_162/183 y RN-03) |

Resultado: 10 → **2 CU**.

### 4.7 Permisos → fusionado en Roles (decisión del equipo, v2)

Permisos es redundante con Roles: los permisos son un **catálogo fijo del sistema** (se cargan por semilla), el administrador no los crea; su objetivo real es **decidir qué puede hacer cada rol**.

| HU | Nombre actual | Destino |
|---|---|---|
| HU_008 | Crear permiso | → eliminada (catálogo fijo por semilla) |
| HU_009 | Listar permisos | → paso de HU_005 (el sistema muestra los permisos disponibles) |
| HU_010 | Ver detalle del permiso | → HU_003 (Ver detalle del rol y permisos configurados) |
| HU_011 | Editar permiso | → eliminada |
| HU_012 | Cambiar estado del permiso | → eliminada |
| HU_013 | Eliminar permiso | → eliminada |
| HU_005 | Asignar permisos al rol | **CU** — ⚠ debe volver al diagrama de Roles (la v2 lo quitó) |

Resultado: módulo Permisos 6 → **0 CU**; Roles conserva HU_005.

Cascada específica:
- Manual v2: borrar sección "Permisos:" de las fichas (HU_008–013); agregar "Asignar permisos al rol" al diagrama de Roles; revisar texto de "Configuración y Seguridad" ("Gestión de roles, permisos, usuarios…").
- `05_Casos_de_Uso/Diagramas_PUML/PERMISOS.puml` + PNG/SVG → eliminar; `ROLES.puml` → incluir HU_005.
- `Especificaciones/CU_01_Configuracion_y_Seguridad.md`, `casos_de_uso_v3/01_configuracion_y_seguridad.md`, `casos_de_uso_v3/README.md`, `casos_de_uso_v3.md`, `mapa_interactivo_svg.md`, `00_MOC_Casos_de_Uso.md`, `00_INDICE_GENERAL.md`.
- Matriz HU / Kanban: HU_008–013 → "Fusionada en Roles (HU_003 / HU_005)" o "Eliminada".
- C4: revisar `C4_Nivel3_Componentes.puml`, `C4_Nivel4_Codigo_Clases.puml`, `Arquitectura_C4_JackSoft.md` (quitar componente/controlador de gestión de permisos si existe).
- **⚠ Reemplazado el 2026-10-30:** el equipo decidió no tener tablas de permisos (`bd.uml` v3.5): lo que hace cada rol se define en la aplicación, y "Asignar permisos al rol" también sale. Lo siguiente queda solo como historial.
- **BD: NO se eliminan** las tablas `permisos` y `rol_permisos` (`DB_Tablas_Usuarios_Permisos.md`): el RBAC las sigue necesitando; solo se aclara que `permisos` es catálogo semilla sin CRUD.
- Ficha de proyecto (`06_.../Fichas_Tecnicas/`): verificar si lista "Permisos" como módulo.

---

## 5. Propuestas para módulos NO comentados (mismo error — validar con el equipo)

| Módulo | HU a revisar | Propuesta |
|---|---|---|
| Producto Terminado | HU_111, 112, 113 | Campos de HU_108 |
| Producto Terminado | HU_115, 116, 117 | Un solo reporte de producción con filtro de período |
| Productos | HU_057, 058, 060 | → Ver detalle HU_053 |
| Proveedores | HU_067, 068 | → Ver detalle HU_063 |
| Insumos | HU_041, 042, 043 | Un solo reporte de inventario con tipo/período |
| Compras | HU_077, 078, 079 | Un solo reporte de compras con filtros |
| Producción | HU_093 | → Ver detalle HU_089 |
| Acceso | HU_022 | Paso/include de HU_021 |
| Monitoreo | HU_205, 206, 207 | Un CU "Monitorear entregas en mapa" |
| Monitoreo | HU_209 | → Filtrar HU_212 |
| Monitoreo | HU_213, 214 | Un solo reporte de entregas por estado |
| Incidencias | HU_218, 219, 220, 221 | Revisar solapamiento (gestionar ≈ dar solución ≈ responder) |
| Dashboard | HU_224–241 | Agrupar en paneles (Comercial, Producción, Logística, Estratégico) |
| Usuarios / Roles / Permisos / Cat. Insumos | Eliminar vs RN-07 | Borrado lógico → confirmar si "Eliminar" se mantiene |

---

## 6. Cascada — documentos a actualizar por cada módulo corregido

| Módulo | PUML | PNG/SVG | Manual: diagrama | Manual: fichas CU | Especificaciones `CU_0x.md` | `casos_de_uso_v3` | Matriz HU / Kanban | RN referenciadas |
|---|---|---|---|---|---|---|---|---|
| Servicio | 🔲 | 🔲 | ✅ v2 | ✅ v2.1 | 🔲 CU_04 | 🔲 04 | 🔲 | — |
| Suscripciones | 🔲 | 🔲 | 🔲 | 🔲 | 🔲 CU_05 | 🔲 05 | 🔲 | RN-01, 02, 04, 05, 06 |
| Ruta y Domiciliarios | 🔲 | 🔲 | 🔲 | 🔲 | 🔲 CU_06 | 🔲 06 | 🔲 | RN-04, 07 |
| Ficha Técnica | 🔲 | 🔲 | ✅ v2 | 🔲 | 🔲 CU_03 | 🔲 03 | 🔲 | — |
| Clientes | 🔲 | 🔲 | ✅ v2 | ✅ v2.1 | 🔲 CU_05 | 🔲 05 | 🔲 | RN-04 |
| Calendario | 🔲 | 🔲 | ✅ v2 | 🔲 | 🔲 CU_04 | 🔲 04 | 🔲 | RN-02, 03 |
| Permisos → Roles | 🔲 | 🔲 | ⚠ falta HU_005 en Roles | ✅ v2.1 (fichas HU_008–013 borradas) | 🔲 CU_01 | 🔲 01 | 🔲 | — |

Rutas:
- PUML: `05_Casos_de_Uso/Diagramas_PUML/`
- PNG / SVG: `05_Casos_de_Uso/Diagramas_PNG/`, `05_Casos_de_Uso/Diagramas_SVG/`
- Especificaciones: `05_Casos_de_Uso/Especificaciones/` (+ `Documentacion_Casos_de_Uso_JackSoft.docx`)
- casos_de_uso_v3: `05_Casos_de_Uso/casos_de_uso_v3/`
- Matriz HU: `06_Gestion_de_Proyecto_Scrum/Historias_de_Usuario_y_Kanban/`
- Reglas: `02_Reglas_de_Negocio/`
- Generador: `05_Casos_de_Uso/scripts/generar_svg_casos_uso.py` (⚠ regenera desde el CSV y reintroduciría el error; no usar sin adaptarlo)

**Regla para las fichas del manual:** al fusionar una HU, su ficha se elimina y su contenido pasa a la ficha destino: campos → paso "Ingresa los datos"; validaciones → "Situaciones excepcionales"; reglas → respuesta del sistema + referencia RN-xx. Actualizar "Incluido / Extendido" según la sección 3.

**Numeración de HU:** se conservan los números existentes (no se renumeran) para no romper la trazabilidad con el backlog; las HU fusionadas se marcan en la matriz como "Fusionada en HU_xxx".

---

## 7. Otros pendientes del manual (sin comentario, pero incompletos)

- [ ] Anexos: actas firmadas por cliente y aprendices (C40) — **equipo**
- [ ] Anexos: evidencias (videos, entrevistas, fotos) (C41) — **equipo**
- [ ] Despliegue de hardware (vacío)
- [ ] Prototipo (React) — pantallazos / link
- [ ] Modelo de BD y diccionario de datos (tiene el ejemplo `IdVenta` de la plantilla)
- [ ] Seguridad (5 subsecciones vacías)
- [ ] Requerimientos mínimos cliente/servidor
- [ ] Bibliografía APA
- [ ] Control del documento (dice "Abril 2021")

---

## 8. Bitácora

| Fecha | Cambio | Documentos tocados |
|---|---|---|
| 2026-09-25 | Análisis de comentarios, criterio y decisiones por módulo | Este documento |
| 2026-09-25 | Compañero entrega Manual v2: rehace los 22 diagramas de CU (draw.io), agrega descripciones y figuras a los mockups, quita los comentarios C9–C14 | Manual v2 |
| 2026-09-25 | Revisión de la v2 (sección 9) | Este documento |
| 2026-09-25 | Decisión 4.7: Permisos se fusiona en Roles (se mantienen tablas BD) | Este documento |
| 2026-09-25 | **v2.1:** borradas fichas de Permisos (HU_008–013) y ajustado el texto de "Configuración y Seguridad". Servicio: HU_129–133 fusionadas en HU_124/126/127 (campos + validaciones de valor y duración). Clientes: HU_149–154 fusionadas en HU_145/148 (campos, modalidad fija/híbrida, cobertura RN-04), HU_155–156 en HU_147 (detalle), HU_159–160 en HU_158, renombrada "Generar reporte de clientes" | `Manual Técnico v2.1 Jacksoft.docx` |
| 2026-10-30 | `bd.uml` v3.5 pasa a ser el modelo vigente: acceso único, sin tablas de permisos (reemplaza la decisión 4.7 sobre las tablas), festivos según RN-02 | `04_Modelado_DB/Modelo_Relacional/v3_2026-10-30/bd.uml`, Contexto_e_Incongruencias_JackSoft.md |
| 2026-10-30 | Copia de la Ficha con las dos frases de festivos corregidas, pendiente de autorización del cliente; el original no se tocó | `Ficha_3agosto Jacksoft CF_v2_festivos.docx` |
| 2026-10-30 | C4 rehecho según la guía (niveles 1 a 4, nuevo detalle de suscripciones). Versión anterior archivada; PNG para evidencia en `Evidencia_C4_PNG/` | `05_Casos_de_Uso/Arquitectura_C4/v2_2026-10-30/` |

---

## 9. Revisión del Manual v2 (septiembre 25)

### 9.1 Qué cambió respecto a la v1

- ✅ Los 22 diagramas de CU se rehicieron: ya no hay campos/validaciones como casos de uso. **Esto atiende el fondo de C9–C14.**
- ✅ Mockups con descripción por módulo y numeración de figuras (Figura 1–22).
- ⚠ Las **243 fichas de casos de uso son idénticas a la v1** (mismo texto, mismas HU_129–133, HU_167–190, etc.). Hoy **diagramas y fichas se contradicen**.
- ⚠ Se **borraron del .docx los comentarios C9–C14** de la evaluadora (solo quedan C4, C40, C41).
- Sin cambios: introducción, C4, BD, seguridad, requerimientos, bibliografía, anexos.

### 9.2 Hallazgos por diagrama (v2)

| Diagrama v2 | Estado | Hallazgo |
|---|---|---|
| Dashboard | ✅ | 4 paneles + Filtrar + Exportar; coincide con la propuesta de la sección 5 |
| Roles | ❌ | Se perdió **"Asignar permisos al rol"** (HU_005). Con Permisos eliminado, hoy los permisos no aparecen en ningún diagrama |
| Permisos | 🟡 | Eliminado intencionalmente (redundante con Roles, decisión 4.7): sin mockup ni diagrama, **pero siguen las fichas HU_008–013** |
| Usuarios | ✅ | — |
| **Acceso** | ❌ | Se perdieron **Iniciar sesión, Recuperar contraseña y Cerrar sesión** (HU_021, 023, 025); se reemplazaron por "Listar log de acceso / Ver acceso / Reporte de acceso", que no existen en las HU |
| Categoría de Insumos | ✅ | "Eliminar" vs RN-07 (borrado lógico) |
| Insumos | ✅ | "Eliminar insumo" vs RN-07 |
| Proveedores | ✅ | "Eliminar proveedor" vs RN-07 |
| **Compras** | ⚠ | "Anular compra" (HU_075) se cambió por **"Eliminar compra"**: una compra que afectó inventario se anula, no se elimina (RN-07) |
| Categoría de Productos / Productos | ✅ | "Eliminar" vs RN-07 |
| Ficha Técnica | ✅ | Atiende C12 |
| **Producción** | ❌ | Falta **"Crear orden de producción"** (HU_087) — el módulo no permite producir. Óvalo "Listar" sin nombre. "Ver estado de producción" debería ser "Cambiar estado" |
| Producto Terminado | ✅ | Atiende la propuesta de la sección 5 |
| Empleados | ✅ | "Eliminar empleados" vs RN-07 |
| Categoría de Servicios | ✅ | — |
| Servicio | ✅ | Atiende C10. "Ver servicios activos" es en realidad un filtro |
| Calendario | ✅ | Atiende C14. "Visualizar calendario" y "Ver calendario" son redundantes |
| Clientes | ✅ | Atiende C13 |
| **Suscripciones** | ❌ | Quedó en Crear / Listar / Ver / Reporte. Se perdieron **Editar, Cambiar estado, Renovar, Registrar comprobante de pago, Cotizar** — el núcleo del negocio (RN-05, RN-06). Ver decisión 4.2 |
| **Ruta y Domiciliarios** | ❌ | Renombrado a "Gestión de domiciliarios": **desaparecieron las rutas** (Crear/Editar ruta, asignar domiciliario a ruta). C11 pedía unir asignar+reasignar, no eliminar rutas. Óvalo "Listar" sin nombre. Ver decisión 4.3 |
| Monitoreo | ⚠ | "Gestión de cobertura" pertenece a Rutas/zonas; "Interactuar con el monitoreo" es vago |
| **Incidencias** | ⚠ | Texto cortado **"Generar reporte de"**; se perdió **dar solución / gestionar incidencia** (HU_218–219), que es el objetivo principal; "Ver estado" duplica "Ver incidencia" |

### 9.3 Hallazgos transversales (todos los diagramas v2)

- **Notación UML:** dice "Extends" / "Include"; lo correcto es `«extend»` / `«include»`. Las líneas punteadas **no tienen punta de flecha** (salvo Gestión → Listar), así que no se ve la dirección.
- **"Crear X — include — Listar X"** se mantiene (ver criterio sección 3: crear no ejecuta el listado).
- **Sin nombre del módulo** dentro del límite del sistema (la v1 lo tenía) y **sin pie de figura** (los mockups sí tienen "Figura N").
- Se quitó el título **"Diagramas de Casos de Uso (Análisis)"** (Heading 2) → desaparece de la tabla de contenido.
- **Resolución:** JPG de 683 px de ancho estirados a página completa → se verán borrosos al imprimir. Exportar PNG a ≥2x.
- **Nombres inconsistentes:** "Crear clientes / servicios / incidencias / empleados" (plural), "listar servicios" (minúscula), "Ver suscripcion" (sin tilde), "Gestion de rol" (sin tilde).
- **Eliminar vs RN-07:** casi todos los módulos tienen "Eliminar"; la RN-07 exige borrado lógico → usar "Cambiar estado" o documentar la excepción.
- **Portada** sigue en "Versión 1.0" y el **Control de cambios** no registra la v2.

### 9.4 Siguiente paso recomendado

1. Corregir los 5 diagramas ❌ (Roles + HU_005, Acceso, Producción, Suscripciones, Ruta y Domiciliarios) y los ⚠.
2. **Actualizar las fichas** para que coincidan con los diagramas v2 (aplicar sección 4 y regla de fichas de la sección 6).
3. Ajustes transversales de notación, títulos, resolución y nombres.
4. Luego la cascada al resto del vault (sección 6).

### 9.5 Pendientes detectados al corregir las fichas (v2.1)

- **Clientes:** el diagrama v2 tiene "Cambiar estado de clientes" pero **no existe ficha ni HU** para ese caso de uso → crear HU nueva o quitarlo del diagrama.
- **Clientes:** existe ficha HU_157 "Filtrar / consultar clientes", pero el diagrama v2 no la muestra → agregarla al diagrama.
- **Servicio:** el diagrama v2 dice "Ver servicios activos"; la ficha es HU_134 "Filtrar / consultar servicios por nombre, tipo, estado" → unificar nombre (recomendado: "Filtrar servicios").
- **Relaciones en fichas:** siguen diciendo "Incluido: Listar X" en Crear/Editar/Ver; se corrigen junto con la notación de los diagramas (sección 3) para que ambos coincidan.
- Al abrir la v2.1 en Word: **actualizar la tabla de contenido** (clic derecho → Actualizar campo) para que desaparezca "Permisos".

## Actualización 2026-11-03
- **Numeración de HU:** se reemplaza la decisión de "no renumerar": desde el manual v2.2 las fichas van **HU_001–HU_248** en orden del documento (el manual usa los mismos números que la Documentación de CU v3).
- **Asignar permisos al rol:** queda **eliminado** (Permisos fuera del alcance, D-E). Reemplaza la nota de la línea de Roles que pedía devolverlo al diagrama.
