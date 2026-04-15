import json
import os
from datetime import datetime

RUTA = os.path.join(os.path.dirname(__file__), "cuentas_banco.json")

# ---------------- ARCHIVOS ----------------

def cargar():
    try:
        with open(RUTA, "r") as f:
            return json.load(f)
    except:
        return {}

def guardar(cuentas):
    with open(RUTA, "w") as f:
        json.dump(cuentas, f, indent=4)

# ---------------- CUENTA ----------------

def crear(cuentas):
    nombre = input("Nombre: ")

    pin = input("PIN (4 dígitos): ")
    while not (pin.isdigit() and len(pin) == 4):
        print("PIN inválido")
        pin = input("PIN (4 dígitos): ")

    num = str(len(cuentas) + 1001)

    cuentas[num] = {
        "nombre": nombre,
        "pin": pin,
        "saldo": 0,
        "historial": []
    }

    guardar(cuentas)
    print("Cuenta creada:", num)


def login(cuentas):
    for _ in range(3):
        num = input("Cuenta: ")
        pin = input("PIN: ")

        if num in cuentas and cuentas[num]["pin"] == pin:
            print("Bienvenido", cuentas[num]["nombre"])
            return num

        print("Datos incorrectos")

    return None


def saldo(cuentas, c):
    print("Saldo:", cuentas[c]["saldo"])


def depositar(cuentas, c):
    monto = pedir_monto()
    if monto is None:
        return

    cuentas[c]["saldo"] += monto
    guardar_mov(cuentas, c, "deposito", monto)

    print("Depósito realizado")


def retirar(cuentas, c):
    monto = pedir_monto()
    if monto is None:
        return

    if monto > cuentas[c]["saldo"]:
        print("Saldo insuficiente")
        return

    cuentas[c]["saldo"] -= monto
    guardar_mov(cuentas, c, "retiro", monto)

    print("Retiro realizado")


def transferir(cuentas, origen):
    destino = input("Cuenta destino: ")

    if destino not in cuentas or destino == origen:
        print("Cuenta inválida")
        return

    monto = pedir_monto()
    if monto is None:
        return

    if monto > cuentas[origen]["saldo"]:
        print("Saldo insuficiente")
        return

    cuentas[origen]["saldo"] -= monto
    cuentas[destino]["saldo"] += monto

    fecha = ahora()

    guardar_mov(cuentas, origen, "envío", monto, fecha)
    guardar_mov(cuentas, destino, "recibo", monto, fecha)

    guardar(cuentas)
    print("Transferencia realizada")


def historial(cuentas, c):
    if not cuentas[c]["historial"]:
        print("Sin movimientos")
        return

    for mov in cuentas[c]["historial"]:
        print(mov)




def pedir_monto():
    try:
        m = float(input("Monto: "))
        if m <= 0:
            print("Monto inválido")
            return None
        return m
    except:
        print("Número inválido")
        return None


def ahora():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def guardar_mov(cuentas, c, tipo, monto, fecha=None):
    if not fecha:
        fecha = ahora()

    cuentas[c]["historial"].append({
        "tipo": tipo,
        "monto": monto,
        "fecha": fecha,
        "saldo": cuentas[c]["saldo"]
    })

    guardar(cuentas)