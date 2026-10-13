# Recursos del vídeo «Este flujo de n8n terminó en verde y no quitó ni un duplicado»

Todo lo necesario para repetir la prueba del vídeo. Datos sintéticos: ningún correo, cliente ni empresa reales.

| Archivo | Qué es |
|---|---|
| `flujo_n8n_quitar_duplicados.json` | El flujo de n8n del vídeo (con Split Out), sin credenciales. Impórtalo en n8n: menú ⋯ → *Import from file*. |
| `datos_entrada_1000_filas.json` | 1.000 filas sintéticas: 800 únicas y 200 repeticiones exactas. Identidad: `record_id`. |
| `salida_esperada_800_filas.json` | La salida correcta, calculada **antes** de ejecutar el flujo. |
| `verificar.py` | Comprueba tu salida contra la esperada: recuento, claves y valores. Sin dependencias. |

## Cómo repetirlo
1. Importa el flujo en n8n (probado con la versión 2.42.3 en una instancia local) y apunta el nodo de lectura al archivo de entrada.
2. Ejecuta el flujo y exporta la salida del último nodo como JSON (`salida.json`).
3. Comprueba:

```bash
python3 verificar.py salida.json salida_esperada_800_filas.json --autocomprobar
```

`--autocomprobar` ejecuta cuatro manipulaciones que **deben** fallar (quitar una fila única, duplicar una, cambiar un valor, cambiar una clave). Si alguna no falla, el verificador no sirve y no te fíes del resultado.

## Lo que verás
- Sin **Split Out**, el flujo termina en verde y la salida es **1 item** con las 1.000 filas dentro: no quitó nada. El verificador lo avisa.
- Con Split Out y *Remove Duplicates* comparando **todos los campos**: 800 filas, coincide.
- Caso límite (misma clave, contenido distinto): 801 filas comparando todos los campos; 800 comparando solo `record_id`, y la segunda desaparece sin aviso. Decide tú qué política quieres.

Licencia: datos y scripts de este directorio, CC0 (dominio público). n8n es una marca de n8n GmbH; este material no está afiliado ni patrocinado por n8n.
