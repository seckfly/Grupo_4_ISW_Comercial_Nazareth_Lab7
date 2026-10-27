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

> «¿Cubierto?» indica que existe la cadena REQ → CU → CLS → PRU. No demuestra que las pruebas se hayan ejecutado con éxito ni que se cubran todas las condiciones funcionales de cada requisito. CU-001 incluye CU-003; CU-002 extiende CU-001 solo cuando el comprador se identifica como cliente registrado.

## Respaldo de cada clase en el diagrama

Clases y operaciones tomadas de `modelos/clases.drawio`. No se agregaron clases ni métodos fuera del modelo.

| Requisito | Clase y operaciones que lo respaldan |
|---|---|
| REQ-001 | CLS-Venta (`calcularTotal()`, `calcularVuelto()`, `confirmar()`), CLS-DetalleVenta (`calcularSubtotal()`), CLS-Producto (`descontarStock(cantidad)`), CLS-MovimientoInventario (`registrarSalida()`) |
| REQ-002 | CLS-Producto (`tieneStockBajo()`; atributos `stock`, `stockMinimo` y `activo`) |
| REQ-007 | CLS-Producto (`buscar(nombre, categoria)`, `estaDisponible()`), CLS-ListaProductos (`agregarProducto(producto)`), CLS-Cliente (`crearLista(nombre, tipo)`) |
| REQ-010 | CLS-Venta (`vincularCliente(cliente)`) y CLS-Cliente, con asociación 0..1 a * |
| REQ-015 | CLS-Producto (`registrar()`, `actualizarPrecio(precio)`, `ajustarStock(cantidad)`), CLS-MovimientoInventario (`registrarAjuste()`, `consultarHistorial()`) |

## Cambios frente al archivo actual de `main`

| Elemento | Antes | Después |
|---|---|---|
| Título | Matriz de trazabilidad de Comercial Nazareth | … (v1.0) |
| Columna Clase | «Sin asociación» en las 5 filas | Clases del diagrama |
| ¿Cubierto? | No en las 5 filas | Sí en las 5 filas |
| Cobertura | 5 de 5 requisitos (100 %) | 5 de 5 = (5 ÷ 5) × 100 = 100 % |

## Métricas de la revisión

| Indicador | Resultado |
|---|---|
| Requisitos totales | 5 |
| Pruebas documentadas | 6 |
| Requisitos con prueba | 5 |
| Cobertura documental | 100 % |
| Trazabilidad completa en la matriz original | 0/5 |
| Trazabilidad completa en la propuesta v1.0 | 5/5 |
| Pruebas con ejecución acreditada | 0/6 |

Se cuentan requisitos, no filas de prueba: REQ-001 tiene dos pruebas y suma una sola vez. El valor 0/6 significa que el repositorio no contiene evidencia de ejecución; no implica que las pruebas nunca se hayan ejecutado. Cobertura documental, trazabilidad completa y validación funcional son tres medidas distintas: la primera es 100 %, la segunda 5/5 con la propuesta y la tercera no tiene evidencia.

---

# Matriz de trazabilidad de Comercial Nazareth (v1.1)

Estructura propuesta, pendiente de aprobación y actualización. CR-001 no está registrado en el repositorio revisado, por lo que ninguna fila tiene asignado todavía un requisito afectado. Las celdas «Pendiente de CR-001» se completan con lo que aprueben y apliquen las partes 1, 2 y 4.

| Requisito | Descripción | Caso de uso | Clase | Prueba | ¿Cubierto? | Último CR |
|---|---|---|---|---|---|---|
| REQ-001 | Registrar venta | CU-001 | CLS-Venta, CLS-DetalleVenta, CLS-Producto, CLS-MovimientoInventario | PRU-001, PRU-003 | Sí | Pendiente de CR-001 |
| REQ-002 | Consultar existencias y alertas | CU-006 | CLS-Producto | PRU-002 | Sí | Pendiente de CR-001 |
| REQ-007 | Consultar catálogo, favoritos y listas | CU-003, incluido por CU-001 | CLS-Producto, CLS-ListaProductos, CLS-Cliente | PRU-007 | Sí | Pendiente de CR-001 |
| REQ-010 | Vincular cliente a la venta | CU-002; extiende CU-001 | CLS-Cliente, CLS-Venta | PRU-004 | Sí | Pendiente de CR-001 |
| REQ-015 | Mantener productos e inventario | CU-006 | CLS-Producto, CLS-MovimientoInventario | PRU-016 | Sí | Pendiente de CR-001 |

**Cobertura:** Pendiente de CR-001. Se calcula como (requisitos con prueba ÷ requisitos totales) × 100 con la SRS v1.1.

## Reglas para actualizarla

1. Cambiar el título a «(v1.1)» y añadir la columna **Último CR**. Las filas que CR-001 no toca llevan «—».
2. Poner **CR-001** solo en los requisitos que declare el Issue y en los que cambie su texto, flujo o pruebas. No se asigna por defecto a REQ-001 ni a ningún otro requisito.
3. Revisar uno por uno los elementos compartidos: CLS-Producto aparece en las 5 filas, CU-006 cubre REQ-002 y REQ-015, y CU-001 se relaciona con REQ-007 y REQ-010. Si el cambio no altera lo que exige un requisito, su fila queda con «—».
4. Conservar las pruebas de v1.0 y añadir las nuevas en la misma celda con los IDs que defina la parte 4, sin renombrar las existentes.
5. Si CR-001 añade una clase, agregarla junto a las anteriores. Si solo añade un método a una clase que ya figura, la celda Clase no cambia; el método se informa en el reporte y se destaca en el PNG.
6. Recalcular la cobertura con los requisitos de la SRS v1.1.

## Información necesaria de otras partes

| Parte | Información | Uso en la matriz v1.1 |
|---|---|---|
| Parte 1 | Issue CR-001 con requisitos afectados y decisión; nombre de la rama del cambio. | Columna Último CR y requisitos modificados. |
| Parte 2 | Casos de uso, clases o métodos modificados por CR-001. | Columnas Caso de uso y Clase. |
| Parte 4 | IDs de las pruebas nuevas o actualizadas y el requisito de cada una. | Columna Prueba y cobertura v1.1. |
