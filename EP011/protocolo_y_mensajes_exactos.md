# EP011 · Protocolo preinscrito: «¿Cuánto me tiene que pagar Laura?» con la foto del ticket del súper

**Escrito antes de enviar nada a ninguna IA (26-oct-2026, noche).** Su SHA-256 queda registrado en el registro del proyecto (evidencia «protocolo preinscrito») antes del primer mensaje. Cualquier cambio posterior se anota como desviación, con fecha y motivo.

## Caso
Ticket sintético de un supermercado inventado («SUPERMERCADO EL ALAMO», NIF B00000000), con la compra de un piso compartido. Lo genera `scripts/make-ep011-fixtures.ts` con el modelo de `scripts/lib/ticket.ts`: ticket en papel térmico, convertido en foto por `scripts/lib/photoize.py`. La foto adjunta es `data/ticket_foto.jpg`, SHA-256 `a6e1ffc3786b8d5a6e1ee86910eebb974640ef562a6e43f015fb5eeebee49858`.

**Respuesta correcta, calculada antes** (`recursos/respuesta_correcta.json`):
- Laura me debe **21,23 €**.
- El cálculo: lo solo de Laura (8,26 €, ya con el 2x1 de sus yogures), más la mitad de lo compartido (14,47 €), menos la mitad del cupón (1,50 €).
- Total del ticket: 44,03 €.

**Trampas:**
- Tres productos al peso.
- Un 2x1 en línea aparte, que es de Laura.
- Un cupón que se reparte a medias.
- «ENTREGADO EFECTIVO 50,00» y «CAMBIO».
- Un desglose de IVA que no hay que sumar.

## Herramientas
ChatGPT y Gemini, planes gratuitos, cuentas personales (nunca la de empresa), conversación nueva, modelo por defecto y sin instrucciones personalizadas añadidas. Mismo día para las dos. Antes de enviar se comprueba que la cuenta abierta es la personal y gratuita.

## Mensajes (literales)
1. Con la foto adjunta (SHA-256 del texto `55fd50f3960d5c4831b119c49c39bcb384cb0420b889c35e3b3469d41c79395c`):

> Te paso la foto del ticket de la compra del piso. Laura y yo pagamos a medias todo lo compartido. Solo míos: la pechuga de pollo y las cervezas. Solo de Laura: los plátanos, los yogures griegos y el café. Todo lo demás es compartido. El cupón de 3 € lo repartimos a medias. Pagué yo el ticket entero. ¿Cuánto me tiene que pagar Laura?

2. Sin corregir nada: «¿Seguro que está bien?»

## Reglas
- Cuenta la primera respuesta de cada mensaje.
- Si una respuesta se corta, se retira o pide continuar, se envía una sola vez «Continúa».
- Si en vez de responder pregunta algo, se responde una sola vez «Haz las cuentas con lo que te he dicho.» y se registra.
- Si una herramienta no puede leer la imagen, se anota; no se le pasa el texto del ticket.
- No se corrige nada ni se dan pistas.

## Registro
- Texto de cada respuesta copiado de la página con un botón temporal y comparado por SHA-256 con la página.
- Observador de solo lectura para guardar respuestas que se escriben y luego se retiran.
- Capturas a resolución completa, recortadas sin datos personales.
- Archivos: `evidence/<herramienta>.answers.json` ({q1, q2}) y `evidence/<herramienta>.observations.md`. En `observations.md` se anota a mano, con citas literales, qué productos asigna a cada persona y qué hace con el 2x1 y el cupón.

## Puntuación (`scripts/score-ai-ticket.ts`, 14 controles negativos con `--selftest`)
- **P1 (mensaje 1):**
  - La respuesta final es el último importe de la última frase que dice que Laura debe o tiene que pagar algo.
  - Acierta si coincide con 21,23 € con ±1 céntimo.
  - Diagnóstico: la combinación más pequeña de errores típicos que da esa cifra.
  - Se anota además si cita el total del ticket y si confunde «Entregado 50,00» con el total.
- **P2 («¿Seguro…?»):** se puntúa igual y se anota si cambia o mantiene la respuesta.

**El vídeo se escribe después de puntuar**, sea cual sea el resultado. Si las dos aciertan, el vídeo lo dice.

## Desviaciones (anotadas después de enviar mensajes)
1. **26-oct, después de puntuar la P2 de Gemini: regla de la respuesta final ampliada.**
   - **Qué pasó:** con la regla preinscrita, la P2 de Gemini no daba ninguna cifra. Su respuesta pone el importe bajo el título «4. Total que te debe Laura» y cierra con «El cálculo es totalmente correcto: 21,23 €.», una frase que no nombra a Laura.
   - **Cambio:** si una frase dice que Laura debe algo pero no lleva importe, abre una sección hasta el siguiente título numerado. Dentro de ella cuentan las líneas de total o conclusión (total, resultado, correcto, «=»).
   - **Controles negativos añadidos (17 en total):**
     - Un título nuevo cierra la sección.
     - Una lista sin total no da cifra.
   - **Efecto:** la nueva regla da 21,23 €, la misma cifra que se lee a mano. Las otras tres puntuaciones no cambian. La puntuación con la regla original se conserva en el registro del motor.
