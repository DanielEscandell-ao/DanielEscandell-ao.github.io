# Tipos de datos navitos en Python.
# En Python todo es un objeto = sintaxis de uso del punto despdués de la variable o
# el literal.
# En lenguajes de programación, la programación orientada a objetos es uno de los 
# paradigmas más importantes de la programación. 
# Un objeto, en código, es un tipo de dato virtual que además incorpora métodos y
# atributos que son accesibles a partir de una sintaxis "nombre_objeto.nombre_atributo"
# si queremos acceder a un atributo o "nombre_objeto.nombre_método" si queremos acceder
# a un método.

# Objeto 1 = tipo string o "str" en Python. Es NATIVO del del lenguaje.
cadena = str() # Creamos una variable llamada "cadena" del tipo str ("string").
cadena = "Hola que tal Pascual."
print(cadena)
print()
print('Estoy imprimiendo un literal')
print("")
cadena = "Primera sesión del 23 de septiembre."
print(cadena)
cadena2 = "HOLA QUE TAL"
print(cadena2)
cadena = "cosa" # El operador "=" en Python (y otros lenguajes de programación) se conoce
# como el operador de asignación --> asigna un contenido y sobreescribe el que tenía
# anteriormente la variable.

# A continuación ejemplificamos como el tipo str (sus objetos) SON INMUTABLES.
print("")
print(cadena.upper()) #Imprimimos lo que nos genera el método upper() de la clase "str"()
print()
print(cadena)
print()
cadena = cadena.upper() #EL orden de ejecución siempre es de derecha a izquierda a no
# ser que lo modifiquemos con el uso de paréntesis.
print(cadena)


# Tipo de dato "int" (entero -números sin decimal-). Se suelen usar 16 bits para representarlo
entero = int()
entero = 1250

# Tipo de dato "float" (número con decimales). Se suele representar con 32 bits.
decimal = float()
decimal = 5.6578494

#APUNTE! Siempre hay que seleccionar el tipo de dato correcto para el objeto que 
# queremos representar. Ejemplo: no usaremos un decimal ("float") para representar
# un elemento de la realidad que puede ser representado en números enteros (utilizaríamos
# más memoria de la necesaria).

# Tipo de dato booleano = "bool". Representa un cierto-falso, si o no.
# Este tipo de dato se almacena habitualmente usando un solo bit.
booleano = bool()
booleano = False
booleano = True

# Tipo de dato binario, o tratamiento de enteros desde binario, los métodos
# bin(), oct(), hex(). Nos permiten transformar números enteros en las diferentes
# representaciones binarias de la información digital.
# El sistema octal es un encapsulamiento de 3 bits (0 - 7)
# El sistema de representación hexadecimal es un encapsulamiento de 4 bits (0 - F)
print()
print(bin(157))
print()
print(oct(157))
print()
print(hex(157))

# Número complejo representado en Python: podemos transformar string que representa
# un número complejo en una clase o tipo "complex" usando el método complex(str)
# El formato de los números complejos es = a + bj (bi) - La a representa la parte real
# o numérica del número comblejo (eje x o dimensión horizontal) y la b representa la
# parte imaginaria del número complejo (eje y o dimensión vertical).
complejo1 = complex('1+3j')
complejo2 = complex('2-4j')
print(complejo1 + complejo2)

# Python tiene la habilidad de identificar el tipo de dato desde la asignación a una variable
# , a diferencia de otros lenguajes de programación, no necesitamos declarar el tipo de dato
# antes de usarlo = Python es capaz de reconocerlo e INSTANCIARLO.
numero = 125
cadena2 = "hola que tal Pascual"
complejo3 = 1 + 3j
booleano2 = False
print(numero.__class__)
print(cadena2.__class__)
print(complejo3.__class__)
print(booleano2.__class__)

# Operadores con números en Python.
# Operadores numéricos (aritméticos).
print('Seguidamente mostraremos diferentes resultados de operadores matemáticos:')
numero1 = 32
numero2 = 4.0

# Operador suma -> +
print('Operador Suma \'+\' :')
print(numero1 + numero2)

# Operador resta -> -
print('Operador resta \'-\' :')
print(numero1 - numero2)

# Operador multiplicación -> *
print('Operador multiplicación \'*\' :')
print(numero1 * numero2)

# Operador división -> / (slash)
print('Operador división \'/\' :')
print(numero1 / numero2)

# Operador potencia -> **, también existe la función o método pow(a,b) = a^b
print('Operador potencia \'**\' :')
print(numero2**2)

# Operador división entera -> // (doble slash) -- Quita la parte decimal pero no redondea.
print('Función división entera \'//\' :')
print(31 // 4)

# Valor absoluto -> se realiza a través del método abs(num)
print('Función valor absoluto \'abs(num)\' :')
print(abs(-35))

# Operador módulo % --> nos calcula/devuelve el resto de la división.
print('Función valor absoluto \'%\' :')
print(30 % 4)

# Función/método round(num) nos redondea siguiendo las normas de redondeo clásicas un
# número decimal a su valor aproximado.
print('Función round(num):')
print(round(7.7563514351))
print(round(7.7563514351, 1))
print(round(7.7563514351, 2))