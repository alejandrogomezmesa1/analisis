---
title: "00 MOC — Reglas de Negocio (La Coca de Jacks)"
type: MOC
tags:
  - moc
  - reglas-de-negocio
  - politicas
aliases:
  - MOC Reglas Negocio
  - Mapa Reglas Negocio
related:
  - "[[00_INDICE_GENERAL]]"
  - "[[RN_Logistica_Cocas]]"
  - "[[RN_Festivos_y_Agenda]]"
  - "[[RN_Suspensiones_Voluntarias]]"
  - "[[RN_Domiciliarios_y_Rutas]]"
  - "[[RN_Suscripciones_y_Menus]]"
  - "[[RN_Pagos_y_Comprobantes]]"
  - "[[RN_QA_y_Auditoria]]"
---

# ⚖️ 00 MOC — Reglas de Negocio (RN)

Este Mapa de Contenido centraliza la documentación oficial de las políticas, restricciones lógicas, modelos operativos y criterios de calidad que gobiernan la plataforma **JackSoft**.

---

## 🗺️ Mapa Visual de las Reglas de Negocio

```mermaid
graph TD
    MOC_RN["[[00_MOC_Reglas_Negocio]]"] --> RN_COCAS["[[RN_Logistica_Cocas]]"]
    MOC_RN --> RN_FEST["[[RN_Festivos_y_Agenda]]"]
    MOC_RN --> RN_SUSP["[[RN_Suspensiones_Voluntarias]]"]
    MOC_RN --> RN_DOM["[[RN_Domiciliarios_y_Rutas]]"]
    MOC_RN --> RN_SUSC["[[RN_Suscripciones_y_Menus]]"]
    MOC_RN --> RN_PAGOS["[[RN_Pagos_y_Comprobantes]]"]
    MOC_RN --> RN_QA["[[RN_QA_y_Auditoria]]"]

    RN_COCAS --> DB_RUTA["[[DB_Tabla_Ruta_Clientes]]"]
    RN_FEST --> DB_AGENDA["[[DB_Tabla_Agenda]]"]
    RN_SUSP --> DB_SUSP["[[DB_Tabla_Suspensiones]]"]
    RN_DOM --> DB_GEO["[[DB_Tabla_Geolocalizacion]]"]
    RN_SUSC --> DB_SUSCR["[[DB_Tabla_Suscripciones]]"]
```

---

## 📋 Catálogo de Reglas de Negocio

1. **[[RN_Logistica_Cocas]]**: Política de rotación de recipientes reutilizables, cobro único inicial de $80.000 COP, control de cocas entregadas/recogidas y reporte de incidencias por rotura o extravío.
2. **[[RN_Festivos_y_Agenda]]**: Gestión del calendario operativo, días no laborables, liquidación proporcional con descuento automático de festivos y principio de no desplazamiento del vencimiento semanal.
3. **[[RN_Suspensiones_Voluntarias]]**: Tratamiento de ausencias notificadas por el cliente, supresión de orden de producción sin devoluciones de dinero ni extensión de vigencia.
4. **[[RN_Domiciliarios_y_Rutas]]**: Geofencing por polígonos, asignación de rutas por zona de cobertura, rastreo GPS en tiempo real y flujo de entregas.
5. **[[RN_Suscripciones_y_Menus]]**: Tipos de venta (Nueva, Renovación, Reingreso), recargo por menú personalizado (+$10.000 COP), tipos de plan y ciclos de vida.
6. **[[RN_Pagos_y_Comprobantes]]**: Proceso de validación de comprobantes de transferencia bancaria, estados del pago (Pendiente, Aprobado, Rechazado) y liberación de suscripción.
7. **[[RN_QA_y_Auditoria]]**: Políticas de calidad, conservación de trazabilidad mediante borrado lógico (campo `estado`) y restricciones de integridad referencial.

## 🔄 Nueva regla (2026-11-03)
* [[RN_Limite_Suscripcion_Semanal]] — Día y hora límite para suscribirse a la semana siguiente, gracia de pago y solicitudes fuera del límite.
