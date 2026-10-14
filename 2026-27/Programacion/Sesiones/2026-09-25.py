# Apunte para el trabajo con strings -> uso del carácter de escape. = \
cadena = 'hola que tal \'amigo\'.'
cadena2 = "hola que tal 'amigo'."
cadena3 = "hola que tal \"amigo\"."

# El caracter de escape se usa también para definir caracteres invisibles en el texto,
# como:
saltodelinea = '\n' # -> Caràcter de salto de línea.
tabulador = '\t' # -> tabulador o tabulación.
retornodecarro = '\r\n' # -> retorno de carro (muy parecido al \n)

# Operadores lógicos o booleanos. (De comparación).

# 1 Operador de comparación 'igual' --> ==
# Siempre tiene que comparar variables del mismo tipo o clase o que su contenido
# sea equiparable. Compara el contenido de estas. Obviamente también puede
# comparar literales aunque sería absurdo (aunque es habitual comparar una variable
# con un literal).
print('Ejemplo operaciones de comparación de igualdad.')
print()
num1 = 5
num2 = 5

print(num1 == num2)
print()


num1 = 4
print(num1 == num2)
print()

cadena1 = 'hola'
cadena2 = 'hola'
print(cadena1 == cadena2)
print()

cadena2 = 'Hola'
print(cadena1 == cadena2)
print()

num1 = 5.0
num2 = 5
print(num1 == num2)
print()

num5 = '5'
print(int(num5) == num2)
print()

# Comparador de 'es diferente a' --> !=
# Tenemos que procurar que la comparación siempre sea entre variables del mismo tipo o clase.
# Pero como hemos visto en las líneas anteriores, hay ciertos tipos que debido a su
# similitud pueden ser comparados sin conversión previa.
print('Ejemplo operaciones de comparación de desigualdad.')
print()
print(num1 != num2)
print()

print(cadena1 != cadena2)
print()

# Comparador de 'es mayor que' --> >
print('Ejemplo operaciones de comparación de mayor que.')
print()
num1 = 6
print(num1 > num2)
print()

# Ejemplo un poquito más complejo con el uso de la función len(str)->int
# len() es una función que coje un str como argumento y devuelve su longitud
# de caracteres en formato entero.

print(len('hola que tal') > len('janders'))

# Comparador de 'es menor que' --> <
print('Ejemplo operaciones de comparación de menor que.')
print()
print(num2 < num1)
print()
print(num1 < num2)
print()
num1 = 5
print(num1 < num2)
print()

# Comparador de 'es mayor o igual que' --> >=
print('Ejemplo operaciones de comparación de mayor o igual que.')
print()
print(num1 >= num2)
print()
num1 = 7
print(num1 >= num2)
print()

# Comparador de 'es menor o igual que' --> <=
print('Ejemplo operaciones de comparación de menor o igual que.')
print()
print(num1 <= num2)
print()
num1 = 5
print(num1 <= num2)
print()


# Operador 'o' lógico (or en inglés).
# El resultado del operador 'or' siempre será True cuando al menos una de las condiciones
# sea cierta o True.
# num1 = float(input('Introduce un número menor que 100 o mayor que 1000: '))
# Hay que recordar que la función Input('Mensaje de entrada') recibe datos desde el teclado
# y asume o los considera de tipo str(), si queremos operar con ellos debemos hacer la
# conversión de datos adecuada a las operaciones que queramos realizar.

print('Ejemplo operaciones con booleanos.')
print()
print((num1 < 100) or (num1 > 1000))
print()
print(False or True)
print(False or False)

# El comparador del lenguaje lógico 'y' (and en inglés) --> and
# Solo resultará verdadero si los dos operadores son True (Verdadero)

print()
print(True and True)
print(True and False)
num1 = float(input('Introduce un número mayor que 100 y menor que 1000: '))
print((num1 > 100) and (num1 < 1000))
print()

# Pequeñas demostraciones sobre conversión de tipos (casting)
castfloat = float('2.5e-4')
# castfloat2 = float('0,5E-25')
print(castfloat)

# El operador lógico 'no' (not en inglés) --> not
# Es un operador que invierte un booleano o el resultado de una comparación lógica.
# Además, este comparador suele ir acompañado de la palabra clave 'is' (es en Español)
# Hay que ir con cuidado con esta palabra clave, usualmente compara si es la
# misma instancia y puede dar resultados inesperados si esperamos una comparación
# de contenido.
print(True and not False)
print()

# Hagamos un ejemplo que solo responda True a si tiene derecho a una beca si la persona
# que la solicita es de género femenino y a superado el grado superior.

sexopersona1 = 'f'
sexopersona2 = 'm'
sexopersona3 = 'f'

tituladosuppers1 = True
tituladosuppers2 = True
tituladosuppers3 = False


print('La persona 1 tiene derecho a beca?')
print((sexopersona1 == 'f') and tituladosuppers1)
print('La persona 2 tiene derecho a beca?')
print((sexopersona2 == 'f') and tituladosuppers2)
print('La persona 3 tiene derecho a beca?')
print((sexopersona3 == 'f') and tituladosuppers3)