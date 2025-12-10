#Exercicis de teoria:
#1 - Explica els diferents tipus de contenidors de dades i les seves característiques i, per tant, les seves diferències. 1 punt

# Los diferentes contenedores de datos que existen en python son:
# - variables: las variables son contenedores de datos que almacenan un dato.
# - listas: Las listas son contenedores de datos que almacenan mas de un dato.
# - sublistas: las sublistas son contenedores de datos que estan dentro de una lista.

#2 - Digues quin tipus de dades natius de Python hem vist a classe i explica’ls. 0.75 punts.

# - Str: los tipos de datos str 'string' son los que contienen caracteres de todo tipo.
# - int: los tipos de datos int 'enteros' son los que contienen numeros enteros.
# - float: los tipos de datos float son los que contienen numeros enteros y reales.
# - bin: los tipos de datos bin 'binario' son los que contienen numeros en formato binario.
# - booleanos: los tipos de datos booleanos son los que contienen 'true' o 'false'.
# - hex: los tipos de datos hex 'hexadecimal' son los que contienen numeros en formato hexadecimal.
# - oct: los tipos de datos oct 'octales' son los que contienen numeros en formato octal.

#Exercicis de condicionals:
#3 - Crea un petit programa que demani que l’usuari introdueixi per teclat una  opció de l’1 al 5 (pot ser processat com a enter o com a caràcter) i que imprimeixi per pantalla 
#“Has introduït l'opció -nombre introduït-” o, en el cas de no introduir una opció correcte imprimeixi “No has introduït una opció vàlida”. 1’75 punts
n = int(input('Introduce un numero del 1 al 5: '))
if n == 1:
    print(f'Has introducido la opcion {n}')
elif n == 2: 
    print(f'Has introducido la opcion {n}')
elif n == 3:
    print(f'Has introducido la opcion {n}')
elif n == 4:
    print(f'Has introducido la opcion {n}')
elif n == 5: 
    print(f'Has introducido la opcion {n}')
else:
    print('No has introducido una opcion valida!')      

#4 - (Exercici amb condicionals). Escriu un programa que llegeixi una lletra per teclat i digui si es tracta d’una vocal. 
# Haureu de tenir en compte les majúscules també, no serà necessari tenir en compte les vocals amb accent o altres. Una altra cosa que haurà de fer el programa serà la d’imprimir un missatge d’error 
# “Has introduït més d’una lletra” si l’usuari introdueix 2 o més lletres com a missatge d’entrada. 1’75 punt
letra = input('Introduce una letra: ')
letral = list(letra)
letrac = len(letral)
letram = letra.lower()
if letrac >= 2:
    print(f'Has introducido {letrac} letras. Por favor intentalo de nuevo.')
else:
    if letram == 'a' or letram == 'e' or letram == 'i' or letram == 'o' or letram == 'u':
        print('Tu letra es una vocal')
    else:
        print('Tu letra no es una vocal.')

#5 - (Exercici amb condicionals). Crea una calculadora per donar-te un impost d’IRPF total a pagar en funció d’un salari introduït per l’usuari. 
# Una vegada que l’usuari introdueixi el seu salari (haurà de ser transformat en ‘float’) la calculadora fará el següent:
#Si el salari és inferior o igual a 15000€ anuals, l’usuari no haurà de pagarà res.
#Si el salari és troba entre els 15000€ i els 30000€ (aquest darrer inclòs) l’usuari haurà de pagar el 17% d’aquest en IRPF (multiplica el salari per 0.17 i ja tens la quantitat).
#Si el salari es troba entre els 30000€ i els 45000€ (aquest darrer inclòs) l’usuari haurà de pagar el 23% d’aquest en IRPF (multiplica el salari per 0.23 i ja tens la quantitat).
#Si el salari és superior a 45000€ l’usuari haurà de pagar el 37% d’aquest salari en IRPF (multiplica el salari per 0.37 i ja tens la quantitat). 2 punts
impuesto = float(input('Introduce tu salario: '))
if impuesto < 15000:
    print('No tienes que pagar nada!')
elif impuesto > 15000 and impuesto < 30000:
    print(f'Tienes que pagar {impuesto * 0.17}')
elif impuesto > 30000 and impuesto < 45000:
    print(f'Tienes que pagar {impuesto * 0.23}')
elif impuesto > 45000:
    print(f'Tienes que pagar {impuesto * 0.37}')

#Exercicis de bucles:
#6 - Crea un menú ‘infinit’ del qual només es pugui sortir quan l’usuari introdueix per teclat el número 3. Aquest menú haurà de tenir 3 opcions: 1.5 punts.
#1a opció: ‘Introdueix el número 1 per saludar-te’, i si l’usuari introueix aquest número el programa haurà de contestar: ‘Hola que tal Pascual’.
#2a opció: ‘Introdueix el número 2 per fer una suma’, llavors, demanará dos números per teclat i imprimirà per pantalla: “La suma del ‘num1’+ ‘num2’ és: ‘resultat de la suma’”.
#3a opció: ‘Introdueix el número 3 per sortir d’aquest menú’, si el usuari introdueix el número 3, haurà d’imprimir ‘Adeu Mateu.’ i haurà de finalitzar.
while True:
    n = int(input('Introduce un numero del 1 al 3: '))
    if n == 1:
        print('Hola que tal Pascual.')
    elif n == 2:
        a = int(input('Introduce el primer numero: '))
        b = int(input('Introduce el segundo numero: '))
        print(f'La suma de {a} + {b} es igual a: {a + b}')
    elif n == 3:
        print('Adeu Mateu')
        break

#7 - Realitza un programa que demani a l’usuari un nombre i un caràcter d’entrada i a partir d’aquests realitzi el següent patró (exemple per a nombre = 4 y per a caràcter = #) :
#“””
#1#
#2##2##
#3###3###3###
#4####4####4####4####
#1.25 punts.
n = int(input('Introduce un numero: '))
caracter = input('Introduce un caracter: ')
i = 1
while n >= i:
    print((i,caracter * i) * i)
    i = i + 1