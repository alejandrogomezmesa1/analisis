---
title: "DB-07: Tablas de Usuarios, Roles, Permisos y Seguridad (RBAC)"
type: Modelo_DB
tags:
  - base-de-datos
  - rbac
  - usuarios
  - roles
  - permisos
  - dbml
aliases:
  - Tablas Usuarios Permisos
  - Modelo RBAC DB
related:
  - "[[00_MOC_Modelo_DB]]"
  - "[[RN_QA_y_Auditoria]]"
  - "[[CU_01_Configuracion_y_Seguridad]]"
---

# 🗄️ DB-07: Tablas de Usuarios, Roles, Permisos y Seguridad (RBAC)

## 📌 Descripción del Módulo de Seguridad
Este conjunto de tablas implementa el modelo de **Control de Acceso Basado en Roles (RBAC)** en JackSoft. Permite administrar las credenciales de los clientes, empleados y administradores, asegurando que cada rol solo acceda a los módulos permitidos.

---

## 📐 Estructura de Tablas (DBML)

```dbml
Table roles {
  id int [pk, increment]
  nombre varchar(50) [not null, unique]
  descripcion text
  estado estado_general [default: 'activo']
  created_at timestamp [default: `current_timestamp`]
}

Table permisos {
  id int [pk, increment]
  modulo varchar(50) [not null]
  accion varchar(50) [not null]
  descripcion text
  estado estado_general [default: 'activo']
}

Table rol_permisos {
  rol_id int [ref: > roles.id]
  permiso_id int [ref: > permisos.id]
  indexes {
    (rol_id, permiso_id) [pk]
  }
}

Table usuarios {
  id int [pk, increment]
  rol_id int [ref: > roles.id]
  nombre_completo varchar(100) [not null]
  documento_identidad varchar(20) [unique, not null]
  correo_electronico varchar(100) [unique, not null]
  telefono varchar(20)
  contrasena_hash varchar(255) [not null]
  direccion_defecto varchar(255)
  restricciones_alimentarias text
  estado estado_general [default: 'activo']
  created_at timestamp [default: `current_timestamp`]
}
```

---

## 🔗 Conexión con Reglas y Casos de Uso
* Aplica el principio de borrado lógico por `estado` de [[RN_QA_y_Auditoria]].
* Sustenta las funciones del módulo funcional [[CU_01_Configuracion_y_Seguridad]].

## 🔄 Cambio de alcance 2026-11-02
* Ya no existe la tabla `empleados` ni un módulo de empleados: el personal interno (cocina, despacho y domiciliarios) se registra como **usuario** con su rol.
* Permisos sigue fuera del alcance (decisión D-E): lo que puede hacer cada rol se define en la aplicación.
* Las configuraciones generales del sistema viven en [[DB_Tabla_Configuraciones_Sistema]].
