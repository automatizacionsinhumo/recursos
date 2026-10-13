# Recursos del vídeo «Quitó los duplicados, el contador decía 190 y faltaban tres personas»

Todo lo necesario para repetir la prueba del vídeo. Datos sintéticos: nombres, correos y teléfonos inventados (dominio reservado `correo-de-prueba.test`).

| Archivo | Qué es |
|---|---|
| `flujo_n8n_una_fila_por_correo.json` | El flujo del vídeo: lee los dos listados, los junta y deja una fila por persona usando el correo sin espacios y en minúsculas como clave; si el mismo correo trae datos distintos, marca la fila para revisar. Sin credenciales. Impórtalo en n8n: menú ⋯ → *Import from file*. |
| `flujo_n8n_primer_intento_por_nombre.json` | El primer intento: junta los listados y quita duplicados comparando nombre y apellidos tal cual. Devuelve 190 filas (el número correcto) con 3 repetidas dentro y 3 personas perdidas. Para reproducir el fallo. |
| `clientes_tienda_120_filas.csv` · `clientes_web_100_filas.csv` | Los dos listados sintéticos (separador `;`): 30 personas están en los dos; 3 con el correo escrito con mayúsculas o espacios, 3 con el nombre sin acentos o en minúsculas, 3 parejas de homónimos y 2 teléfonos distintos. |
| `respuesta_correcta_190_personas.json` | Una fila por persona, calculada **antes** de ejecutar, con los datos esperados y qué filas deben quedar «a revisar». |
| `verificar.py` | Compara tu listado unido, persona a persona, con la respuesta correcta. Sin dependencias. |

## Cómo repetirlo
1. Copia los dos CSV a la carpeta que n8n lee como `/data/` (probado con n8n 2.42.3 en una instancia local; en Docker, monta la carpeta).
2. Importa el flujo y ejecútalo; la salida queda en `/data/out/` (JSON y Excel).
3. Comprueba:

```bash
python3 verificar.py EP005B.observed.json respuesta_correcta_190_personas.json --autocomprobar
```

`--autocomprobar` ejecuta manipulaciones que **deben** fallar (una persona borrada, una fila repetida, un teléfono cambiado, un conflicto dado por bueno, un correo sin normalizar). Si alguna no falla, el verificador no sirve.

## Lo que verás
- Primer intento (por nombre): 190 filas, exactamente el número correcto; pero «Pérez» con acento y «Perez» sin acento siguen siendo dos filas, y las tres parejas que se llaman igual se funden en una persona. El contador cuadra y el listado está mal.
- Por correo normalizado: 190 personas, 188 correctas y 2 a revisar (teléfono distinto en cada listado), comprobado persona a persona.
- Límites: sirve cuando el correo identifica a la persona; dos personas con el mismo correo, o una con dos correos, no se detectan. Los conflictos se marcan para que alguien los mire.

Licencia: datos y scripts de este directorio, CC0 (dominio público). n8n es una marca de n8n GmbH; este material no está afiliado ni patrocinado por n8n.
