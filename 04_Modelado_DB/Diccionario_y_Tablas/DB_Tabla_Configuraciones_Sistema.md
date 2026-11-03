---
title: "DB: Tablas `configuraciones_sistema` e `historial_configuraciones`"
type: Modelo_DB
tags:
  - base-de-datos
  - tabla
  - configuracion
  - dbml
aliases:
  - Configuraciones del sistema
related:
  - "[[00_MOC_Modelo_DB]]"
  - "[[CU_01_Configuracion_y_Seguridad]]"
  - "[[RN_Logistica_Cocas]]"
  - "[[RN_Suscripciones_y_Menus]]"
  - "[[RN_Suspensiones_Voluntarias]]"
---

# 🗄️ Tablas de Configuraciones del sistema

Agregadas en `bd.uml` **v3.6** (Cambio de alcance 2026-11-02). Subproceso **Configuraciones del sistema** del proceso de Configuración.

## 📌 Descripción
Guardan los parámetros que el negocio puede ajustar sin cambiar el código: **valores del negocio** (cobro del kit de cocas, recargo por menú personalizado, hora límite de suspensión) y **funcionalidades activables** (dirección híbrida, menú personalizado). Se pueden agregar configuraciones nuevas. La liquidación copia el valor vigente a la suscripción, así un cambio posterior no altera ventas ya registradas.

## 📐 `configuraciones_sistema`

| Campo | Tipo | Restricción | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | integer | PK | Identificador. |
| `clave` | varchar | UNIQUE, NOT NULL | Nombre técnico (ej. `cobro_cocas`, `modalidad_hibrida_activa`). |
| `nombre` | varchar | NOT NULL | Nombre visible. |
| `categoria` | varchar | NOT NULL | `valores_negocio` · `funcionalidades` (abierta). |
| `tipo_valor` | enum `tipo_valor_configuracion` | NOT NULL | numero · moneda · texto · hora · dia_semana · booleano. |
| `valor` / `valor_por_defecto` | varchar | NOT NULL | Valor actual y valor de fábrica. |
| `valor_minimo` / `valor_maximo` | varchar | opcional | Rango permitido. |
| `descripcion` | text | | Explicación para el administrador. |
| `estado` | estado_general | default `activo` | |
| `updated_at` / `updated_by_usuario_id` | timestamp / FK usuarios | | Último cambio. |

## 📐 `historial_configuraciones`
Bitácora de solo inserción: `configuracion_id` (FK), `valor_anterior`, `valor_nuevo`, `usuario_id` (FK), `fecha`.

## 🧾 Valores iniciales

| Clave | Valor | Regla relacionada |
| :--- | :--- | :--- |
| `cobro_cocas` | 70000 | [[RN_Logistica_Cocas]] |
| `recargo_menu_personalizado` | 10000 | [[RN_Suscripciones_y_Menus]] |
| `hora_limite_suspension` | 17:00 | [[RN_Suspensiones_Voluntarias]] |
| `modalidad_hibrida_activa` | true | [[RN_Domiciliarios_y_Rutas]] |
| `menu_personalizado_activo` | true | [[RN_Suscripciones_y_Menus]] |
| `dia_limite_suscripcion` | domingo | [[RN_Limite_Suscripcion_Semanal]] |
| `hora_limite_suscripcion` | 17:00 | [[RN_Limite_Suscripcion_Semanal]] |
| `horas_gracia_pago` | 15 | [[RN_Limite_Suscripcion_Semanal]] |
| `solicitudes_fuera_limite_activas` | false | [[RN_Limite_Suscripcion_Semanal]] |
