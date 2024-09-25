import os

def cuales_faltan():
    os. system("cls") 
    print("\n Bienvenido al programa cuales faltan")
    

lista = []

def opciones():
    opc = int(input("De las siguientes opciones elegi el programa que quieras usar: "
                "\n 1. Primera grafica"
                "\n 2. Primera grafica"
                "\n 3. Primera grafica"
                "\n 4. Primera grafica"
                "\n 5. Salir"
                "\n "
                ))
    return opc

def opciones2():
    os. system("cls") 
    opc2 = int(input("De las siguientes opciones elegi el programa que quieras usar: "
                "\n 1. Primera grafica"
                "\n 2. Primera grafica"
                "\n 3. Primera grafica"
                "\n 4. Salir"
                "\n "
                ))
    return opc2

print("Hola somos videojuegos y sus consumidores")
nombre = input("Como te llamas? ")
print (f"ok, {nombre} que quieres hacer ")
opc = opciones()
opc2 = opciones2()


while True:
    if opc == 1:
        cuales_faltan()
        while True:
            if opc2 == 1:
               cuales_faltan()
               opc2 = opciones2()
            if opc2 == 2:
                cuales_faltan()
                opc2 = opciones2()
            if opc2 == 3:
                cuales_faltan()
                opc2 = opciones2()
            if opc2 == 4:
                os. system("cls") 
                print("Seleccionaste la opcion de salir. Saliste del submenu")
                break
        opc = opciones()
    if opc == 2:
        cuales_faltan()
        opc2 = opciones()
    if opc == 3:
        cuales_faltan()
        opc2 = opciones()
    if opc == 4:
        cuales_faltan()
        opc2 = opciones()
    if opc == 5:
        os. system("cls") 
        print("Seleccionaste la opcion de salir. Gracias por usar el programa")
        break
    else:
        os. system("cls") 
        print("Dame una opcion valida")
        opc = opciones()