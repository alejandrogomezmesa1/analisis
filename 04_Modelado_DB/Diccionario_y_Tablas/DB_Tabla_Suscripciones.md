---
title: "DB-01: Tabla `suscripciones`"
type: Modelo_DB
tags:
  - base-de-datos
  - tabla
  - suscripciones
  - dbml
aliases:
  - Tabla Suscripciones
  - DB Suscripciones
related:
  - "[[00_MOC_Modelo_DB]]"
  - "[[RN_Suscripciones_y_Menus]]"
  - "[[RN_Logistica_Cocas]]"
  - "[[RN_Pagos_y_Comprobantes]]"
  - "[[PROC_Registro_y_Venta]]"
---

# 🗄️ DB-01: Tabla `suscripciones`

## 📌 Descripción de la Entidad
La tabla `suscripciones` representa el contrato comercial entre el cliente y La Coca de Jacks S.A.S. Almacena las fechas de vigencia, modal de entrega, preferencias de proteína, cobros de cocas y comprobante de pago.

---

## 📐 Estructura de Columnas (DBML)

| Campo | Tipo de Dato | Restricción / FK | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | `INT` | `PK, AUTO_INCREMENT` | Identificador único de la suscripción. |
| `cliente_id` | `INT` | `FK -> usuarios.id` | Cliente titular de la suscripción. |
| `servicio_id` | `INT` | `FK -> servicios.id` | Plan contratado (Semanal, Quincenal, Mensual). |
| `tipo_venta` | `Enum` | `tipo_venta` | `'nueva'`, `'renovacion'`, `'reingreso'`. |
| `tipo_menu` | `Enum` | `tipo_menu` | `'estandar'`, `'pollo'`, `'cerdo'`. |
| `modalidad_entrega` | `Enum` | `modalidad_entrega` | `'fija'`, `'hibrida'`. |
| `cobro_cocas` | `DECIMAL(10,2)` | Default `0.00` | Cobro inicial de $70.000 COP si aplica ([[RN_Logistica_Cocas]]). |
| `recargo_menu` | `DECIMAL(10,2)` | Default `0.00` | Recargo de $10.000 COP si el menú es personalizado. |
| `valor_total` | `DECIMAL(10,2)` | `NOT NULL` | Liquidación final pagada por el cliente. |
| `comprobante_pago_url` | `VARCHAR(255)` | `NULLABLE` | URL del archivo de transferencia subido. |
| `estado` | `Enum` | `estado_suscripcion` | `'pendiente'`, `'activa'`, `'cancelada'`, `'vencida'`. |
| `fecha_inicio` | `DATE` | `NULLABLE` | Fecha de primera entrega programada. |
| `fecha_vencimiento` | `DATE` | `NULLABLE` | Fecha fin calculada omitiendo festivos. |
| `created_at` | `TIMESTAMP` | Default `CURRENT_TIMESTAMP` | Auditoría de creación. |

---

## 🔗 Relaciones de Clave Foránea (FK)
```dbml
Ref: suscripciones.cliente_id > usuarios.id
Ref: suscripciones.servicio_id > servicios.id
```

---

## 🔗 Conexión con Reglas y Procesos
* Mantiene los campos exigidos por [[RN_Suscripciones_y_Menus]] y [[RN_Logistica_Cocas]].
* Es actualizada por [[PROC_Validacion_de_Pagos]] cuando pasa de `'pendiente'` a `'activa'`.

## 🔄 Ajuste con el frontend 2026-11-03 (bd.uml v3.7)
| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `estado` | estado_suscripcion | pendiente_pago · verificando · activa · finalizada · rechazada · cancelada |
| `fecha_solicitud` | timestamp | Se compara con el corte semanal (sábado 12:00 m). |
| `inicio_sin_pago` | boolean | Renovación o reingreso que inició sin pagar. |
| `pago_pendiente` | boolean | `true` mientras no se valide el pago. |
| `fecha_limite_pago` | date | Inicio + 3 días hábiles; si vence, decide el administrador. |

Se eliminaron `tipo_menu`, `recargo_menu_personalizado`, `fuera_de_limite`, `aprobacion_fuera_limite` y `aprobada_por_usuario_id`. Precios: planes de 75/150/300 mil y kit de 80 mil. Regla: [[RN_Limite_Suscripcion_Semanal]].
