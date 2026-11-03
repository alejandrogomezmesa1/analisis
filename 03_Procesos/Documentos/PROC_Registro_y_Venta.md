---
title: "PROC-01: Registro de Clientes y Venta de Suscripciones"
type: Proceso
tags:
  - proceso
  - ventas
  - registro-cliente
  - suscripcion
aliases:
  - Proceso de Venta
  - Registro de Clientes
related:
  - "[[00_MOC_Procesos]]"
  - "[[RN_Suscripciones_y_Menus]]"
  - "[[RN_Logistica_Cocas]]"
  - "[[RN_Domiciliarios_y_Rutas]]"
  - "[[DB_Tabla_Suscripciones]]"
  - "[[CU_05_Clientes_y_Ventas]]"
---

# 🛒 PROC-01: Registro de Clientes y Venta de Suscripciones

## 📌 Resumen del Proceso
El proceso de Registro y Venta gestiona el ingreso de nuevos usuarios o la renovación/reingreso de clientes existentes. Permite seleccionar el plan deseado, configurar preferencias alimentarias, validar la cobertura geográfica y realizar la liquidación inicial incluyendo el kit de recipientes cuando corresponda.

---

## 🔄 Flujo Paso a Paso (Diagrama de Actividades)

```mermaid
flowchart TD
    A["Cliente ingresa a la App/Web"] --> B["Registra datos personales, contacto\ny restricciones/alergias alimentarias"]
    B --> C["Ingresa dirección(es) de entrega\n(Modalidad Fija o Híbrida)"]
    C --> D{"¿Dirección está dentro de\npolígono de cobertura?"}

    D -- No --> E["⛔ Muestra mensaje de bloqueo:\nSin cobertura en la zona"]
    D -- Sí --> F["Selecciona tipo de plan:\nSemanal (5d), Quincenal (10d), Mensual (20d)"]

    F --> G{"¿Prefiere Menú Personalizado?\n(Exclusivo Pollo o Cerdo)"}
    G -- Sí --> H["Añade recargo de $10.000 COP"]
    G -- No --> I["Mantiene tarifa base menú estándar"]

    H --> J{"¿Es Venta Nueva y no posee cocas?"}
    I --> J

    J -- Sí --> K["Añade cobro único de cocas:\n$70.000 COP"]
    J -- No --> L["Exonera cobro de cocas\n(Renovación / Reingreso)"]

    K --> M["Sistema calcula Total A Pagar\ny muestra datos de transferencia bancaria"]
    L --> M
    M --> N["Cliente sube foto del comprobante de pago"]
    N --> O["Crea suscripción en estado 'pendiente'\ny pasa a [[PROC_Validacion_de_Pagos]]"]
```

---

## 📑 Entradas y Salidas del Proceso

* **Entradas**:
  * Datos personales del cliente (Nombre, ID, Teléfono, Correo).
  * Restricciones y alergias alimentarias.
  * Dirección(es) y coordenadas GPS de entrega.
  * Plan seleccionado y preferencia de proteína.
  * Comprobante de transferencia bancaria (imagen/PDF).
* **Salidas**:
  * Registro en la tabla de clientes.
  * Registro en la tabla [[DB_Tabla_Suscripciones]] en estado `pendiente`.
  * Ticket de notificación enviado al panel del Administrador.

---

## 🔗 Vinculación con Reglas y Base de Datos
* Aplicación estricta de [[RN_Logistica_Cocas]] ($70.000 COP) y [[RN_Suscripciones_y_Menus]] (+$10.000 COP recargo).
* Verificación geográfica mediante polígonos descritos en [[RN_Domiciliarios_y_Rutas]].
* Mapeo de la entidad en [[DB_Tabla_Suscripciones]].
