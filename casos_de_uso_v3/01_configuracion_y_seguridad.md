# Macro-Proceso: Configuración y Seguridad

Gestión de roles, permisos, usuarios y mecanismos de autenticación/acceso al sistema.

## Subprocesos Integrados

### Subproceso: ROLES
- **Total de Casos de Uso / Acciones:** 7
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Crear rol
2. Listar roles
3. Ver detalle del rol y permisos configurados
4. Editar  rol
5. Asignar permisos al rol
6. Cambiar estado del rol
7. Eliminar rol

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "ROLES" {
  usecase "Gestión de roles" as UC_Main
  usecase "Crear rol" as UC_1
  usecase "Listar roles" as UC_2
  usecase "Ver detalle del rol y permisos configurados" as UC_3
  usecase "Editar  rol" as UC_4
  usecase "Asignar permisos al rol" as UC_5
  usecase "Cambiar estado del rol" as UC_6
  usecase "Eliminar rol" as UC_7
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

### Subproceso: PERMISOS
- **Total de Casos de Uso / Acciones:** 6
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Crear permiso
2. Listar permisos
3. Ver detalle del permiso
4. Editar permiso
5. Cambiar estado del permiso
6. Eliminar permiso

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "PERMISOS" {
  usecase "Gestión de permisos" as UC_Main
  usecase "Crear permiso" as UC_1
  usecase "Listar permisos" as UC_2
  usecase "Ver detalle del permiso" as UC_3
  usecase "Editar permiso" as UC_4
  usecase "Cambiar estado del permiso" as UC_5
  usecase "Eliminar permiso" as UC_6
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

### Subproceso: USUARIOS
- **Total de Casos de Uso / Acciones:** 7
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Crear usuario
2. Listar usuarios
3. Ver detalle de usuario
4. Editar usuario
5. Cambiar estado de usuario
6. Generar reportes de usuarios activos e inactivos
7. Eliminar usuario

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "USUARIOS" {
  usecase "Gestión de usuarios" as UC_Main
  usecase "Crear usuario" as UC_1
  usecase "Listar usuarios" as UC_2
  usecase "Ver detalle de usuario" as UC_3
  usecase "Editar usuario" as UC_4
  usecase "Cambiar estado de usuario" as UC_5
  usecase "Generar reportes de usuarios activos e inactivos" as UC_6
  usecase "Eliminar usuario" as UC_7
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

### Subproceso: ACCESO
- **Total de Casos de Uso / Acciones:** 5
- **Actor Principal:** Administrador / Rol correspondiente

#### Listado de Casos de Uso
1. Iniciar sesión
2. Validar credenciales
3. Recuperar / restablecer  contraseña
4. Consultar estado de la cuenta
5. Cerrar sesión

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Administrador" as admin
package "ACCESO" {
  usecase "Gestión de acceso" as UC_Main
  usecase "Iniciar sesión" as UC_1
  usecase "Validar credenciales" as UC_2
  usecase "Recuperar / restablecer  contraseña" as UC_3
  usecase "Consultar estado de la cuenta" as UC_4
  usecase "Cerrar sesión" as UC_5
}
admin --> UC_Main
UC_1 ..> UC_Main : <<extends>>
UC_2 ..> UC_Main : <<extends>>
UC_3 ..> UC_Main : <<extends>>
UC_4 ..> UC_Main : <<extends>>
UC_5 ..> UC_Main : <<extends>>
@enduml
```

---
