# 10

text = input("Introdueix un text: ")
invertit = ""
i = 0

while i < len(text):
    invertit = text[i] + invertit
    i += 1

print("Text invertit:", invertit)
# 11

n = int(input("Introdueix un nombre: "))

fila = 1
while fila <= n:
    columna = 1
    while columna <= fila:
        print("*", end=" ")
        columna += 1
    print()
    fila += 1
fila = n - 1
while fila >= 1:
    columna = 1
    while columna <= fila:
        print("*", end=" ")
        columna += 1
    print()
    fila -= 1

# 12

numero = int(input("Introdueix un nombre: "))
comptador = 0

if numero == 0:
    comptador = 1
else:
    while numero != 0:
        numero //= 10
        comptador += 1

print("Nombre de xifres:", comptador)

# 13

cantidad = int(input("Quants números s'introduiran? "))

primer = int(input("Introdueix el primer número: "))
contador = 1

while contador < cantidad:
    num = int(input("Introdueix un número: "))
    if num <= primer:
        print("Aquest número no és més gran que el primer")
    contador += 1

# 14
cantidad = int(input("¿Cuántos números quieres introducir? "))

i = 0
anterior = ''

while i < cantidad:
    num = int(input("Introduce un número: "))

    if i > 0 and num <= anterior:
        print("El número no es mayor que el anterior")

    anterior = num
    i += 1
# 15
cantidad = int(input("¿Cuántos números quieres introducir? "))

i = 0
pares = []
senars = []

while i < cantidad:
    num = int(input("Introduce un número: "))

    if num % 2 == 0:
        pares.append(num)
    else:
        senars.append(num)

    i += 1

print("Cantidad de pares:", len(pares))
print("Cantidad de senars:", len(senars))
print("Lista de pares:", pares)
print("Lista de senars:", senars)

# 16
inicio = int(input("Introduce el primer número: "))
fin = int(input("Introduce el segundo número: "))

suma = 0
i = inicio

while i <= fin:
    suma += i
    i += 1

print("La suma es:", suma)


# 18
primer = int(input("Introduce el primer número: "))
cantidad = int(input("¿Cuántos números más quieres introducir? "))

i = 0
contador = 0

while i < cantidad:
    num = int(input("Introduce un número: "))

    if num == primer:
        contador += 1

    i += 1

print("El número", primer, "se repite", contador, "veces")

# 19
frase = input("Introduce una frase: ")

i = 0
vocales = 0

while i < len(frase):
    letra = frase[i].lower()

    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vocales += 1

    i += 1

print("Número de vocales:", vocales)