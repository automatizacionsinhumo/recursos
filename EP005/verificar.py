#!/usr/bin/env python3
"""Comprueba, persona a persona, la salida de un flujo que une dos listados contra la respuesta correcta.

Uso:  python3 verificar.py salida_de_n8n.json respuesta_correcta_190_personas.json [--autocomprobar]

Acepta la exportación de n8n (lista de items con "json") o una lista de filas con las columnas
nombre, apellidos, email, telefono, ciudad (y, si existen, estado y aviso). La clave de persona es el correo
sin espacios y en minúsculas. Comprueba: una fila por persona (ni falta ni sobra nadie, ninguna repetida),
cada dato igual al esperado, correos normalizados y conflictos marcados como «revisar». Sin librerías externas.
Con --autocomprobar ejecuta manipulaciones que DEBEN fallar (controles negativos).
"""
import copy, json, sys

def clave(e): return str(e or "").strip().lower()

def cargar(ruta):
    with open(ruta, encoding="utf-8") as f:
        d = json.load(f)
    if isinstance(d, dict) and "rows" in d: return d
    if isinstance(d, dict) and "data" in d and isinstance(d["data"], list): d = d["data"]
    filas = [x["json"] if isinstance(x, dict) and "json" in x else x for x in d]
    return [r for r in filas if r.get("nombre") != "RESUMEN"], next((r for r in filas if r.get("nombre") == "RESUMEN"), None)

def comparar(filas, resumen, esperado):
    fallos = []
    exp = {e["clave"]: e for e in esperado["rows"]}
    vistos = {}
    for r in filas: vistos.setdefault(clave(r.get("email")), []).append(r)
    if len(filas) != len(exp): fallos.append("recuento: %d filas, esperadas %d personas" % (len(filas), len(exp)))
    for k, e in exp.items():
        if k not in vistos: fallos.append("falta %s %s <%s>" % (e["nombre"], e["apellidos"], k)); continue
        if len(vistos[k]) > 1: fallos.append("repetida %s (%d filas)" % (k, len(vistos[k])))
        r = vistos[k][0]
        for c in ("nombre", "apellidos", "telefono", "ciudad"):
            if str(r.get(c, "")) != e[c]: fallos.append("%s: %s %r, esperado %r" % (k, c, r.get(c), e[c]))
        if str(r.get("email", "")) != k: fallos.append("%s: correo sin normalizar %r" % (k, r.get("email")))
        if "estado" in r and r.get("estado") != e["estado"]: fallos.append("%s: estado %r, esperado %s" % (k, r.get("estado"), e["estado"]))
    for k in vistos:
        if k not in exp: fallos.append("sobra %s" % k)
    return fallos

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) < 2: print(__doc__); sys.exit(2)
    filas, resumen = cargar(args[0]); esperado = cargar(args[1])
    fallos = comparar(filas, resumen, esperado)
    estados = {}
    for r in filas: estados[r.get("estado", "(sin estado)")] = estados.get(r.get("estado", "(sin estado)"), 0) + 1
    print("Filas: %d · estados: %s" % (len(filas), ", ".join("%s=%d" % kv for kv in sorted(estados.items(), key=lambda kv: str(kv[0])))))
    if fallos:
        print("NO COINCIDE (%d problemas):" % len(fallos))
        for f in fallos[:40]: print("  -", f)
    else:
        print("COINCIDE con la respuesta correcta, persona a persona.")
    if "--autocomprobar" in sys.argv:
        print("\nControles negativos (deben fallar):")
        def mut(f):
            fs, rs = copy.deepcopy(filas), copy.deepcopy(resumen); f(fs, rs); return comparar(fs, rs, esperado)
        def borrar(fs, rs): fs.pop(0)
        def repetir(fs, rs): fs.append(copy.deepcopy(fs[1]))
        def telefono(fs, rs): fs[5]["telefono"] = "600 000 000"
        def conflicto(fs, rs):
            r = next(x for x in fs if x.get("estado") == "revisar"); r["estado"] = "ok"; r["aviso"] = ""
        def mayusculas(fs, rs): fs[2]["email"] = fs[2]["email"].upper()
        todos = True
        for nombre, f in [("una persona borrada", borrar), ("una fila repetida", repetir), ("un teléfono cambiado", telefono), ("un conflicto dado por bueno", conflicto), ("un correo sin normalizar", mayusculas)]:
            try: detectado = bool(mut(f))
            except StopIteration: detectado = False
            todos = todos and detectado
            print("  - %s: %s" % (nombre, "detectado" if detectado else "NO DETECTADO"))
        print("Verificador %s." % ("fiable" if todos else "NO fiable: no te fíes del resultado"))
        if not todos: sys.exit(1)
    sys.exit(1 if fallos else 0)

if __name__ == "__main__":
    main()
