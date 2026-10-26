# Pruebas de Comercial Nazareth

Los datos numéricos son datos de prueba para comprobar el comportamiento esperado.

| ID | Requisito | Datos y procedimiento | Resultado esperado |
|---|---|---|---|
| PRU-001 | REQ-001 | Con una sesión administrativa activa, usar un producto activo con stock 10 y precio S/ 6,70. Registrar una venta de 3 unidades con datos de pago válidos. Repetir desde el estado inicial provocando un fallo de guardado. | En el primer caso se guardan la venta, el detalle y la salida de 3 unidades; el total es S/ 20,10 y el stock queda en 7. En el caso de fallo, no se confirma la venta ni quedan registros parciales; el stock permanece en 10. |
| PRU-002 | REQ-002 | Configurar un mínimo de 5 para productos activos con stock 4, 5 y 6. Consultar las existencias y alertas. Repetir con un producto inactivo cuyo stock sea 4. | La consulta muestra las existencias. La alerta incluye los productos activos con stock 4 y 5; excluye el de stock 6 y el producto inactivo. |
| PRU-003 | REQ-001 | Registrar 3 unidades a S/ 6,70 y un pago en efectivo de S/ 50,00. Comparar el cálculo mostrado con el importe guardado. | El total es S/ 20,10 y el vuelto es S/ 29,90. Los importes mostrados y guardados coinciden y tienen dos decimales. |
| PRU-004 | REQ-010 | Registrar una venta identificando a un cliente registrado y otra venta sin identificar a ningún cliente. Usar productos con stock suficiente y datos de pago válidos en ambos casos. | La primera venta queda asociada al cliente elegido. La segunda se confirma sin cliente vinculado. |
| PRU-007 | REQ-007 | Consultar un producto existente por nombre, aplicar su categoría y comprobar el precio y disponibilidad. Buscar después un nombre inexistente. Desde una cuenta de cliente registrado, guardar un producto en favoritos y en una lista y consultar ambas selecciones. | Los filtros muestran los productos correspondientes, con su precio y disponibilidad. La búsqueda sin coincidencias muestra un estado vacío. El producto elegido aparece en favoritos y en la lista del cliente. |
| PRU-016 | REQ-015 | Con acceso autorizado, registrar un producto con precio S/ 6,70 y stock inicial 10. Actualizar su precio a S/ 7,00 y ajustar el stock a 8. Consultar el producto y su historial. | El producto conserva el precio S/ 7,00 y stock 8. El historial permite consultar el ajuste desde el stock 10 al stock 8 sin perder los registros anteriores. |

