# Estructura iterable (bucle) "for <value> in <iterable)".
# Només serveix per a recórrer iterables o contenidors de dades (llistes, tuples, diccionaris, conjunts, strings...)
# Exemple 1:

llista1 = ['a', 'c', 1, 3, 45, 'Janders', 'final']
i = 1
for element in llista1:
    print(f'En la iteració {i}, el valor de la variable element es: {element}')
    i += 1

# Imagineu ara que amb el for volem executar un nombre d'iteracions en funció
# d'una variable numèrica entera que e podem entrar per teclat.
# Exemple 2: imagina que vols demanar una quantitat de nombres en funció d'un número introduït per l'usuari a través
# del teclat (si introdueix un 2, hauràs de demanar 2 números, si introdueix un 3, hauras de demanar 3 números...)
# Podem utilitzar una funció nativa al llenguatge que es diu "range()".
print()
nombrentr = int(input('Introdueix un nombre enter positiu: '))
iterablerange = range(nombrentr)
print(f'La funció range(nombrentr) resulta en el següent {iterablerange}')
print(f'La funció range(nombrentr) resulta en el següent {list(iterablerange)}')

llistanum =  []
for numero in iterablerange:
    llistanum.append(float(input(f'Introdueix el {numero+1}º nombre en la llista: ')))

print()
print(f'La llista que em emplenat conté {llistanum}.')

# NO ES POT UTILITZAR EL FOR AMB EL RANGE PER SIMULAR UN WHILE, només vull que conegueu que exiteix aquesta possibilitat.
# Només (pel moment) utilitzarem el for per recórrer iteratius.
print()
cadena = input('Introdueix una cadena cualsevol: ')
numchar = 1
for caracter in cadena:
    print(f'El carcater num {numchar} de la cadena"{cadena}" es: {caracter}')
    numchar += 1 # numchar = numchar + 1

# Deures per al proper dia:
# Fer els exercicis de l'1 al 6 de la pràctica 7 publicada en el classroom.
# Fer el següent exercici:
# Es demanar a l'usuari que introdueixi una cadena de caràcters per teclat y el bucle for haurà de processar aquesta cadena
# i crear-ne una de nova amb les lletres minúscules y majúscules alternades.
# Exemple:
# Si l'usuari introdueix la cadena "MaduroMArica"
# La sortida haurà de ser: "MaDuRoMaRiCa"

# Recordeu
print()
cadena = 'MaduroMariquita'
print(cadena.upper())
print(cadena)