from inventario import *



while True:
    print(" ------- Elige la opcion que deseas ------- "),
    print("1. Productos disponibles"),
    print("2. Agregar productos al carrito"),
    print("3. Ver carrito decompras"),
    print("4. Pagar y salir"),
    print("5. Salir sin pagar")
    opcion = input("que opcion deseas elegir?: ") 
    
    match opcion:
        case "1" : print(stock(inventario))
    







