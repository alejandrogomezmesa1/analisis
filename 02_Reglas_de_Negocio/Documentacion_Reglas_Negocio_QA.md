# Documentación de Reglas de Negocio y Base de Datos - La Coca de Jacks
*Consolidado de preguntas y respuestas sobre la operación y el modelo relacional.*

---

### 1. Gestión de los Recipientes ("Cocas")
**¿Cómo funciona la logística física de las cocas para el negocio?**
El núcleo logístico se basa en un sistema de rotación de dos juegos de cocas por cliente (para no depender de desechables).
* Cuando se entrega el almuerzo del día en un juego lleno, el domiciliario debe recoger inmediatamente el juego vacío del día anterior.
* Si el cliente es nuevo y no tiene sus propios recipientes, el sistema le realiza un **cobro único y obligatorio de $70.000 COP** en su primera factura. En renovaciones futuras, este cobro no se vuelve a aplicar.

**¿Cómo gestiona la base de datos esta rotación e incidencias de cocas?**
* **Cobro Inicial:** Se gestiona en la tabla `suscripciones` mediante el campo `cobro_cocas` ($70.000), sumándose al `valor_total`.
* **Rotación Diaria:** En la tabla `ruta_clientes` (que representa las paradas del domiciliario) existen los campos `cocas_entregadas` y `cocas_recogidas` para llevar el inventario físico en cada visita.
* **Incidencias:** Si un cliente daña una coca, la devuelve sucia o no la entrega, el domiciliario crea un reporte inmediato desde su App. Esto viaja a la tabla `incidencias`, levantando un ticket al administrador para cobrar la reposición o tomar medidas.

---

### 2. Días Festivos y Ciclos de Operación
**Si hay un día festivo en la semana, ¿se desplaza la entrega de ese almuerzo a la próxima semana?**
**No.** Por ningún motivo se pospone un almuerzo a la próxima semana, ya que los menús rotan semanalmente y la cocina inicia un nuevo ciclo operativo los lunes. 
* Si un cliente compra un plan (ej. Semanal de Lunes a Viernes) y el miércoles es festivo, **el sistema descuenta automáticamente el valor de ese día**. 
* En lugar de cobrarle 5 días ($65.000), le cobra 4 días ($52.000). El ciclo termina estrictamente el viernes.

**¿Cómo lo soporta el modelo de datos?**
La tabla `agenda` centraliza el calendario operativo marcando con `es_festivo = true` los feriados. Cuando la tabla `suscripciones` calcula el total a cobrar, consulta la `agenda` en ese rango de fechas y resta los días no operativos.

---

### 3. Suspensiones Voluntarias (Viajes o ausencias del cliente)
**Si el cliente ya pagó la semana pero se va de viaje un día o decide no recibir el almuerzo, ¿qué pasa?**
Funciona similar al festivo en el sentido de que no se le envía el almuerzo para no desperdiciar insumos, **pero con la diferencia de que el cliente asume la pérdida**.
* **No hay devoluciones de dinero.**
* **No se aplaza ni extiende la `fecha_vencimiento` de la suscripción.**

**¿Cómo se ve esto en el sistema?**
El cliente notifica desde su App y se guarda un registro en la tabla `suspensiones_entrega`. A las 5:00 PM, cuando el sistema arma las `ordenes_produccion` y las `rutas` del día siguiente, omite a este cliente. Sin embargo, su plan sigue caducando el mismo viernes estipulado originalmente.

---

### 4. Gestión de Domiciliarios y Rutas
**¿Cómo se estructuran los domiciliarios y cómo resuelven la trazabilidad?**
El proceso de Logística resuelve el problema de las "entregas a ojo" mediante varias tablas conectadas:
1. **Identidad:** Son usuarios con el rol Domiciliario (desde el 2026-11-02 ya no existe la tabla `empleados`).
2. **Trabajo Diario:** Cada día se les crea una `ruta` asignada a una `zona_cobertura` (ej. El Poblado).
3. **Paradas Optimizadas:** La tabla `ruta_clientes` le indica el `orden_entrega` de cada cliente que debe visitar hoy.
4. **Ubicación en Vivo:** La tabla `geolocalizacion_domiciliarios` recibe constantemente las coordenadas GPS (latitud y longitud) desde la App del repartidor. Esto le permite al administrador saber exactamente dónde están en tiempo real.

---

### 5. Suscripciones y Personalización
**¿Cómo funciona el corazón de las ventas (las suscripciones)?**
La tabla `suscripciones` actúa como el contrato inteligente entre el cliente y el negocio. Conecta a la persona con el catálogo de `servicios` (Plan Semanal, Quincenal o Mensual).
* **Personalización:** Si un cliente quiere exclusividad de menú (solo pollo o solo cerdo), el campo `tipo_menu` lo registra y añade un recargo de $10.000 al total.
* **Ciclo de Vida:** Nace en estado `pendiente`. Solo cuando el administrador valida la transferencia bancaria en la tabla `pagos`, la suscripción pasa a estado `activa`.
* **Automatización:** Solo las suscripciones en estado `activa` son tomadas en cuenta por el sistema para generar la orden a la cocina (`ordenes_produccion`) y despachar a los domiciliarios.

---
*Documento generado para revisión de la arquitectura del software "La Coca de Jacks".*
