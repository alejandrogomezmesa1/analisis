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

Subproceso **Menú** del proceso de Ventas. Actualizado en `bd.uml` **v3.7** (2026-11-03): publicación por semana y alternativas por restricción; ya no hay variantes de pollo o cerdo.

## 📐 `menus_semana`
`semana_inicio` (lunes, única), `estado` (borrador · publicado), `publicado_por_usuario_id`, `publicado_en`. Solo los menús de una semana publicada se muestran a los clientes y generan órdenes.

## 📐 `menus_diarios`
`menu_semana_id`, `calendario_id` (día hábil, uno por día), `nombre` (plato del día), `descripcion`.

## 📐 `menu_items`
Platos del día: `menu_id`, `tipo_recipiente_id` (coca), `producto_id`.

## 📐 `menu_alternativas`
`menu_item_id`, `restriccion` (carne · cerdo · mariscos · gluten · lacteos), `producto_alternativo_id`, `orden`. Si el cliente no puede comer lo que contiene el plato, recibe la alternativa.

## 🔗 Relaciones
* `ordenes_produccion.menu_id` → 1 menú del día = 1 orden; sus líneas están en `producto_terminado`.
* El cliente consulta el menú de la semana desde la app con el plato o la alternativa que le corresponde.
