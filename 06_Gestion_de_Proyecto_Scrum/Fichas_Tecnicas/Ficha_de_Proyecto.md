---
title: "Ficha Técnica de Proyecto — JackSoft (SENA ADSO 3312824)"
type: Scrum
tags:
  - ficha-proyecto
  - sena
  - adso
  - clientes
  - objetivos
aliases:
  - Ficha de Proyecto
  - Ficha SENA 3312824
related:
  - "[[00_MOC_Gestion_Proyecto]]"
  - "[[Planteamiento_del_Problema]]"
  - "[[Arbol_de_Objetivos]]"
  - "[[Scrum_Artefactos_y_Sprints]]"
---

# 📄 Ficha Técnica de Proyecto — JackSoft (SENA ADSO)

## 📌 Información General

| Campo | Detalle Institucional |
| :--- | :--- |
| **Nombre del Aplicativo** | **JackSoft** |
| **Cliente / Empresa** | La Coca de Jacks S.A.S. (Representante: Richard Daniel Ortiz) |
| **Ubicación** | Calle 27 # 65 B - 40, Medellín, Antioquia |
| **Contacto Cliente** | lacocadejacksmed@gmail.com / Tel: 3116437887 |
| **Programa de Formación** | Tecnología en Análisis y Desarrollo de Software (ADSO) |
| **Número de Ficha** | **3312824** |
| **Instructor Titular** | NEWTON WILLARD POMARE |
| **Sector** | Economía Popular / Servicio Gastronómico por Suscripción |

---

## 👥 Aprendices Participantes

| Documento ID | Nombre Completo | Correo Electrónico | Teléfono |
| :---: | :--- | :--- | :---: |
| 1000899884 | Alejandro Gomez Mesa | alejandrogomezmesa1@gmail.com | 3016845559 |
| 1066598600 | Omar David Meneses Verona | ODMV36335917@soy.sena.edu.co | 3026406048 |
| 1003540637 | Erick Santiago Camargo | camargosantiago78@gmail.com | 3203157261 |
| 1025649345 | Luis Gabriel Mesa | mesluis702@gmail.com | 3213939084 |
| 1023630420 | Samuel Morales Marin | samuelmarinmorales@gmail.com | 3182531805 |

---

## 🎯 Objetivos del Proyecto

### Objetivo General
Desarrollar un sistema web y móvil que gestione los procesos de configuración, usuarios, compras, producción, servicios, ventas y logística de la compañía, administrando roles, módulos, zonas de cobertura geográfica y capacidad de producción estipuladas para el servicio de alimentación por suscripción según las reglas de negocio de **La Coca de Jacks S.A.S.**.

### Objetivos Específicos
1. Gestionar la configuración de los roles y de los parámetros del sistema de acuerdo con las reglas de negocio de la empresa ([[CU_01_Configuracion_y_Seguridad]]).
2. Gestionar las cuentas de usuarios de acuerdo con la seguridad del aplicativo.
3. Gestionar las compras de insumos a proveedores de acuerdo a las necesidades de la empresa ([[CU_02_Compras_e_Inventario]]).
4. Gestionar el proceso de producción (fichas técnicas) de acuerdo a las necesidades operativas ([[CU_03_Produccion_y_Recetas]]).
5. Gestionar los servicios y la agenda operativa de acuerdo a la oferta del establecimiento ([[CU_04_Servicios_y_Operacion]]).
6. Gestionar las ventas, suscripciones, menús y pagos de acuerdo a las políticas de la empresa ([[CU_05_Clientes_y_Ventas]]).
7. Gestionar la medición y desempeño de los procesos (Dashboard KPIs) de acuerdo a los requerimientos del cliente ([[CU_07_Analitica_y_Metricas]]).

---

## 🔗 Relaciones con el Sistema
* Define el marco institucional que guía los 11 Sprints descritos en [[Scrum_Artefactos_y_Sprints]].
* Articula las decisiones diagnósticas abordadas en [[Planteamiento_del_Problema]] y el [[Arbol_de_Objetivos]].

## 🧭 Alcance vigente (Ficha v8 — Cambio de alcance 2026-11-02)

| Proceso | Subprocesos web |
| :--- | :--- |
| Configuración | Roles · **Configuraciones del sistema** (incluye el cierre semanal de suscripciones) |
| Usuarios | Gestión de usuarios · Gestión de acceso |
| Compras | Categoría de insumos · Insumos · Categoría de productos · Productos · Proveedores · Compras |
| Producción | Orden de producción · Ficha técnica · Producto terminado |
| Servicios | Servicios · Categoría de servicios · Agenda |
| Ventas | Clientes · Suscripciones · **Menú** |
| Logística | Rutas y domiciliarios · Monitoreo en tiempo real · Incidencias |
| Dashboard | Medición y desempeño |

**Mobile:** Acceso · Seguimiento/renovación de suscripción · **Consulta de menú** · Seguimiento de entrega · Suspensión de entrega · Reporte de incidencias · Gestión de domiciliarios.

**Retirados:** Empleados (el personal es un usuario con rol), Permisos y Categoría de proveedor (decisión D-E).
Archivo: `Fichas_Tecnicas/v8_2026-11-02/Ficha_Jacksoft_CF_v8_alcance.docx`. Es la versión oficial vigente (la v6 tuvo el VoBo de requisitos del 10/09/2026).
