# EP007 · Protocolo preinscrito: «30 facturas en PDF a Excel con IA»

**Escrito y versionado antes de enviar nada a ninguna IA (20-oct-2026).** Cualquier cambio posterior se anota como desviación con su motivo; no se repite una prueba para buscar un resultado mejor.

## Entrada
Las 30 facturas sintéticas públicas de EP002 (`episodes/EP002/data/facturas`, zip publicado sha256 `9fbe4437…cbd21`): 20 PDF digitales y 10 PDF de imagen sin capa de texto. Trampas conocidas: IVA del 10 % (0005, 0022), separador de miles (0009), etiquetas distintas (0017, 0026) y un total impreso que no cuadra con base + IVA (0013: impreso 416,74; base 336,15 + IVA 70,59 = 406,74).

## Herramientas
- Gemini, plan gratuito, modelo por defecto («Automático»), cuenta personal, conversación nueva.
- ChatGPT, plan gratuito, cuenta personal, conversación nueva.
- Sin instrucciones personalizadas añadidas para la prueba; se anota la fecha y el modelo que muestre la interfaz.

## Mensajes (literales, iguales para todas las herramientas)
1. Con las facturas adjuntas: «Te paso 30 facturas en PDF. Pásalas a una tabla que pueda copiar en Excel, con una fila por factura y estas columnas: archivo, número de factura, proveedor, NIF, fecha, base imponible, % de IVA, cuota de IVA y total.»
2. Después de la respuesta, sin corregir nada: «¿Has comprobado que en cada factura la base imponible más la cuota de IVA da exactamente el total? Dime cuáles no cuadran.»

Si la herramienta no admite 30 archivos en un mensaje, se envían en tandas del máximo admitido, en orden, en la misma conversación. Primera tanda: «Te voy a pasar 30 facturas en PDF en varias tandas. No hagas nada hasta que te diga que están todas.» Tandas intermedias sin texto o con «Sigue.». Tras la última: el mensaje 1 sustituyendo «Te paso 30 facturas en PDF» por «Ya están las 30».

Cuenta la **primera respuesta**. Si la herramienta se corta o pide continuar, se responde solo «Continúa». No se reformula ni se reintenta.

## Puntuación (script `scripts/score-ai-invoices.ts`, con autocomprobación negativa)
- 8 campos por factura × 30 = 240: número, proveedor, NIF, fecha, base, % IVA, cuota IVA y total.
- El total se compara con **lo impreso** en la factura (tarea de transcripción). En 0013 se clasifica aparte: copia el impreso sin avisar, corrige sin avisar o avisa del descuadre.
- Normalización (formato, no contenido): números en formato español o inglés iguales si difieren menos de medio céntimo; fechas en cualquier formato si es el mismo día; proveedor sin distinguir mayúsculas, acentos, puntuación ni espacios; NIF sin espacios ni guiones.
- Categorías por campo: correcto, incorrecto (valor distinto), vacío o marcado como ilegible. Por fila: facturas sin fila, filas que no corresponden a ninguna factura y filas duplicadas.
- Se informa por separado: digitales frente a escaneadas, y si la herramienta afirma haber procesado 30 cuando no lo ha hecho.

## Captura
Capturas reales de la interfaz con la barra lateral plegada (sin historial, cuenta ni ubicación). La tabla se lee del propio documento de la página, sin exportar a Drive. Texto íntegro de las respuestas guardado en `episodes/EP007/evidence/`.

## Adenda preinscrita (20-oct, antes de ejecutarla): prueba B con un único PDF
Motivo: ChatGPT gratis admitió 3 archivos y bloqueó el resto hasta el 21-oct 12:11 (ver evidence/chatgpt.run1.observations.md). Lo primero que haría un usuario es juntar las facturas en un solo PDF.
- Entrada: las mismas 30 facturas unidas en orden en `facturas_30_en_un_pdf.pdf` (pdfunite; se guarda su sha256).
- Ambas herramientas, conversación nueva, mismo modelo por defecto. Mensaje 1: «Te paso un PDF con 30 facturas. Pásalas a una tabla que pueda copiar en Excel, con una fila por factura y estas columnas: archivo, número de factura, proveedor, NIF, fecha, base imponible, % de IVA, cuota de IVA y total.» Mensaje 2: idéntico al de la prueba A.
- Como no hay nombres de archivo dentro de un PDF unido, la columna «archivo» no se puntúa; las filas se emparejan por número de factura. Resto de reglas, iguales.
- Gemini B se ejecuta el 20-oct; ChatGPT B en cuanto su límite lo permita (21-oct a partir de las 12:11). La prueba A de Gemini no se repite.
