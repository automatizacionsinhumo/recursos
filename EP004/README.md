# Recursos del vídeo «Importó un CSV de ventas y el total pasó de 1.484.818 € a 13.895 €: la coma y el punto»

Todo lo necesario para repetir la prueba del vídeo. Datos sintéticos: productos, clientes e importes inventados.

| Archivo | Qué es |
|---|---|
| `flujo_n8n_leer_formato_espanol.json` | El flujo del vídeo: lee el CSV declarando el formato español (punto de miles, coma decimal), códigos como texto, vacío = dato ausente, tres cifras tras la coma = revisar, y quita la marca invisible (BOM). Sin credenciales. Impórtalo en n8n: menú ⋯ → *Import from file*. |
| `flujo_n8n_primer_intento_convertir_a_numero.json` | El primer intento: cambia la coma por punto y convierte a número. Total de 13.895,64 € en vez de 1.484.818,94 €, códigos sin ceros, vacíos como 0 y columna fecha perdida. Para reproducir el fallo. |
| `ventas_200_filas_formato_espanol.csv` | 200 filas de ventas sintéticas: separador `;`, coma decimal, punto de miles, fechas dd/mm/aaaa, códigos con ceros, celdas vacías, devoluciones en negativo, dos celdas ambiguas («1,200»). Con BOM, como exporta Excel en español. |
| `respuesta_correcta_200_filas.json` | El valor real de cada celda y los totales, calculados **antes** de ejecutar. `null` = celda vacía (dato ausente). |
| `verificar.py` | Compara tu salida celda a celda con la respuesta correcta. Sin dependencias. |

## Cómo repetirlo
1. Copia el CSV a la carpeta que n8n lee como `/data/ventas.csv` (probado con n8n 2.42.3 en una instancia local; en Docker, monta la carpeta).
2. Importa el flujo y ejecútalo; la salida queda en `/data/out/` (JSON y Excel).
3. Comprueba:

```bash
python3 verificar.py EP004B.observed.json respuesta_correcta_200_filas.json --autocomprobar
```

`--autocomprobar` ejecuta manipulaciones que **deben** fallar (un código sin ceros, un céntimo de más, una celda vacía convertida en cero, una fila borrada, un total con los miles perdidos). Si alguna no falla, el verificador no sirve.

## Lo que verás
- Primer intento: «1.006,54» → «1.006.54» → 1,006 (el ordenador lee hasta el segundo punto). 167 importes pierden los miles; «00310» → 310; vacío → 0; la columna `fecha` llega como `﻿fecha` por el BOM y «desaparece».
- Con el formato declarado: 192 filas correctas, 6 incompletas (celdas vacías) y 2 a revisar (ambiguas); total de las correctas 1.484.815,99 €.
- Límites: hay que declarar el formato del archivo (si viene en inglés, el inglés); una celda mal escrita que cumpla el formato no se detecta; las ambiguas se marcan para una persona.

Licencia: datos y scripts de este directorio, CC0 (dominio público). n8n es una marca de n8n GmbH; este material no está afiliado ni patrocinado por n8n.
