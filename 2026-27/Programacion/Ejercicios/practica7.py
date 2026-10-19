# 1 Imagina 4 pizzes que t’agradin, emmagatzema-les dins tipus llista i utilitza el bucle for per imprimir cadascun del nom d’aquestes pizzes.
# Modifica el bucle per tal de que en comptes de només imprimir el nom de la pizza, imprimeixi una oració com per exemple ‘M’agrada la pizza de pepperoni’.
# Afegeix una línia que imprimeixi ‘M’encanten les pizzes’ una vegada que surtis del bucle.
pizzas = ['peperoni', '4 quesos', 'jamon y queso', 'jamon serrano']
for i in pizzas:
    print(f'Me gusta la pizza de {i}')
print('Me encantan las pizzas.')
# 2 Escriure un programa que demani a l'usuari 
# un nombre enter positiu i mostri per pantalla tots els números imparells des d'1 fins a aquest nombre separats per comes.
num = int(input('Introduce un numero entero positivo: '))
i = int(1)
if num <= 0:
    print('Por favor introduce un numero entero positivo.')
else:
    while num >= i:
        print(i)
        i += 2
# 3 Escriure un algorisme en Python que imprimeixi els 10 primers números parells començant a 2 i imprimiu també els seus respectius cubs. 
# Per exemple: 2 – 8; 4 – 64; 6 – 216 … Modifica aquest programa perquè en comptes d’imprimir els 10 primers nombres parells, 
# imprimeixi els primers n nombres parells on n es un enter positiu introduït per teclat.

num = int(input('Introduce un numero: '))
i = 2
j = 1
while j <= num:
    print(f'{i} - {i**3}')
    i += 2
    j += 1
# 4 Realitza un programa que primer, llegeixi una frase per teclat i segón, que compti el nombre de paraules que té aquesta frase. 
# Recorda que hauràs d’utilitzar mètodes built-in de la classe String i de la clase List a més d’utilitzar el bucle for.
frase = input('Introduce una frase: ')
i = 0
for letra in frase:
    if letra == ' ':
        i += 1
i += 1
print(i)
# 5 Escriure un programa que demani a l'usuari un número sencer i mostri per pantalla un triangle rectangle com el de més avall, 
# d'alçada el número introduït. La imatge següent mostra l’exemple de la sortida del programa si introduïm el número 5.
num = int(input('Introduce un numero: '))
carac = ''
i = 1
while i <= num:
    carac += '*'
    print(carac)
    i += 1
# 6 Escriure un programa que demani a l’usuari una paraula i la mostri per pantalla 10 vegades.
# Modifica aquest programa perquè a l’usuari se li demani per teclat el nombre de vegades que vol repetir la paraula i 
# la repeteixi tantes vegades com les introduïdes per l’usuari.
palabra = input('Introduce una palabra: ')
num = int(input('Introduce un numero: '))
i = 1
while i <= num:
    print(palabra)
    i += 1
# 7 Fes un programa que llegeixi un nombre sencer per teclat i per pantalla imprimeixi tots els nombres primers des de l’1 fins al 
# nombre introduït. Modifica aquest programa per a que comprovi si el nombre introduït sigui un nombre sencer, 
# en cas contrari s’imprimirà per pantalla el missatge ‘El nombre introduït no és un nombre sencer’.
n = int(input('Introdueix un numero positiu: '))
if n <= 0:
    print('Has d’introduir un numero positiu.')
else:
    num = 2
    while num <= n:
        divisor = 2
        es_primer = True
        while divisor < num:
            if num % divisor == 0:
                es_primer = False
                break
            divisor = divisor + 1
        if es_primer:
            print(num)
        num = num + 1
# 8 Es col·loca un capital C, a un interès I (que oscil·la entre 0 i 100), durant M anys i es vol saber quan s'hi haurà convertit 
# aquest capital en “M” anys, sabent que és acumulatiu (se refiere al interés, es decir, que cuando se calcule el interés en un año 
# determinado, se calculará respecto a la cantidad original más las cantidades de los intereses de los años anteriores). 
# Crea un programa utilitzant el bucle for que ens calculi l’interés acumulat d’aquest capital. El capital C i l'interès I s'hauran 
# d’introduir per teclat.
capital = float(input('Introduce tu capital: '))
interes = float(input('Introduce el porcentaje de interes: '))
años = int(input('Introduce cuantos años: '))

while interes < 0 or interes > 100:
    interes = float(input('No has introducido un interes valido, introduce el porcentaje de interes: '))

i = 0
c = capital
while i < años:
    calculointeres = c * (interes / 100)
    capital += calculointeres
    i += 1

