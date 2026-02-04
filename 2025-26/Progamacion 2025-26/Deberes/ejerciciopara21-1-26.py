import math
# 7

numero = int(input('Introduce un numero: '))

lista = []
objetivo = 2  

while objetivo <= numero:
    esprimo = True
    num = 2

    while num <= int(math.sqrt(objetivo)):
        if objetivo % num == 0:
            esprimo = False
            break
        num += 1

    if esprimo:
        lista.append(objetivo)

    objetivo += 1

print(lista)

# 8

capital = float(input("Introdueix el capital inicial: "))
interes = float(input("Introdueix l'interès anual (%): "))
anys = int(input("Introdueix el nombre d'anys: "))

for any in range(anys):
    capital = capital + capital * interes / 100

print("El capital acumulat després de", anys, "anys és:", capital)
# 9

n = int(input("Introdueix un nombre sencer: "))

suma = 0
i = 1

while i <= n // 2:
    if n % i == 0:
        suma = suma + i
    i = i + 1

print("La suma dels divisors és:", suma)
