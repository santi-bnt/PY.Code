def imprimir(name,age):
    print (name)
    print (age)


def datos():
    nombre = input()
    edad = input()
    imprimir(nombre,edad)

datos()

producto1 = float(input("Dame el precio 1 "))
producto2 = float(input("Dame el precio 2 "))
producto3 = float(input("Dame el precio 3 "))

precio_final = producto2 + producto1 + producto3

descuentoi = precio_final // 100

print ("El total sin descuento es " + f"{precio_final}")

if precio_final >= 100 and precio_final < 200:
    print ("El descuento es de " f"{descuentoi*10}")
    print ("El precio es de " f"{precio_final -(descuentoi*30)}")
    

if precio_final >= 200 and precio_final < 300:
    print ("El descuento es de " f"{descuentoi*20}")
    print ("El precio es de " f"{precio_final -(descuentoi*30)}")
   

if precio_final >= 300:
    print ("El descuento es de " f"{descuentoi*30}")
    print ("El precio es de " f"{precio_final -(descuentoi*30)}")
    
else:
    print ("No hay descuento aplicado")
    print ("El total es " + f"{precio_final}")
