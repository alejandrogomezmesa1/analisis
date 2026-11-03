---
title: "PROC-04: Despacho, Distribución y Rotación de Recipientes en Ruta"
type: Proceso
tags:
  - proceso
  - despacho
  - distribucion
  - ruta
  - cocas
aliases:
  - Proceso de Despacho
  - Logistica de Entregas
related:
  - "[[00_MOC_Procesos]]"
  - "[[RN_Logistica_Cocas]]"
  - "[[RN_Domiciliarios_y_Rutas]]"
  - "[[DB_Tabla_Ruta_Clientes]]"
  - "[[DB_Tabla_Geolocalizacion]]"
  - "[[CU_06_Logistica_y_Domicilios]]"
---

# 🛵 PROC-04: Despacho, Distribución y Rotación de Recipientes en Ruta

## 📌 Resumen del Proceso
El proceso de Despacho y Distribución abarca desde la salida de los paquetes empacados desde la cocina hasta la entrega física en la puerta del cliente. Gestiona la asignación de rutas por zona, el ordenamiento óptimo de paradas, la transmisión GPS en vivo del repartidor y el intercambio físico de recipientes reutilizables.

---

## 🔄 Flujo Operativo en Ruta (Franja 11:30 AM - 1:30 PM)

```mermaid
flowchart TD
    PACK["Cocina empaca almuerzos calientes\nen cocas oficiales rotuladas con restricciones"] --> GROUP["Administrador agrupa pedidos por polígonos de zona\ny asigna repartidor en [[DB_Tabla_Ruta_Clientes]]"]

    GROUP --> MOBILE["Domiciliario inicia ruta en App Móvil:\nVisualiza lista ordenada de paradas"]

    MOBILE --> GPS["App activa geolocalización en tiempo real:\nTransmite coordenadas a [[DB_Tabla_Geolocalizacion]]"]

    GPS --> PARADA["Domiciliario llega a la dirección del cliente"]

    PARADA --> INTER["1. Entrega coca llena del día\n2. Recoge coca vacía del día anterior"]

    INTER --> CHECK{"¿El intercambio fue correcto\nsin novedades?"}

    CHECK -- Sí --> CONFIRM["Registra cocas_entregadas=1, cocas_recogidas=1\nEstado parada -> 'entregado'"]
    CHECK -- No --> INCIDENCIA["Registra novedad en App:\n(Cliente ausente / Coca dañada / No entrega)\nPasa a [[PROC_Gestion_Incidencias]]"]

    CONFIRM --> NEXT{"¿Faltan clientes en la ruta?"}
    NEXT -- Sí --> PARADA
    NEXT -- No --> END["Finaliza jornada:\nRetorna a cocina con cocas vacías recogidas"]
```

---

## 📊 Matriz de Entregables de la Ruta
* **Almuerzo Caliente Empacado**: Rotulado con el nombre del cliente y alergias especificadas.
* **Confirmación Digital**: Timestamp y coordenadas del momento del despacho.
* **Control de Inventario Físico de Cocas**: Balance actualizado en el sistema al cerrar el recorrido.

---

## 🔗 Vinculación con Reglas de Negocio
* Se rige por las políticas de rotación de envases de [[RN_Logistica_Cocas]].
* Aplica las restricciones de zonas de geofencing descritas en [[RN_Domiciliarios_y_Rutas]].
* Alimenta las entidades [[DB_Tabla_Ruta_Clientes]] y [[DB_Tabla_Geolocalizacion]].
