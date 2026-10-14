# También: definir concretamente (y dar un ejemplo de código)
# de lo que realizan las funciones:
# diccionario_dnis.get()
# diccionario_dnis.items()
# diccionario_dnis.popitem()
# diccionario_dnis.pop()

# Concepto y uso del "casting"

diccionario_dnis = {'Pepe':'65856545c', 'Jose':'11234567b', 'Roberto':'56234578h'}
print('El dni de Pepe es: ', end='') 
diccionario_dnis.update({'Sonia':'25367894f', 'Pedro':'12345678g'})

print()
# La función get() de los diccionarios es la de devolver un valor a través de una clave
# que se le pasa por argumento único a la función.
# Equivale a la sintaxis diccionario[clave] y recuperar el valor asociado a dicha clave.

valor_get = diccionario_dnis.get('Roberto') 
valor_sintaxis_listas = diccionario_dnis['Roberto']
print('El contenido de valor_get cuando recuperamos un valor con get() es', valor_get)
print(f'El contenido de valor_sintaxis_listas cuando recuperamos un valor con sintaxis de acceso a listas es {valor_sintaxis_listas}')

# La función de diccionario items me devuelve el diccionario completo en un formato de lista de tuplas.

print(f'Resultado de items() a diccionario_dnis: {list(diccionario_dnis.items())}')

# La función popitems() nos devuelve el último par clave-valor del diccionario y lo elimina de este.
# Como es fácil de deducir e la parte "pop" de dicha función en referencia a la función pop() de las listas.

print(f'El resultado devuelto por popitem() del diccionario diccionario_dnis es: {diccionario_dnis.popitem()}')
popitemdnis = diccionario_dnis.popitem
print(f'El resultado devuelto por popitem() del diccionario diccionario_dnis es: {popitemdnis()}')

# La funcipon pop() nos permite extraer un par clave-valor que se indica concretamente mediante clave
# como argumento de la función:

print(f'Resultado de items() a diccionario_dnis: {list(diccionario_dnis.items())}')
print(f'El resultado devuelto por popitem() del diccionario diccionario_dnis es: {diccionario_dnis.pop('Jose')}')
print(f'Resultado de items() a diccionario_dnis: {list(diccionario_dnis.items())}')

# El último contenedor básico nativo a Python son los set() o conjuntos.

# A estos se les puede aplicar las operaciones matemáticas asociadas a conjuntos.
# Hasta ahora hemos visto 3 contenedores: lista, diccionario y tupla.
# En general, tendremos suficiente con usar listas, también por su versatilidad de métodos.
# El conjunto o 'set' (en inglés) es un contenedor, que a diferencia de los demás
# 1 - Sus elementos en su interior no estan ordenados por ningún tipo de índice:
# Es decir, no se usan índices para acceder a su contenido (los objetos que contiene)
# y por tanto se encuentran 'desordenados' en su interior.
# 2 - Los elementos de su interior no pueden estar repetidos. En gran medida porque
# los elementos no estan indexados. No deja almacernar objetos con el mismo contenido.
# 
# De igual manera a las listas y diccionarios, es un contenedor mutable, es decir,
# podemos añadir, quitar, modificar objetos en su interior.

conjunto = set()

# Tanto la clase set como la clase diccionrio (dict) usan los mismos delimitadores 
# sintácticamente = {}
# El tema es que si queremos crear un set en vez de un dict y hacemos lo siguiente,
# se creará un dict.

print()
conjunto2 = {}

print(f'La instancia que apunta conjunto2 es un set? {isinstance(conjunto2, set)}')
print(f'La instancia u objeto que apunta conjunto2 es: {conjunto2.__class__}')
print()
conjunto2 = {1, 2, 3, 4, 5, 6, 7}

print()
print(f'Ahora la instancia que apunta conjunto2 es un set? {isinstance(conjunto2, set)}')
print(f'Ahora la instancia u objeto que apunta conjunto2 es: {conjunto2.__class__}')

# Métodos propios de los conjuntos:
# 1 - Los sets o conjuntos dhacen referencia directamente a los sets o cojuntos
# matemáticos, es decir, se operan como aquellos, por lo tanto, tienen asociadas funciones 
# matemáticas de: direrencia, intersección, unión.
# Además tiene funciones típicas o clásicas de otros conjuntos como las de añadir
# un elemento o varios, borrar elementos, etc.
# Ejemplos
# 1 - set.intersection() -> nos devuelve la instersección entre el mismo objeto que invoca
# al método y los iterables (otros contenedores, strings, etc...) que le pasemos como
# argumento/s.

