# Entrada: edad de la persona 
#Salida : Poner si o no dependiendo de si puede obtener su licencia o no
#algoritmo: Se genrara un programa que te diga si depedniendo de la edad puede obtener su licencia o no poniendo s/n y depues si o no
#caso de prueba=
# 21
# s
# si

"""print ("Dime tu edad")
edad = float(input())

if edad > 120:
 print("dame tu edad real")

elif edad >= 16: 
 print ("si")

else:
 print ("no")
"""
anio = float(input())
mes = float(input())
dia = float(input())

if 1 <= dia <= 27:
    dia += 1
    print("el anio es " + f"{anio}")
    print("el mes es " + f"{mes}")
    print("el dia es " + f"{dia}")
  
elif dia == 28:
  if mes == 2:
   if anio %4 == 0:
     dia += 1
     print("el anio es " + f"{anio}")
     print("el mes es " + f"{mes}")
     print("el dia es " + f"{dia}")
   else:
     mes += 1
     dia = 1
     print("el anio es " + f"{anio}")
     print("el mes es " + f"{mes}")
     print("el dia es " + f"{dia}")

if 1 <= dia <= 29:
    dia += 1
    print("el anio es " + f"{anio}")
    print("el mes es " + f"{mes}")
    print("el dia es " + f"{dia}")

if dia == 31 and mes == 12:
    anio += 1
    mes = 1
    dia = 1
    print("el anio es " + f"{anio}")
    print("el mes es " + f"{mes}")
    print("el dia es " + f"{dia}")
    
if dia == 31:
  mes += 1
  dia = 1
  print("el anio es " + f"{anio}")
  print("el mes es " + f"{mes}")
  print("el dia es " + f"{dia}")


if dia == 30:
  if mes == 4 or mes == 6 or mes == 9 or mes == 11:
     mes += 1
     dia = 1
     print("el anio es " + f"{anio}")
     print("el mes es " + f"{mes}")
     print("el dia es " + f"{dia}")
 

else:
  if anio < 0 or mes < 0 or dia < 0:
    print("valor invalido")  
  