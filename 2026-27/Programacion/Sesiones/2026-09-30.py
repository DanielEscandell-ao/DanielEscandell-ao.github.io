# Revisaremos hoy las funciones solicitadas a definir de la sesión anterior.
# lista.count()
# lista.pop()
# lista.remove()
# lista.sort()
# lista.reverse()
# lista.clear()

lista = [1, 2, 3, 4, 6, 34, 5, 67, 89, 123, 1, 4, 7]

print(lista)

# Ejemplos de uso de la función sort() mediante el uso de key
palabras = ["casa", "sol", "ordenador", "mesa"]

palabras.sort(key=len)

print(palabras)

print()
palabras = ["casa", "sol", "ordenador", "mesa"]

palabras.sort(key=len)

print(palabras)

print()
nombres = ["Pedro", "ana", "Luis", "bea"]

nombres.sort(key=str.lower)

print(nombres)

# Ejemplos de la función count()
print(f'El número de veces que aparece el 1 en la lista {lista} es: {lista.count(1)}')

# Ejemplos de uso de la función pop() -> nos retorna el último elemento de la lísta y lo
# elimina de esta.


print(f'La lista sin eliminar objetos es: {lista}')
ultimo_num = lista.pop()

print(f'El último número de la lista {lista} era: {ultimo_num}')

# Ejemplo de la función index de las listas:
lista = [1, 2, 3, 4, 6, 34, 5, 67, 89, 123, 1, 4, 7]
print(f'La posición del primer 3 de esta lista: {lista} se encuentra en el índice {lista.index(3)}')

# 2 Las tuplas: contenedores no modificables.
# Se declaran con la palabra 'tuple' y su contenido no es modificable (al igual que 
# los str), en vez de usar corchetes cuadrados, usaremos paréntesis.
tupla = tuple()
tupla1 = ()
# Solo dispone de 2 métodos regulares: count() y index() --> su función es exactamente
# la misma que en el caso de las listas.
tupla = (1, 2, 3, 4, 5, 6)
# Python dispone del "Garbage Collector" --> libera la memoria en la que existen objetos
# a los que no está apuntando ninguna variable.
# Eliminar no es lo mismo que liberar, no se elimina el contenido en esas posiciones
# de memoria que contienen el objeto no apuntado, sinó que se consideran de uso libre.

print()
print('Pruebas con tuplas:')
try:
    tupla[0] = 3
except Exception as mensaje:
    print(mensaje)


print(f'El elemento 3 en la tupla se encuentra en la posición: {tupla.index(3)}')

# Otro contenedor de datos muy útil en función de las necesidades de tratamiento de datos
# son las listas mapeadas o los DIccionarios (dict). Este tipo de contenedor me permite
# usar como valores de índices tipos diferentes a los enteros, es decir,
# puedo usar también otros tipos para localicar un objeto contenido en el diccionario
# como un tipo str. Para crear un diccionario vacío, usaremos dos símbolos de
# claudator de apertura y cierre '{}'.
diccionario_dnis = dict()
diccionario_dnis = {}

# Los diccionarios funcionan con pares 'clave:valor'
diccionario_dnis = {'Pepe':'65856545c', 'Jose':'11234567b', 'Roberto':'56234578h'}
print('El dni de Pepe es: ', end='') 
print(diccionario_dnis['Pepe'])
print()

# Métodos relacionados con diccionarios.
# Método .keys() --> devuelve una lista con los elementos 'clave' 
lista_claves = list(diccionario_dnis.keys())
print('Las claves del diccionario son: ', diccionario_dnis.keys())
print('Las claves del diccionario son', lista_claves)

# Método .values() --> devuelve una lista con los elementos 'valores'.
lista_valores = list(diccionario_dnis.values())
print('Las valores del diccionario son: ', diccionario_dnis.values())
print('Las valores del diccionario son', lista_valores)


# Método para añadir elementos 'clave:valor' a los diccionarios.
# diccionario_dnis.update(dict(['Antonio', '45612378t'])) -- 
diccionario_dnis.update({'Sonia':'25367894f', 'Pedro':'12345678g'})
print('EL nuevo contenido del diccionario es: ', diccionario_dnis)

# También: definir concretamente (y dar un ejemplo de código)
# de lo que realizan las funciones:
# diccionario_dnis.get()
# diccionario_dnis.items()
# diccionario_dnis.popitem()
# diccionario_dnis.pop()

# Concepto y uso del "casting"

# Para sesión de día 09-10-2025 investigar la diferencia entre las instrucciones de las
# líneas 44 y 45, qué es lo distinto?