# Macro-Proceso: Producción y Recetas

Gestión de personal de producción, órdenes de producción, fichas técnicas y producto terminado.

## Subprocesos Integrados

### Subproceso: EMPLEADOS
- **Total de Casos de Uso / Acciones:** 7
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Crear empleado
2. Listar empleados
3. Ver detalle del empleado
4. Editar empleado
5. Cambiar estado de empleados
6. Filtrar / consultar empleados por nombre, documento, cargo, estado
7. Generar reporte de empleados activos por área

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "EMPLEADOS" {
  usecase "Gestión de empleados" as UC_Main
  usecase "Crear empleado" as UC_1
  usecase "Listar empleados" as UC_2
  usecase "Ver detalle del empleado" as UC_3
  usecase "Editar empleado" as UC_4
  usecase "Cambiar estado de empleados" as UC_5
  usecase "Filtrar / consultar empleados por nombre, documento, cargo, estado" as UC_6
  usecase "Generar reporte de empleados activos por área" as UC_7
}
admin --> UC_Main
UC_1 ..> UC_Main : <<extends>>
UC_2 ..> UC_Main : <<extends>>
UC_3 ..> UC_Main : <<extends>>
UC_4 ..> UC_Main : <<extends>>
UC_5 ..> UC_Main : <<extends>>
UC_6 ..> UC_Main : <<extends>>
UC_7 ..> UC_Main : <<extends>>
@enduml
```

---

### Subproceso: PRODUCCION
- **Total de Casos de Uso / Acciones:** 7
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Crear orden de producción
2. Listar órdenes de producción
3. Ver detalle de orden de produccion
4. Editar orden de producción
5. Cambiar estado de orden de produccion
6. Filtrar / consultar órdenes por cantidad, fecha, restricciones y alergias
7. Consultar insumos requeridos

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "PRODUCCION" {
  usecase "Gestión de produccion" as UC_Main
  usecase "Crear orden de producción" as UC_1
  usecase "Listar órdenes de producción" as UC_2
  usecase "Ver detalle de orden de produccion" as UC_3
  usecase "Editar orden de producción" as UC_4
  usecase "Cambiar estado de orden de produccion" as UC_5
  usecase "Filtrar / consultar órdenes por cantidad, fecha, restricciones y alergias" as UC_6
  usecase "Consultar insumos requeridos" as UC_7
}
admin --> UC_Main
UC_1 ..> UC_Main : <<extends>>
UC_2 ..> UC_Main : <<extends>>
UC_3 ..> UC_Main : <<extends>>
UC_4 ..> UC_Main : <<extends>>
UC_5 ..> UC_Main : <<extends>>
UC_6 ..> UC_Main : <<extends>>
UC_7 ..> UC_Main : <<extends>>
@enduml
```

---

### Subproceso: FICHA TECNICA PRODUCTO
- **Total de Casos de Uso / Acciones:** 14
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Crear ficha técnica
2. Listar fichas técnicas
3. Ver detalle de ficha técnica
4. Editar ficha técnica
5. Cambiar estado de la ficha tecnica
6. Registrar insumos requeridos
7. Registrar cantidades exactas de insumos
8. Registrar tiempo estimado de preparación
9. Registrar procedimiento de elaboración
10. Registrar número de porciones
11. Consultar costo unitario estimado
12. Filtrar / consultar fichas por producto, insumo, estado
13. Generar reporte de fichas técnicas
14. Generar reporte de costo unitario estimado

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "FICHA TECNICA PRODUCTO" {
  usecase "Gestión de ficha tecnica producto" as UC_Main
  usecase "Crear ficha técnica" as UC_1
  usecase "Listar fichas técnicas" as UC_2
  usecase "Ver detalle de ficha técnica" as UC_3
  usecase "Editar ficha técnica" as UC_4
  usecase "Cambiar estado de la ficha tecnica" as UC_5
  usecase "Registrar insumos requeridos" as UC_6
  usecase "Registrar cantidades exactas de insumos" as UC_7
  usecase "Registrar tiempo estimado de preparación" as UC_8
  usecase "Registrar procedimiento de elaboración" as UC_9
  usecase "Registrar número de porciones" as UC_10
  usecase "Consultar costo unitario estimado" as UC_11
  usecase "Filtrar / consultar fichas por producto, insumo, estado" as UC_12
  usecase "Generar reporte de fichas técnicas" as UC_13
  usecase "Generar reporte de costo unitario estimado" as UC_14
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
@enduml
```

---

### Subproceso: PRODUCTO TERMINADO
- **Total de Casos de Uso / Acciones:** 10
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Registrar producto terminado
2. Listar productos terminados
3. Ver detalle del producto terminado
4. Registrar cantidad producida
5. Registrar fecha de elaboración
6. Asociar orden de producción
7. Filtrar / consultar por fecha, producto, estado
8. Generar reporte de producción diaria
9. Generar reporte de producción semanal
10. Generar reporte de producción mensual

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "PRODUCTO TERMINADO" {
  usecase "Gestión de producto terminado" as UC_Main
  usecase "Registrar producto terminado" as UC_1
  usecase "Listar productos terminados" as UC_2
  usecase "Ver detalle del producto terminado" as UC_3
  usecase "Registrar cantidad producida" as UC_4
  usecase "Registrar fecha de elaboración" as UC_5
  usecase "Asociar orden de producción" as UC_6
  usecase "Filtrar / consultar por fecha, producto, estado" as UC_7
  usecase "Generar reporte de producción diaria" as UC_8
  usecase "Generar reporte de producción semanal" as UC_9
  usecase "Generar reporte de producción mensual" as UC_10
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
@enduml
```

---
