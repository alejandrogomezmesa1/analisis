---
title: "RN-06: Pagos, Comprobantes Bancarios y Estados de Transacción"
type: Regla_de_Negocio
tags:
  - reglas-de-negocio
  - pagos
  - comprobantes
  - transferencias
aliases:
  - Regla de Pagos
  - Comprobantes Bancarios
related:
  - "[[00_MOC_Reglas_Negocio]]"
  - "[[DB_Tabla_Suscripciones]]"
  - "[[PROC_Validacion_de_Pagos]]"
  - "[[CU_05_Clientes_y_Ventas]]"
---

# 💳 RN-06: Pagos, Comprobantes Bancarios y Estados de Transacción

## 📌 Declaración de la Regla
El flujo transaccional de **La Coca de Jacks S.A.S.** se realiza mediante **transferencia bancaria directa** (Bancolombia, Nequi u otras entidades). Para evitar fraudes y pérdidas financieras, **ninguna suscripción genera entregas de almuerzo ni órdenes a cocina mientras permanezca en estado `pendiente`**.

---

## ⚙️ Máquina de Estados del Pago y Suscripción

```mermaid
stateDiagram-v2
    [*] --> Pendiente: Cliente registra suscripción\ny adjunta foto de comprobante
    
    state Pendiente {
        [*] --> EnRevision: Administrador abre el módulo de pagos
    }
    
    EnRevision --> Aprobada: Comprobante válido y dinero acreditado en cuenta bancaria
    EnRevision --> Rechazada: Comprobante ilegible, editado o con monto insuficiente
    
    Aprobada --> Activa: Sistema actualiza suscripción a 'activa', define fecha_inicio e integra a Cocina/Ruta
    Rechazada --> [*]: Notifica al cliente para adjuntar nuevo comprobante o cancelar
```

### 1. Requisitos para la Aprobación del Pago
El administrador valida desde el backoffice los siguientes campos obligatorios del comprobante:
1. **Monto Exacto**: Coincidencia total con el `valor_total` de la suscripción (Plan + Menú Personalizado + Cocas si aplica).
2. **Número de Referencia/Comprobante**: Código único de la transacción bancaria.
3. **Fecha y Hora de la Transferencia**: Coincidencia con la ventana de contratación.

### 2. Transición a Estado `Activa`
* Al marcar el pago como `aprobado`, el sistema ejecuta una transacción atómica:
  * Cambia el estado de la suscripción de `pendiente` a `activa`.
  * Calcula la `fecha_vencimiento` oficial cruzando la cantidad de días contratados con [[DB_Tabla_Agenda]].
  * Registra la suscripción en el consolidado de producción para la fecha de inicio.

---

## 🔗 Relaciones del Sistema
* **Procesos**: [[PROC_Validacion_de_Pagos]], [[PROC_Registro_y_Venta]].
* **Tablas de BD**: [[DB_Tabla_Suscripciones]].
* **Casos de Uso**: [[CU_05_Clientes_y_Ventas]].
