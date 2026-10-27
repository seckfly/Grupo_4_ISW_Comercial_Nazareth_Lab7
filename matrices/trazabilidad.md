# Matriz de trazabilidad de Comercial Nazareth (v1.0)

La columna «¿Cubierto?» indica si el requisito está vinculado a un caso de uso, una clase y una prueba.

| Requisito | Descripción | Caso de uso | Clase | Prueba | ¿Cubierto? |
|---|---|---|---|---|---|
| REQ-001 | Registrar venta | CU-001 | CLS-Venta, CLS-DetalleVenta, CLS-Producto, CLS-MovimientoInventario | PRU-001, PRU-003 | Sí |
| REQ-002 | Consultar existencias y alertas | CU-006 | CLS-Producto | PRU-002 | Sí |
| REQ-007 | Consultar catálogo, favoritos y listas | CU-003, incluido por CU-001 | CLS-Producto, CLS-ListaProductos, CLS-Cliente | PRU-007 | Sí |
| REQ-010 | Vincular cliente a la venta | CU-002; extiende CU-001 | CLS-Cliente, CLS-Venta | PRU-004 | Sí |
| REQ-015 | Mantener productos e inventario | CU-006 | CLS-Producto, CLS-MovimientoInventario | PRU-016 | Sí |

**Cobertura:** 5 de 5 requisitos con prueba = (5 ÷ 5) × 100 = 100 %