print(f'Durante {años} años, el capital final ha aumentado hasta: {capital}')
# 9 Crea un programa que calculi la suma de tots els divisors (sencers) d’un nombre sencer introduït per teclat 
# (recorda que els divisors poden ser com a molt grans fins a la meitat del nombre introduït).
num = int(input('Introduce un numero: '))
i = 1
divmax = num / 2
divisores = []
while i <= divmax:
    if num % i == 0:
        divisores.append(str(i))
    i += 1
print(f'Los divisores de {num} son {', '.join(divisores)}, {num}')
# 10 Crea un programa que demani un text per teclat i que la sortida sigui el text invertit. 
# No podrás fer servir la sintaxi [::-1] per invertir aquest texte sinó que hauràs de llegir-lo caràcter a caràcter i 
# invertir-lo amb el bucle for.
texto = input('Introduce una frase: ')
textoinv = ''
itexto = len(texto) - 1
while len(texto) > len(textoinv):
    textoinv += texto[itexto]
    itexto -= 1
print(f'El texto {texto} invertido es: {textoinv}')
# 11 Imprimeix el següent patró utilitzant el bucle for, les dimensions del patró dependran d’un nombre introduït per teclat, 
# en el cas següent es mostra el patró si el nombre introduït és el 5:
# *
# * * 
# * * *
# * * * *
# * * * * * 
# * * * *
# * * * 
# * *
# *
num = int(input('Introduce un numero: '))
i = 1
while i <= num:
    print('* ' * i)
    i += 1
i -= 2
while i > 0:
    print('* ' * i)
    i -=1
# 12 Escriu un programa que donat un nombre sencer introduït per teclat imprimeixi tots els nombres primers des del número 1 
# fins a aquest nombre. 
'''
Es igual al 7.
'''
# 13 Crea un programa utilitzant el bucle for que compti el nombre de xifres que té un número sencer introduït per teclat.
num = float(input('Introduce un numero: '))
cifras = 0
for cifra in str(num):
    if cifra == '.':
        continue
    elif int(cifra) < 10 or int(cifra) >= 0:
        cifras += 1
print(f'El numero {num} tiene {cifras} cifras.')
# 14 Escriu un programa que pregunti quants números s'introduiran, demaneu aquests números, i mostri un missatge cada 
# vegada que un nombre no sigui més gran que el primer nombre introduït.
num = int(input('Introduce cuantos numeros se van a introducir: '))
i = num - 1
numintr = int(input('Introduce un numero: '))
while i > 0:
    numintr2 = int(input('Introduce un numero: '))
    if numintr > numintr2:
        print('El numero introducido es menor al introducido al principio.')
    i -= 1
# 15 Escriviu un programa que pregunti quants números s'introduiran, demaneu aquests números, i mostri un missatge 
# cada vegada que un nombre no sigui més gran que l'anterior.
num = int(input('Introduce cuantos numeros se van a introducir: '))
i = num - 1
nums = []
numintr = int(input('Introduce un numero: '))
while i > 0:
    nums.append(numintr)
    numintr = int(input('Introduce un numero: '))
    if numintr < nums[len(nums)-1]:
        print('El numero introducido no es menor que el introducido anteriormente.')
    i -= 1
# 16 Escriviu un programa que pregunti quants números s'introduiran, demaneu aquests números, i digueu al final quants 
# han estat parells i quants senars a més d’imprimir una llista dels parells i una llista dels senars.
num = int(input('Introduce cuantos numeros se van a introducir: '))
i = num
numspar = []
numsimpar = []
while i > 0:
    numintr = int(input('Introduce un numero: '))
    if numintr % 2 == 0:
        numspar.append(str(numintr))
    else:
        numsimpar.append(str(numintr))
    i -= 1
print(f'Los numeros pares introducidos son: {', '.join(numspar)}')
print(f'Los numeros impares introducidos son: {', '.join(numsimpar)}')
# 17 y 18 Escriviu un programa que demani dos nombres enters i escriviu la suma de tots els enters des del primer número fins al segon.
num1 = int(input('Introduce un numero: '))
num2 = int(input('Introduce otro numero: '))
sumanums = 0
listanums = []
if num1 > num2:
    i = num2 
    while i <= num1:
        sumanums += i
        listanums.append(str(i))
        i += 1
    print(f'La suma desde {num2} hasta {num1} es {sumanums}')
    print(f'{' + '.join(listanums)} = {sumanums}')
elif num2 > num1:
    i = num1 
    while i <= num2:
        sumanums += i
        listanums.append(str(i))
        i += 1
    print(f'La suma desde {num1} hasta {num2} es {sumanums}')
    print(f'{' + '.join(listanums)} = {sumanums}')
else:
    print(f'No hay suma porque has puesto el mismo numero.')
