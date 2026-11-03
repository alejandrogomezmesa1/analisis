---
title: "DB-06: Tabla `geolocalizacion_domiciliarios`"
type: Modelo_DB
tags:
  - base-de-datos
  - tabla
  - gps
  - geolocalizacion
  - dbml
aliases:
  - Tabla Geolocalizacion
  - DB Geolocalizacion
related:
  - "[[00_MOC_Modelo_DB]]"
  - "[[RN_Domiciliarios_y_Rutas]]"
  - "[[PROC_Despacho_y_Distribucion]]"
---

# 🗄️ DB-06: Tabla `geolocalizacion_domiciliarios`

## 📌 Descripción de la Entidad
La tabla `geolocalizacion_domiciliarios` almacena el histórico de posiciones geográficas (Latitud y Longitud) enviadas periódicamente desde el dispositivo móvil del repartidor durante su turno de despacho.

---

## 📐 Estructura de Columnas (DBML)

| Campo | Tipo de Dato | Restricción / FK | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | `INT` | `PK, AUTO_INCREMENT` | Identificador único de la coordenada. |
| `domiciliario_id` | `INT` | `FK -> usuarios.id` | Usuario con rol Domiciliario que transmite su ubicación GPS (desde bd.uml v3.6 ya no existe la tabla `empleados`). |
| `latitud` | `DECIMAL(10,8)` | `NOT NULL` | Coordenada de latitud en grados decimales. |
| `longitud` | `DECIMAL(11,8)` | `NOT NULL` | Coordenada de longitud en grados decimales. |
| `fecha_hora` | `TIMESTAMP` | Default `CURRENT_TIMESTAMP` | Timestamp exacto de la emisión del GPS. |

---

## 🔗 Relaciones de Clave Foránea (FK)
```dbml
Ref: geolocalizacion_domiciliarios.domiciliario_id > usuarios.id
```

---

## 🔗 Conexión con Reglas y Procesos
* Soporta el rastreo en vivo de [[RN_Domiciliarios_y_Rutas]].
* Es leída en tiempo real en la vista de monitoreo de [[PROC_Despacho_y_Distribucion]].
