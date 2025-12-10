# 1: Ejercicio Pizzas
pizzas = ['Pepperoni', '4 Quesos', 'Jamon y Queso', 'Jamon Serrano']
while True:
    print(f'Me agrada la pizza de {pizzas[0]}')
    print(f'Me agrada la pizza de {pizzas[1]}')
    print(f'Me agrada la pizza de {pizzas[2]}')
    print(f'Me agrada la pizza de {pizzas[3]}')
    print(f'Me encanten les pizzes')
    break
# 2: Numeros impares
n = int(input('Introduce un numero positivo: '))
i = int(1)
if n <= 0:
    print(f'Porfavor introduce un numero positivo.')
else:
    i = 1
    while i <= n:
        print(f'{i},')
        i = i + 2
# 3: Algoritmo numeros pares
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


# 7
paraula = input('Introdueix una paraula: ')
vegades = int(input('Introdueix el nombre de repeticions: '))
if vegades <= 0:
    print('Has d’introduir un numero positiu.')
else:
    i = 1
    while i <= vegades:
        print(paraula)
        i = i + 1


# 8
n = int(input('Introdueix un numero positiu: '))
if n <= 0:
    print('Has d’introduir un numero positiu.')
else:
    num = 2
    while num <= n:
        divisor = 2
        es_primer = True
        while divisor < num:
            if num % divisor == 0:
                es_primer = False
                break
            divisor = divisor + 1
        if es_primer:
            print(num)
        num = num + 1


# 9
valor = input('Introdueix un numero: ')
if valor.isdigit() == False:
    print('El nombre introduït no és un nombre sencer')
else:
    n = int(valor)
    num = 2
    while num <= n:
        divisor = 2
        es_primer = True
        while divisor < num:
            if num % divisor == 0:
                es_primer = False
                break
            divisor = divisor + 1
        if es_primer:
            print(num)
        num = num + 1


# 10
capital = float(input('Introdueix el capital inicial: '))
interes = float(input('Introdueix l’interès (0-100): '))
anys = int(input('Introdueix els anys: '))
i = 1
while i <= anys:
    capital = capital + (capital * interes / 100)
    i = i + 1
print(f'El capital final és: {capital}')


# 11
n = int(input('Introdueix un numero positiu: '))
if n <= 0:
    print('El numero ha de ser positiu.')
else:
    i = 1
    suma = 0
    while i <= n // 2:
        if n % i == 0:
            suma = suma + i
        i = i + 1
    print(f'La suma dels divisors és: {suma}')


# 12
text = input('Introdueix un text: ')
invertit = ''
i = len(text) - 1
while i >= 0:
    invertit = invertit + text[i]
    i = i - 1
print(invertit)


# 13
n = int(input('Introdueix un numero: '))
if n <= 0:
    print('El numero ha de ser positiu.')
else:
    fila = n
    while fila >= 1:
        print('*' * fila)
        fila = fila - 1


# 14
n = input('Introdueix un numero: ')
i = 0
comptador = 0
while i < len(n):
    if n[i].isdigit():
        comptador = comptador + 1
    i = i + 1
print(f'El número té {comptador} xifres.')


# 15
q = int(input('Quants numeros s’introduiran?: '))
primer = int(input('Introdueix el primer numero: '))
i = 2
while i <= q:
    num = int(input('Introdueix un numero: '))
    if num <= primer:
        print('El número no és més gran que el primer.')
    i = i + 1