---
title: "Árbol de Objetivos — Medios y Fines (JackSoft)"
type: Investigacion
tags:
  - arbol-objetivos
  - medios-fines
  - marco-logico
aliases:
  - Arbol de Objetivos
  - Arbol de Medios y Fines
related:
  - "[[00_MOC_Investigacion]]"
  - "[[Arbol_de_Problemas]]"
  - "[[Ficha_de_Proyecto]]"
  - "[[PROC_Registro_y_Venta]]"
  - "[[RN_Logistica_Cocas]]"
  - "[[DB_Esquema_General]]"
---

# 🎯 Árbol de Objetivos — Medios y Fines (JackSoft)

El Árbol de Objetivos traduce las situaciones negativas expresadas en el [[Arbol_de_Problemas]] en condiciones positivas deseables y alcanzables mediante la implementación del sistema **JackSoft**.

---

## 📊 Diagrama del Árbol de Objetivos (Mermaid)

```mermaid
graph TD
    %% Fines Indirectos (Nivel Superior)
    FI1_1["Validación rápida de pagos"] --> FD1["FIN DIRECTO 1:\nReducción de errores y\ndemoras operativas"]
    FI1_2["Control de rotación de cocas"] --> FD1
    FI2_1["Ventas dentro de cobertura"] --> FD2["FIN DIRECTO 2:\nIncremento de ventas y\nfidelización de clientes"]
    FI2_2["Activación oportuna de planes"] --> FD2

    FD1 --> OC
    FD2 --> OC

    %% Objetivo Central (Tronco)
    OC["🎯 OBJETIVO CENTRAL:\nOptimizar la operación de La Coca de Jacks S.A.S.\nmediante una solución tecnológica integral (JackSoft)"]

    %% Medios Directos (Raíces Principales)
    OC --> MD1["MEDIO DIRECTO 1:\nPasarela / Validación de\npagos automatizada"]
    OC --> MD2["MEDIO DIRECTO 2:\nControl digital de inventario\ny rotación de envases"]
    OC --> MD3["MEDIO DIRECTO 3:\nGeorreferenciación y\ncobertura logística"]

    %% Medios Indirectos / Acciones
    MD1 --> MI1_1["Validación automática o asistida de comprobantes"]
    MD1 --> MI1_2["Módulo de gestión de suscripciones activas"]
    MD2 --> MI2_1["Seguimiento digital a cocas entregadas/recogidas"]
    MD2 --> MI2_2["Cálculo automático de cupos de cocina"]
    MD3 --> MI3_1["Zonas georreferenciadas con polígonos interactivos"]
    MD3 --> MI3_2["Planificación con agenda de festivos integrada"]
```

---

## 🎯 Articulación de Medios y Fines

### 1. Medios de Solución (Acciones Tecnológicas)
* **Medio 1 (Pagos)**: Módulo de registro y validación de transferencias bancarias que pasa suscripciones de `pendiente` a `activa` de forma transparente.
* **Medio 2 (Inventario y Cocas)**: Aplicación móvil que permite al domiciliario auditar `cocas_entregadas` y `cocas_recogidas` en cada parada, registrando incidencias en tiempo real.
* **Medio 3 (Georreferenciación)**: Mapeo interactivo de zonas de cobertura que bloquea automáticamente ventas fuera del perímetro y optimiza la ruta de despacho.

### 2. Fines Perseguidos (Beneficios del Negocio)
* **Reducción de Errores Operativos**: Cero desabastecimiento en cocina y control absoluto de los recipientes en circulación.
* **Incremento de Ventas y Retención**: Mejora drástica en el tiempo de atención al cliente y entregas puntuales.

---

## 🔗 Relación con los Requerimientos del Sistema
Los medios definidos en este árbol constituyen los módulos funcionales del sistema especificados en [[00_MOC_Casos_de_Uso]] y formalizados en los objetivos de la [[Ficha_de_Proyecto]].
