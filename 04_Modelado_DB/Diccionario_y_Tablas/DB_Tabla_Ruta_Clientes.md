---
title: "DB-02: Tabla `ruta_clientes`"
type: Modelo_DB
tags:
  - base-de-datos
  - tabla
  - rutas
  - cocas
  - dbml
aliases:
  - Tabla Ruta Clientes
  - DB Ruta Clientes
related:
  - "[[00_MOC_Modelo_DB]]"
  - "[[RN_Logistica_Cocas]]"
  - "[[RN_Domiciliarios_y_Rutas]]"
  - "[[PROC_Despacho_y_Distribucion]]"
  - "[[DB_Tabla_Incidencias]]"
---

# 🗄️ DB-02: Tabla `ruta_clientes`

## 📌 Descripción de la Entidad
La tabla `ruta_clientes` actúa como la entidad intermedia transaccional que modela la parada física del domiciliario en la puerta del cliente. Controla el orden de entrega en el mapa, las cocas entregadas/recogidas y la confirmación de la visita.

---

## 📐 Estructura de Columnas (DBML)

| Campo | Tipo de Dato | Restricción / FK | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | `INT` | `PK, AUTO_INCREMENT` | Identificador único de la parada. |
| `ruta_id` | `INT` | `FK -> rutas.id` | Ruta asignada a la jornada. |
| `suscripcion_id` | `INT` | `FK -> suscripciones.id` | Suscripción del cliente visitado. |
| `direccion_entrega` | `VARCHAR(255)` | `NOT NULL` | Dirección de entrega del día (Fija o Híbrida). |
| `orden_entrega` | `INT` | `NOT NULL` | Secuencia numérica de parada en la ruta (1, 2, 3...). |
| `cocas_entregadas` | `INT` | Default `1` | Cantidad de recipientes llenos entregados. |
| `cocas_recogidas` | `INT` | Default `1` | Cantidad de recipientes vacíos recogidos. |
| `estado_entrega` | `Enum` | `estado_entrega` | `'pendiente'`, `'en_ruta'`, `'entregado'`, `'no_entregado'`. |
| `hora_confirmacion` | `DATETIME` | `NULLABLE` | Timestamp exacto del reporte en App Móvil. |

---

## 🔗 Relaciones de Clave Foránea (FK)
```dbml
Ref: ruta_clientes.ruta_id > rutas.id
Ref: ruta_clientes.suscripcion_id > suscripciones.id
```

---

## 🔗 Conexión con Reglas y Procesos
* Fundamenta el registro diario de [[RN_Logistica_Cocas]].
* Es consumida y actualizada en vivo por [[PROC_Despacho_y_Distribucion]].
