# Riesgos asociados a CR-001

Los niveles son estimaciones cualitativas para la aplicación del cambio, no incidencias observadas. Probabilidad e impacto se expresan como baja, media o alta.

| ID | Riesgo | Probabilidad | Impacto | Prevención | Contingencia |
|---|---|---|---|---|---|
| R-01 | Se actualiza el stock sin conservar el motivo del ajuste. | Media | Alta | Guardar ajuste, motivo y stock en una transacción; revisar PRU-016. | Revertir el intento y corregir el flujo antes de aceptar el ajuste. |
| R-02 | Se acepta un motivo vacío o compuesto solo por espacios. | Media | Media | Validar antes de guardar; revisar PRU-017 y PRU-018. | Rechazar el ajuste y solicitar un motivo válido. |
| R-03 | La nueva validación afecta las salidas de stock generadas por ventas. | Baja | Alta | Mantener separadas las reglas de CU-006 y CU-001; revisar PRU-001. | Retirar la validación del flujo de ventas y repetir sus pruebas. |
| R-04 | La actualización documental supera las dos horas estimadas. | Media | Media | Seguir los enlaces de REQ-015 en la matriz y comprobar los IDs. | Revisar el esfuerzo pendiente y ajustar la planificación antes de cerrar la revisión. |
