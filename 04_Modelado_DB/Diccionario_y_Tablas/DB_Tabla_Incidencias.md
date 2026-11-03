---
title: "DB-03: Tabla `incidencias`"
type: Modelo_DB
tags:
  - base-de-datos
  - tabla
  - incidencias
  - soporte
  - dbml
aliases:
  - Tabla Incidencias
  - DB Incidencias
related:
  - "[[00_MOC_Modelo_DB]]"
  - "[[RN_Logistica_Cocas]]"
  - "[[PROC_Gestion_Incidencias]]"
  - "[[DB_Tabla_Ruta_Clientes]]"
---

# 🗄️ DB-03: Tabla `incidencias`

## 📌 Descripción de la Entidad
La tabla `incidencias` almacena el historial auditado de novedades operacionales reportadas durante el despacho de pedidos o el consumo del servicio (cocas dañadas, ausencias del cliente, reclamos de calidad).

---

## 📐 Estructura de Columnas (DBML)

| Campo | Tipo de Dato | Restricción / FK | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | `INT` | `PK, AUTO_INCREMENT` | Identificador único de la incidencia. |
| `ruta_cliente_id` | `INT` | `FK -> ruta_clientes.id` | Parada específica donde ocurrió la novedad. |
| `reportante_tipo` | `Enum` | `tipo_reportante` | `'cliente'`, `'domiciliario'`. |
| `tipo_incidencia` | `VARCHAR(100)` | `NOT NULL` | E.g. `'coca_danada'`, `'coca_no_devuelta'`, `'ausente'`. |
| `descripcion` | `TEXT` | `NOT NULL` | Detalle narrativo del imprevisto. |
| `fotografia_url` | `VARCHAR(255)` | `NULLABLE` | Evidencia fotográfica subida desde App Móvil. |
| `estado` | `Enum` | `estado_incidencia` | `'abierta'`, `'en_gestion'`, `'resuelta'`. |
| `observaciones_solucion` | `TEXT` | `NULLABLE` | Respuesta final y acción aplicada por Administrador. |
| `created_at` | `TIMESTAMP` | Default `CURRENT_TIMESTAMP` | Timestamp del reporte. |

---

## 🔗 Relaciones de Clave Foránea (FK)
```dbml
Ref: incidencias.ruta_cliente_id > ruta_clientes.id
```

---

## 🔗 Conexión con Reglas y Procesos
* Genera los cobros de reposición exigidos en [[RN_Logistica_Cocas]].
* Se administra a través del proceso [[PROC_Gestion_Incidencias]].
