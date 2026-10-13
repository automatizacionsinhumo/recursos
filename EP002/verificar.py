#!/usr/bin/env python3
"""Comprueba la salida del flujo «facturas PDF → Excel» contra la respuesta correcta.

Uso:  python3 verificar.py salida_de_n8n.json respuesta_correcta_30_facturas.json [--autocomprobar]

Acepta la exportación de n8n (lista de items con "json") o una lista de filas con las columnas
archivo, estado, base, iva, total (las que escribe el flujo con comprobaciones). Sin red ni librerías.
Para cada factura comprueba el estado esperado (ok / revisar / sin_texto) y, cuando hay texto, los
importes (base, IVA y total impreso) y que no se haya inventado ningún importe en las escaneadas.
Con --autocomprobar ejecuta cuatro manipulaciones que DEBEN fallar (controles negativos).
"""
import copy, json, sys

def cargar(ruta):
    with open(ruta, encoding="utf-8") as f:
        datos = json.load(f)
    if isinstance(datos, dict) and "data" in datos and isinstance(datos["data"], list):
        datos = datos["data"]
    return [x["json"] if isinstance(x, dict) and "json" in x and isinstance(x["json"], dict) else x for x in datos]

def cerca(a, b):
    return a is not None and b is not None and abs(float(a) - float(b)) < 0.005

def comparar(observado, esperado):
    fallos = []
    por_archivo = {r.get("archivo"): r for r in observado}
    for e in esperado:
        r = por_archivo.get(e["file"])
        if r is None:
            fallos.append("%s: falta la fila" % e["file"]); continue
        quiero = {"ok": "ok", "revisar_no_cuadra": "revisar", "sin_texto": "sin_texto"}[e["expected_status"]]
        if r.get("estado") != quiero:
            fallos.append("%s: estado %s, esperado %s" % (e["file"], r.get("estado"), quiero))
        if quiero == "sin_texto":
            for k in ("base", "iva", "total"):
                if r.get(k) is not None:
                    fallos.append("%s: importe inventado en un PDF sin texto (%s=%s)" % (e["file"], k, r.get(k)))
        else:
            if not cerca(r.get("base"), e["base"]): fallos.append("%s: base %s ≠ %s" % (e["file"], r.get("base"), e["base"]))
            if not cerca(r.get("iva"), e["iva"]): fallos.append("%s: iva %s ≠ %s" % (e["file"], r.get("iva"), e["iva"]))
            if not cerca(r.get("total"), e["total_impreso"]): fallos.append("%s: total leído %s ≠ impreso %s" % (e["file"], r.get("total"), e["total_impreso"]))
    if len(observado) != len(esperado):
        fallos.append("recuento: %d filas, esperadas %d" % (len(observado), len(esperado)))
    return fallos

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) < 2:
        print(__doc__); sys.exit(2)
    observado, esperado = cargar(args[0]), cargar(args[1])
    fallos = comparar(observado, esperado)
    estados = {}
    for r in observado: estados[r.get("estado")] = estados.get(r.get("estado"), 0) + 1
    print("Filas: %d · estados: %s" % (len(observado), ", ".join("%s=%d" % kv for kv in sorted(estados.items(), key=lambda kv: str(kv[0])))))
    if fallos:
        print("NO COINCIDE (%d problemas):" % len(fallos))
        for f in fallos[:40]: print("  -", f)
    else:
        print("COINCIDE con la respuesta correcta: estados e importes, sin importes inventados.")
    if "--autocomprobar" in sys.argv:
        print("\nControles negativos (deben fallar):")
        def mutado(f):
            o = copy.deepcopy(observado); f(o); return o
        def un_centimo(o):
            r = next(x for x in o if x.get("estado") == "ok"); r["total"] = float(r["total"]) + 0.01
        def borrar(o):
            o.pop(0)
        def imagen_ok(o):
            r = next(x for x in o if x.get("estado") == "sin_texto"); r["estado"] = "ok"; r["base"], r["iva"], r["total"] = 100, 21, 121
        def descuadre_ok(o):
            r = next(x for x in o if x.get("estado") == "revisar"); r["estado"] = "ok"
        todos = True
        for nombre, f in [("un total cambiado en un céntimo", un_centimo), ("una fila borrada", borrar), ("una escaneada marcada ok con importes inventados", imagen_ok), ("la factura descuadrada marcada ok", descuadre_ok)]:
            try:
                detectado = bool(comparar(mutado(f), esperado))
            except StopIteration:
                detectado = False
            todos = todos and detectado
            print("  - %s: %s" % (nombre, "detectado" if detectado else "NO DETECTADO"))
        print("Verificador %s." % ("fiable" if todos else "NO fiable: no te fíes del resultado"))
        if not todos: sys.exit(1)
    sys.exit(1 if fallos else 0)

if __name__ == "__main__":
    main()
