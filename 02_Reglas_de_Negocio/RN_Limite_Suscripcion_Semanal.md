---
title: "RN: Corte semanal e inicio sin pago"
type: Regla_Negocio
tags:
  - reglas-de-negocio
  - suscripciones
  - configuracion
aliases:
  - Cierre semanal de suscripciones
  - Límite semanal de suscripción
related:
  - "[[00_MOC_Reglas_Negocio]]"
  - "[[RN_Suscripciones_y_Menus]]"
  - "[[RN_Festivos_y_Agenda]]"
  - "[[DB_Tabla_Configuraciones_Sistema]]"
  - "[[DB_Tabla_Suscripciones]]"
  - "[[CU_05_Clientes_y_Ventas]]"
---

# ⚖️ RN: Corte semanal e inicio sin pago

Actualizada el 2026-11-03 (bd.uml v3.7). Reemplaza la versión del 2026-11-02, que tenía horas de gracia y solicitudes fuera del límite aprobadas por el administrador; esas reglas **se eliminaron**.

## Regla
1. **Corte semanal:** las solicitudes recibidas antes del corte entran en la **semana siguiente**; las que llegan después, en la **semana subsiguiente**. Por defecto el corte es el **sábado a las 12:00 m** (configurable).
2. **Venta nueva:** debe pagar antes de iniciar (incluye el kit de cocas).
3. **Renovación y reingreso:** si la configuración **inicio sin pago** está activa, la suscripción inicia en la semana que corresponde aunque el cliente no haya pagado. Ejemplo: pide antes del corte, inicia el lunes, recibe el lunes y el martes con normalidad y paga el miércoles.
4. **Plazo de pago:** el cliente tiene **3 días hábiles** desde el inicio (configurable). Si `plazo_pago_cuenta_dia_inicio` está activo (por defecto), el día de inicio cuenta como día 1: inicia el lunes y vence el miércoles al final del día; si no, vence el jueves. Mientras tanto la suscripción está **activa** con `pago_pendiente` y `fecha_limite_pago`.
5. **Si no paga a tiempo:** el **administrador decide** (caso de uso *Gestionar suscripciones con pago vencido*): extender el plazo, suspender las entregas o cancelar. La decisión queda registrada y se notifica al cliente.
6. La fecha de inicio siempre es el primer **día hábil** de la semana que corresponda ([[RN_Festivos_y_Agenda]]).

## Configuración ([[DB_Tabla_Configuraciones_Sistema]])
| Clave | Valor por defecto |
| :--- | :--- |
| `dia_corte_suscripcion` | sabado |
| `hora_corte_suscripcion` | 12:00 |
| `inicio_sin_pago_activo` | true |
| `dias_habiles_plazo_pago` | 3 |
| `plazo_pago_cuenta_dia_inicio` | true |

## Datos ([[DB_Tabla_Suscripciones]])
`fecha_solicitud`, `inicio_sin_pago`, `pago_pendiente`, `fecha_limite_pago`.