# 19 Escriviu un programa que demani primer un nombre, després, escriu el nombre de vegades que voleu introduir altres nombres. 
# Seguidament, haureu d’emmagatzemar aquests nombres dins d’una llista i haureu de mostrar per pantalla quantes vegades s’ha 
# repetit el primer nombre introduït dins la llista de nombres introduïts.
num = int(input('Introduce un numero: '))
numveces = int(input('Introduce el numero de veces que quieres introducir un numero: '))
listanums = []
i = numveces
while i > 0:
    num1 = int(input('Introduce un numero: '))
    if num1 == num:
        listanums.append(num1)
    i -= 1
print(f'El numero de veces que has introducido el numero {num} son: {len(listanums)}')
# 20 Escriu un programa que demani una frase a l’usuari i que compti i mostri el nombre de vegades que apareixen les vocals. 
frase = input('Introduce una frase: ').lower()
i = 0
vocales = 0
while i < len(frase):
    if frase[i] == 'a' or frase[i] == 'e' or frase[i] == 'i' or frase[i] == 'o' or frase[i] == 'u':
        vocales += 1
    i += 1
print(f'La frase {frase} tiene {vocales} vocales.')
# 1 Escriviu un programa que pregunteu una vegada i una altra si voleu continuar amb el programa, sempre que es contesti 
# exactament sí (en minúscules i amb titlla).
while True:
    pregunta = input('Quieres continuar con el programa: ')
    if pregunta == 'sí':
        continue
    break
# 2 Escriviu un programa que pregunteu una vegada i una altra si voleu continuar amb el programa, sempre que es contesti 
# un sí, podrà ser un ‘si’ en minúscula o majúscula parcialment o totalment o amb accent o sense
while True:
    pregunta = input('Quieres continuar con el programa: ').lower()
    if pregunta == 'sí' or pregunta == 'si':
        continue
    break
# 3 Realitza un programa que llegeixi dos números per teclat i permeti triar entre 3 opcions en un menú:
# Mostra una suma dels dos números
# Mostrar una resta dels dos números (el primer menys el segon)
# Mostrar una multiplicació dels dos números
# En cas de no introduir una opció vàlida, el programa informarà que no és correcta.
num1 = int(input('Introduce un numero: '))
num2 = int(input('Introduce un numero: '))
while True:
    print('Introduce un numero entre el 1 y el 3 para hacer las siguientes acciones:')
    print('1: haz la suma de los dos numeros')
    print('2: haz la resta de los dos numeros')
    num3 = int(input('3: haz la multiplicacion de los dos numeros: '))
    match num3:
        case 1:
            print(f'La suma de {num1} y {num2} da {num1 + num2}')
        case 2:
            if num1 < num2:
                print(f'La resta de {num2} y {num1} da {num2 - num1}')
            else:
                print(f'La resta de {num1} y {num2} da {num1 - num2}')
        case 3:
            print(f'La multiplicacion de {num1} y {num2} da {num1 * num2}')
        case _:
            print(f'No has introducido ninguna opcion valida. Saliendo del programa...')
            break
# 4 Realitza un programa que llegeixi un nombre imparell per teclat. Si l'usuari no introdueix un nombre imparell, 
# s'ha de repetir el procés fins que l'introdueixi correctament.
while True:
    num = int(input('Introduce un numero impar: '))
    if num % 2 != 0:
        break
# 5 Realitza un programa que sumi tots els números sencers parells des del 0 fins al 100.
i = 1
suma = 0
while i <= 100:
    if i % 2 == 0:
        suma += i
    i += 1
print(f'La suma de todos los numeros pares desde el 0 al 100 son: {suma}')
# 6 Realitza un programa que demani a l'usuari un nombre enter del 0 al 9 i que mentre el número no sigui 
# correcte es repeteixi el procés. Després heu de comprovar si el número es troba a la llista de números i notificar-ho. 
# La llista de nombres que faràs servir és [1, 3, 6, 9].
listanums = [1, 3, 6, 9]
while True:
    num = int(input('Introduce un numero: '))
    if num < 10:
        if num >= 0:
            for i in listanums:
                if num == i:
                    print(f'El numero {num} esta en la lista')
        break
# 7 Donades dues llistes, has de generar una tercera amb tots els elements que s'hi repeteixin en cada una d’elles 
# (és a dir, els elements repetits de llista 1 + els elements repetits de llista 2), però no s'ha de repetir cap element a 
# la nova llista. Les dues llistes que utilitzaràs són (no utilitzeu el tipus set()):
lista1 = [1,1,2,3,4,5,5,6,7,7,8,9,9,1,11,12,13,14,15,16,15,1,2]
lista2 = [1,2,2,3,3,4,5,6,7,7,8,8,9,9]
nuevalist = []
lista1.extend(lista2)
nuevalist.append(lista1[0])
for num in lista1:
        for j in nuevalist:
            if num == j:
                break
        else:
            nuevalist.append(num)
print(f'La nueva lista combinada sin repetir ningun numero es: {nuevalist}')