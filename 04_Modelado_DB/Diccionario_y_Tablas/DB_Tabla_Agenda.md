---
title: "DB-04: Tabla `agenda`"
type: Modelo_DB
tags:
  - base-de-datos
  - tabla
  - agenda
  - festivos
  - dbml
aliases:
  - Tabla Agenda
  - DB Agenda
related:
  - "[[00_MOC_Modelo_DB]]"
  - "[[RN_Festivos_y_Agenda]]"
  - "[[PROC_Registro_y_Venta]]"
  - "[[PROC_Planeacion_Cocina_y_Recetas]]"
---

# 🗄️ DB-04: Tabla `agenda`

## 📌 Descripción de la Entidad
La tabla `agenda` almacena el calendario operativo parametrizado de La Coca de Jacks S.A.S. Identifica explícitamente los días hábiles de producción y marca los días festivos nacionales como jornadas no operativas para la liquidación automática de suscripciones.

---

## 📐 Estructura de Columnas (DBML)

| Campo | Tipo de Dato | Restricción / FK | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | `INT` | `PK, AUTO_INCREMENT` | Identificador único del registro de calendario. |
| `fecha` | `DATE` | `UNIQUE, NOT NULL` | Fecha calendario específica (YYYY-MM-DD). |
| `es_festivo` | `BOOLEAN` | Default `false` | `true` si es feriado oficial o día no hábil. |
| `descripcion` | `VARCHAR(255)` | `NULLABLE` | Nombre del feriado (Ej: "Año Nuevo", "Batalla de Boyacá"). |

---

## 🔗 Conexión con Reglas y Procesos
* Base de cálculo para [[RN_Festivos_y_Agenda]] durante el checkout de [[PROC_Registro_y_Venta]].
* Consultada a las 5:00 PM por [[PROC_Planeacion_Cocina_y_Recetas]].
