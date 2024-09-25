total = float(input("Dame el total: "))

descuento = total / 100

cliente = (input("Eres cliente frecuente? "))

def clienteF():

        if  total < 100: 
            print ("El descuento es de " f"{descuento*5}")
            print ("El precio es de " f"{total -(descuento*5)}")

        if  total >= 100 and total < 500:
            print ("El descuento es de " f"{descuento*15}")
            print ("El precio es de " f"{total -(descuento*15)}")
   

        if  total >= 500:
            print ("El descuento es de " f"{descuento*25}")
            print ("El precio es de " f"{total -(descuento*25)}")
    
def clienteN(): 
 
        if total < 100:
            print ("No hay descuento aplicado")
            print ("El total es " + f"{total}")

        if total >= 100 and total < 500:
            print ("El descuento es de " f"{descuento*10}")
            print ("El precio es de " f"{total -(descuento*10)}")
   

        if total >= 500:
            print ("El descuento es de " f"{descuento*20}")
            print ("El precio es de " f"{total -(descuento*20)}")


if cliente == ("SI") or cliente == ("si"): 
    clienteF()

if cliente == ("No") or cliente == ("no"): 
     clienteN()