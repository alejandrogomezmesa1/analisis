# Macro-Proceso: Logística y Domicilios

Asignación de rutas y domiciliarios, rastreo en tiempo real y gestión de incidencias.

## Subprocesos Integrados

### Subproceso: RUTA Y DOMICILIARIOS
- **Total de Casos de Uso / Acciones:** 14
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Consultar clientes activos georreferenciados
2. Visualizar zonas de cobertura
3. Agrupar clientes por zona
4. Crear ruta
5. Listar rutas
6. Ver detalle de ruta
7. Editar ruta
8. Eliminar ruta
9. Asignar domiciliario a ruta
10. Reasignar domiciliario
11. Consultar clientes asociados a ruta
12. Consultar domiciliario asociado
13. Filtrar / consultar por zona, rutas, domiciliario y estado
14. Habilitar y deshabilitar entregas hibridas

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "RUTA Y DOMICILIARIOS" {
  usecase "Gestión de ruta y domiciliarios" as UC_Main
  usecase "Consultar clientes activos georreferenciados" as UC_1
  usecase "Visualizar zonas de cobertura" as UC_2
  usecase "Agrupar clientes por zona" as UC_3
  usecase "Crear ruta" as UC_4
  usecase "Listar rutas" as UC_5
  usecase "Ver detalle de ruta" as UC_6
  usecase "Editar ruta" as UC_7
  usecase "Eliminar ruta" as UC_8
  usecase "Asignar domiciliario a ruta" as UC_9
  usecase "Reasignar domiciliario" as UC_10
  usecase "Consultar clientes asociados a ruta" as UC_11
  usecase "Consultar domiciliario asociado" as UC_12
  usecase "Filtrar / consultar por zona, rutas, domiciliario y estado" as UC_13
  usecase "Habilitar y deshabilitar entregas hibridas" as UC_14
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

### Subproceso: MONITOREO DE ENTREGA TIEMPO REAL
- **Total de Casos de Uso / Acciones:** 10
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Listar ubicación de domiciliarios
2. Visualizar domiciliarios en mapa
3. Monitorear ubicación en tiempo real
4. Consultar avance de entregas
5. Consultar entregas por ruta
6. Consultar estado de rotación de cocas
7. Consultar registro de cocas recogidas
8. Filtrar / consultar por ruta, domiciliario, fecha
9. Generar reporte de entregas completadas
10. Generar reporte de entregas pendientes

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "MONITOREO DE ENTREGA TIEMPO REAL" {
  usecase "Gestión de monitoreo de entrega tiempo real" as UC_Main
  usecase "Listar ubicación de domiciliarios" as UC_1
  usecase "Visualizar domiciliarios en mapa" as UC_2
  usecase "Monitorear ubicación en tiempo real" as UC_3
  usecase "Consultar avance de entregas" as UC_4
  usecase "Consultar entregas por ruta" as UC_5
  usecase "Consultar estado de rotación de cocas" as UC_6
  usecase "Consultar registro de cocas recogidas" as UC_7
  usecase "Filtrar / consultar por ruta, domiciliario, fecha" as UC_8
  usecase "Generar reporte de entregas completadas" as UC_9
  usecase "Generar reporte de entregas pendientes" as UC_10
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

### Subproceso: INCIDENCIAS
- **Total de Casos de Uso / Acciones:** 9
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Registrar incidencia
2. Listar incidencias
3. Ver detalle de incidencia
4. Gestionar incidencia
5. Dar solución a incidencia
6. Registrar respuesta al usuario
7. Consultar estado de solución
8. Gestionar suspensión de entrega
9. Filtrar / consultar incidencias por tipo, cliente, domiciliario y estado

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "INCIDENCIAS" {
  usecase "Gestión de incidencias" as UC_Main
  usecase "Registrar incidencia" as UC_1
  usecase "Listar incidencias" as UC_2
  usecase "Ver detalle de incidencia" as UC_3
  usecase "Gestionar incidencia" as UC_4
  usecase "Dar solución a incidencia" as UC_5
  usecase "Registrar respuesta al usuario" as UC_6
  usecase "Consultar estado de solución" as UC_7
  usecase "Gestionar suspensión de entrega" as UC_8
  usecase "Filtrar / consultar incidencias por tipo, cliente, domiciliario y estado" as UC_9
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
