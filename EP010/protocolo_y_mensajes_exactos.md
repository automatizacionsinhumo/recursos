# EP010 · Protocolo preinscrito: «¿Quién paga a quién?» repartiendo los gastos de un viaje con IA

**Escrito y versionado antes de enviar nada a ninguna IA (25-oct-2026, noche).** Cualquier cambio posterior se anota como desviación, con fecha y motivo.

## Caso
Viaje sintético de cuatro días, cinco amigos con nombres inventados (Ana, Bruno, Carla, David y Elena), 16 gastos, una fianza devuelta y un adelanto en efectivo (`data/caso.json`, generado por `scripts/make-ep010-fixtures.ts` con el modelo de `scripts/lib/split.ts`). Todos los importes se reparten exactos al céntimo.

**Respuesta correcta, calculada antes** (`recursos/respuesta_correcta.json`):
- Total del viaje: 1.505,90 €.
- Saldos (positivo: le deben; negativo: debe): Ana +124,98 €, Bruno +127,03 €, Carla −101,97 €, David −118,47 €, Elena −31,57 €.
- Mínimo de transferencias: 4. Una solución: David → Bruno 118,47 €, Carla → Ana 101,97 €, Elena → Ana 23,01 €, Elena → Bruno 8,56 €. Vale cualquier otra que deje a todos a cero. Con 3 es imposible.

**Trampas** (todas dichas de forma explícita en el mensaje):
- Gastos de solo una parte del grupo: kayak (3), Cudillero (4), museo (2), comida del domingo (4) y gasolina de la vuelta (4).
- Un gasto de una sola persona pagado por otra: el autobús de Carla.
- Un gasto pagado a medias por dos.
- La fianza devuelta (−100 €, para los cinco).
- 50 € que Elena adelantó a Ana en efectivo.

## Herramientas
ChatGPT y Gemini, planes gratuitos, cuentas personales (nunca una cuenta de empresa), conversación nueva, modelo por defecto, sin instrucciones personalizadas añadidas. Mismo día para las dos.

Antes de enviar se comprueba que la cuenta abierta es la personal y gratuita (ChatGPT: dominio del correo y plan en la sesión, sin copiar el correo a la evidencia). Sin archivos adjuntos: el caso va en el texto.

## Mensajes (literales)
1. Con el texto exacto de `data/mensajes.json` (SHA-256 `888abdd5557b8fafd76b4c6df7fabec54113e0d99b7a7bbd373e88b784344fc3`):

> Hemos hecho un viaje de cuatro días a Asturias cinco amigos: Ana, Bruno, Carla, David y Elena. Estos son los gastos. Salvo que diga otra cosa, cada gasto es para los cinco.
> - Alquiler del coche: 236,40 €, pagó Bruno.
> - Gasolina de la ida: 68,90 €, pagó David.
> - Casa rural, tres noches: 540 €, pagó Ana (incluye 100 € de fianza).
> - Compra en el supermercado: 87,35 €, pagó Carla.
> - Cena en la sidrería: 132,50 €, pagó Elena.
> - Peajes: 23,60 €, pagó Bruno.
> - Kayak: 105 €, pagó Carla. Fueron solo Ana, Carla y David.
> - Comida en Cudillero: 96 €, pagó David. Elena no vino, se quedó en la casa.
> - Museo: Bruno pagó su entrada y la de Elena, 18 € en total. Los demás no entraron.
> - Cafés y churros: 21,75 €, pagó Ana.
> - Helados: 14,50 €, pagó Carla.
> - Compra para la cena del sábado: 54,20 €, pagó Elena.
> - Parking en Oviedo: 12,40 €, pagó David.
> - Ana le compró a Carla el autobús de vuelta: 31,50 €, porque Carla se volvió el domingo por la mañana.
> - Comida del domingo: 118,80 €, pagó Bruno. Carla ya se había ido.
> - Gasolina de la vuelta: 45 €, la pagaron a medias Bruno y David. Carla ya no venía.
> Además, al dejar la casa le devolvieron a Ana los 100 € de fianza, y el primer día Elena le dio a Ana 50 € en efectivo a cuenta de la casa.
> ¿Cuánto ha pagado cada uno, cuánto le toca pagar a cada uno y quién tiene que pagar a quién, con el menor número de transferencias, para quedar en paz?

2. Sin corregir nada: «¿Seguro que las cuentas están bien?»

**Reglas.**
- Cuenta la primera respuesta de cada mensaje.
- Si una respuesta se corta, se retira o pide continuar, se envía una sola vez «Continúa».
- Si en vez de responder pregunta algo, se responde una sola vez «Haz las cuentas con lo que te he dicho.» y se registra.
- No se corrige nada ni se dan pistas.

## Registro
- Texto de cada respuesta copiado de la página con un botón temporal y comparado por SHA-256 con la página.
- Observador de solo lectura para guardar respuestas que se escriben y luego se retiran.
- Capturas a resolución completa, recortadas sin datos personales.
- Archivos: `evidence/<herramienta>.answers.json` ({q1, q2}) y `evidence/<herramienta>.observations.md`. En `observations.md` se anota a mano, con citas literales, lo que declara por persona (pagado, le toca, saldo) y el total.

## Puntuación (`scripts/score-ai-split.ts`, 16 controles negativos con `--selftest`)
- **P1 (mensaje 1):**
  - Se toma el último bloque de transferencias (la propuesta final).
  - Saldo implícito de cada persona (lo que recibe − lo que paga) frente a su saldo correcto, y personas con saldo correcto (±2 céntimos).
  - Si quedan en paz con las cuentas de verdad, y el dinero mal repartido (suma de diferencias / 2).
  - Número de transferencias frente a 4.
  - Diagnóstico: qué combinación más pequeña de errores típicos explica sus saldos (±5 céntimos), si alguna lo hace.
- **P2 («¿Seguro…?»):** si cambia su propuesta, se puntúa igual que P1. Se anota si afirma que está bien y si lo está.

El título y la miniatura se escriben después de puntuar, sea cual sea el resultado; si las dos aciertan, el vídeo lo dice.

## Desviaciones (anotadas después de enviar mensajes)
1. **25-oct-2026, observador de ChatGPT en el mensaje 1.** ChatGPT cambió la estructura de su página. El selector del observador (`[data-message-author-role]`) ya no existe, así que no registró nada mientras se escribía la respuesta 1. Para el mensaje 2 se usó el selector nuevo (`[data-dil-message-id]`). La respuesta 1 se conserva igualmente con su comparación SHA-256, y su texto es coherente de principio a fin.
2. **25-oct-2026, puntuador (formato «tarjeta»).** ChatGPT escribió las transferencias como tarjetas: «Carla → Ana», una línea de descripción y el importe solo en otra línea. `score-ai-split.ts` se amplió para leer ese formato, con un control negativo nuevo (17). No cambia ninguna regla de puntuación.
3. **25-oct-2026, diagnóstico.** El error de ChatGPT (la gasolina de la vuelta cargada solo a los dos que la pagaron) no estaba entre los errores típicos previstos. Se añadió a `scripts/lib/split.ts` con un control negativo (18). Solo afecta al diagnóstico: que «queden en paz» o no se decide igual que antes.
4. **25-oct-2026, forma de escribir los mensajes.** El texto se insertó en el cuadro de cada herramienta con un pegado simulado (ChatGPT) o con `insertText` línea a línea (Gemini). Antes de enviar se comprobó que el texto del cuadro era idéntico, carácter a carácter, al preinscrito.
