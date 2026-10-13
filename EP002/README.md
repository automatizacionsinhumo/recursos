# Recursos del vídeo «Pasó 30 facturas de PDF a Excel, terminó en verde y 11 estaban mal»

Todo lo necesario para repetir la prueba del vídeo. Datos sintéticos: empresas, NIF e importes inventados; ninguna factura real.

| Archivo | Qué es |
|---|---|
| `flujo_n8n_facturas_con_comprobaciones.json` | El flujo del vídeo con las tres comprobaciones (¿hay texto? ¿están los seis datos? ¿base + IVA = total?), sin credenciales. Impórtalo en n8n: menú ⋯ → *Import from file*. |
| `flujo_n8n_primer_intento_sin_comprobar.json` | El primer intento: termina en verde y escribe 11 filas mal sin avisar. Para reproducir el fallo. |
| `facturas_sinteticas_30_pdf.zip` | 30 facturas: 20 PDF digitales (con capa de texto) y 10 «escaneadas» (imagen sin texto). Incluye `README.json` con los hashes. |
| `respuesta_correcta_30_facturas.json` | Para cada factura, los importes correctos y el estado esperado, calculados **antes** de ejecutar: 19 `ok`, 1 `revisar_no_cuadra` (FAC-2026-0013) y 10 `sin_texto`. |
| `verificar.py` | Compara la salida de tu flujo con la respuesta correcta: estados, importes y que no se invente nada en las escaneadas. Sin dependencias. |

## Cómo repetirlo
1. Descomprime las facturas en una carpeta a la que n8n tenga acceso (en Docker: monta la carpeta y apunta el nodo *Leer facturas* a ella; probado con n8n 2.42.3 en una instancia local, con `/data/facturas/*.pdf`).
2. Importa el flujo con comprobaciones, ajusta las rutas de los nodos *Guardar Excel* y *Guardar JSON*, y ejecútalo.
3. Comprueba la salida JSON (o exporta la salida del nodo *Sacar importes y comprobar*):

```bash
python3 verificar.py salida.json respuesta_correcta_30_facturas.json --autocomprobar
```

`--autocomprobar` ejecuta cuatro manipulaciones que **deben** fallar (cambiar un céntimo, borrar una fila, marcar una escaneada como ok, marcar la factura descuadrada como ok). Si alguna no falla, el verificador no sirve y no te fíes del resultado.

## Lo que verás
- Primer intento: 30 filas en verde; 10 con las casillas vacías (las escaneadas: *Extract From PDF* devuelve texto vacío sin error) y 1 con un total que no cuadra, copiado tal cual.
- Con comprobaciones: cada fila lleva `estado` y `motivo`; las que hay que mirar salen arriba. 10 `sin_texto`, 1 `revisar`, 19 `ok`. Coincide con la respuesta correcta.
- Límites: sirve para PDF digitales con una estructura parecida (ajusta las expresiones del nodo de código a tus facturas). Las escaneadas se apartan; leerlas (OCR) es otro paso. Un importe mal leído que cuadre por casualidad no se detecta.

Licencia: datos y scripts de este directorio, CC0 (dominio público). n8n es una marca de n8n GmbH; este material no está afiliado ni patrocinado por n8n.
