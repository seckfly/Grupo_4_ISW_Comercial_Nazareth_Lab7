# Convención de identificadores

| Elemento | Formato | Ejemplo |
|---|---|---|
| Requisito | REQ-### | REQ-001 |
| Caso de uso | CU-### | CU-001 |
| Clase | CLS-Nombre | CLS-Venta |
| Prueba | PRU-### | PRU-001 |
| Solicitud de cambio | CR-### | CR-001 |

Cada identificador corresponde a un solo elemento. Se conserva cuando se modifica el contenido y no se reutiliza si el elemento se retira.

PRU identifica una prueba documentada. Pull Request identifica la solicitud de integración de GitHub.

## Uso en la trazabilidad

El recorrido documentado va de REQ a CU, CLS y PRU. También se comprueba en sentido inverso: cada caso de uso, clase y prueba de estos artefactos debe tener al menos un requisito asociado en la matriz. Los IDs siguen siendo los mismos tras CR-001.
