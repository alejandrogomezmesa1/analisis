---
title: "00 MOC — Modelado de Base de Datos (JackSoft)"
type: MOC
tags:
  - moc
  - base-de-datos
  - modelo-relacional
  - dbml
aliases:
  - MOC Modelo DB
  - Mapa Base de Datos
related:
  - "[[00_INDICE_GENERAL]]"
  - "[[00_MOC_Manual_Tecnico]]"
  - "[[DB_Esquema_General]]"
  - "[[DB_Tabla_Suscripciones]]"
  - "[[DB_Tabla_Ruta_Clientes]]"
  - "[[DB_Tabla_Incidencias]]"
  - "[[DB_Tabla_Agenda]]"
  - "[[DB_Tabla_Suspensiones]]"
  - "[[DB_Tabla_Geolocalizacion]]"
  - "[[DB_Tablas_Usuarios_Permisos]]"
  - "[[DB_Tablas_Inventario_Compras]]"
---

# 🗄️ 00 MOC — Modelado de Base de Datos (DB)

Este Mapa de Contenido estructura la arquitectura física y relacional del esquema de base de datos del software **JackSoft**, diseñado a partir de la especificación DBML oficial.

---

## 🗺️ Mapa de Dominio de la Base de Datos

```mermaid
graph TD
    MOC_DB["[[00_MOC_Modelo_DB]]"] --> DB_GEN["[[DB_Esquema_General]]"]
    MOC_DB --> DB_SUSC["[[DB_Tabla_Suscripciones]]"]
    MOC_DB --> DB_RUTA["[[DB_Tabla_Ruta_Clientes]]"]
    MOC_DB --> DB_INC["[[DB_Tabla_Incidencias]]"]
    MOC_DB --> DB_AGE["[[DB_Tabla_Agenda]]"]
    MOC_DB --> DB_SUSP["[[DB_Tabla_Suspensiones]]"]
    MOC_DB --> DB_GEO["[[DB_Tabla_Geolocalizacion]]"]
    MOC_DB --> DB_USR["[[DB_Tablas_Usuarios_Permisos]]"]
    MOC_DB --> DB_INV["[[DB_Tablas_Inventario_Compras]]"]

    DB_SUSC -. Foreign Keys .-> DB_USR
    DB_RUTA -. Foreign Keys .-> DB_SUSC
    DB_INC -. Foreign Keys .-> DB_RUTA
```

---

## 📋 Entidades y Tablas del Esquema

1. **[[DB_Esquema_General]]**: Visión global del modelo E-R, convenciones de claves primarias, enumeraciones (Enums) e integridad referencial.
2. **[[DB_Tabla_Suscripciones]]**: Entidad principal de contratación, montos, personalización de menús y cobro de cocas.
3. **[[DB_Tabla_Ruta_Clientes]]**: Tabla intermedia de paradas diarias de reparto y conteo de cocas entregadas/recogidas.
4. **[[DB_Tabla_Incidencias]]**: Auditoría de novedades físicas (recipientes dañados, ausencias, ausencias).
5. **[[DB_Tabla_Agenda]]**: Calendario operativo parametrizado con festivos oficiales.
6. **[[DB_Tabla_Suspensiones]]**: Registro de ausencias voluntarias notificadas por los clientes.
7. **[[DB_Tabla_Geolocalizacion]]**: Histórico de coordenadas GPS enviadas por los domiciliarios.
8. **[[DB_Tablas_Usuarios_Permisos]]**: Modelo RBAC (`usuarios`, `roles`, `permisos`, `rol_permisos`).
9. **[[DB_Tablas_Inventario_Compras]]**: Cadena de abastecimiento (`insumos`, `proveedores`, `compras`, `fichas_tecnicas`, `ordenes_produccion`).

---

## 🗃️ Archivos de Esquema y Diagramas

- **Esquemas DBML (`04_Modelado_DB/Modelo_Relacional/vN_fecha/`):**
  - `v5_2026-11-03/bd.uml`: ⭐ Versión vigente, DBML v3.7 (3 de noviembre, 41 tablas, 68 relaciones): ajuste con el frontend.
  - `v4_2026-11-02/bd.uml`: DBML v3.6 (2 de noviembre, 36 tablas, 56 relaciones, 23 subprocesos). Sin `empleados`; nuevas [[DB_Tabla_Configuraciones_Sistema]] y menús en [[DB_Tablas_Menu]].
  - `v3_2026-10-30/bd.uml`: DBML v3.5 (30 de octubre, 35 tablas, 53 relaciones, 22 TableGroups).
  - `v1_2026-08-13/jacksoft_modelo_relacional_v1.dbml`: Versión inicial (13 de agosto, 33 tablas).
  - `v2_2026-08-24/jacksoft_modelo_relacional_v2.dbml`: Versión consolidada (24 de agosto, 33 tablas adaptadas a los módulos vigentes).
- **Diagrama Relacional Vectorial:** ⭐ `04_Modelado_DB/Diagramas/v3_2026-11-03/LaCocaDiagramDB.svg` (generado desde bd.uml v3.7). Anteriores: `v2_2026-11-02/` (v3.6). Histórico en `v1_2026-08-21/`:
  - `LaCocaDiagramDB.svg`: Diagrama conceptual y físico completo de la base de datos (37 tablas con relaciones foráneas).
