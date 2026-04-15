from funciones import *

cuentas = cargar()

while True:
    print("\n======= BANK =======")
    print("1. Crear cuenta")
    print("2. Iniciar sesión")
    print("3. Salir")

    op = input("Seleccione: ").strip()

    match op:
        case "1":
            crear(cuentas)

        case "2":
            cuenta = login(cuentas)

            if cuenta:
                while True:
                    print("\n======= MENÚ =======")
                    print("1. Saldo")
                    print("2. Depositar")
                    print("3. Retirar")
                    print("4. Transferir")
                    print("5. Historial")
                    print("6. Cerrar sesión")

                    op2 = input("Seleccione: ").strip()

                    match op2:
                        case "1":
                            saldo(cuentas, cuenta)

                        case "2":
                            depositar(cuentas, cuenta)

                        case "3":
                            retirar(cuentas, cuenta)

                        case "4":
                            transferir(cuentas, cuenta)

                        case "5":
                            historial(cuentas, cuenta)

                        case "6":
                            print("Sesión cerrada")
                            break

                        case _:
                            print("Opción inválida")

        case "3":
            print("Saliendo")
            break

        case _:
            print("Opción inválida")