# Recursos del vídeo «Le pedí a ChatGPT repartir los gastos de un viaje: a dos amigos les cobró de más»

Todo lo necesario para repetir la prueba o repartir los gastos de tu propio viaje. Datos inventados: los cinco amigos y los gastos no son reales.

| Archivo | Qué es |
|---|---|
| `plantilla_repartir_gastos.xlsx` | Para repartir gastos entre amigos y comprobar las transferencias que te propone una IA (o tú). Apuntas los nombres, los gastos (quién pagó y una «x» en quienes participan), el dinero que uno ya le dio a otro durante el viaje y las transferencias propuestas. La hoja «Resumen» calcula lo que pagó y lo que le toca a cada uno, su saldo, y si con esas transferencias todos quedan a cero. Si no, lo dice. |
| `ejemplo_viaje_chatgpt.xlsx` · `ejemplo_viaje_gemini.xlsx` | El viaje del vídeo ya apuntado, con las transferencias que propuso cada IA. Con las de ChatGPT (primera respuesta): «NO CUADRA», cuatro personas a 11,25 €. Con las de Gemini: «CUADRA». |
| `gastos_del_viaje.csv` | Los gastos del caso (separador `;`). |
| `respuesta_correcta.json` | Calculada antes de preguntar: lo pagado, lo que le toca y el saldo de cada persona, una liquidación con 4 transferencias y los saldos que salen con cada error típico. |
| `protocolo_y_mensajes_exactos.md` | Las reglas escritas antes de la prueba y los dos mensajes exactos. |
| `resultados/` | Las respuestas literales de ChatGPT y Gemini a los dos mensajes y la puntuación de cada una. |

## Cómo usar la plantilla
1. En «Resumen», escribe los nombres en la columna A (hasta 8).
2. En «Gastos», una fila por gasto: importe, quién pagó y una «x» en cada persona que participa. Si dos pagaron a medias, pon dos filas. Una devolución (una fianza) va en negativo.
3. En «Entre amigos», el dinero que alguien ya le dio a otro durante el viaje.
4. En «Transferencias», lo que te propone la IA. Mira «Resultado».

Plantilla comprobada en Google Sheets el 25-oct-2026: con el viaje del vídeo da los saldos correctos, «NO CUADRA» con las transferencias de ChatGPT y «CUADRA» con las de Gemini.

Ojo: que el total cuadre no prueba nada. La respuesta equivocada de ChatGPT también sumaba 1.505,90 €. Lo que cuenta es que cada persona quede a cero.

Límites: una prueba, un día, plan gratuito, una conversación por herramienta.

Licencia: datos, plantilla y textos de este directorio, CC0 (dominio público). ChatGPT y Gemini son marcas de OpenAI y Google; este material no está afiliado ni patrocinado por ninguna de las dos.
