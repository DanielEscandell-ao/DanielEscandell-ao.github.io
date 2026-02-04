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