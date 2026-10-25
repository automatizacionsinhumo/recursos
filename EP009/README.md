# Recursos del vídeo «Uní dos listas de clientes con ChatGPT: dijo 187 personas y eran 190»

Todo lo necesario para repetir la prueba. Datos sintéticos: nombres, correos y teléfonos inventados (dominio reservado `correo-de-prueba.test`).

| Archivo | Qué es |
|---|---|
| `plantilla_comprobar_union.xlsx` | Pega tus dos listados originales y el listado unido que te dé la IA. La hoja «Resumen» cuenta las personas distintas de los originales (por correo, sin espacios y en minúsculas), las filas del unido, las personas repetidas, las que faltan, las que no tienen fila propia porque su correo está en la fila de otra persona, los teléfonos que no coinciden y las filas con el mismo nombre. Si algo no cuadra, lo dice. |
| `clientes_tienda.xlsx` · `clientes_web.xlsx` | Los dos listados de la prueba (120 y 100 filas). También en `.csv` (separador `;`). Son los mismos de EP005. |
| `respuesta_correcta_190_personas.json` | Una fila por persona, calculada antes: 190 personas, 30 en los dos listados, 3 parejas que se llaman igual y son personas distintas, y 2 personas con un teléfono distinto en cada listado. |
| `protocolo_y_mensajes_exactos.md` | Las reglas escritas antes de la prueba y los tres mensajes exactos. |
| `resultados/` | La tabla de repetidas de ChatGPT, su listado unido de 187 filas y la puntuación persona a persona. |

## Cómo repetirlo
1. Abre una conversación nueva con tu IA, adjunta los dos `.xlsx` y envía los mensajes de `protocolo_y_mensajes_exactos.md`.
2. Copia su listado unido en la hoja «Unido» de la plantilla.
3. Mira «Resultado» en la hoja «Resumen».

Plantilla comprobada en Google Sheets con la respuesta correcta («CUADRA») y con una unión hecha por nombre (190 filas, 3 repetidas y 3 perdidas: «NO CUADRA»). Con el listado de ChatGPT: 187 filas frente a 190 personas y 6 personas sin fila propia.

Límites: la regla identifica a cada persona por su correo. Una persona con dos correos distintos, o dos personas que comparten correo, no se detectan así. Prueba de un día con el plan gratuito.

Licencia: datos, plantilla y textos de este directorio, CC0 (dominio público). ChatGPT es una marca de OpenAI; este material no está afiliado ni patrocinado por OpenAI.
