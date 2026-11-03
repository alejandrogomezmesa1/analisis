---
title: "DB: Tablas del subproceso Menú (`menus_diarios`, `menu_items`)"
type: Modelo_DB
tags:
  - base-de-datos
  - tabla
  - menu
  - dbml
aliases:
  - Tablas de Menú
related:
  - "[[00_MOC_Modelo_DB]]"
  - "[[CU_05_Clientes_y_Ventas]]"
  - "[[RN_Suscripciones_y_Menus]]"
  - "[[DB_Tabla_Agenda]]"
---

# 🗄️ Tablas del subproceso Menú

Desde `bd.uml` **v3.6** (Cambio de alcance 2026-11-02) estas tablas pertenecen al subproceso **Menú** del proceso de Ventas (antes estaban en Producción).

## 📐 `menus_diarios`
| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | integer PK | |
| `calendario_id` | FK calendario, UNIQUE | Día hábil del menú (un menú por día). |
| `semana_inicio` | date | Lunes de la semana; agrupa la programación semanal (nuevo en v3.6). |
| `nombre`, `descripcion` | varchar, text | |
| `estado` | estado_general | Un menú inactivo no se muestra al cliente ni genera orden de producción. |

## 📐 `menu_items`
Platos del menú: `menu_id` (FK), `tipo_recipiente_id` (coca), `producto_id`, `variante` (común, proteína estándar, pollo, cerdo).

## 🔗 Relaciones
* `ordenes_produccion.menu_id` → 1 menú del día = 1 orden de producción.
* El cliente consulta el menú de la semana desde la app móvil con la variante de su suscripción.
