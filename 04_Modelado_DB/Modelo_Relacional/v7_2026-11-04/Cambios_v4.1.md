# Modelo relacional v4.1 — notas de revisión (2026-11-04)

Cambios pedidos en las notas del visor (https://claude.ai/artifact/61mqHjLZm1YSZAVvvoqy8t). Parte de la v4.0 ([Cambios_v4.0.md](../v6_2026-11-04/Cambios_v4.0.md)).

Resultado: **38 tablas, 55 relaciones**, máximo 12 columnas por tabla.

## Tablas eliminadas

| Tabla | Motivo |
| :--- | :--- |
| `historial_configuraciones` | Solo servía para consultar el historial de cambios de configuración; ningún proceso la usa. |
| `tipos_recipiente` | Repetía la categoría del producto: la categoría ya es la coca (Seco, Sopa, Ensalada, Bebida). |
| `menu_alternativas` | Integrada en menu_items con restriccion y reemplaza_item_id. |

## Campos que cambian

| Tabla | Antes | Ahora |
| :--- | :--- | :--- |
| `categorias_productos` | `tipo_recipiente_id` | Se elimina: la categoría es la coca (Seco, Sopa, Ensalada, Bebida). |
| `recipientes` | `tipo_recipiente_id` | `categoria_producto_id` (qué pieza del juego es). |
| `menu_items` | `tipo_recipiente_id` | Se elimina: la coca sale de la categoría del producto. |
| `menu_items` | — | `restriccion` (vacío = plato base) y `reemplaza_item_id` (plato base que reemplaza la alternativa). |

## Se mantiene

- `juegos_cocas` y `recipientes`, para la trazabilidad de cocas por cliente.

## Menú en 3 tablas

`menus_semana` (publicación de la semana) → `menus_diarios` (menú de cada día hábil) → `menu_items` (platos del día y sus alternativas). Ejemplo: el chicharrón es plato base; el pollo a la plancha es su alternativa para clientes con restricción `cerdo`.

## Pendiente en cascada

- Story Mapping: quitar la HU "Consultar historial de cambios" (Configuraciones del sistema).
- Ficha, manual técnico y documentación de casos de uso: actualizar campos y tablas de v4.0 y v4.1.
- Avisar al agente del frontend en el chat de Drive.
