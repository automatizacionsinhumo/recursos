# Recursos de los vídeos «Le pasé la foto del ticket del súper a ChatGPT y Gemini»

Todo lo necesario para repetir la prueba o repartir tu propio ticket entre dos. Datos inventados: el supermercado, la dirección, el NIF y la compra no son reales.

| Archivo | Qué es |
|---|---|
| `plantilla_ticket_compartido.xlsx` | Para repartir un ticket entre dos y comprobar la cifra de una IA. En la hoja «Líneas» apuntas cada línea del ticket con su importe (los descuentos, el 2x1 y el cupón, en negativo) y de quién es: «mío», «suyo» o «a medias». La hoja «Resumen» calcula cuánto te debe la otra persona, si pagaste tú. También comprueba que las líneas suman el total del ticket y si la cifra de la IA coincide. |
| `ejemplo_ticket_del_video.xlsx` | El ticket del vídeo ya apuntado: te debe 21,23 €, «CUADRA» con el total (44,03 €) y «COINCIDE» con lo que dijeron las dos IA. |
| `ticket_foto.jpg` | La foto exacta que recibieron ChatGPT y Gemini. |
| `lineas_del_ticket.csv` | Las líneas del ticket y de quién es cada una (separador `;`). |
| `respuesta_correcta.json` | Calculada antes de preguntar: lo de cada uno, la cuenta y la cifra que sale con cada error típico (sin el 2x1, el cupón ignorado, todo a medias…). |
| `protocolo_y_mensajes_exactos.md` | Las reglas escritas antes de la prueba, los dos mensajes exactos y la desviación anotada después. |
| `resultados/` | Las respuestas literales de ChatGPT y Gemini a los dos mensajes y la puntuación de cada una. |

## Cómo usar la plantilla
1. En «Líneas», una fila por línea del ticket: importe y «mío», «suyo» o «a medias». Los descuentos y el cupón van en negativo, con el dueño que les toque: el 2x1 es de quien compró ese producto. El cupón, como lo acordéis; en el ejemplo, «a medias».
2. No apuntes «Entregado» ni «Cambio», ni el desglose de IVA: no son líneas de la compra.
3. En «Resumen», escribe el total del ticket y la cifra que te da la IA. Mira «¿Cuadra con el ticket?» y «¿Coincide con la IA?».

Plantilla comprobada en Microsoft Excel el 26-oct-2026. Con el ticket del vídeo da 21,23 €, «CUADRA» y «COINCIDE». Vacía, pide el total y la cifra de la IA.

La comprobación rápida, sin plantilla: tu parte más la suya tiene que dar el total del ticket. En el ejemplo: 22,80 € + 21,23 € = 44,03 €.

Límites: una prueba, un día, plan gratuito, una conversación por herramienta. Esta vez las dos acertaron; otro día, con otro ticket, puede salir distinto.

Licencia: datos, plantilla, foto y textos de este directorio, CC0 (dominio público). ChatGPT y Gemini son marcas de OpenAI y Google; este material no está afiliado ni patrocinado por ninguna de las dos.
