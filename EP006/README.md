# Recursos del vídeo «Comparó dos tarifas, contó 33 cambios, eran 16 y tres subidas de precio no aparecían»

Todo lo necesario para repetir la prueba del vídeo. Datos sintéticos: productos, precios y proveedores inventados.

| Archivo | Qué es |
|---|---|
| `flujo_n8n_limpiar_y_comparar.json` | El flujo del vídeo: lee las dos tarifas, limpia antes de comparar (código sin espacios, números como números, espacios y mayúsculas ignorados), empareja por código y saca una línea por cambio con el valor anterior y el nuevo; un retirado y un nuevo con el mismo nombre se marcan como posible cambio de código. Sin credenciales. Impórtalo en n8n: menú ⋯ → *Import from file*. |
| `flujo_n8n_primer_intento_comparar_tal_cual.json` | El primer intento: el nodo Compare Datasets tal cual, emparejando por código letra a letra. Reporta 33 «cambios» (23 distintas + 5 solo en enero + 5 solo en febrero) cuando hay 16; 14 son solo formato y 3 subidas de precio quedan escondidas. Para reproducir el fallo. |
| `tarifa_enero_150_filas.csv` · `tarifa_febrero_150_filas.csv` | Las dos versiones sintéticas (separador `;`, coma decimal). Febrero viene en otro orden, con 14 celdas que solo cambian de forma y 3 códigos con un espacio al final. |
| `respuesta_correcta_16_cambios.json` | La lista exacta de cambios, calculada **antes** de ejecutar: 8 precios, 3 existencias, 1 nombre, 2 nuevos, 2 retirados; 2 líneas «a revisar» (posible cambio de código 00120 → 00152). |
| `verificar.py` | Compara tu lista de cambios, uno a uno, con la respuesta correcta. Sin dependencias. |

## Cómo repetirlo
1. Copia los dos CSV a la carpeta que n8n lee como `/data/` con los nombres `tarifa_enero.csv` y `tarifa_febrero.csv` (probado con n8n 2.42.3 en una instancia local; en Docker, monta la carpeta).
2. Importa el flujo y ejecútalo; la salida queda en `/data/out/` (JSON y Excel).
3. Comprueba:

```bash
python3 verificar.py EP006B.observed.json respuesta_correcta_16_cambios.json --autocomprobar
```

`--autocomprobar` ejecuta manipulaciones que **deben** fallar (una subida de precio omitida, un cambio inventado por formato, antes y después intercambiados, un producto nuevo sin reportar, un posible cambio de código dado por bueno). Si alguna no falla, el verificador no sirve.

## Lo que verás
- Primer intento: «12,50» y «12,500» cuentan como distintos; «Papel A4 » con espacio al final también; y un código con un espacio al final sale como retirado y como nuevo a la vez, con su subida de precio escondida entre medias.
- Limpiando antes de comparar: 16 cambios, cada uno con lo que había y lo que hay ahora, y 2 marcados para que alguien decida si es el mismo producto con otro código.
- Límites: sirve cuando el código identifica la fila; si cambian el código y el nombre a la vez, el flujo verá un retirado y un nuevo.

Licencia: datos y scripts de este directorio, CC0 (dominio público). n8n es una marca de n8n GmbH; este material no está afiliado ni patrocinado por n8n.
