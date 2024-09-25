import math 

print ("Dame el ancho del rectangulo")
ancho = float(input())
print ("Dame el largo del rectangulo")
largo = float(input())
diagonal = math.sqrt(ancho**2 + largo**2)
print ("La diagonal de tu rectangulo es " + f"{diagonal}")
print ("")


print("Ahora calcularemos la cantidad de litros de pintura")
print("Dame el area a pintar en m2")
area = float(input())
print("Dame la cantidad de m2 que quieras cubrir")
metros = float(input())
litros = math.ceil (area/metros)
print ("Tienes que comprar " + f"{litros}" + " litros de pintura")
print ("")


print("Para calcular la distancia necesito las coordenadas de x1,y1,x2,y2 ")
print ("Dame la coordenada de x1")
x1 = int(input())
print ("Dame la coordenada de y1")
y1 = int(input())
print ("Dame la coordenada de x2")
x2 = int(input())
print ("Dame la coordenada de y2")
y2 = int(input())
distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("distancia=" + f"{distancia:.2f}" )
