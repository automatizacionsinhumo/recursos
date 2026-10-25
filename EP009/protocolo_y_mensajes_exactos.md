# EP009 · Protocolo preinscrito: «Une estos dos listados sin duplicados» con IA

**Escrito y versionado antes de enviar nada a ninguna IA (20-oct-2026).** Cualquier cambio posterior se anota como desviación, con fecha y motivo.

## Entrada
Los dos listados sintéticos públicos de EP005 (CC0), convertidos a Excel con los textos exactos: `clientes_tienda.xlsx` (120 filas) y `clientes_web.xlsx` (100 filas), columnas nombre, apellidos, email, teléfono y ciudad (`scripts/make-ep009-inputs.ts`, hashes en `data/inputs.json`). Respuesta correcta, calculada antes de EP005: `episodes/EP005/recursos/respuesta_correcta_190_personas.json`.
- **190 personas distintas.** 30 están en los dos listados: 24 escritas igual, 3 con el correo en mayúsculas o con espacios y 3 con el nombre sin acento, en minúsculas o con espacios de más.
- **Trampas:** 3 parejas de homónimos (mismo nombre y apellidos, distinto correo, teléfono y ciudad; una en cada listado) que son 6 personas distintas; 2 personas repetidas con un teléfono distinto en cada listado, que deben quedar una vez y marcadas para revisar.
- Unir por nombre da 190 filas con 3 repetidas dentro y 3 personas perdidas (comprobado en EP005).

## Herramientas
ChatGPT y Gemini, planes gratuitos, cuenta personal, conversación nueva, modelo por defecto, sin instrucciones personalizadas añadidas. Mismo día para las dos.

## Mensajes (literales)
1. Con los dos archivos adjuntos: «Te paso dos listados de clientes: el de la tienda y el de la web. Júntalos en uno solo sin duplicados, una fila por persona. ¿Cuántas personas distintas hay en total? Dime también qué personas estaban repetidas, en una tabla con nombre, apellidos y correo.»
2. «Escríbeme aquí el listado completo ya unido, en formato CSV con punto y coma (nombre;apellidos;email;telefono;ciudad), para copiarlo a Excel.»
3. Sin corregir nada: «¿Seguro que no queda nadie repetido y que no has quitado a nadie que no estuviera repetido?»

**Reglas.** Cuenta la primera respuesta de cada mensaje. Si una respuesta se corta, se retira o pide continuar, se envía una sola vez «Continúa». Si en el mensaje 2 escribe solo una parte a propósito («…y el resto igual»), se envía una sola vez «Escríbelo completo, por favor.» y se registran las dos respuestas. Si una herramienta no acepta los dos archivos a la vez, se envía el primero con el mensaje 1 y el segundo justo después con «Este es el segundo listado.». Si una herramienta no puede leer `.xlsx`, se repite en conversación nueva con los `.csv` del mismo contenido y se anota. Si una herramienta ofrece solo un archivo para descargar, no se descarga: se registra y se le pide el texto con el mensaje 2 tal cual.

## Registro
Texto de cada respuesta y tablas extraídos del DOM de la conversación, con comparación SHA-256 dentro de la página; observador de solo lectura para guardar respuestas que se escriben y luego se retiran; capturas a resolución completa recortadas sin datos personales. Archivos: `evidence/<herramienta>.answers.json` ({q1, q2, q3}), `evidence/<herramienta>.observations.md`.

## Puntuación (`scripts/score-ai-merge.ts`, 11 controles negativos con `--selftest`)
- **P1:** total declarado frente a 190; repetidas encontradas de 30, por tipo (escritas igual, correo con mayúsculas o espacios, nombre sin acento o en minúsculas); homónimos dados por repetidos; personas que no estaban repetidas y aparecen como tales (fantasmas).
- **P2 (listado):** filas; personas perdidas (y si son homónimos); repetidas que quedan (mismo correo sin espacios y en minúsculas); personas inventadas; errores de teléfono, ciudad o nombre (sin contar acentos, mayúsculas ni espacios; en los dos conflictos vale cualquiera de los dos teléfonos).
- **Conflictos de teléfono avisados:** si alguna respuesta nombra a Sergio Cano Lozano o a Adrián Lozano García con un teléfono distinto, o da los dos números.
- **P3:** lo que afirma frente a lo verificado en P1 y P2.

El título y la miniatura se escriben después de puntuar, sea cual sea el resultado; si las dos aciertan, el vídeo lo dice.

## Desviaciones (anotadas después de enviar mensajes)
1. **25-oct-2026, puntuador.** ChatGPT escribió el total como «Personas distintas: 187» (etiqueta antes del número) y puso dos correos en una misma celda para las personas que fusionó. `score-ai-merge.ts` se amplió para leer ese formato y para contar cada correo adicional de una celda como persona fusionada en esa fila (sin fila propia), con 4 controles negativos nuevos (15 en total). No cambia ninguna regla de puntuación: una persona sin fila propia ya contaba como perdida.
2. **25-oct-2026, Gemini en dos tiempos.** Al pulsar «Subir archivos», Gemini mostró por primera vez un aviso que hay que aceptar («Crear contenido a partir de imágenes y archivos»: derechos sobre los archivos y política de usos prohibidos). Se canceló para pedir permiso antes de aceptarlo; el propietario del canal lo autorizó («Sí a todo») y la prueba con Gemini se hizo ese mismo día por la tarde, con los mismos archivos y mensajes. Se mantiene «mismo día para las dos».
3. **25-oct-2026, extracción del mensaje 2.** El texto del CSV no se pudo leer por trozos (la herramienta bloquea texto con punto y coma) y se copió al portapapeles mediante un botón temporal en la página, con comparación SHA-256 entre la página y el archivo.
4. **25-oct-2026, puntuador (lectura del total).** Gemini escribió «Total de personas distintas en el listado unificado: 190 personas»; el lector del total admitía hasta 20 caracteres entre la etiqueta y los dos puntos y tomó «30 personas» de la línea anterior. Se amplió a 45 caracteres con un control negativo con esa frase exacta (16 en total). Las demás cifras no dependen de esa lectura.
