import os

T = True

while T == True:
    calificacion = 0
    suma = 0
    nombre = input("Nombre del alumno: ")      
    no_materias = int(input("Cuantas materias a capturar:"))       
    for i in range (no_materias):
        materia = input(f"Materia {i + 1}: ")
        calificacion = float(input("Cual es su calificacion? "))
        suma = suma + calificacion

    print (f"El promedio del alumno {nombre} es {suma/no_materias: 2f}")
    opc = input("Quieres calcular el promedio de otro alumno: ")
    if opc == "si" or opc == "Si":
        T = True
        os.system("cls")
    else:
        T = False