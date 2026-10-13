#!/usr/bin/env python3
"""Comprueba la hoja de solicitudes y los correos de tu bandeja contra la respuesta correcta.

Uso:  python3 verificar.py registro.json respuesta_correcta_50_envios.json [--mailpit http://127.0.0.1:8025] [--autocomprobar]

registro.json: la hoja escrita por el flujo 2 (lista de filas con id, email, estado, correo_enviado).
Con --mailpit, descarga los correos de la bandeja local (API de Mailpit) y comprueba que cada solicitud
registrada recibió exactamente un correo (la referencia va en el asunto) y que duplicados y rechazados, ninguno.
Con --autocomprobar ejecuta manipulaciones que DEBEN fallar (controles negativos). Sin librerías externas.
"""
import copy, json, sys, urllib.request

def cargar(ruta):
    with open(ruta, encoding="utf-8") as f:
        d = json.load(f)
    if isinstance(d, dict) and "rows" in d: return d
    if isinstance(d, dict) and "data" in d and isinstance(d["data"], list): d = d["data"]
    return [x["json"] if isinstance(x, dict) and "json" in x else x for x in d]

def correos_de(url):
    with urllib.request.urlopen(url.rstrip("/") + "/api/v1/messages?limit=5000") as r:
        return json.load(r)["messages"]

def comparar(hoja, esperado, correos):
    fallos = []
    filas = {r.get("id"): r for r in hoja}
    for e in esperado["rows"]:
        r = filas.get(e["id"])
        if r is None: fallos.append("%s: falta en la hoja" % e["id"]); continue
        if r.get("estado") != e["outcome"]: fallos.append("%s: estado %s, esperado %s" % (e["id"], r.get("estado"), e["outcome"]))
        if e["outcome"] == "duplicada" and r.get("duplicado_de") != e["duplicate_of"]: fallos.append("%s: duplicado_de %s, esperado %s" % (e["id"], r.get("duplicado_de"), e["duplicate_of"]))
        if e["email_expected"] and not r.get("correo_enviado"): fallos.append("%s: no está marcada como enviada" % e["id"])
        if not e["email_expected"] and r.get("correo_enviado"): fallos.append("%s: marcada como enviada sin deber" % e["id"])
        if correos is not None:
            n = sum(1 for m in correos if ("%s:" % e["id"]) in (m.get("Subject") or ""))
            if e["email_expected"] and n != 1: fallos.append("%s: %d correos en la bandeja (esperado 1)" % (e["id"], n))
            if not e["email_expected"] and n != 0: fallos.append("%s: %d correos en la bandeja (esperado 0, %s)" % (e["id"], n, e["outcome"]))
    if len(hoja) != len(esperado["rows"]): fallos.append("recuento: %d filas, esperadas %d" % (len(hoja), len(esperado["rows"])))
    if correos is not None and len(correos) != esperado["totals"]["correos_esperados"]: fallos.append("bandeja: %d correos, esperados %d" % (len(correos), esperado["totals"]["correos_esperados"]))
    return fallos

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) < 2: print(__doc__); sys.exit(2)
    hoja, esperado = cargar(args[0]), cargar(args[1])
    correos = None
    if "--mailpit" in sys.argv:
        correos = correos_de(sys.argv[sys.argv.index("--mailpit") + 1])
    fallos = comparar(hoja, esperado, correos)
    estados = {}
    for r in hoja: estados[r.get("estado")] = estados.get(r.get("estado"), 0) + 1
    print("Filas: %d · estados: %s%s" % (len(hoja), ", ".join("%s=%d" % kv for kv in sorted(estados.items(), key=lambda kv: str(kv[0]))), "" if correos is None else " · correos en la bandeja: %d" % len(correos)))
    if fallos:
        print("NO COINCIDE (%d problemas):" % len(fallos))
        for f in fallos[:40]: print("  -", f)
    else:
        print("COINCIDE con la respuesta correcta.")
    if "--autocomprobar" in sys.argv:
        print("\nControles negativos (deben fallar):")
        def mut_hoja(f):
            h = copy.deepcopy(hoja); f(h); return comparar(h, esperado, correos)
        def dup_ok(h):
            r = next(x for x in h if x.get("estado") == "duplicada"); r["estado"] = "registrada"
        def rech_enviado(h):
            r = next(x for x in h if x.get("estado") == "rechazada"); r["correo_enviado"] = True
        def borrar(h):
            h.pop(0)
        pruebas = [("un duplicado marcado como registrada", lambda: mut_hoja(dup_ok)), ("un rechazado marcado como enviado", lambda: mut_hoja(rech_enviado)), ("una fila borrada", lambda: mut_hoja(borrar))]
        if correos is not None:
            pruebas.append(("un correo repetido en la bandeja", lambda: comparar(hoja, esperado, correos + [correos[0]])))
            pruebas.append(("un correo borrado de la bandeja", lambda: comparar(hoja, esperado, correos[1:])))
        todos = True
        for nombre, f in pruebas:
            try: detectado = bool(f())
            except StopIteration: detectado = False
            todos = todos and detectado
            print("  - %s: %s" % (nombre, "detectado" if detectado else "NO DETECTADO"))
        print("Verificador %s." % ("fiable" if todos else "NO fiable: no te fíes del resultado"))
        if not todos: sys.exit(1)
    sys.exit(1 if fallos else 0)

if __name__ == "__main__":
    main()
