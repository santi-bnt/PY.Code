"""
import os
lista = []
suma = 0
numero = int(input("dame el numero de elemtos para tu lista: "))

while True:
    if numero > 0:
            for i in range (numero):
                elemento = int(input(f"{i+1} elemento de la lista: "))
                suma = suma + elemento
                lista.append(elemento)
            while elemento < 0:
                 elemento = int(input(f"{i+1} elemento de la lista: "))
            for i in range(len(lista)):
                print(f"lista[{i+1}] = {lista[i]}")
            print(lista)
            print(suma)
            break
            
    else:
        print("Numero no valido")
        numero = int(input("dame el numero de elemtos para tu lista: "))
"""""

import os
par = []
impar= []
suma = 0

while True:
   elemento = int(input(f"{suma+1} elemento de la lista: "))
   while elemento > 0:
                
                if elemento %2 == 0:
                    par.append(elemento)
                if elemento == 0:
                    par.append(elemento)
                if elemento %2 != 0:
                    impar.append(elemento)
                suma = suma +1
                elemento = int(input(f"{suma+1} elemento de la lista: ")) 
   while elemento < 0:
        print(f"Pares: {len(par)}")
        print(f"Impares: {len(impar)}")   
        break
   break
            