set1 = {1, 2, 3, 4, 'hola', 'feo'}
set2 = {3, 4, 'hola', 'janders', 5, 6}

print()
print(f'La intersección entre set1 y set2 es: {set1.intersection(set2)}')
print(f'La intersección entre set1 y set2 es: {set2.intersection(set1)}')

# 2 - set.union() -> nos devuelve la unión entre el mismo objeto que invoca
# al método y los iterables (otros contenedores, strings, etc...) que le pasemos como
# argumento/s.

print()
print(f'La unión entre set1 y set2 es: {set1.union(set2)}')
print(f'La unión entre set1 y set2 es: {set2.union(set1)}')

# 3 - set.difference() -> Nos devuelve la diferencia o objetos que NO tienen en común dos conjuntos
# ¡OJO! No se trata de una operación simétrica como vemos a continuación.

print()
print(f'La diferencia entre set1 y set2 es: {set1.difference(set2)}')
print(f'La diferencia entre set2 y set1 es: {set2.difference(set1)}')

# Luego, derivadas de los 3 métodos anteriores, tenemos funciones de actualización.
# set.difference_update(set2) modifica set dejando en éste solo los elementos que 
# no tiene set2, o dicho de otro modo, elimina de set los elementos que también
# estan en set2.


set1.difference_update(set2)
print()
print(f'La ejecución de set1.difference_update(set2) resulta en: {set1}') 
print(f'El contenido de set2 queda inalterado: {set2}')

# set.intersection_update(set2) modifica set dejando en este solo los elements en común
# con set2, o dicho de otro modo, elimina de set los elementos que no tiene 
# set2 en su interior.

set1 = {1, 2, 3, 4, 'hola', 'feo'}
set2 = {3, 4, 'hola', 'janders', 5, 6}
set1.intersection_update(set2)
print()
print(f'La ejecución de set1.intersection_update(set2) resulta en: {set1}') 

# Otras funciones interesantes de los conjuntos:
# set.clear() -> Elimina todos los elementos de un conjunto dejándolo vacío.
# set.discard(objeto) -> Elimina el objeto que le pasamos como argumento del conjunto si existía en este
# si no estaba dentro del conjunto, no hace nada.
# set.copy() -> Devuele una copia "superficial" del conjunto, es decir, solo devuelve
# una referencia a este conjunto sin realmente copiarlo creando uno nuevo.
# set.remove(objeto) -> Hace lo mismo que discard, pero si el objeto argumento no se encuentra
# en el conjunto sí que devuelve una execpción de tipo KeyError.
# set.isdisjoint(set2) -> devuelve un Booleano indicando si los dos conjuntos no tienen
# ningún elemento en común (True), False si lo tienen.
# set.issubset(set2) -> Devuelve True si los elementos de set están contenidos o forman
# parte de set2.

set1 = {1, 2}
set2 = {1, 2, 'janders', 3, 4}
set3 = {1, 3}
set4 = {1, 2}

print()
print(f'set1 es un subconjunto de set2? = {set1.issubset(set2)}')
print(f'set1 es un subconjunto de set3? = {set1.issubset(set3)}')
print(f'set1 es un subconjunto de set4? = {set1.issubset(set4)}')

# set.supersert(set2) -> Devuelve True si set2 a sido creado a partir de elementos o 
# de los objetos de set, es decir, que set2 es un subconjunto de set, devuelve False
# en caso contrario.

print()
print(f'set1 es un superconjunto de set2? = {set1.issuperset(set2)}')
print(f'set1 es un superconjunto de set3? = {set1.issuperset(set3)}')
print(f'set1 es un superconjunto de set4? = {set1.issuperset(set4)}')

set1 = {1, 2, 'janders', 3, 4}
print()
print(f'Set1 ahora es: {set1}')
print(f'set1 es un superconjunto de set2? = {set1.issuperset(set2)}')
print(f'set1 es un superconjunto de set3? = {set1.issuperset(set3)}')
print(f'set1 es un superconjunto de set4? = {set1.issuperset(set4)}')