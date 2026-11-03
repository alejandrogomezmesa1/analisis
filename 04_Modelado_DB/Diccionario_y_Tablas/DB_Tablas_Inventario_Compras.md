---
title: "DB-08: Tablas de Inventario, Proveedores, Compras y Fichas Técnicas"
type: Modelo_DB
tags:
  - base-de-datos
  - inventario
  - compras
  - proveedores
  - fichas-tecnicas
  - dbml
aliases:
  - Tablas Inventario Compras
  - DB Cadena Abastecimiento
related:
  - "[[00_MOC_Modelo_DB]]"
  - "[[PROC_Planeacion_Cocina_y_Recetas]]"
  - "[[CU_02_Compras_e_Inventario]]"
  - "[[CU_03_Produccion_y_Recetas]]"
---

# 🗄️ DB-08: Tablas de Inventario, Proveedores, Compras y Fichas Técnicas

## 📌 Descripción de la Cadena de Abastecimiento
Este grupo de tablas gestiona la materia prima (insumos), los proveedores asociados, las órdenes de compra, la definición de recetas (fichas técnicas) y la ejecución diaria en cocina (órdenes de producción).

---

## 📐 Estructura de Tablas (DBML)

```dbml
Table categoria_insumos {
  id int [pk, increment]
  nombre varchar(100) [not null]
  estado estado_general [default: 'activo']
}

Table insumos {
  id int [pk, increment]
  categoria_id int [ref: > categoria_insumos.id]
  nombre varchar(100) [not null]
  unidad_medida varchar(20) [not null]
  stock_disponible decimal(10,2) [default: 0]
  stock_minimo decimal(10,2) [default: 0]
  precio_unitario decimal(10,2) [not null]
  estado estado_general [default: 'activo']
}

Table proveedores {
  id int [pk, increment]
  razon_social varchar(150) [not null]
  nit_documento varchar(20) [unique, not null]
  contacto_nombre varchar(100)
  telefono varchar(20)
  direccion varchar(255)
  estado estado_general [default: 'activo']
}

Table compras {
  id int [pk, increment]
  proveedor_id int [ref: > proveedores.id]
  fecha_compra date [not null]
  valor_total decimal(12,2) [not null]
  estado estado_compra [default: 'pendiente']
  created_at timestamp [default: `current_timestamp`]
}

Table productos {
  id int [pk, increment]
  nombre varchar(100) [not null]
  descripcion text
  precio_estimado decimal(10,2)
  estado estado_general [default: 'activo']
}

Table fichas_tecnicas {
  id int [pk, increment]
  producto_id int [ref: > productos.id]
  procedimiento text
  tiempo_preparacion_min int
  porciones_rendimiento int [default: 1]
  costo_unitario_estimado decimal(10,2)
  estado estado_general [default: 'activo']
}

Table ficha_tecnica_detalle {
  ficha_tecnica_id int [ref: > fichas_tecnicas.id]
  insumo_id int [ref: > insumos.id]
  cantidad_requerida decimal(10,2) [not null]
  indexes {
    (ficha_tecnica_id, insumo_id) [pk]
  }
}
```

---

## 🔗 Conexión con Reglas y Procesos
* Abastece la materia prima requerida en [[PROC_Planeacion_Cocina_y_Recetas]].
* Sombra las funciones de los módulos [[CU_02_Compras_e_Inventario]] y [[CU_03_Produccion_y_Recetas]].
