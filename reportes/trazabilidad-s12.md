# Reporte de trazabilidad (sesión 12)

Generado con `python3 scripts/verificar-trazabilidad.py` a partir de los artefactos del repositorio.

Requisitos con CU, CLS y PRU: **5/5**.
IDs de origen: 5 REQ, 4 CU, 6 CLS y 8 PRU.

| Requisito | Casos de uso | Clases | Pruebas |
|---|---|---|---|
| REQ-001 | CU-001 | CLS-DetalleVenta, CLS-MovimientoInventario, CLS-Producto, CLS-Venta | PRU-001, PRU-003 |
| REQ-002 | CU-006 | CLS-Producto | PRU-002 |
| REQ-007 | CU-001, CU-003 | CLS-Cliente, CLS-ListaProductos, CLS-Producto | PRU-007 |
| REQ-010 | CU-001, CU-002 | CLS-Cliente, CLS-Venta | PRU-004 |
| REQ-015 | CU-006 | CLS-MovimientoInventario, CLS-Producto | PRU-016, PRU-017, PRU-018 |

## Comprobación bidireccional

Sin vínculos de ID faltantes o sobrantes.

La cobertura mide relaciones entre documentos. Las pruebas están documentadas; este reporte no acredita su ejecución.
