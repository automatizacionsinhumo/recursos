# Recursos de «Automatización sin humo»

Aquí no se vende humo. Se prueba. Este repositorio guarda, vídeo a vídeo, todo lo necesario para repetir cada prueba del canal: el flujo o la hoja, los datos de ejemplo, la salida esperada calculada antes de ejecutar y un verificador.

Canal: https://www.youtube.com/@automatizacionsinhumo

| Vídeo | Carpeta |
|---|---|
| Este flujo de n8n terminó en verde y no quitó ni un duplicado | [`EP001/`](EP001/) |
| Pasó 30 facturas de PDF a Excel, terminó en verde y 11 estaban mal | [`EP002/`](EP002/) |
| Confirmó 50 solicitudes por correo: 5 personas recibieron dos y nadie se enteró | [`EP003/`](EP003/) |
| Importó un CSV de ventas y el total pasó de 1.484.818 € a 13.895 €: la coma y el punto | [`EP004/`](EP004/) |
| Quitó los duplicados, el contador decía 190 y faltaban tres personas | [`EP005/`](EP005/) |
| Comparó dos tarifas, contó 33 cambios, eran 16 y tres subidas de precio no aparecían | [`EP006/`](EP006/) |
| Pasé 30 facturas de PDF a Excel con ChatGPT y Gemini: ninguna avisó del error | [`EP007/`](EP007/) |
| Comparar dos Excel con ChatGPT y Gemini: los 16 cambios… y otros que no lo eran | [`EP008/`](EP008/) |
| Uní dos listas de clientes con ChatGPT: dijo 187 personas y eran 190 | [`EP009/`](EP009/) |
| Le pedí a ChatGPT repartir los gastos de un viaje: a dos amigos les cobró de más | [`EP010/`](EP010/) |

## Reglas de la casa
- Datos siempre sintéticos: ningún correo, cliente ni empresa reales.
- La salida esperada se calcula **antes** de ejecutar la herramienta; el verificador compara recuento, claves y valores, y trae controles negativos que deben fallar.
- Versiones y entorno declarados en cada carpeta. Si algo deja de funcionar en una versión nueva, se documenta, no se borra.

## Licencia
Todo el contenido de este repositorio es de dominio público ([CC0 1.0](LICENSE)). n8n, Excel, Google Sheets, Power Automate, ChatGPT y Gemini son marcas de sus respectivos propietarios; este material no está afiliado ni patrocinado por ellos.
