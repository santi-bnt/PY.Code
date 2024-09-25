
import random

print("Vamos a jugar un juego llamdo adivina el número")
print ("Voy a escoger un numero del 1 al 100 tienes hasta 5 intentos")

n = random.randint(1, 100)
primer = float(input())


def juego():
    if n == primer:
     print ("Victoria")
    
    elif n < primer: 
       print ("Es menor")
    
    elif n > primer: 
       print ("Es mayor")
    
      
juego()

primer = float(input())
juego()

primer = float(input())
juego()

primer = float(input())
juego()

segundo = float(input())

if n == segundo:
     print ("Victoria")
    
if n != segundo:
      print("Derrota el numero era " + f"{n}")
    

