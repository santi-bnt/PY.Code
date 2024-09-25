
cantidad = int(input("Dame la cantidad de datos del uno al diez para tu lista: "))
lista = [1,2,3,4,5,6,7,8,9]

while True:
    if cantidad < 10 or cantidad <0 :
        
            for i in range(cantidad):
                numero = int(input("dame un valor del 1 al 9: " ))
                if numero < 10 or numero <0 :
                        if numero in lista:
                            lista.remove(numero)
                else:
                        print("Dame una numero valido")
                        numero = int(input("dame un valor del 1 al 9: "))
            print(" ".join(map(str, lista)))
            print("")
            break
            

    else:
     print("Dame una cantidad validad")
     cantidad = int(input("Dame una cantidad del uno al diez para tu lista: "))


n = int(input("Cauntos datos fibonacci quieres en la lista: "))
fibonacci = []
a, b = 0, 1

while True:
    if n > 0:
        for i in range(n):
            fibonacci.append(a)
            a, b = b, a + b
        print (fibonacci)
        print("")
        break
        

    else:
        print('invalido')
        n = int(input("Cauntos elementos quieres en la lista: "))


l1 = []
l2 = []
lo = []

while True:
        n= str(input("Dame un numero para agrergar a la 1era lista y (*) cuando quieres que acabe: "))
        if n == "*":
            print("")
            break
        else: 
            l1.append(int(n))
while True:
    
        n= str(input("Dame un numero para agrergar a la 2nda lista y (*) cuando quieres que acabe: "))
        if n == "*":
            lo = l1 + l2
            lo.sort()
            print("")
            print(lo)
            break
        else: 
            l2.append(int(n))


print("")       
l1c = int(input("Cuantos datos quieres en la primera lista: "))
l2c = int(input("Cuantos datos quieres en la segunda lista: "))   
print("-----")   
l1 = []
l2 = []
lo = []

for i in range(l1c):
     dato = (input(f"Dame el {i+1} dato de la primera lista: "))
     l1.append(dato)
     
print("-----")

for i in range(l2c):
     dato = (input(f"Dame el {i+1} dato de la segunda lista: "))
     l2.append(dato)
print("-----")

for i in range(max(l1c, l2c)):
    if i < l1c:
        lo.append(l1[i])
    if i < l2c:
        lo.append(l2[i])

print(lo)