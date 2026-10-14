# Continuació d'estructures de control de fluxe:
# Les estructures iteratives (bucles)
# Com hem pogut veure, per a dur a terme un algoritme (una seqüència de passes ordenades per executar o dur a terme una tasca)
# no sempre es poden sol.lucionar amb diversificació de branques d'execució, de vegades s'ha de repetir una passa
# fins a que es compleix una condició per poder continuar amb la consecució de l'algoritme.

# La básica es el while (condición):
# Literalmente repite en orden las instrucciones que se encuentran dentro de este bloque
# mientras que la condición sea TRUE.

# Imaginaos un bucle (<- palabra clave) en el que preguntamos por una entrada, por un valor
# y hasta que no se introduce, no continuamos.

entrada = input('Introduce el 5: ')
while entrada != '5':
    entrada = input('Introduce el 5: ')

print('Muy bien paquete, te ha costado pero has introducido el 5 al final...')

# Obviamente, existen infinidad de maneras de combinar y utilizar los bucles.
# A parte, tenemos modificadores de su comportamiento que nos permiten
# romper el bucle (break) o saltarnos las instrucciones siguientes que faltan por
# evaluar dentro de él (continue).

# Cada vez que ejecutamos las instrucciones dentro de un bucle y volvemos al while (o
# a la primera línea) a evaluar la condición, a eso se le conoce como una iteración.

opcion = input('Introduce una opción del 1 al 4: ')

# Mientras no escriba como entrada al input un 1, 2, 3, o 4 se seguirá pidiendo una
# entrada correcta indicando que la entrada anterior no lo era.
'''opcion = int(input('Introduce una opción del 1 al 4: '))'''

# Mientras no escriba como entrada al input un 1, 2, 3, o 4 se seguirá pidiendo una
# entrada correcta indicando que la entrada anterior no lo era.

# Solución 1
'''
while not((opcion == 1) or (opcion == 2) or (opcion == 3) or (opcion == 4)):
    opcion = int(input('Introduce una opción del 1 al 4: '))'''

# Solución 2
'''opcion = int(input('Introduce una opción del 1 al 4: '))
while (opcion != 1) and (opcion != 2) and (opcion != 3) and (opcion != 4):
    opcion = int(input('Introduce una opción del 1 al 4: '))

print('Has introducido una opción correcta.')'''

# Existe una abreviación / atajo en Python que nos permite evaluar si un objeto
# tiene un "clon" (otro objeto con el mismo valor) en cualquier contenedor.
# La palabra clave "in"

# Solució 3 con el uso de in
'''listaOpciVal = [1, 2, 3, 4]
opcion = int(input('Introduce una opción del 1 al 4: '))

while opcion not in listaOpciVal:
    opcion = int(input('Introduce una opción del 1 al 4: '))'''

# Hasta mediados del segundo trimestre, el uso de in está prohibido.

# Otro tipo de bucle que tenemos en Python (y otros lenguajes) es el
# for
# A diferencia de otros lenguajes, el "for" en Python solo está diseñado
# para recorrer listas.
print()
lista = [1, 2, 3, 4, 'hola', 'janders', 5, 6]

for a in lista:
    print(f'El elemento siguiente de la lista es {a}')

# Vamos a probar con sets (conjuntos)

conjunto = {1, 2, 3, 4, 5}
print()
for a in conjunto:
    print(f'El elemento siguiente del conjunto es {a}')

# Nos puede imprimir todos los elementos del conjunto pero no tiene porqué imprimirlos
# de manera ordenada ya que no tienen índice

# Vamos a probar ocn diccionarios 

diccionario = {1:'uno', 2:'dos', 3:'tres', 4:'cuatro', 5:'porel*telainco'}
print()
print(diccionario.items())
for (clave, valor) in diccionario.items():
     print(f'El elemento siguiente del diccionario es {clave}:{valor}')

# Recorrer con for una tupla se hace de exactamente el mismo modo que una lista.
print()
lista2 = [[1,3], [3,4], ['hola','tres'], ['5',5]]

for a in lista2:
    print(f'El siguiente valor de lista2 es: {a}')

print()
for [a,b] in lista2:
    print(f'El siguiente valor de lista2 es: {a} y {b}')

lista3 = [[1,3], [3,4], ['hola','tres'], ['5',5], [1, 2, 'janders']]

# La ejecuvión del siguiente bucle elevará una excepción ya que siempre espera
# que cada elemento de la lista3 sea otra lista forzosamente de solo 2 elementos.
''' print()
for [a,b] in lista3:
    print(f'El siguiente valor de lista2 es: {a} y {b}')'''

# Como recorrer contenedores con while -> usando la sintaxis de acceso a elementos de
# contenedores u otros iterables.
# iterables = cualquier objeto que tiene elementos que se puedan recorrer, entre ellos
# estan todos los contenedores pero también strings i otros tipos.

#Ejemplo: queremos recorrer la lista 'lista3' mediante un bucle while.

