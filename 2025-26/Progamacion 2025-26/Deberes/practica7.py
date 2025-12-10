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
# 4: Contar las palabras
