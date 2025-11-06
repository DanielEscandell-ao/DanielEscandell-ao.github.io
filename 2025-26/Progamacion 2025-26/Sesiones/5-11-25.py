# Otros tipos de datos nativos a Python (y otros lenguajes).
# Parece bastante obvio que podamos trabajar tambien con binarios, exadecimales y octales.
# Tipo 'bin'

binario1 = bin(58)
print(f'El número binario1 = 58 se traduce en binario a {binario1}') # Uso de cadenas formateadas f'' en el print.

# Por ejemplo, aquí llamamos a un método __str__() que pertenece a casi todos los objetos 
# en Python.
print(binario1.__str__())

# Aquí imprimios de qué se trata __str__() a través de la DEFINICIÓN (la clase) de los objetos bin.
print(bin.__str__())

# En PYthon tenemos definiciones de objetos y tenemos los objetos que son creaciones de conjuntos de
# datos a partir de esas definiciones.
# Definicion es -> El "tipo" o "clase" de dato.
# El objeto es -> el dato en si mismo (ej: un string o un entero concreto).

# Para comprenderlo mejor pensemos en un ejemplo:
# Por un lado tenemos la DEFINICIÓN de un coche, es decir, la explicación detallada de como son los coches.
# A eso lo llamaríamso una CLASE, la CLASE 'COCHE'.
# Por otro lado tenemos coches en la realidad, un ferrario rojo con una matrícula 4987HMR sería un OBJETO
# concreto de TIPO o CLASE CHOCHE.

# La diferencia es que en lenguajes de programación todo son datos, no existe otra realidad física.

# Dentro de los tipos de información lógico relacionado con los binarios tambien tenemos:
# Hexadecimales.
# Octales.

hexadecimal1 = hex(53521351351)
print(f'El número entero 53521351351 se traduce al hexadecimal {hexadecimal1}')

octal1 = oct(53521351351)
print(f'El número entero 53521351351 se traduce al hexadecimal {octal1}')

# Otro tipo de dato nativo y básico de cualquier lenguaje: los Booleanos o 'Bool' en Python.
verdadero = True
falso = False
# Solo existen estos dos posibles valores y nos permiten realizar todo tipo de operaciones 
# cuyo resultado sea o Verdad (True) o Mentira o Falso (False).
# Dentro de la interpretación de valores como True o False tenemos los Truthy y Falsy
# Estos dos últimos son equivalencias de otros datos que significan True o Falso (respectivamente).
# Por ejemplo: 
# 1 -> Un valor entero o float diferente de 0 se interpretará siempre como verdadero (aunque sea negativo).
# 2 -> El valor 0 (ya sea entero o float) se interpretará siempre como falso o 'False'.
# 3 -> Un string vacío ('' o "") se interpretará siempre com falso o 'False'.
# 4 -> Un string NO vacío siempre se interpretará como verdadero o 'True'.

# LOS CONTENEDORES EN PYTHON
# TIPOS

# 1 EL MÁS VERSÁTIL Y POPULAR ES LA LISTA ('LIST' EN PYTHON):
# Se trata de un conjunto de datos ordenado.
# Ordenado te refieres de mayor a menor? o alfabéticamente? -> NO NO NO NO
# En este caso, en programación, ordenado hace referencia a que se puede acceder a este dato
# usando un índice que indica su posición dentro de la lista.
# En las listas (y otros contenedores) las posiciones se indican por número entero y la primera
# posición siempre es la '0'.
# Ejemplo de inicialización de una lista:

listaejempl1 = [1, 2, 4, 3, 5, 6, 8, 1, 2, 3] # La lista siempre está contenida por los caracteres []
# y sus elementos o los objetos que contiene están separados por coma (los espacios no son obligatorios)
# pero forman parte de las normas de buena codificación.
# En este caso el primer elemento (1) estará en la posición 0 y el último elemento (3) está en
# la posición 9; pero OJOJOJO, la lista contiene 10 elementos.
# Entonces, podemos decir que el último elemento de una lista estará en la posición n - 1 donde n es
# la longitud de la lista (o su tamaño).

# Cómo hago yo para recuperar el objeto o elemento que está en la posición 8?
print(f'El elemento en la posición 8 de listaejempl1 es {listaejempl1[7]}')

# Como hemos dicho, todos los tipos de datos (incluso los contenedores como las listas) tienen
# atributos y métodos (o funciones) asociados.

# Para el próximo día me váis a investigar qué hacen los siguientes métodos e las listas.
list.append()
list.clear()
list.count()
list.extend()
list.insert()
list.remove()
list.reverse()
# Ayudaos del bocadillo contextual de Python.

# Además de estudiar todo lo que se ha dado hasta el momento (preguntas).