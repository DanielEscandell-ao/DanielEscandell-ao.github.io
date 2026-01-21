# Deures per al proper dia:
# Fer els exercicis de l'1 al 6 de la pràctica 7 publicada en el classroom.
# 1
pizzas = ['Pepperoni', '4 Quesos', 'Jamon y Queso', 'Jamon Serrano']
while True:
    print(f'Me agrada la pizza de {pizzas[0]}')
    print(f'Me agrada la pizza de {pizzas[1]}')
    print(f'Me agrada la pizza de {pizzas[2]}')
    print(f'Me agrada la pizza de {pizzas[3]}')
    print(f'Me encanten les pizzes')
    break
# 2
n = int(input('Introduce un numero positivo: '))
i = int(1)
if n <= 0:
    print(f'Porfavor introduce un numero positivo.')
else:
    i = 1
    while i <= n:
        print(f'{i},')
        i = i + 2
# 3
n = int(input('Introduce un numero: '))
if n <= 0:
    print(f'Porfavor introduce un numero positivo.')
else:
    i = 1
    numparejo = 2
    while i <= n:
        print(f'{numparejo ** 3}')
        i = i + 1
        numparejo = numparejo + 2

# 4
frase = input('Introdueix una frase: ')
paraules = frase.split()
i = 0
comptador = 0
while i < len(paraules):
    comptador = comptador + 1
    i = i + 1
print(f'La frase té {comptador} paraules.')


# 5
n = int(input('Introdueix un numero: '))
if n <= 0:
    print('El numero ha de ser positiu.')
else:
    fila = 1
    while fila <= n:
        print('*' * fila)
        fila = fila + 1


# 6
paraula = input('Introdueix una paraula: ')
i = 1
while i <= 10:
    print(paraula)
    i = i + 1
# Fer el següent exercici:
# Es demanar a l'usuari que introdueixi una cadena de caràcters per teclat y el bucle for haurà de processar aquesta cadena
# i crear-ne una de nova amb les lletres minúscules y majúscules alternades.
cadena = input("Introdueix una cadena: ")

nova_cadena = ""
minuscula = True

for lletra in cadena:
    if minuscula:
        nova_cadena += lletra.lower()
    else:
        nova_cadena += lletra.upper()
    minuscula = not minuscula

print(nova_cadena)

# 7
nombre = int(input('Introduce tu nombre: '))
i = 1
while i <= nombre:
    print(i)
    i = i + 1

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