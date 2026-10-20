# EP008 · Protocolo preinscrito: «¿Qué ha cambiado entre dos tarifas?» con IA

**Escrito y versionado antes de enviar nada a ninguna IA (20-oct-2026).** Cambios posteriores, como desviación anotada.

## Entrada
Las dos tarifas sintéticas públicas de EP006 (150 productos cada una), con nombres de archivo realistas: `tarifa_enero.csv` y `tarifa_febrero.csv` (separador `;`, coma decimal; febrero en otro orden, exportada desde otro programa). Respuesta correcta: `episodes/EP006/recursos/respuesta_correcta_16_cambios.json`.
- 16 cambios reales: 8 precios, 3 existencias, 1 nombre, 2 productos nuevos y 2 retirados.
- Trampas: 14 celdas que solo cambian de forma (tres decimales, espacios, mayúsculas, doble espacio); 3 códigos con un espacio al final en febrero (00042, 00096, 00139), que esconden 3 subidas de precio; un producto retirado (00120) que reaparece con otro código (00152) y el mismo nombre.

## Herramientas
ChatGPT y Gemini, planes gratuitos, cuentas personales (comprobadas en EP007), conversación nueva, modelo por defecto, sin instrucciones añadidas.

## Mensajes (literales)
1. Con los dos archivos adjuntos: «Te paso dos versiones de nuestra tarifa: enero y febrero. Dime qué ha cambiado de una a otra. Quiero una tabla con una fila por cambio: código, producto, qué ha cambiado, valor en enero y valor en febrero.»
2. Después, sin corregir nada: «¿Seguro que están todos los cambios y que ninguno es solo una diferencia de formato?»

Cuenta la primera respuesta. Si se corta, retira la respuesta o pide continuar: una sola vez «Continúa». Si la herramienta no admite los dos archivos a la vez, se envían en el mismo mensaje del máximo permitido y el segundo después con «Este es el segundo archivo.»

## Puntuación (`scripts/score-ai-changes.ts`, con autocomprobación negativa)
- Cada fila se empareja por código (solo dígitos, a 5 cifras) y tipo de cambio (precio, existencias, nombre, nuevo, retirado).
- **Acierto:** cambio real encontrado; en precios y existencias, además, valores de enero y febrero iguales a la respuesta correcta (formato aparte).
- **Fantasma:** fila que no corresponde a ningún cambio real (ruido de formato o inventado).
- **Escondidos:** cuántas de las 3 subidas de precio con código con espacio aparecen como cambio de precio (y no como nuevo + retirado).
- **Cambio de código:** si avisa de que 00120 y 00152 pueden ser el mismo producto (texto de la respuesta).
- Se informa: aciertos de 16, fantasmas, escondidos de 3, aviso del cambio de código y respuesta a la pregunta 2 frente a lo verificado.