indice = 0
while indice <= (len(lista3) - 1):
    print(f'El siguiente elemento de la lista3 es: {lista3[indice]}')
    indice += 1 # indice = indice + 1 ¡Ojo! SIEMPRE TENEMOS QUE ACTUALIZAR EL O LOS ÍNDICES!

# Ejercicio: tambien quiero imprimir por pantalla cada elemento u objeto individual
# de las listas contenidas en lista3.
lista3 = [[1,3], [3,4], ['hola','tres'], ['5',5], [1, 2, 'janders']]
indice = 0
while indice <= (len(lista3) - 1):
    print(f'El siguiente elemento de la lista3 es: {lista3[indice]}')
    indelem = 0
    while indelem <= (len(lista3[indice]) - 1):
        print(f'El primer elemento de la sublista {lista3[indice]} es: {lista3[indice][indelem]}')
        indelem += 1
    indice += 1 

# Escriurem la sortida dels bucles anteriors d'aquesta manera:
'''
- Iteración bucle principal 1:
    Resultados del print y valores de variables.
    - Iteración bucle interno 1:
        Resultados del print y valores de variables.
            .
            .
            .
            .
    - Iteración bucle interno N2:
        Resultados del print y valores de variables.
    .
    .
    .
- Iteración bucle principal N:
    Resultados del print y valores de variables.
    - Iteración bucle interno 1:
        Resultados del print y valores de variables.
            .
            .
            .
            .
    - Iteración bucle interno N2:
        Resultados del print y valores de variables.
'''

# Ejercicio
'''
1º Iteracion bucle while indice <= (len(lista3) - 1):
    prints:
    El siguiente elemento de la lista3 es: [1,3]
    valores:
    indice = 0
    indelem = 0
    1º iteracion bucle while indelem <= (len(lista3[indice]) - 1):
        prints:
        El siguiente elemento de la sublista [1,3] es: 1
        valores:
        indelem = 1
    2º iteracion bucle while indelem <= (len(lista3[indice]) - 1):
        prints:
        El siguiente elemento de la sublista [1,3] es: 3
        valores:
        indelem = 2
    valores:
    indice = 1
    indelem = 2
2º Iteracion bucle while indice <= (len(lista3) - 1):
    prints:
    El siguiente elemento de la lista3 es: [3,4]
    valores:
    indice = 1
    indelem = 0
    1º iteracion bucle while indelem <= (len(lista3[indice]) - 1):
        prints:
        El siguiente elemento de la sublista [3,4] es: 3
        valores:
        indelem = 1
    2º iteracion bucle while indelem <= (len(lista3[indice]) - 1):
        prints:
        El siguiente elemento de la sublista [3,4] es: 4
        valores:
        indelem = 2
    valores:
    indice = 2
    indelem = 2
3º Iteracion bucle while indice <= (len(lista3) - 1):
    prints:
    El siguiente elemento de la lista3 es: ['hola','tres']
    valores:
    indice = 2
    indelem = 0
    1º iteracion bucle while indelem <= (len(lista3[indice]) - 1):
        prints:
        El siguiente elemento de la sublista ['hola','tres'] es: 'hola'
        valores:
        indelem = 1
    2º iteracion bucle while indelem <= (len(lista3[indice]) - 1):
        prints:
        El siguiente elemento de la sublista ['hola','tres'] es: 'tres'
        valores:
        indelem = 2
    valores:
    indice = 3
    indelem = 2
4º Iteracion bucle while indice <= (len(lista3) - 1):
    prints:
    El siguiente elemento de la lista3 es: ['5',5]
    valores:
    indice = 3
    indelem = 0
    1º iteracion bucle while indelem <= (len(lista3[indice]) - 1):
        prints:
        El siguiente elemento de la sublista ['5',5] es: '5'
        valores:
        indelem = 1
    2º iteracion bucle while indelem <= (len(lista3[indice]) - 1):
        prints:
        El siguiente elemento de la sublista ['5',5] es: 5
        valores:
        indelem = 2
    valores:
    indice = 4
    indelem = 2
5º Iteracion bucle while indice <= (len(lista3) - 1):
    prints:
    El siguiente elemento de la lista3 es: [1, 2, 'janders']]
    valores:
    indice = 4
    indelem = 0
    1º iteracion bucle while indelem <= (len(lista3[indice]) - 1):
        prints:
        El siguiente elemento de la sublista [1, 2, 'janders']] es: 1
        valores:
        indelem = 1
    2º iteracion bucle while indelem <= (len(lista3[indice]) - 1):
        prints:
        El siguiente elemento de la sublista [1, 2, 'janders']] es: 2
        valores:
        indelem = 2
    3º iteracion bucle while indelem <= (len(lista3[indice]) - 1):
        prints:
        El siguiente elemento de la sublista [1, 2, 'janders']] es: 'janders'
        valores:
        indelem = 3
    valores:
    indice = 5
    indelem = 3
'''