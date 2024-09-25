lista = []
n = int(input())

while True:
    if n > 0:
        for i in range(n):
            valor = int(input())
            lista.append(valor)
        while valor < 0:
            valor = int(input())

        for i in range(lista):
            print(lista[i])
