---
title: "RN-07: QA, Auditoría y Conservación de Trazabilidad (Borrado Lógico)"
type: Regla_de_Negocio
tags:
  - reglas-de-negocio
  - qa
  - auditoria
  - borrado-logico
aliases:
  - Regla de QA
  - Borrado Logico
related:
  - "[[00_MOC_Reglas_Negocio]]"
  - "[[DB_Esquema_General]]"
  - "[[DB_Tablas_Usuarios_Permisos]]"
---

# 🛡️ RN-07: QA, Auditoría y Conservación de Trazabilidad (Borrado Lógico)

## 📌 Declaración de la Regla
Para garantizar la integridad referencial de los datos históricos, auditoría financiera y cumplimiento de estándares de QA en el software **JackSoft**, **está estrictamente prohibido el borrado físico (`DELETE`) de registros maestros y transaccionales en la base de datos**.

---

## ⚙️ Políticas de Trazabilidad y Seguridad

```mermaid
graph LR
    REQ["Solicitud de Eliminación de Registro\n(Ej: Usuario, Insumo, Producto, Rol)"] --> CHECK{"¿El registro tiene referencias históricas\no transacciones activas?"}

    CHECK -- Prohibido DELETE Físico --> LOGIC["Aplica Borrado Lógico:\nActualiza campo estado = 'inactivo'"]
    LOGIC --> SAFE["Mantiene Integridad Referencial:\nConserva facturas, compras y rutas pasadas"]
```

### 1. Mecanismo de Borrado Lógico (`estado`)
* Todas las tablas del sistema incorporan una columna de estado general (`estado` Enum `'activo'`, `'inactivo'`).
* Cuando un administrador ejecuta una acción de "eliminar" sobre un usuario, producto, insumo o proveedor:
  * El sistema efectúa un `UPDATE tabla SET estado = 'inactivo' WHERE id = :id`.
  * El registro se oculta en los listados operativos habituales, pero permanece accesible en consultas de auditoría y reportes históricos.

### 2. Auditoría Atómica (`created_at`, `updated_at`)
* Cada tabla transaccional registra marcas temporales inalterables:
  * `created_at`: Fecha y hora exacta de creación del registro.
  * `updated_at`: Fecha y hora del último cambio realizado.

---

## 🔗 Relaciones del Sistema
* **Modelado DB**: [[DB_Esquema_General]], [[DB_Tablas_Usuarios_Permisos]].
* **Casos de Uso**: [[CU_01_Configuracion_y_Seguridad]].
