# Macro-Proceso: Compras e Inventario

Administración de insumos, categorías de insumos, productos, proveedores y órdenes de compra.

## Subprocesos Integrados

### Subproceso: CATEGORIA DE INSUMOS
- **Total de Casos de Uso / Acciones:** 7
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Crear categoría de insumo
2. Listar categorías de insumos
3. Ver detalle de la categoría
4. Editar categoría
5. Eliminar categoria de insumos
6. Cambiar estado de la categoría de insumos
7. Filtrar / consultar categorías por nombre, estado

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "CATEGORIA DE INSUMOS" {
  usecase "Gestión de categoria de insumos" as UC_Main
  usecase "Crear categoría de insumo" as UC_1
  usecase "Listar categorías de insumos" as UC_2
  usecase "Ver detalle de la categoría" as UC_3
  usecase "Editar categoría" as UC_4
  usecase "Eliminar categoria de insumos" as UC_5
  usecase "Cambiar estado de la categoría de insumos" as UC_6
  usecase "Filtrar / consultar categorías por nombre, estado" as UC_7
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

### Subproceso: INSUMOS
- **Total de Casos de Uso / Acciones:** 12
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Crear insumo
2. Listar insumos
3. Ver detalle del insumo
4. Editar insumo
5. Cambiar estado del insumo
6. Consultar movimientos de inventario
7. Consultar existencias
8. Consultar alertas de stock mínimo
9. Generar reporte de inventario
10. Generar reporte de consumo por período
11. Generar reporte de alertas de reabastecimiento
12. Filtrar / consultar insumos por nombre, categoría, proveedor, estado

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "INSUMOS" {
  usecase "Gestión de insumos" as UC_Main
  usecase "Crear insumo" as UC_1
  usecase "Listar insumos" as UC_2
  usecase "Ver detalle del insumo" as UC_3
  usecase "Editar insumo" as UC_4
  usecase "Cambiar estado del insumo" as UC_5
  usecase "Consultar movimientos de inventario" as UC_6
  usecase "Consultar existencias" as UC_7
  usecase "Consultar alertas de stock mínimo" as UC_8
  usecase "Generar reporte de inventario" as UC_9
  usecase "Generar reporte de consumo por período" as UC_10
  usecase "Generar reporte de alertas de reabastecimiento" as UC_11
  usecase "Filtrar / consultar insumos por nombre, categoría, proveedor, estado" as UC_12
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
@enduml
```

---

### Subproceso: CATEGORIA PRODUCTOS
- **Total de Casos de Uso / Acciones:** 6
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Crear categoría de producto
2. Listar categorías de productos
3. Ver detalle de categoría
4. Editar categoría
5. Cambiar estado de la categoria del producto
6. Filtrar / consultar categorías por nombre, estado

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "CATEGORIA PRODUCTOS" {
  usecase "Gestión de categoria productos" as UC_Main
  usecase "Crear categoría de producto" as UC_1
  usecase "Listar categorías de productos" as UC_2
  usecase "Ver detalle de categoría" as UC_3
  usecase "Editar categoría" as UC_4
  usecase "Cambiar estado de la categoria del producto" as UC_5
  usecase "Filtrar / consultar categorías por nombre, estado" as UC_6
}
admin --> UC_Main
UC_1 ..> UC_Main : <<extends>>
UC_2 ..> UC_Main : <<extends>>
UC_3 ..> UC_Main : <<extends>>
UC_4 ..> UC_Main : <<extends>>
UC_5 ..> UC_Main : <<extends>>
UC_6 ..> UC_Main : <<extends>>
@enduml
```

---

### Subproceso: PRODUCTOS
- **Total de Casos de Uso / Acciones:** 10
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Crear producto
2. Listar productos
3. Ver detalle del producto
4. Editar producto
5. Cambiar estado del producto
6. Filtrar / consultar productos por nombre, categoría, estado
7. Consultar insumos requeridos
8. Consultar especificaciones de preparación
9. Generar reporte de productos activos
10. Consultar costo unitario estimado

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "PRODUCTOS" {
  usecase "Gestión de productos" as UC_Main
  usecase "Crear producto" as UC_1
  usecase "Listar productos" as UC_2
  usecase "Ver detalle del producto" as UC_3
  usecase "Editar producto" as UC_4
  usecase "Cambiar estado del producto" as UC_5
  usecase "Filtrar / consultar productos por nombre, categoría, estado" as UC_6
  usecase "Consultar insumos requeridos" as UC_7
  usecase "Consultar especificaciones de preparación" as UC_8
  usecase "Generar reporte de productos activos" as UC_9
  usecase "Consultar costo unitario estimado" as UC_10
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

### Subproceso: PROVEEDORES
- **Total de Casos de Uso / Acciones:** 9
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Crear proveedor
2. Listar proveedores
3. Ver detalle del proveedor
4. Editar proveedor
5. Cambiar estado del proveedor
6. Filtrar / consultar proveedores por nombre, documento, categoría, estado
7. Consultar productos o insumos suministrados
8. Consultar historial de compras
9. Generar reporte de historial de compras

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "PROVEEDORES" {
  usecase "Gestión de proveedores" as UC_Main
  usecase "Crear proveedor" as UC_1
  usecase "Listar proveedores" as UC_2
  usecase "Ver detalle del proveedor" as UC_3
  usecase "Editar proveedor" as UC_4
  usecase "Cambiar estado del proveedor" as UC_5
  usecase "Filtrar / consultar proveedores por nombre, documento, categoría, estado" as UC_6
  usecase "Consultar productos o insumos suministrados" as UC_7
  usecase "Consultar historial de compras" as UC_8
  usecase "Generar reporte de historial de compras" as UC_9
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
@enduml
```

---

### Subproceso: COMPRAS
- **Total de Casos de Uso / Acciones:** 10
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Crear compra
2. Listar compras
3. Ver detalle de compra
4. Editar compra
5. Cambiar estado de compra
6. Anular compra
7. Filtrar / consultar compras por proveedor, fecha, insumo, estado
8. Generar reporte de compras por período
9. Generar reporte de compras por proveedor
10. Generar reporte de compras por insumo

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "COMPRAS" {
  usecase "Gestión de compras" as UC_Main
  usecase "Crear compra" as UC_1
  usecase "Listar compras" as UC_2
  usecase "Ver detalle de compra" as UC_3
  usecase "Editar compra" as UC_4
  usecase "Cambiar estado de compra" as UC_5
  usecase "Anular compra" as UC_6
  usecase "Filtrar / consultar compras por proveedor, fecha, insumo, estado" as UC_7
  usecase "Generar reporte de compras por período" as UC_8
  usecase "Generar reporte de compras por proveedor" as UC_9
  usecase "Generar reporte de compras por insumo" as UC_10
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
