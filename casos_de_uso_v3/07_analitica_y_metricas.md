# Macro-Proceso: Analítica y Métricas

Tablero de control (Dashboard), consulta de KPIs, métricas e indicadores de rendimiento.

## Subprocesos Integrados

### Subproceso: DASHBOARD
- **Total de Casos de Uso / Acciones:** 20
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Consultar ingresos por tipo de plan
2. Consultar conversión por modalidad de venta
3. Consultar impacto del menú personalizado
4. Consultar estado de comprobantes de transferencia
5. Consultar proyección diaria de almuerzos
6. Consultar restricciones alimentarias
7. Consultar consumo de insumos
8. Consultar entregas completadas
9. Consultar entregas pendientes
10. Consultar desempeño de domiciliarios
11. Consultar inventario de cocas en rotación
12. Consultar incidencias de ruta
13. Consultar margen de rentabilidad por tipo de plan
14. Consultar tasa de retención de clientes
15. Consultar tasa de deserción de clientes
16. Consultar costo-beneficio logístico por zona
17. Consultar proyección de crecimiento
18. Consultar capacidad máxima de producción
19. Filtrar / consultar información por rango de fechas, zona, plan
20. Exportar informes estratégicos

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "DASHBOARD" {
  usecase "Gestión de dashboard" as UC_Main
  usecase "Consultar ingresos por tipo de plan" as UC_1
  usecase "Consultar conversión por modalidad de venta" as UC_2
  usecase "Consultar impacto del menú personalizado" as UC_3
  usecase "Consultar estado de comprobantes de transferencia" as UC_4
  usecase "Consultar proyección diaria de almuerzos" as UC_5
  usecase "Consultar restricciones alimentarias" as UC_6
  usecase "Consultar consumo de insumos" as UC_7
  usecase "Consultar entregas completadas" as UC_8
  usecase "Consultar entregas pendientes" as UC_9
  usecase "Consultar desempeño de domiciliarios" as UC_10
  usecase "Consultar inventario de cocas en rotación" as UC_11
  usecase "Consultar incidencias de ruta" as UC_12
  usecase "Consultar margen de rentabilidad por tipo de plan" as UC_13
  usecase "Consultar tasa de retención de clientes" as UC_14
  usecase "Consultar tasa de deserción de clientes" as UC_15
  usecase "Consultar costo-beneficio logístico por zona" as UC_16
  usecase "Consultar proyección de crecimiento" as UC_17
  usecase "Consultar capacidad máxima de producción" as UC_18
  usecase "Filtrar / consultar información por rango de fechas, zona, plan" as UC_19
  usecase "Exportar informes estratégicos" as UC_20
}
admin --> UC_Main
UC_1 ..> UC_Main : <<extends>>
UC_2 ..> UC_Main : <<extends>>
UC_3 ..> UC_Main : <<extends>>
UC_4 ..> UC_Main : <<extends>>
UC_5 ..> UC_Main : <<extends>>
UC_6 ..> UC_Main : <<extends>>
UC_7 ..> UC_Main : <<extends>>
UC_8 ..> UC_Main : <<extends>>
UC_9 ..> UC_Main : <<extends>>
UC_10 ..> UC_Main : <<extends>>
UC_11 ..> UC_Main : <<extends>>
UC_12 ..> UC_Main : <<extends>>
UC_13 ..> UC_Main : <<extends>>
UC_14 ..> UC_Main : <<extends>>
UC_15 ..> UC_Main : <<extends>>
UC_16 ..> UC_Main : <<extends>>
UC_17 ..> UC_Main : <<extends>>
UC_18 ..> UC_Main : <<extends>>
UC_19 ..> UC_Main : <<extends>>
UC_20 ..> UC_Main : <<extends>>
@enduml
```

---
