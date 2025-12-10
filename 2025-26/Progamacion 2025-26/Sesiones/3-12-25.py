# INtroducción a las estructuras iterativas.
# Estructura while (condició):
# 'While' que vol dir 'mentres que' en  Català indica que les línies o instruccions que 
# pertanyin a aquest bucle es repeteixin mentres que el compleix la condició, és adir,
# mentres la condició resulta ser True.
# L'estructura concreta és:
# while (condició -dona un booleà-):
#   instrucció 1
#   instrucció 2
#   ...
#   instrucció n
# Dins del 'while' hi ha paraules clau que modifiquen el comportament del bucle.
# break -> si troba aquesta paraula clau dins el bucle, en surt automàticament sense executar la resta de les
# instruccions que es troben baix de ell-
# continue -> interromp l'execució de les instruccions i torna a la línia on es troba el 'while' anterior.

# Exemple de menú repetitiu:

menu = '''Introdueix una de les següents opcions:
    1 - Introdueix l'1 per una salutació.
    2 - Introdueix el 2 per una suma de nombres.
    3 - Introdueix el 3 per realitzar una divisió de 2 nombres.
    4 - Introdueix el 4 per sortir.
'''

opcio = input(menu)

while True:
    match opcio:
        case '1':
            print(f'Hola que tal Pascual.')
        case '2':
            num1 = float(input('Introdueix el primer nombre per la suma: '))
            num2 = float(input('Introdueix el segón nombre per la suma: ')) 
            print(f'La suma de {num1} + {num2} resulta en: {num1 + num2}')
        case '3':
            num1 = float(input('Introdueix el dividend: '))
            num2 = float(input('Introdueix el divisor: ')) 
            print(f'La divisió de {num1} entre {num2} resulta en: {num1/num2}')
        case '4':
            print(f'Fins la pròxima')
            break
        case _:
            print(f'No has introduït una opció correcta.')
            
    print()
    opcio = input(menu)

# Exemple 2: 
# Utilitzarem l'estructura 'while' per a realitzar un patró en funció d'una entrada.
# Es demanarà un nombre sence n, en el cas de que n = 4, el patró resultant seria:
# - *
# - * - * 
# - * - * - *
# - * - * - * - *

n = int(input('Introdueix un nombre sencer: '))
numLin = 1

while numLin <= n:
    print(f'{numLin*'- * '}')
    numLin = numLin + 1

# Feu un bucle que realitzi el següent patró:
# En el cas d'introduïr un nombre n = 4 y una paraula = 'hola' tendria la següent forma.
# hola
# hola hola
# hola hola hola
# hola hola hola hola
# aloh aloh aloh
# aloh aloh
# aloh

n = int(input('INtrodueix un nombre sencer: '))
paraula = input('INtrodueix una paraula: ')
paraulainv = list(paraula)
paraulainv = paraulainv[::-1]
paraulainv = ''.join((paraulainv))
print(paraulainv)

numLin = 1
while numLin <= 2*n - 1:
    if numLin <= n:
        print((paraula + ' ')*numLin)
    else:
        print((paraulainv + ' ')*(2*n - numLin))
    numLin = numLin + 1