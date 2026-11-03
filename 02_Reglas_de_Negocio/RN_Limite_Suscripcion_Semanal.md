---
title: "RN: Límite semanal de suscripción"
type: Regla_Negocio
tags:
  - reglas-de-negocio
  - suscripciones
  - configuracion
aliases:
  - Cierre semanal de suscripciones
related:
  - "[[00_MOC_Reglas_Negocio]]"
  - "[[RN_Suscripciones_y_Menus]]"
  - "[[RN_Festivos_y_Agenda]]"
  - "[[DB_Tabla_Configuraciones_Sistema]]"
  - "[[DB_Tabla_Suscripciones]]"
  - "[[CU_05_Clientes_y_Ventas]]"
---

# ⚖️ RN: Límite semanal de suscripción

Definida el 2026-11-03. Aplica a **venta nueva, renovación y reingreso**.

## Regla
1. Existe un **límite semanal** (día + hora) para suscribirse a la semana siguiente. Por defecto: **domingo a las 5:00 PM**.
2. Una solicitud recibida **antes del límite** entra en la **semana siguiente** si el pago se registra dentro del **plazo de gracia** (por defecto 15 horas: hasta el **lunes a las 8:00 AM**). Si el pago llega después, la suscripción inicia la **semana subsiguiente**.
3. Una solicitud recibida **después del límite** inicia la **semana subsiguiente**.
4. Si la configuración **"permitir solicitudes fuera del límite"** está activa (por defecto, desactivada), el cliente puede enviar la solicitud después del límite y el **administrador decide** si entra en la semana siguiente (caso de uso *Aprobar solicitud fuera de límite*). La decisión queda registrada (quién y cuándo) y se notifica al cliente.
5. La fecha de inicio siempre se ajusta al primer **día hábil** de la semana que corresponda ([[RN_Festivos_y_Agenda]]).

## Configuración ([[DB_Tabla_Configuraciones_Sistema]])
| Clave | Valor por defecto |
| :--- | :--- |
| `dia_limite_suscripcion` | domingo |
| `hora_limite_suscripcion` | 17:00 |
| `horas_gracia_pago` | 15 |
| `solicitudes_fuera_limite_activas` | false |

## Datos ([[DB_Tabla_Suscripciones]])
`fecha_solicitud`, `fuera_de_limite`, `aprobacion_fuera_limite`, `aprobada_por_usuario_id`.
