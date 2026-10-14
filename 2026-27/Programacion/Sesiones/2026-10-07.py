# VERY IMPORTANT!
# SI NO SABES USAR ESTO, LA ASIGNATURA DE PROGRAMACIÓN SE VUELVE IMPOSIBLE DE SUPERAR.
# Estructuras de control de flujo de ejecución.

# ESTRUCCTURAS DE CONTROL DE FLUJO DE EJECUCIÓN:
# Estructuras de control de flujo sin bucle.
# La palabra clave 'if' - 'else' -> Comprobación condicionante

# Parentesis: introducción al "casting"
# El "casting" es la conversión de tipos compatibles.
# Se realiza a traves de: clase_a_convertir(objeto_de_case_diferente)
# Ejemplos:
# Convertimos a tipo int un string:
numero = int('5')
cadena = str(52365.5)
decimal = float(5)

# ¡OJO! No podéis hacer conversiones no compatibles, no todas las expuestas arriba
# son bidireccionales, os puede devolver una excepción de tipo TypeError o de error
# de conversión.

# Función para leer desde teclado, devuelve una cadena de caracteres (str) con los
# valores de las teclas pulsadas hasta el momento de pulsar la tecla "Intro" (que no devuelve).
# Función 'input()'


numero = float(input('Introduce un número: '))

if numero > 10:
    print('El número introducido es mayor que 10.')
else:
    if numero == 10:
        print('EL número introducido es el 10.')
    #No tengo obligación de poner el else, pero lo haremos idependientemente de si es necesario.
    else:
        print('El número introducido es menor que 10')

# Si tenemos que comparar o evaluar varios condicionantes al mismo tiempo, podemos
# poner en un mismo if varias operaciones lógicas i concatenarlas con 'or' o 
# con 'and' según la lógica. Los operadores clásicos de or son '||' y el operador
# clásico del 'and' es '&'

# Imaginemos que tenemos que evaluar que el número introducido sea mayor o igual que
# 10 en un mismo if, tenemos 2 opciones:

if (numero > 10) or (numero == 10):
    print('El número es mayor o igual a 10.')

if numero >= 10:
    print('Hacemos lo mismo que en el condicional anterior pero con el operador >=')


# Utilizando la palabra reservada 'elif', lo anterior, lo podríamos hacerlo de la manera
# siguiente.


if numero > 10:
    print('El número introducido es mayor que 10.')
elif numero == 10:
    print('EL número introducido es el 10.')
else:
    print('El número introducido es menor que 10')

# Lo anterior sería equivalente a
if numero > 10:
    print('El número introducido es mayor que 10.')
else:
    if numero == 10:
        print('EL número introducido es el 10.')
    else:
        print('El número introducido es menor que 10')

# Python nos ofrece una comparación inmediata cuando tenemos un número de opciones
# limitadas y cuantificadas --> El bloque match - case - case _: -->
# Las ventaja del uso de este bloque en particular es el ahorro de ejecución de 
# instrucciones de comparación cuando sabemos el número de opciones que tenemos = 
# solo se ejecuta una vez y el flujo de ejecución se sitúa en la deseada.
menu = ''' 1 - Elige la opción 1 introduciendo este número.
2 - Elige  la opción 2 introduciendo este número.
3 - Elige  la opción 3 introduciendo este número.
4 - Elige  la opción 4 introduciendo este número.
Otro caracter - Introduce cualquier otra cosa.

'''

mensaje_sal = 'Has elegido la opción:'

menu_sel = int(input(menu))
match menu_sel:
    case 1: # En cada case 'valor' se especifica el 'valor' a ser comprobado.
        print(mensaje_sal, 1)
    case 2: # El case solo adminte LITERALES, no admite variables.
        print(mensaje_sal, 2)
    case 3:
        print(mensaje_sal, 3)
    case 4:
        print(mensaje_sal, 4)
    case _: #La barra baja proces el 'caso por defecto' es decir: cualquiera que no sea de los anteriores
        print('No has elegido ninguna de las opciones válidas')