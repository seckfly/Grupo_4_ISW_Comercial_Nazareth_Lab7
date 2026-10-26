# Requisitos de Comercial Nazareth

Se seleccionaron cinco requisitos del proyecto para construir la trazabilidad del laboratorio. Los roles internos corresponden a Humberto Dávalos, propietario y único trabajador del negocio. El cliente registrado utiliza el portal.

| ID | ID de origen | Requisito | Comportamiento requerido | Caso de uso |
|---|---|---|---|---|
| REQ-001 | RF-01 | Registrar venta | Registrar los productos, cantidades y método de pago, calcular el total y guardar la venta, su detalle y la salida de stock en una misma transacción. | CU-001 |
| REQ-002 | RF-02 | Consultar existencias y alertas | Mostrar las existencias y señalar los productos activos cuyo stock sea menor o igual al mínimo configurado. | CU-006 |
| REQ-007 | RF-07 | Consultar catálogo | Buscar productos por nombre y categoría, mostrar su precio y disponibilidad, y permitir al cliente registrado guardar favoritos y listas en el portal. | CU-003 |
| REQ-010 | RF-10 | Vincular cliente a la venta | Asociar un cliente registrado cuando el comprador se identifique y permitir que la venta continúe sin cliente vinculado. | CU-002, dentro de CU-001 |
| REQ-015 | RF-15 | Mantener productos e inventario | Registrar y actualizar productos, precios y stock inicial; permitir ajustes autorizados de existencias conservando su historial. | CU-006 |

## Reglas aplicables

- La venta utiliza el precio consultado por el servicio y redondea los importes a dos decimales. El cálculo de descuentos debe coincidir entre la interfaz y el servicio (RB-02 del proyecto).
- Una venta puede registrarse sin cliente asociado (RB-03).
- Efectivo, Yape y Plin son métodos de pago registrados. La referencia de Yape o Plin no constituye una confirmación bancaria automática (RB-01).
- La alerta incluye el stock igual al mínimo. La condición de reposición del proyecto se mantiene separada: stock menor al mínimo y decisión de Humberto de reponer (RB-06).
- La venta, su detalle y el movimiento de inventario se confirman juntos. Ante un error, la transacción se revierte sin dejar cambios parciales (RNF-04).

Los requisitos describen el comportamiento esperado. Este repositorio contiene documentos del laboratorio; su contenido no acredita que las funciones estén implementadas o que las pruebas se hayan ejecutado.
