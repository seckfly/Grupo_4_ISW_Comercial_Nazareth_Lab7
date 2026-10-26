# Convención de identificadores

| Elemento | Formato | Ejemplo |
|---|---|---|
| Requisito del laboratorio | REQ-### | REQ-001 |
| Caso de uso | CU-### | CU-001 |
| Clase | CLS-Nombre | CLS-NombreClase |
| Prueba | PRU-### | PRU-001 |
| Solicitud de cambio | CR-### | CR-001 |

Cada identificador corresponde a un solo elemento. Se conserva cuando se modifica el contenido y no se reutiliza si el elemento se retira.

Los códigos REQ, CU y PRU mantienen el número del requisito RF, caso CU o comprobación PR del repositorio anterior. Por ejemplo, REQ-010 corresponde a RF-10, CU-001 a CU01 y PRU-007 a PR-07. Los saltos de numeración conservan esa correspondencia.

PRU identifica una prueba documentada. Pull Request identifica la solicitud de integración de GitHub. Los nombres de clases y CR-001 se incorporarán cuando se desarrollen esas partes del laboratorio.
