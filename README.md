# Recursos de «Automatización sin humo»

Aquí no se vende humo. Se prueba. Este repositorio guarda, vídeo a vídeo, todo lo necesario para repetir cada prueba del canal: el flujo o la hoja, los datos de ejemplo, la salida esperada calculada antes de ejecutar y un verificador.

Canal: https://www.youtube.com/@automatizacionsinhumo

| Vídeo | Carpeta |
|---|---|
| Este flujo de n8n terminó en verde y no quitó ni un duplicado | [`EP001/`](EP001/) |

## Reglas de la casa
- Datos siempre sintéticos: ningún correo, cliente ni empresa reales.
- La salida esperada se calcula **antes** de ejecutar la herramienta; el verificador compara recuento, claves y valores, y trae controles negativos que deben fallar.
- Versiones y entorno declarados en cada carpeta. Si algo deja de funcionar en una versión nueva, se documenta, no se borra.

## Licencia
Todo el contenido de este repositorio es de dominio público ([CC0 1.0](LICENSE)). n8n, Excel, Google Sheets y Power Automate son marcas de sus respectivos propietarios; este material no está afiliado ni patrocinado por ellos.
