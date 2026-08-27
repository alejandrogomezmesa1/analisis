# Macro-Proceso: Servicios y Operación

Definición de servicios, categorías de servicios y programación de calendario operativo.

## Subprocesos Integrados

### Subproceso: CATEGORIA DE SERVICIOS
- **Total de Casos de Uso / Acciones:** 6
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Crear categoría de servicio
2. Listar categorías de servicios
3. Ver detalle de categoría
4. Editar categoría
5. Cambiar el estado de la categoria
6. Filtrar / consultar categorías por nombre, estado

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "CATEGORIA DE SERVICIOS" {
  usecase "Gestión de categoria de servicios" as UC_Main
  usecase "Crear categoría de servicio" as UC_1
  usecase "Listar categorías de servicios" as UC_2
  usecase "Ver detalle de categoría" as UC_3
  usecase "Editar categoría" as UC_4
  usecase "Cambiar el estado de la categoria" as UC_5
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

### Subproceso: SERVICIO
- **Total de Casos de Uso / Acciones:** 11
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Crear servicio
2. Listar servicios
3. Ver detalle del servicio
4. Editar servicio
5. Cambiar el estado del servicio
6. Registrar nombre del plan
7. Registrar tipo de plan
8. Registrar descripción
9. Registrar valor
10. Registrar duración en días
11. Filtrar / consultar servicios por nombre, tipo, estado

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "SERVICIO" {
  usecase "Gestión de servicio" as UC_Main
  usecase "Crear servicio" as UC_1
  usecase "Listar servicios" as UC_2
  usecase "Ver detalle del servicio" as UC_3
  usecase "Editar servicio" as UC_4
  usecase "Cambiar el estado del servicio" as UC_5
  usecase "Registrar nombre del plan" as UC_6
  usecase "Registrar tipo de plan" as UC_7
  usecase "Registrar descripción" as UC_8
  usecase "Registrar valor" as UC_9
  usecase "Registrar duración en días" as UC_10
  usecase "Filtrar / consultar servicios por nombre, tipo, estado" as UC_11
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
@enduml
```

---

### Subproceso: CALENDARIO
- **Total de Casos de Uso / Acciones:** 10
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Parametrizar calendario operativo
2. Listar calendario operativo
3. Identificar días hábiles
4. Registrar días festivos nacionales
5. Identificar jornadas no operativas
6. Cruzar agenda con suscripciones activas
7. Programar producción diaria
8. Calcular días de servicio
9. Calcular fechas de vencimiento
10. Generar información para liquidación proporcional

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "CALENDARIO" {
  usecase "Gestión de calendario" as UC_Main
  usecase "Parametrizar calendario operativo" as UC_1
  usecase "Listar calendario operativo" as UC_2
  usecase "Identificar días hábiles" as UC_3
  usecase "Registrar días festivos nacionales" as UC_4
  usecase "Identificar jornadas no operativas" as UC_5
  usecase "Cruzar agenda con suscripciones activas" as UC_6
  usecase "Programar producción diaria" as UC_7
  usecase "Calcular días de servicio" as UC_8
  usecase "Calcular fechas de vencimiento" as UC_9
  usecase "Generar información para liquidación proporcional" as UC_10
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
