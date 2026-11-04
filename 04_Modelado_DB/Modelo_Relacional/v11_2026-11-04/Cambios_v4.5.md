# Modelo relacional v4.5 (2026-11-04)

Antes: [Cambios_v4.4.md](../v10_2026-11-04/Cambios_v4.4.md).

**Resultado:** 37 tablas y 51 relaciones.

| Campo | Decisión | Motivo |
| :--- | :--- | :--- |
| `producto_terminado.responsable_id` | **Sale** (había vuelto en la v4.4). | La cocina trabaja en equipo y ningún reporte necesita saber quién hizo cada línea. Se aplica la regla Q1: solo se guarda quién hizo algo en pagos e incidencias. Hay que avisar al PO, porque lo había pedido el 2-nov. |
| `producto_terminado.motivo` | **Se mantiene.** | Es obligatorio al anular una línea, como pidió el PO. |
