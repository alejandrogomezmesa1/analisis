---
title: "DB-05: Tabla `suspensiones_entrega`"
type: Modelo_DB
tags:
  - base-de-datos
  - tabla
  - suspensiones
  - ausencias
  - dbml
aliases:
  - Tabla Suspensiones
  - DB Suspensiones
related:
  - "[[00_MOC_Modelo_DB]]"
  - "[[RN_Suspensiones_Voluntarias]]"
  - "[[PROC_Planeacion_Cocina_y_Recetas]]"
---

# 🗄️ DB-05: Tabla `suspensiones_entrega`

## 📌 Descripción de la Entidad
La tabla `suspensiones_entrega` almacena el histórico de notificaciones de ausencias voluntarias realizadas por los clientes antes de la hora de corte de las 5:00 PM.

---

## 📐 Estructura de Columnas (DBML)

| Campo | Tipo de Dato | Restricción / FK | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | `INT` | `PK, AUTO_INCREMENT` | Identificador único de la suspensión. |
| `suscripcion_id` | `INT` | `FK -> suscripciones.id` | Suscripción del cliente que notifica la ausencia. |
| `fecha_suspension` | `DATE` | `NOT NULL` | Fecha específica en que NO se enviará el almuerzo. |
| `motivo` | `VARCHAR(255)` | `NULLABLE` | Breve justificación (Ej: "Viaje de trabajo"). |
| `created_at` | `TIMESTAMP` | Default `CURRENT_TIMESTAMP` | Timestamp de notificación (Debe ser <= 5:00 PM). |

---

## 🔗 Relaciones de Clave Foránea (FK)
```dbml
Ref: suspensiones_entrega.suscripcion_id > suscripciones.id
```

---

## 🔗 Conexión con Reglas y Procesos
* Fundamenta la regla de negocio [[RN_Suspensiones_Voluntarias]].
* Es filtrada automáticamente en el query de consolidación de [[PROC_Planeacion_Cocina_y_Recetas]].
