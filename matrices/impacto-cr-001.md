# Análisis de impacto de CR-001

Cambio evaluado: [motivo obligatorio en ajustes manuales de existencias](https://github.com/seckfly/Grupo_4_ISW_Comercial_Nazareth_Lab7/issues/5). Comparación entre la línea base v1.0 y los documentos v1.1.

| Dimensión | Artefactos afectados | Efecto y medida |
|---|---|---|
| Alcance | REQ-015, CU-006, CLS-MovimientoInventario, PRU-016 a PRU-018, matriz y reporte v1.1 | Un requisito, un caso de uso y una clase modificados. Se actualizó una prueba y se añadieron dos. La regla se aplica solo a ajustes manuales; la salida por venta mantiene su flujo. |
| Tiempo | Documentación, modelo y revisión de vínculos | El CR registró una estimación inicial de 2 horas para actualizar y comprobar documentación y modelo. No hay en el repositorio una reprogramación de hitos. |
| Calidad/costo | Validación del motivo, historial, stock y pruebas documentadas | Se documentan pruebas de aceptación con motivo válido y de rechazo de motivo vacío o compuesto por espacios. Las pruebas documentadas pasan de 6 a 8; la cobertura de requisitos con prueba sigue en 5/5. No se registró un costo monetario. |

En el diseño, CLS-MovimientoInventario incorpora `motivo` y `validarMotivo`; `registrarAjuste` recibe el motivo. El ajuste, su motivo y el stock deben guardarse en una misma transacción.
