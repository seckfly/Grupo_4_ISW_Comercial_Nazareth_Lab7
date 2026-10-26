# Casos de uso de Comercial Nazareth

| ID | Caso de uso | Actor | Requisitos relacionados |
|---|---|---|---|
| CU-001 | Registrar venta | Vendedor | REQ-001; utiliza REQ-007 y, cuando el comprador se identifica, REQ-010 |
| CU-002 | Vincular cliente a la venta | Vendedor | REQ-010 |
| CU-003 | Consultar catálogo | Cliente registrado, Vendedor y Responsable de compras | REQ-007 |
| CU-006 | Gestionar inventario | Responsable de almacén | REQ-002, REQ-015 |

## CU-001: Registrar venta

Actor: Vendedor, rol desempeñado por Humberto Dávalos.

Precondiciones: Humberto tiene una sesión administrativa activa. Los productos están activos y cuentan con precio y stock registrados.

### Flujo principal

1. Humberto consulta el catálogo mediante CU-003 y selecciona los productos y cantidades de la venta.
2. El sistema comprueba que la venta tenga productos, que las cantidades sean positivas y que exista stock suficiente.
3. Si el comprador se identifica como cliente registrado, Humberto lo vincula mediante CU-002. En caso contrario, continúa sin cliente asociado.
4. Humberto elige efectivo, Yape o Plin. El sistema calcula el total con los precios del servicio y muestra los campos del método elegido.
5. Humberto registra el monto recibido en efectivo o la referencia de la operación digital.
6. El sistema valida el monto recibido en efectivo o la referencia de la operación digital, según el método elegido, y calcula el vuelto cuando corresponde.
7. El sistema guarda la cabecera y el detalle de la venta, registra la salida de inventario y descuenta el stock en una misma transacción.
8. El sistema confirma el guardado y muestra el identificador de la venta.

### Alternativas y excepciones

| Situación | Respuesta |
|---|---|
| El comprador no se identifica como cliente registrado | Continuar sin vincular una cuenta. |
| El monto recibido en efectivo supera el total | Calcular y mostrar el vuelto. |
| Se selecciona Yape o Plin | Registrar la referencia digital sin atribuirle una confirmación bancaria automática. |
| La venta está vacía o contiene cantidades no válidas | Solicitar la corrección antes de continuar. |
| Un producto no tiene stock suficiente | Identificar el producto y rechazar el intento actual. Humberto puede iniciar una nueva selección. |
| El monto recibido o la referencia digital no son válidos para el método elegido | Solicitar la corrección antes de guardar. |
| Falla el guardado | Revertir la transacción y mostrar que la venta no fue confirmada. |

Postcondición de éxito: quedan guardados la venta, su detalle y el movimiento de salida, con el stock actualizado.

Postcondición ante fallo de guardado: no quedan una venta parcial ni descuentos de stock correspondientes a una venta sin confirmar.

CU-001 incluye CU-003. CU-002 extiende CU-001 cuando el comprador se identifica como cliente registrado.
