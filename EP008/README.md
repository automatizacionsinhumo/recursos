# Recursos del vídeo «Comparar dos Excel con ChatGPT y Gemini: los 16 cambios… y otros que no lo eran»

Todo lo necesario para repetir la prueba con tu IA. Datos sintéticos: productos, precios y proveedores inventados.

| Archivo | Qué es |
|---|---|
| `plantilla_comprobar_cambios.xlsx` | Pega la tabla de cambios de tu IA en la hoja «Comprobar» (desde la fila 6, columnas A a E). Calcula febrero − enero, marca «solo formato» lo que no es un cambio (mismo número, o mismo texto sin espacios sobrantes ni mayúsculas) y te dice cuál fue de verdad la mayor subida de precio. La hoja «Ejemplo ChatGPT» lleva su tabla real. |
| `tarifa_enero.csv` · `tarifa_febrero.csv` | Las dos tarifas de 150 productos (separador `;`, coma decimal). Febrero viene en otro orden y con 14 diferencias de solo formato. |
| `respuesta_correcta_16_cambios.json` | La lista exacta de cambios, calculada antes de la prueba: 8 precios, 3 existencias, 1 nombre, 2 nuevos y 2 retirados; uno de los retirados reaparece con otro código. |
| `protocolo_y_mensajes_exactos.md` | Los dos mensajes literales y las reglas de puntuación, escritos antes de abrir ninguna IA. |
| `resultados/` | Las tablas que devolvió cada IA y la puntuación. |

## Qué pasó (20 de octubre de 2026, planes gratuitos)
- **Las dos** encontraron los 16 cambios reales y las 3 subidas de precio escondidas tras un código con un espacio al final.
- **Gemini** retiró su primera respuesta («Soy un modelo de lenguage…»); tras «continúa», su tabla traía 2 «cambios» que eran solo un doble espacio. Nunca avisó de que el 00120 y el 00152 son el mismo producto.
- **ChatGPT** metió 5 filas de solo formato (mayúsculas y doble espacio) y concluyó que la mayor subida era la del 00073 (+12,13 €). La mayor es la del 00058 (+18,93 €).
- **Al preguntarles** «¿seguro que están todos y que ninguno es solo formato?», las dos separaron bien los 16 reales y los 14 de formato, y ChatGPT avisó del cambio de código. En otra prueba del canal (facturas, EP007) esa misma pregunta llevó a una IA a afirmar algo falso: preguntar no sustituye a comprobar.

## Cómo repetirlo
1. Pásale a tu IA las dos tarifas con el primer mensaje del protocolo.
2. Pega su tabla en la plantilla: mira cuántas filas son «solo formato» y cuál es la mayor subida calculada.
3. Si quieres la comprobación completa, compara su lista con `respuesta_correcta_16_cambios.json`.

Límites: la plantilla solo comprueba lo que la IA lista; un cambio que la IA no mencione no aparece. Prueba de un día con planes gratuitos.

Licencia: datos, plantilla y textos de este directorio, CC0 (dominio público). ChatGPT es una marca de OpenAI y Gemini de Google; este material no está afiliado ni patrocinado por ninguna de las dos.
