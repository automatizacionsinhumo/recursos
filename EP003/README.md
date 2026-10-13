# Recursos del vídeo «Confirmó 50 solicitudes por correo: 5 personas recibieron dos y nadie se enteró»

Todo lo necesario para repetir la prueba del vídeo. Datos sintéticos: personas y correos inventados en el dominio reservado `.test`; los correos solo llegan a una bandeja local de pruebas. Ningún correo real.

| Archivo | Qué es |
|---|---|
| `flujo_n8n_1_registrar_con_comprobaciones.json` | Paso 1: lee los envíos, comprueba datos y duplicados (mismo correo + misma solicitud) y escribe la hoja. **No envía nada.** |
| `flujo_n8n_2_aprobar_y_enviar.json` | Paso 2: una persona lo ejecuta tras mirar la hoja; envía **un** correo por solicitud registrada y marca la fila como enviada. Ejecutarlo otra vez no envía nada. |
| `flujo_n8n_primer_intento_confirmar_al_momento.json` | El primer intento del vídeo (confirmar al momento, «si falla, sigue»): 48 correos, 5 personas con dos, 2 fallos dados por buenos. Para reproducir el fallo. |
| `credencial_smtp_bandeja_local_mailpit.json` | Credencial SMTP de la bandeja local (host `mailpit`, puerto 1025, sin usuario ni contraseña). Impórtala con `n8n import:credentials` o créala a mano. |
| `envios_formulario_50.json` | Los 50 envíos sintéticos del formulario (42 normales, 5 reenvíos, 3 incompletos). |
| `respuesta_correcta_50_envios.json` | Para cada envío, el resultado esperado (registrada / duplicada con referencia / rechazada con motivo) y si debe recibir correo, calculado **antes** de ejecutar. |
| `verificar.py` | Compara tu hoja (y, si quieres, tu bandeja Mailpit) con la respuesta correcta. Sin dependencias. |

## Cómo repetirlo
1. Bandeja de pruebas: `docker run -d --name mailpit --network n8n-local -p 127.0.0.1:8025:8025 axllent/mailpit` (o la imagen de Mailpit que tengas) y n8n en la misma red Docker (`--network n8n-local`). Interfaz: http://127.0.0.1:8025. Nada sale de tu máquina.
2. Copia `envios_formulario_50.json` a la carpeta que n8n lee como `/data/envios.json` y crea una hoja vacía: `echo '[]' > /data/out/registro.json`.
3. Importa la credencial y los dos flujos; ejecuta el paso 1 y mira la hoja (`/data/out/registro.json` y `solicitudes.xlsx`); después ejecuta el paso 2 (y repítelo: no debe enviar nada).
4. Comprueba:

```bash
python3 verificar.py registro.json respuesta_correcta_50_envios.json --mailpit http://127.0.0.1:8025 --autocomprobar
```

`--autocomprobar` ejecuta manipulaciones que **deben** fallar (un duplicado marcado como bueno, un rechazado enviado, una fila borrada, un correo repetido o borrado). Si alguna no falla, el verificador no sirve y no te fíes del resultado.

## Lo que verás
- Primer intento: 50 filas «confirmadas», 48 correos; 5 personas con dos confirmaciones; 2 fallos de envío tragados por «si falla, sigue».
- Con los dos pasos: 42 registradas, 5 duplicadas (con referencia), 3 rechazadas (con motivo); 0 correos al registrar, 42 al aprobar, 0 al repetir.
- Límites: el duplicado es mismo correo + mismo asunto (la misma persona puede pedir dos cosas distintas); la aprobación es una persona que ejecuta el paso 2; para correo real, cambia la credencial SMTP por la de tu servidor, con las mismas comprobaciones. Con Google Forms o Typeform cambia el nodo de entrada, no la lógica.

Licencia: datos y scripts de este directorio, CC0 (dominio público). n8n es una marca de n8n GmbH; Mailpit es software libre de terceros; este material no está afiliado ni patrocinado por ellos.
