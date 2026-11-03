---
title: "PROC-03: Planeación de Cocina, Fichas Técnicas y Recetas"
type: Proceso
tags:
  - proceso
  - cocina
  - producción
  - recetas
  - fichas-tecnicas
aliases:
  - Proceso de Cocina
  - Planeacion de Produccion
related:
  - "[[00_MOC_Procesos]]"
  - "[[RN_Suspensiones_Voluntarias]]"
  - "[[RN_Festivos_y_Agenda]]"
  - "[[DB_Tablas_Inventario_Compras]]"
  - "[[CU_03_Produccion_y_Recetas]]"
---

# 🍳 PROC-03: Planeación de Cocina, Fichas Técnicas y Recetas

## 📌 Resumen del Proceso
Este proceso consolida diariamente, de forma automatizada a las 5:00 PM, la cantidad exacta de almuerzos que la cocina debe preparar para la jornada del día siguiente. Cruza las suscripciones activas, las restricciones dietéticas de los clientes, las suspensiones notificadas y las fichas técnicas de los platos para generar la orden de producción y la lista de compras de insumos.

---

## 🔄 Algoritmo de Consolidación Diaria de Producción

```mermaid
flowchart TD
    CUT["Corte Automático: 5:00 PM del día anterior"] --> SQL1["1. Filtra suscripciones en estado 'activa'\ncon vigencia para la fecha de mañana"]
    SQL1 --> SQL2["2. Excluye clientes con registro de ausencia\nen [[DB_Tabla_Suspensiones]]"]
    SQL2 --> SQL3["3. Consulta la [[DB_Tabla_Agenda]]\n(Verifica que mañana no sea festivo)"]

    SQL3 --> MENUS["4. Agrupa solicitudes por Tipo de Menú:\n- Estándar (Pollo / Res / Cerdo)\n- Personalizado Pollo\n- Personalizado Cerdo"]

    MENUS --> ALERGIAS["5. Genera Consolidado de Restricciones Alimentarias\n(Ej. Sin Cebolla, Sin Mariscos, Bajo en Sal)"]

    ALERGIAS --> FT["6. Multiplica por Fichas Técnicas de Productos"]
    FT --> ORD["7. Genera Orden de Producción Diaria\ny Requerimientos de Insumos a Compras"]
```

---

## 📋 Fichas Técnicas y Porcionado
Cada producto del menú se compone de una Ficha Técnica detallada que registra:
* **Ingredientes e Insumos**: Cantidad exacta por porción (gramos, mililitros, unidades).
* **Proteína Principal**: Tipo de carne (Pollo, Res, Cerdo, Pescado).
* **Costo Unitario Estimado**: Sumatoria de insumos por plato.

### Ejemplo de Ficha Técnica: *Almuerzo Casero Pechuga a la Plancha*
| Insumo / Ingrediente | Categoría | Porción por Cliente | Unidad de Medida |
| :--- | :--- | :---: | :---: |
| Pechuga de Pollo | Proteína | 220 | Gramos |
| Arroz Blanco | Carbohidrato | 150 | Gramos |
| Ensalada Mixta | Vegetal | 100 | Gramos |
| Papa Salada | Tubérculo | 1 | Unidad |
| Jocoque / Aderezo | Salsa | 30 | Mililitros |

---

## 🔗 Vinculación con Reglas y Módulos
* Cruza con [[RN_Suspensiones_Voluntarias]] (exclusión de clientes) y [[RN_Festivos_y_Agenda]].
* Entidades involucradas: [[DB_Tablas_Inventario_Compras]] (fichas técnicas, productos, insumos).
* Casos de uso: [[CU_03_Produccion_y_Recetas]].
