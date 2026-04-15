import random

jugadores = []
historial = []
estadisticas = {}

def registrar():
    print("\n" + "="*20)
    print("registro de jugadores")
    print("="*20)

    while True:
        nombre = input("escribe el nombre del jugador: ")

        if nombre in jugadores:
            print("="*10 + " ese nombre ya esta " + "="*10)
            continue

        jugadores.append(nombre)
        print("="*10 + f" agregado: {nombre} " + "="*10)

        estadisticas[nombre] = {
            "victorias": 0,
            "piedra": 0,
            "papel": 0,
            "tijera": 0,
            "eliminado": None
        }

        if len(jugadores) >= 4:
            continuar = input("quieres agregar otro jugador? (s/n): ")
            if continuar.lower() != "s":
                break


def gana(e1, e2):
    if e1 == e2:
        return 0
    
    if (e1 == "piedra" and e2 == "tijera") or \
        (e1 == "tijera" and e2 == "papel") or \
        (e1 == "papel" and e2 == "piedra"):
        return 1
    else:
        return 2
    

def juego(j1, j2, ronda):
    v1 = 0
    v2 = 0

    print("\n" + "="*20)
    print(f"{j1} vs {j2} (mejor de 3)")
    print("="*20)

    while v1 < 2 and v2 < 2:
        e1 = input(f"{j1}, elige (piedra/papel/tijera): ").lower()
        e2 = input(f"{j2}, elige (piedra/papel/tijera): ").lower()

        if e1 not in ["piedra", "papel", "tijera"] or e2 not in ["piedra", "papel", "tijera"]:
            print("="*10 + " jugada invalida " + "="*10)
            continue

        estadisticas[j1][e1] += 1
        estadisticas[j2][e2] += 1

        r = gana(e1, e2)

        if r == 0:
            print("="*10 + " empate " + "="*10)
        elif r == 1:
            v1 += 1
            print("="*10 + f" punto para {j1} " + "="*10)
        else:
            v2 += 1
            print("="*10 + f" punto para {j2} " + "="*10)

    g = j1 if v1 == 2 else j2
    p = j2 if g == j1 else j1

    print("="*10 + f" gana {g} " + "="*10)

    estadisticas[g]["victorias"] += 1
    estadisticas[p]["eliminado"] = ronda

    historial.append([f"ronda {ronda}", f"{j1} vs {j2}", f"gano {g}"])

    return g


def torneo():
    ronda = 1
    actual = jugadores.copy()

    print("\n" + "="*25)
    print("inicia el torneo")
    print("="*25)

    while len(actual) > 1:
        print("\n" + "="*15 + f" ronda {ronda} " + "="*15)

        random.shuffle(actual)
        ganadores = []

        i = 0
        while i < len(actual):
            if i == len(actual) - 1:
                print("="*10 + f" {actual[i]} pasa solo " + "="*10)
                ganadores.append(actual[i])
                break

            j1 = actual[i]
            j2 = actual[i+1]

            g = juego(j1, j2, ronda)
            ganadores.append(g)

            i += 2

        actual = ganadores
        ronda += 1

    print("\n" + "="*25)
    print(f"el campeon es {actual[0]}")
    print("="*25)


def historial_ver():
    print("\n" + "="*20)
    print("historial")
    print("="*20)

    for h in historial:
        print(h)


def stats():
    print("\n" + "="*20)
    print("   estadisticas")
    print("="*20)

    for j, d in estadisticas.items():
        print("\n" + "-"*10 + f" {j} " + "-"*10)
        print(f"victorias: {d['victorias']}")
        print(f"piedra: {d['piedra']}")
        print(f"papel: {d['papel']}")
        print(f"tijera: {d['tijera']}")
        print(f"eliminado en: {d['eliminado']}")