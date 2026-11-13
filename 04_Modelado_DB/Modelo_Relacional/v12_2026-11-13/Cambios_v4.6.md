# Modelo relacional v4.6: permisos de vuelta (2026-11-13)

Antes: [Cambios_v4.5.md](../v11_2026-11-04/Cambios_v4.5.md).

Resultado: **39 tablas y 53 relaciones**, todas con 12 columnas o menos.

Alejandro decidió en el visor del modelo (nota sobre `roles`, 11-nov) que vuelven los permisos. Estaban fuera del alcance desde la v3.4. Se aplicaron el 13-nov sin esperar el acuerdo del grill G2 con Claude Omar, porque su pregunta sobre permisos (G2-Q1) solo define cómo los muestra el panel, y eso no cambia las tablas.

| Cambio | Detalle |
| :--- | :--- |
| Nueva tabla `permisos` | `id`, `modulo` (subproceso del Story Mapping), `accion` (enum nuevo `accion_permiso`: ver, crear, editar, cambiar_estado) y `estado`. Índice único `(modulo, accion)`. El nombre que se muestra se arma con módulo + acción. |
| Nueva tabla `rol_permisos` | Tabla puente: llave compuesta `(rol_id, permiso_id)`, con referencias a `roles` y `permisos`. |
| `roles` | Su nota quita "Permisos está fuera del alcance" y agrega las HU "Asignar permisos al rol" y "Consultar permisos del rol". |
| Proceso | Las dos tablas van en P1 · Acceso y seguridad. |

El resto de lo decidido en los grills G1 y G2 (alérgenos, imagen del producto, cantidad planificada en la orden, renombres, frutos secos y huevo, bloqueo en el backend) se aplicará como **v4.7** cuando Claude Omar confirme los acuerdos.
