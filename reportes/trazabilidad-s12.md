# Resumen de trazabilidad (sesión 12)

Resumen de la matriz de trazabilidad v1.1 y sus vínculos con SRS, casos de uso, diagrama de clases y pruebas documentadas.

Requisitos con CU, CLS y PRU: **5/5**.
Artefactos vinculados: 5 REQ, 4 CU, 6 CLS y 8 PRU.

| Requisito | Casos de uso | Clases | Pruebas |
|---|---|---|---|
| REQ-001 | CU-001 | CLS-DetalleVenta, CLS-MovimientoInventario, CLS-Producto, CLS-Venta | PRU-001, PRU-003 |
| REQ-002 | CU-006 | CLS-Producto | PRU-002 |
| REQ-007 | CU-001, CU-003 | CLS-Cliente, CLS-ListaProductos, CLS-Producto | PRU-007 |
| REQ-010 | CU-001, CU-002 | CLS-Cliente, CLS-Venta | PRU-004 |
| REQ-015 | CU-006 | CLS-MovimientoInventario, CLS-Producto | PRU-016, PRU-017, PRU-018 |

## Lectura en ambos sentidos

Desde REQ-015 se llega a CU-006, CLS-Producto, CLS-MovimientoInventario y las pruebas PRU-016, PRU-017 y PRU-018. Desde PRU-017 o PRU-018 se vuelve a REQ-015 y a la regla del motivo obligatorio en ajustes manuales.

La cobertura mide relaciones entre documentos, no ejecución de pruebas.
