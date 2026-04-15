from funcion import *

while True:
    print("\n1. registrar jugadores")
    print("2. iniciar torneo")
    print("3. ver historial")
    print("4. ver estadisticas")
    print("5. salir")

    try:
        opcion = int(input("seleccione: "))
    except:
        print("error, escribe un numero")
        continue
    
    match opcion:
        case 1:
            registrar()
        case 2:
            torneo()
        case 3:
            historial_ver()
        case 4:
            stats()
        case 5:
            print("saliendo")
            break
        case _:
            print("error, opcion invalida")