# Recursos del vídeo «Pasé 30 facturas de PDF a Excel con ChatGPT y Gemini: ninguna avisó del error»

Todo lo necesario para repetir la prueba con tu IA. Datos sintéticos: empresas, NIF e importes inventados; ninguna factura real.

| Archivo | Qué es |
|---|---|
| `plantilla_comprobar_facturas.xlsx` | La plantilla de Excel con las dos comprobaciones del vídeo. Pega la tabla de tu IA en la hoja «Comprobar» (desde la fila 6, columnas A a I) y escribe cuántas facturas le pasaste: te dice cuántas faltan y marca «REVISAR» en cada fila donde base + IVA no da el total (o donde los importes no son números). Las hojas «Ejemplo Gemini» y «Ejemplo ChatGPT» llevan las tablas reales de la prueba. |
| `facturas_sinteticas_30_pdf.zip` | Las 30 facturas: 20 PDF digitales y 10 escaneadas (imagen sin texto). Trampas: IVA del 10 %, punto de miles, etiquetas distintas y una factura (2026/013) cuyo total impreso no cuadra. |
| `facturas_30_en_un_pdf.pdf` | Las mismas 30 facturas en un único PDF de 30 páginas. |
| `respuesta_correcta_30_facturas.json` | Los datos correctos de cada factura, calculados antes de la prueba. |
| `protocolo_y_mensajes_exactos.md` | Los mensajes literales y las reglas de puntuación, escritos antes de abrir ninguna IA. |
| `resultados/` | Las tablas que devolvió cada IA y la puntuación dato a dato. |

## Qué pasó (20 de octubre de 2026, planes gratuitos)
- **Gemini**, 30 PDF sueltos: admitió 10 por tanda; su primera respuesta retiró la tabla («Solo soy una IA basada en texto…»); tras «continúa», 240 de 240 datos correctos, también en las escaneadas. Copió la factura 2026/013 sin avisar y, al preguntarle, dijo que todas cuadraban (falso).
- **ChatGPT**, 30 PDF sueltos: admite 20 a la vez, adjuntó 3 y mostró el aviso de límite. Con un solo PDF: 20 filas correctas y la frase «el PDF que has adjuntado contiene 20 facturas, no 30»; las 10 que faltan son las escaneadas. Al preguntarle, encontró la factura descuadrada.
- **Gemini**, un solo PDF: escribió la tabla y la retiró dos veces.

## Cómo repetirlo
1. Descomprime las facturas (o usa el PDF único) y pásaselas a tu IA con el mensaje del protocolo.
2. Pega su tabla en la plantilla y escribe 30 en «Facturas que tienes».
3. Si «Faltan» no es 0 o hay filas «REVISAR», mira esas facturas en el original.

Límites: es una prueba de un día con planes gratuitos; los planes de pago y otras fechas pueden dar otro resultado. La comprobación de base + IVA no detecta un importe mal leído que cuadre por casualidad: para eso hay que comparar con el original (o con `respuesta_correcta_30_facturas.json` en esta prueba).

Plantilla comprobada en Google Sheets el 20-oct-2026: con las tablas de ejemplo da 30 filas y 1 a revisar (Gemini) y 20 filas, faltan 10 y 1 a revisar (ChatGPT). Solo usa funciones básicas de Excel.

Licencia: datos, plantilla y textos de este directorio, CC0 (dominio público). ChatGPT es una marca de OpenAI y Gemini de Google; este material no está afiliado ni patrocinado por ninguna de las dos.
