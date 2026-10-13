#!/usr/bin/env python3
"""Comprueba, celda a celda, la salida de un flujo que importa ventas.csv contra la respuesta correcta.

Uso:  python3 verificar.py salida_de_n8n.json respuesta_correcta_200_filas.json [--autocomprobar]

Acepta la exportación de n8n (lista de items con "json") o una lista de filas con las columnas
fecha, codigo, unidades, precio_unitario, descuento_pct, importe (y, si existen, estado y avisos).
Comprueba: códigos como texto (ceros a la izquierda), fechas, valores numéricos exactos, vacío = ausente (null)
y no cero, celdas ambiguas marcadas como «revisar», y el total de las filas correctas. Sin librerías externas.
Con --autocomprobar ejecuta manipulaciones que DEBEN fallar (controles negativos).
"""
import copy, json, sys

def cargar(ruta):
    with open(ruta, encoding="utf-8") as f:
        d = json.load(f)
    if isinstance(d, dict) and "rows" in d: return d
    if isinstance(d, dict) and "data" in d and isinstance(d["data"], list): d = d["data"]
    filas = [x["json"] if isinstance(x, dict) and "json" in x else x for x in d]
    return [r for r in filas if r.get("fecha") not in ("TOTAL", "RESUMEN")], next((r for r in filas if r.get("fecha") == "RESUMEN"), None)

def cerca(a, b):
    if b is None: return a is None
    return isinstance(a, (int, float)) and abs(a - b) < 0.005

def comparar(filas, resumen, esperado):
    fallos = []
    exp = esperado["rows"]
    if len(filas) != len(exp): fallos.append("recuento: %d filas, esperadas %d" % (len(filas), len(exp)))
    for i, e in enumerate(exp):
        if i >= len(filas): break
        r = filas[i]; n = e["linea"]
        if str(r.get("codigo")) != e["codigo"]: fallos.append("línea %d: código %r, esperado %s (¿se perdieron los ceros?)" % (n, r.get("codigo"), e["codigo"]))
        if r.get("fecha") != e["fecha"]: fallos.append("línea %d: fecha %r, esperada %s" % (n, r.get("fecha"), e["fecha"]))
        for k in ("unidades", "precio_unitario", "descuento_pct", "importe"):
            if not cerca(r.get(k), e[k]): fallos.append("línea %d: %s %r, esperado %r" % (n, k, r.get(k), e[k]))
        quiero = "revisar" if "ambigua_tres_decimales" in e["flags"] else ("incompleta" if e["importe"] is None else "ok")
        if "estado" in r and r.get("estado") != quiero: fallos.append("línea %d: estado %r, esperado %s" % (n, r.get("estado"), quiero))
    total_ok = round(sum(e["importe"] for e in exp if e["importe"] is not None and "ambigua_tres_decimales" not in e["flags"]), 2)
    if resumen is not None and not cerca(resumen.get("importe"), total_ok): fallos.append("total %r, esperado %s (filas correctas)" % (resumen.get("importe"), total_ok))
    return fallos

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) < 2: print(__doc__); sys.exit(2)
    filas, resumen = cargar(args[0]); esperado = cargar(args[1])
    fallos = comparar(filas, resumen, esperado)
    estados = {}
    for r in filas: estados[r.get("estado", "(sin estado)")] = estados.get(r.get("estado", "(sin estado)"), 0) + 1
    print("Filas: %d · estados: %s%s" % (len(filas), ", ".join("%s=%d" % kv for kv in sorted(estados.items(), key=lambda kv: str(kv[0]))), "" if resumen is None else " · total: %s" % resumen.get("importe")))
    if fallos:
        print("NO COINCIDE (%d problemas):" % len(fallos))
        for f in fallos[:40]: print("  -", f)
    else:
        print("COINCIDE con la respuesta correcta, celda a celda.")
    if "--autocomprobar" in sys.argv:
        print("\nControles negativos (deben fallar):")
        def mut(f):
            fs, rs = copy.deepcopy(filas), copy.deepcopy(resumen); f(fs, rs); return comparar(fs, rs, esperado)
        def ceros(fs, rs): fs[0]["codigo"] = str(int(fs[0]["codigo"]))
        def centimo(fs, rs):
            r = next(x for x in fs if x.get("estado", "ok") == "ok" and x.get("importe") is not None); r["importe"] += 0.01
        def vacio_cero(fs, rs):
            r = next(x for x in fs if x.get("importe") is None); r["importe"] = 0; r["estado"] = "ok"
        def borrar(fs, rs): fs.pop(3)
        def miles(fs, rs):
            if rs is not None: rs["importe"] = rs["importe"] / 1000
        todos = True
        for nombre, f in [("un código sin ceros", ceros), ("un importe con un céntimo de más", centimo), ("una celda vacía convertida en cero", vacio_cero), ("una fila borrada", borrar), ("un total con los miles perdidos", miles)]:
            try: detectado = bool(mut(f))
            except StopIteration: detectado = False
            todos = todos and detectado
            print("  - %s: %s" % (nombre, "detectado" if detectado else "NO DETECTADO"))
        print("Verificador %s." % ("fiable" if todos else "NO fiable: no te fíes del resultado"))
        if not todos: sys.exit(1)
    sys.exit(1 if fallos else 0)

if __name__ == "__main__":
    main()
