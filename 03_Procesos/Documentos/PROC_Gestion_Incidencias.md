---
title: "PROC-05: Gestión de Novedades e Incidencias Operativas"
type: Proceso
tags:
  - proceso
  - incidencias
  - soporte
  - novedades
aliases:
  - Proceso de Incidencias
  - Gestion de Novedades
related:
  - "[[00_MOC_Procesos]]"
  - "[[RN_Logistica_Cocas]]"
  - "[[DB_Tabla_Incidencias]]"
  - "[[PROC_Despacho_y_Distribucion]]"
  - "[[CU_06_Logistica_y_Domicilios]]"
---

# ⚠️ PROC-05: Gestión de Novedades e Incidencias Operativas

## 📌 Resumen del Proceso
Este proceso centraliza el reporte, seguimiento y resolución de imprevistos surgidos durante el ciclo de vida del servicio. Permite capturar novedades tanto desde la App del Domiciliario (cliente no encontrado, dirección errónea, coca dañada/no entregada) como desde la App del Cliente (calidad del alimento, empaque defectuoso).

---

## 🔄 Flujo de Gestión y Solución de Incidencias

```mermaid
flowchart TD
    REP["Reporte de Novedad desde App Móvil\n(Actor: Domiciliario o Cliente)"] --> CAT{"Categoría de la Incidencia"}

    CAT --> C1["Coca Dañada / Rota / Sucia"]
    CAT --> C2["Coca No Devuelta / Perdida"]
    CAT --> C3["Cliente No Encontrado / Ausente"]
    CAT --> C4["Calidad del Almuerzo / Empaque"]

    C1 --> REG["Genera Registro en [[DB_Tabla_Incidencias]]\nEstado: 'abierta'"]
    C2 --> REG
    C3 --> REG
    C4 --> REG

    REG --> TICKET["Notificación en Backoffice del Administrador"]
    TICKET --> SOL{"Acción de Solución"}

    SOL --> S1["Cobro de Reposición ($70.000) o Multa"]
    SOL --> S2["Reagendamiento / Contacto Telefónico"]
    SOL --> S3["Reposición de Almuerzo por Cocina"]

    S1 --> CLOSE["Actualiza estado a 'resuelta'\ny registra observaciones de auditoría"]
    S2 --> CLOSE
    S3 --> CLOSE
```

---

## 📋 Tipología de Incidencias y Acciones Correctivas

| Código | Tipo de Incidencia | Reportante | Impacto en Sistema | Acción de Gestión |
| :--- | :--- | :---: | :--- | :--- |
| **INC-01** | Coca Dañada / Defectuosa | Domiciliario | Crea registro en [[DB_Tabla_Incidencias]] | Genera cobro de reposición al cliente o descuento al proveedor. |
| **INC-02** | Coca No Devuelta | Domiciliario | Incrementa contador de cocas pendientes | Bloquea renovaciones hasta que se devuelva o cancele el valor. |
| **INC-03** | Cliente No Encontrado | Domiciliario | Marca estado parada como `no_entregado` | Notifica al cliente vía Push/WhatsApp para coordinar retiro. |
| **INC-04** | Reclamo de Calidad / Menú | Cliente | Notifica con foto adjunta al Administrador | Revisión con jefe de cocina e indemnización si aplica. |

---

## 🔗 Vinculación con Módulos
* Soportado por la entidad [[DB_Tabla_Incidencias]].
* Intersecta las reglas de [[RN_Logistica_Cocas]] y el proceso [[PROC_Despacho_y_Distribucion]].
