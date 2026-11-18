# Acuerdo G3: el frontend frente a la v4.6 y el acceso con Google y Apple

Claude Omar · 2026-11-17 · base `06_Modelo_BD v12` (DBML v4.6). Ronda G3-1 (#022 y #023 → #027). El grill de vuelta es el G4 (#030 → #031).

## Decisiones

| # | Tema | Decisión | Decidió |
|---|---|---|---|
| Q1 | Documento | Enum `tipo_documento` (CC, CE, NIT, PA, PPT) en `usuarios`. Pasa a unique (`tipo_documento`, `documento`). | Alejandro |
| Q2 | Municipio | `direcciones_cliente.municipio` varchar not null. La zona sigue saliendo del polígono. | Alejandro |
| Q3 | Duración | `servicios.dias_habiles` integer not null, editable en el panel. | Alejandro |
| Q4 | Beneficios | `servicios.beneficios` text, una línea por beneficio. | Alejandro |
| Q5 | Rendimiento | `fichas_tecnicas.rendimiento_porciones` integer not null. `porciones_por_tanda` es el tope de la olla. | Alejandro |
| Q6 | Acciones | Solo las 4 del modelo: ver, crear, editar y cambiar_estado. Exportar va con ver. No se borra nada: se inactiva. | Alejandro |
| Q7 | Zonas | `zonas_cobertura` gana `nombre_publico` y `municipio`. Los barrios siguen en el código. | Alejandro |
| Q8 | Pago y hora | `banco_pago`, `tipo_cuenta_pago`, `numero_cuenta_pago`, `titular_cuenta_pago` y `horario_entrega` en `configuraciones_sistema`. Sale `clientes.franja_horaria`. | Alejandro |
| Q9 | Notas | Salen las "Notas para la cocina". Lo de la cocina va en las alergias (G1); lo de la entrega, en las notas de la dirección. | Alejandro |
| Q10 | Sin columna | Salen del frontend: la etiqueta y el sector de la dirección, el contacto del proveedor, el proveedor principal del insumo, "Se empaca en", el estado de la ficha técnica, la descripción y la marca "del sistema" del rol, y el motivo al cancelar. | Alejandro |
| Q11 | Social | Tabla `identidades_externas` (usuario_id, proveedor google/apple, sub, correo, fecha_vinculo), unique (proveedor, sub). `usuarios.password` pasa a opcional. | Alejandro |
| Q12 | Vincular | Si Google o Apple confirman el correo, se vincula a la cuenta existente. Si no, se pide la contraseña antes. | Alejandro |
| Q13 | Equipo | El personal entra solo con correo y contraseña. | Alejandro |

## Qué hace cada lado

**Modelo (Claude Alejo), en la v4.7:**
- Todas las columnas, tablas y claves de arriba, junto con G1, G2, G4 y `menus_diarios.foto_url`.

**Frontend (Claude Omar), desde ya (sobre la API simulada):**
- Clientes y Usuarios guardan el tipo de documento; el número es único por tipo.
- Las direcciones guardan el municipio.
- Servicios edita la duración en días hábiles y los beneficios. La web y el asistente los leen de la API.
- La ficha técnica pide el rendimiento en porciones.
- Sale la acción "Eliminar" de todo el panel. Se inactiva con cambiar estado. Exportar queda con ver.
- Zonas con nombre público y municipio, desde la API.
- Configuración edita los datos de pago y el horario de entrega. El asistente y la web los leen de ahí.
- Salen las notas para la cocina y los campos de Q10.
- El acceso: Google y Apple solo para clientes, con vínculo si el correo está verificado.
- `roles.js` y `business.js` quedan solo como respaldo sin conexión.
