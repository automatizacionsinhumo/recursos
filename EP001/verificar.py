#!/usr/bin/env python3
"""Comprueba la salida de un flujo de «quitar duplicados» contra la salida esperada.

Uso:  python3 verificar.py salida_de_n8n.json salida_esperada_800_filas.json [--clave record_id]

Acepta la exportación de n8n (lista de items con "json") o una lista de filas. No usa red ni
librerías externas. Compara recuento, claves y valores de todos los campos, y explica qué falla.
Con --autocomprobar ejecuta cuatro manipulaciones que DEBEN fallar (controles negativos).
"""
import copy, json, sys

def cargar(ruta):
    with open(ruta, encoding="utf-8") as f:
        datos = json.load(f)
    if isinstance(datos, dict) and "data" in datos and isinstance(datos["data"], list):
        datos = datos["data"]
    filas = []
    for item in datos:
        if isinstance(item, dict) and "json" in item and isinstance(item["json"], dict):
            filas.append(item["json"])
        else:
            filas.append(item)
    # Caso típico de fallo: un único item con la lista entera dentro de un campo (p. ej. "data")
    if len(filas) == 1 and isinstance(filas[0], dict):
        for v in filas[0].values():
            if isinstance(v, list) and len(v) > 1 and all(isinstance(x, dict) for x in v):
                return v, "AVISO: la salida era 1 item con %d filas dentro del campo; el flujo no separó las filas" % len(v)
    return filas, None

def comparar(observado, esperado, clave):
    problemas = []
    if len(observado) != len(esperado):
        problemas.append("recuento: observado %d, esperado %d" % (len(observado), len(esperado)))
    obs = {}
    repetidas = []
    for fila in observado:
        k = fila.get(clave)
        if k in obs:
            repetidas.append(k)
        obs[k] = fila
    if repetidas:
        problemas.append("%d claves repetidas en la salida (p. ej. %s)" % (len(repetidas), repetidas[:3]))
    esp = {fila.get(clave): fila for fila in esperado}
    faltan = sorted(set(esp) - set(obs), key=str)
    sobran = sorted(set(obs) - set(esp), key=str)
    if faltan:
        problemas.append("faltan %d claves esperadas (p. ej. %s)" % (len(faltan), faltan[:3]))
    if sobran:
        problemas.append("sobran %d claves no esperadas (p. ej. %s)" % (len(sobran), sobran[:3]))
    distintos = [k for k in esp if k in obs and obs[k] != esp[k]]
    if distintos:
        problemas.append("%d filas con la misma clave pero valores distintos (p. ej. %s)" % (len(distintos), distintos[:3]))
    return problemas

def autocomprobar(esperado, clave):
    casos = {
        "quitar una fila única": esperado[:-1],
        "duplicar una fila en vez de la única": esperado[:-1] + [esperado[0]],
        "cambiar un valor manteniendo la clave": None,
        "cambiar una clave": None,
    }
    m = copy.deepcopy(esperado); campo = next(c for c in m[0] if c != clave); m[0][campo] = "CAMBIADO"; casos["cambiar un valor manteniendo la clave"] = m
    m2 = copy.deepcopy(esperado); m2[0][clave] = "CLAVE-FALSA"; casos["cambiar una clave"] = m2
    ok = True
    for nombre, datos in casos.items():
        problemas = comparar(datos, esperado, clave)
        print("  control negativo «%s»: %s" % (nombre, "FALLA ✓ (correcto)" if problemas else "NO FALLA ✗ (el verificador no sirve)"))
        ok = ok and bool(problemas)
    return ok

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    clave = "record_id"
    if "--clave" in sys.argv:
        clave = sys.argv[sys.argv.index("--clave") + 1]
        args = [a for a in args if a != clave]
    if len(args) < 2:
        print(__doc__); return 2
    observado, aviso = cargar(args[0]); esperado, _ = cargar(args[1])
    if aviso: print(aviso)
    problemas = comparar(observado, esperado, clave)
    print("Observado: %d filas · Esperado: %d filas · Clave: %s" % (len(observado), len(esperado), clave))
    if problemas:
        print("RESULTADO: NO COINCIDE"); [print("  -", p) for p in problemas]
    else:
        print("RESULTADO: COINCIDE (mismo recuento, mismas claves, mismos valores)")
    if "--autocomprobar" in sys.argv:
        print("Autocomprobación del verificador:")
        if not autocomprobar(esperado, clave): return 3
    return 0 if not problemas else 1

if __name__ == "__main__":
    raise SystemExit(main())
