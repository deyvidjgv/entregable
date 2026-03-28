
inventario = {
    "Papas" : 2500,
    "Gaseosa" : 3000,
    "Galletas" : 1800,
    "Chocolate" : 2200,
    "Jugo" : 2800
}


def stock(inventario):
    inve = inventario.items()
    for key, value in inve:
        print(key, value)
        print("-" * 10)

