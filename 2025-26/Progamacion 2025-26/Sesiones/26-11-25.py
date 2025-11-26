# Repàs d'operadors lògics.
# Exemple
n = 5
n2 = 3
n3 = 3
if n > 5 and (n2 == 3 or n3 > 2):
    '''
    S'executarà primer sempre el que hi ha entre parèntesi, com a les regles matemàtiques
    Haureu de fer servir parèntesi per esclarir la lògica de les operacions.
    '''

# Operadors aritmètics.
# Suma -> +
# Però si l'utilitzo amb tipus de iterables com llistas o str, és un operador de concatenació.

# Resta -> -

# Multiplicació -> *
# Però si l'utilitzo amb str (i amb algun iterables) el que farà es repetir aquell str el nombre de 
# vegades igual al número que es multiplica. !CUIDADO¡ en aquest cas no es poden fer servir els float.
cadena = 'hola '
print(cadena*7)

# Divisio -> / (slash)
print()
print(15/4)

# Operador mòdul -> % 
# Es tracta d'un operador molt utilitzat que ens dona la resta d'una divisió entera.
# S'utilitza molt sovint per comprovar si un nombre es parell o senar quan feiem (num % 2).
print()
print(f'El resultat de 15%2 és = {15%2}')
print(f'El resultat de 16%2 és = {16%2}')

# Operador potència -> **
# 3 ** 2 = 9
print()
print(f'El resultat de 16**2 és = {16**2}')

# Operador de divisió sencera -> //
# Ens dona la part sencera d'una divisió.
print()
print(f'El resultat de 15//2 és = {15//2}')

# Obviament aquests operadors (llevat les excepcions explicades) només es poden aplicar 
# a tipus de nombres (int i float).

# Continuaciò d'estructures de control de fluxe:
# if - elif - else
# elif es una combinació de else i if, vol dir, que si la condició anterior no s'ha complit, comprovem
# la condició (o condicions) que es troben a la dreta del elif:
# Exemple:
# He de fer un algoritme que comprovi en quin rang d'anys cotitzats es troba una persona
# per calcular la seva pensió a l'hora de jubilar-se.
# Diguem que tenim 5 trams d'anys cotitzats:
# 1er tram -> d'1 any a 10 anys
# 2on tram -> de més de 10 anys a 15 anys
# 3er tram -> de més de 15 anys a 20 anys
# 4rt tram -> de més de 20 anys a 30 anys
# 5è tram -> de més de 30 anys
# Primera solució si feiem servir el clàssic if-else:
anyscotit = int(input('Introdueix el nombre d\'anys cotitzats: '))
if anyscotit >= 1 and anyscotit <= 10:
    print('Imprimiem el càlcul de la jubilació del primer tram.')
else:
    if anyscotit <= 15:
        print('Imprimiem el càlcul de la jubilació del segón tram.')
    else:
        if anyscotit <= 20:
            print('Imprimiem el càlcul de la jubilació del tercer tram.')
        else:
            if anyscotit <= 30:
                print('Imprimiem el càlcul de la jubilació del quart tram.')
            else:
                print('Imprimiem el càlcul de la jubilació del cinquè tram.')

# Si ho volguèssim fer tot en la mateixa columna (sense identar):
print()
anyscotit = int(input('Introdueix el nombre d\'anys cotitzats: '))
if anyscotit >= 1 and anyscotit <= 10:
    print('Imprimiem el càlcul de la jubilació del primer tram.')
if (anyscotit > 10) and (anyscotit <= 15):
    print('Imprimiem el càlcul de la jubilació del segón tram.')
if (anyscotit > 15) and (anyscotit <= 20):
    print('Imprimiem el càlcul de la jubilació del tercer tram.')
if (anyscotit > 20) and (anyscotit <= 30):
    print('Imprimiem el càlcul de la jubilació del quart tram.')
if (anyscotit > 30):
    print('Imprimiem el càlcul de la jubilació del cinquè tram.')

# Tenim la possibilitat de no anar-nos a la dreta kilòmetres i no tenir que fer el doble
# de comparacions amb 'elif'
print()
anyscotit = int(input('Introdueix el nombre d\'anys cotitzats: '))
if anyscotit < 1:
    print('Fkn vago!')
elif anyscotit >= 1 and anyscotit <= 10:
    print('Imprimiem el càlcul de la jubilació del primer tram.')
elif (anyscotit <= 15):
    print('Imprimiem el càlcul de la jubilació del segón tram.')
elif (anyscotit <= 20):
    print('Imprimiem el càlcul de la jubilació del tercer tram.')
elif (anyscotit <= 30):
    print('Imprimiem el càlcul de la jubilació del quart tram.')
else:
    print('Imprimiem el càlcul de la jubilació del cinquè tram.')

# Una altra estructura molt interessant quant tenim opcions d'entrada limitades, una estructura
# condicional molt eficient és la de match - case:
# En el cas de l'exercici de determinar el dia de la setmana a través d'un nombre
# enter, farem servir aquesta estructura:

numdia = input('Introdueix el dia de la setmana: ')
match numdia:
    case '1':
        print('És Dilluns.')
    case '2':
        print('És Dimarts.')
    case '3':
        print('És Dimecres.')
    case '4':
        print('És Dijous.')
    case '5':
        print('És Divendres.')
    case '6':
        print('És Dissabte.')
    case '7':
        print('És el dia de tocar-se els cataplins.')
    case _:
        print('No és un día vàlid')
    
# "Slicing" en les llistes:
# És una sintaxi molt últil en Python per seleccionar porcions determinades d'una llista.
# La sintaxi és: llista[primer_index:segon_index]
# Si escribim l'anterior tenint en compte que llista es de tipus 'list' el que farem es 
# agafar una tallada de la llista que anirá des de el valor que es troba a la posició de primer_index
# fins a l'element en la posició de segon_index SENSE INCLUIR AQUEST DARRER.
# Exemple:
llista = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 555555, 3, 2, 1]
# Què faria si vull agafar només la primera meitat de la llista?
# recorda que pots utilitzar la funció len() que et retorna el nombre d'elements que conté
# una llista.
print('La meitat de la llista "llista" seria: ')
print(llista[0:len(llista)//2])

# Què fariem si volem agafar la segona meitat de la llista?
print('La segona meitat de la llista "llista" seria: ')
print(llista[len(llista)//2:len(llista)])

# Es poden agafar elements d'una llista sense ser consecutius fent servir la sintaxi anterior i afegint
# un valor més ->  llista[primer_index:segon_index:salt]
print(llista[0:len(llista):2])

# Si vull obtenir una llista amb els elements invertits, a més d'utilitzar el .reverse()
# puc utilitzar la sintaxi llista[::-1]
print(llista[::-1])