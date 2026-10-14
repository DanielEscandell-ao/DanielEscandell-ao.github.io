import copy
# Contenedores de datos:
# El contenedor básico de Python (y otros lenguajes) es la lista = 'list'
lista = list() # Esto es una manera de declarar una lista genérica.
lista2 = [] # Otra manera habitual de declarar las listas.
# La lista utiliza los simbolos corchetes cuadrados "[]" para declarar su inicio y final.
lista2 = ['hola', 3, 5.5, True] # Este es el formato correcto según las normas PEP de escribir código
# NO es necesario poner espacios pero es recomendable seguir esta norma.
# El primer elemento de la lista siempre tiene el subíndice 0.
print(f'El primer elemento de la lista es: {lista2[0]}')
print(f'El primer elemento de la lista es: {lista2[0].upper()}')  
print(f'El último elemento de la lista es: {lista2[len(lista2)-1]}')
# 'len(lista)' es un método nativo a Python que nos permite saber el número de elementos
# que tiene una lista -> si hacemos la operación 'len(lista) - 1' obtendremos siempre
# el último subíndice (o índice) del último elemento contenido en la misma.
print()
# Otra sintaxis posible para acceder a elementos de una lista o parte de ellos.
sublista = lista2[0:3] # Hay que tener en cuenta que cuando usamos esta sintàxis e 
# 'subacceso' [a:b], obtenemos una sublista desde el elemento 'a' hasta el elemento 'b - 1'
print(f'Escojo del primer elemento al tercero de la lista: {sublista}')
# Si usamos lista2[:] -> es equivalente a seleccionar la lista entera.
print()
# También se puede acceder a elementos desde el final de la lista usando números enteros
# negativos. La sintáxis de acceso al último elemento es [a:] donde podemos ver que después
# de los dos puntos no aparece nada, esto, para Python corresponde a la última posición
# de la lista.
print(f'Imprimimos desde el segundo elemento hasta el final de la lista2: {lista2[1:]}')
print(f'Imprimimos desde el principio de la lista hasta el penúltimo elemento: {lista2[:-1]}')
print()
# La siguiente sintaxis siempre nos devolverá una lista vacía, si utilizamos solamente
# los dos puntos ':' no podemos poner un índice menor a la derecha del valor 
# escrito a la izquierda de los dos puntos:.
print(f'Imprimimos una sublista con primer índice menor que el segundo. {lista2[2:1]}')
print(f'Imprimimos una sublista con primer índice menor que el segundo. {lista2[3:0]}')
print()
# La sintaxis siguiente me permite invertir una lista, de hecho, devuelve una lista
# nueva con sus elementos invertidos en order.
print(f'Imprimimos una sublista con primer índice menor que el segundo. {lista2[::-1]}')

# La sintáxis del doble doble punto en listas se realiza de la manera siguiente:
# lista[inicio:fin:paso]
lista3 = ['inicio', 1, 2, 3, 4, 5, 6, 7, 'fin']
print()
print(f'Elementos salteados de la lista: {lista3[0::2]}')
# Si yo quiero imprimir una lista leída de manera invertida con un salto determinado
# uso números enteros negativos en el parámetro paso de lista[inicio:fin:paso].
print(f'Elementos salteados de la lista: {lista3[::-2]}')
print()

# Cuando utilizo un salto negativo ('hacia atrás') debo usar un margen de valores desde
# el mayor hasta el menor.
# La instrucción siguiente es posible pero innecesaria: no lo uséis.
# print(f'Elementos salteados de la lista: {lista3[len(lista3) - 1:0:-2]}')

listamapeada = [1, 'hola', 2, 'adios', 3, 'tercero', 4, 'quarto']
listapalabras = listamapeada[1::2]
print()
print(f'listapalabras contiene: {listapalabras}')

# Las listas como todo en PYthon son un objeto, por tanto tienen asociados 
# métodos y atributos.
# Métodos que necesitamos conocer de las listas:

# Método .append() de las listas --> añade un elemento al final de la lista si no 
# mencionamos ningún parámetro.
lista3.append('fin2')
print()
print(f'Lista3 con un elemento añadido por append() {lista3}')
# Imaginaos una lista = [1, 2, 3, 4]
# Hacemos lista.append([5,6,7])
# ¿Qué imprimiría print(lista)?
# [1, 2, 3, 4, [5,6,7]]

lista = [1, 2, 3, 4]
lista.append([5,6,7])
print(lista)
print()
lista = [1, 2, 3, 4]
lista.extend([5,6,7])
print(lista)
print()

# Algo equivalente al extend es:
print([1, 2, 3, 4, 5] + [6, 7, 8, 9, 10, 11])

# Método insert(índice, elemento) nos inserta un elmento nuevo dentro de la lista
# en la posición posterior indicada por el número 'índice'.
lista3 = ['inicio', 1, 2, 3, 4, 5, 6, 7, 'fin']
lista3.insert(3,'elementoinsertado')
print(f'Lista3 con un elemento añadido por insert(): {lista3}')

# Si tenemos una lista referenciada por una variable y a esta variable la igualamos
# a otra variable, tendremos 2 variables que apuntan a la misma lista, es decir,
# que apuntan al mismo objeto de clase lista.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
listacopia = lista

# Internamente cada objeto que se crea durante ejecución de código tiene un identificador
# único, si queremos saber si estamos trabajando con un objeto o con su copia
# podemos consultar este identificador on la función id()

print(f'El identificador de lista es: {id(lista)}')
print(f'El identificador de listacopia es: {id(listacopia)}')
print()
lista.append('h')
print(f'Después de añadir \'h\' a lista, esta queda: {lista}')
print(f'listacopia quedara: {listacopia}')

print()
listacopia = copy.deepcopy(lista)
print(f'El identificador de lista es: {id(lista)}')
print(f'El identificador de listacopia es: {id(listacopia)}')


# Para la próxima sesión, investigad los siguientes métodos.
# lista.count()
# lista.pop()
# lista.remove()
# lista.sort()
# lista.reverse()
# lista.clear()
# Realiza un documento explicando estos métodos.'''
