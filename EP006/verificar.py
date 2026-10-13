#!/usr/bin/env python3
"""Comprueba la lista de cambios entre dos versiones de una tabla contra la respuesta correcta.

Uso:  python3 verificar.py salida_de_n8n.json respuesta_correcta_16_cambios.json [--autocomprobar]

Acepta la exportación de n8n (lista de items con "json") o una lista de líneas con las columnas
codigo, tipo (cambiado | añadido | eliminado), campo, antes, despues (y, si existen, estado y aviso).
Comprueba: ni un cambio de más (ruido de formato) ni de menos, valores anterior y nuevo iguales a los esperados y
posibles cambios de código marcados como «revisar». Sin librerías externas.
Con --autocomprobar ejecuta manipulaciones que DEBEN fallar (controles negativos).
"""
import copy, json, sys

def cargar(ruta):
    with open(ruta, encoding="utf-8") as f:
        d = json.load(f)
    if isinstance(d, dict) and "changes" in d: return d
    if isinstance(d, dict) and "data" in d and isinstance(d["data"], list): d = d["data"]
    filas = [x["json"] if isinstance(x, dict) and "json" in x else x for x in d]
    return [r for r in filas if r.get("codigo") != "RESUMEN"], next((r for r in filas if r.get("codigo") == "RESUMEN"), None)

def clave(c): return "%s|%s|%s" % (str(c.get("codigo", "")).strip(), c.get("tipo", ""), c.get("campo") or "")

def igual(a, b):
    if isinstance(b, (int, float)): return isinstance(a, (int, float)) and abs(a - b) < 0.005
    return str(a or "") == str(b or "")

def comparar(filas, resumen, esperado):
    fallos = []
    exp = {clave(c): c for c in esperado["changes"]}
    vistos = {}
    for r in filas: vistos.setdefault(clave(r), []).append(r)
    if len(filas) != len(exp): fallos.append("recuento: %d líneas, esperadas %d" % (len(filas), len(exp)))
    for k, e in exp.items():
        if k not in vistos: fallos.append("falta el cambio %s" % k); continue
        if len(vistos[k]) > 1: fallos.append("repetido %s" % k)
        r = vistos[k][0]
        if not igual(r.get("antes"), e["antes"]) or not igual(r.get("despues"), e["despues"]): fallos.append("%s: antes/después %r→%r, esperado %r→%r" % (k, r.get("antes"), r.get("despues"), e["antes"], e["despues"]))
        if "estado" in r and r.get("estado") != e["estado"]: fallos.append("%s: estado %r, esperado %s" % (k, r.get("estado"), e["estado"]))
    for k in vistos:
        if k not in exp: fallos.append("sobra %s (¿ruido de formato contado como cambio?)" % k)
    return fallos

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) < 2: print(__doc__); sys.exit(2)
    filas, resumen = cargar(args[0]); esperado = cargar(args[1])
    fallos = comparar(filas, resumen, esperado)
    tipos = {}
    for r in filas: tipos[r.get("tipo", "?")] = tipos.get(r.get("tipo", "?"), 0) + 1
    print("Cambios: %d · %s" % (len(filas), ", ".join("%s=%d" % kv for kv in sorted(tipos.items()))))
    if fallos:
        print("NO COINCIDE (%d problemas):" % len(fallos))
        for f in fallos[:40]: print("  -", f)
    else:
        print("COINCIDE con la respuesta correcta, cambio a cambio.")
    if "--autocomprobar" in sys.argv:
        print("\nControles negativos (deben fallar):")
        def mut(f):
            fs, rs = copy.deepcopy(filas), copy.deepcopy(resumen); f(fs, rs); return comparar(fs, rs, esperado)
        def omitir(fs, rs): fs.pop(next(i for i, x in enumerate(fs) if x.get("campo") == "precio"))
        def inventar(fs, rs): fs.append({"codigo": "00001", "tipo": "cambiado", "campo": "precio", "antes": 1, "despues": 1, "estado": "ok"})
        def intercambiar(fs, rs):
            r = next(x for x in fs if x.get("campo") == "precio"); r["antes"], r["despues"] = r["despues"], r["antes"]
        def nuevo(fs, rs): fs.pop(next(i for i, x in enumerate(fs) if x.get("tipo") == "añadido" and x.get("estado", "ok") == "ok"))
        def revisar(fs, rs):
            r = next(x for x in fs if x.get("estado") == "revisar"); r["estado"] = "ok"; r["aviso"] = ""
        todos = True
        for nombre, f in [("una subida de precio omitida", omitir), ("un cambio inventado por formato", inventar), ("antes y después intercambiados", intercambiar), ("un producto nuevo sin reportar", nuevo), ("un posible cambio de código dado por bueno", revisar)]:
            try: detectado = bool(mut(f))
            except StopIteration: detectado = False
            todos = todos and detectado
            print("  - %s: %s" % (nombre, "detectado" if detectado else "NO DETECTADO"))
        print("Verificador %s." % ("fiable" if todos else "NO fiable: no te fíes del resultado"))
        if not todos: sys.exit(1)
    sys.exit(1 if fallos else 0)

if __name__ == "__main__":
    main()
