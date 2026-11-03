---
title: "Árbol de Problemas — La Coca de Jacks"
type: Investigacion
tags:
  - arbol-problemas
  - causas-efectos
  - marco-logico
aliases:
  - Arbol de Problemas
  - Diagnostico Causal
related:
  - "[[00_MOC_Investigacion]]"
  - "[[Planteamiento_del_Problema]]"
  - "[[Arbol_de_Objetivos]]"
  - "[[RN_Pagos_y_Comprobantes]]"
  - "[[RN_Logistica_Cocas]]"
  - "[[RN_Domiciliarios_y_Rutas]]"
---

# 🌳 Árbol de Problemas — La Coca de Jacks S.A.S.

El Árbol de Problemas representa la estructura jerárquica de causalidad formulada mediante la Metodología de Marco Lógico para diagnosticar el problema central de la compañía.

---

## 📊 Diagrama del Árbol de Problemas (Mermaid)

```mermaid
graph BT
    %% Causas Raíz (Nivel 1)
    C1["Causa 1: Cobro y validación\nde pagos manuales"]
    C2["Causa 2: Rotación de cocas\ne inventario sin control"]
    C3["Causa 3: Logística y cobertura\nsin georreferenciación"]

    %% Causas Indirectas (Nivel 2)
    CI1_1["Revisión manual de comprobantes bancarios"] --> C1
    CI1_2["Falta de pasarela automatizada"] --> C1
    CI2_1["Sin registro de cocas entregadas/recogidas"] --> C2
    CI2_2["Conteo manual de cupos diarios"] --> C2
    CI3_1["Zonas y rutas asignadas empíricamente"] --> C3
    CI3_2["Gestión manual de días festivos"] --> C3

    %% Problema Central
    C1 --> PC["⚠️ PROBLEMA CENTRAL:\nOperación manual e ineficiente\nde La Coca de Jacks S.A.S."]
    C2 --> PC
    C3 --> PC

    %% Efectos Directos
    PC --> ED1["Efecto Directo 1:\nErrores y demoras operativas"]
    PC --> ED2["Efecto Directo 2:\nPérdida de ventas y clientes"]

    %% Efectos Indirectos
    ED1 --> EI1_1["Activación de planes demorada (24h-48h)"]
    ED1 --> EI1_2["Pérdida de recipientes y desabastecimiento"]
    ED2 --> EI2_1["Entregas fuera de zona o almuerzos fríos"]
    ED2 --> EI2_2["Cancelación de suscripciones (Churn elevado)"]
```

---

## 🔍 Análisis Causal Detallado

### 1. Causas Raíz (Raíces)
1. **Cobro y Validación de Pagos Manuales**: El administrador debe interrumpir sus labores para validar transferencias en la app del banco.
2. **Rotación de Cocas e Inventario sin Control**: La ausencia de un registro de entregas/recogidas impide saber cuántas cocas tiene cada cliente.
3. **Logística y Cobertura sin Georreferenciación**: Agrupación empírica de pedidos por sectores sin verificación técnica de polígonos.

### 2. Problema Central (Tronco)
> **"Operación manual e ineficiente de La Coca de Jacks S.A.S."**
Los procesos clave de venta, cobro, cocina, empaque, ruta y reportería dependen exclusivamente de chats de WhatsApp y hojas de Excel sin integración.

### 3. Efectos e Impactos (Follaje/Ramas)
* **Errores y Demoras Operativas**: Retrasos en la preparación y pérdidas financieras por reposición no cobrada de recipientes.
* **Pérdida de Ventas y Clientes**: Clientes insatisfechos por demoras en entregas y desatención en horas pico.

---

## 🔗 Conversión a Solución
Este árbol de problemas se convierte directamente en el [[Arbol_de_Objetivos]], transformando las causas en medios y los efectos en fines.
