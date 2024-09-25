cliente = str(input("Eres cliente normal o frecuente: "))
silla = str(input("Quieres una silla basica, estandar o de lujo: "))

Basica = 700 
Estandar = 900
DeLujo = 1500

def sillac(sillaa):
    if sillaa == "basica":
        return Basica
    elif sillaa == "estandar":
        return Estandar
    elif sillaa == "de lujo":
        return DeLujo
    else:
        return 0

precio = sillac(silla)

if precio == 0:
    print("Opción de silla no es válida.")
    
else:
    if cliente == "normal": 
        print(precio)
    elif cliente == "frecuente":
        descuento = precio - (precio / 100)
        print(descuento)
    else:
        print("Tipo de cliente no es válido.")















    
