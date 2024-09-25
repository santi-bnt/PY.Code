num = 1

while num < 11 :
    print (num)
    num +=1
print("")

numero = float(input("dame un numero positivo: "))
while numero < 0:
    numero = float(input("dame un numero positivo: "))
else:
    print (numero)
    print("")

contra = str(input("Dame la Contraseña correcta: "))
while contra != "Contraseña correcta":
    print("Contraseña incorrecta")
    contra = str(input("Dame la Contraseña correcta: "))
else:
    print ("Contraseña correcta")
    print("")

numerito = int(input("Dame un numero: "))

while numerito < 1001:
    numerito = numerito*2

else:
    print (numerito)
    print("")

mayor_10 = int(input("Dame un numero: "))
suma = 0

while mayor_10 >= 10:
    suma = suma + mayor_10
    mayor_10 = int(input("Dame un numero: "))

else:
    suma = suma + mayor_10
    print (suma)