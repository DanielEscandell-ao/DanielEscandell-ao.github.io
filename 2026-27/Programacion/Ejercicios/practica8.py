# 1 - Primer ejercicio:
# Teniendo en cuenta que el número introducido n = 7, se generaría
'''
1 # 7 ## 7 ### 7 #### 7 ##### 7 ###### 7 ####### 7
2 # 2 ## 6 ### 6 #### 6 ##### 6 ###### 6 ##### 6
3 # 3 ## 3 ### 5 #### 5 ##### 5 #### 5 ### 5
4 # 4 ## 4 ### 4 #### 4 ### 4 ## 4 # 4
5 # 5 ## 5 ### 5 ## 5 # 3 ## 3 ### 3
6 # 6 ## 6 # 6 ## 6 # 6 ## 2 # 2
7 # 7 # 7 # 7 # 7 # 7 # 7 # 1

'''
num = int(input('Introduce un numero: '))
i = 1
while i < num:
    p = num
    k = 1
    c = 1
    m = 1
    patron = ''
    while p > 0:
        if c <= i:
            patron += str(i) + ' ' + '#' * m + ' '
        else: 
            patron += str(num-i + 1) + ' ' + '#' * m + ' '
        if k < (num-i + 1):
            m += 1
        else:
            m -= 1
            if m == 0:
                k = 1
                m = 2
        k += 1
        c += 1
        p -= 1
    patron += str(num-i + 1)
    print(patron)
    i += 1
print((str(num) + ' # ') * num + '1')

# 2 - Segundo ejercicio:
'''
Imagina que te han dado la frase = 'Hola como vas amigo mío.'
El patrón a dibujar en función de esta frase será:

Hola
Hola como
Hola como vas
Hola como vas amigo
Hola como vas amigo mío.
mío. amigo vas como
mío. amigo vas
mío. amigo
mío.

"Tened en cuenta que las oraciones introducidas siempre tendrán un solo
espacio entre palabras. Los puntos, comas y otros separadores pertenecen
a la palabra a la que están pegados.
'''

frase = input('Introduce una frase: ')
listfrase = frase.split(' ')
listfinal = []
i = 0
while i < len(listfrase):
    listfinal.append(listfrase[i])
    print(f' '.join(listfinal))
    i += 1
listfinal.reverse()
while i > 0:
    listfinal.remove(listfinal[len(listfinal) - 1])
    print(f' '.join(listfinal))
    i -= 1

# 3 - Tercer ejercicio:
#Ejercicio patrón ex. parcial 1 Robert
# número introducido n = 4
'''
1 - 
* * * *
2 - 22 -
* * *
3 - 33 - 333 -
* *
4 - 44 - 444 - 4444 -
* *
3 - 33 - 333 -
* * *
2 - 22 -
* * * *
1 - 
'''

num = int(input('Introduce un numero: '))
num1 = 1
i = 1
c = num
patron = ''
while i <= (num + num - 1):
    if i < num:
        j = 1 
        patron = ''
        while j <= i:
            patron += str(num1) * j
            patron += ' - '
            j += 1
        print(patron)
        if c > 1:
            print('* ' * c)
        c -= 1
        num1 += 1
    else:
        j = 1 
        patron = ''
        while j <= num1:
            patron += str(num1) * j
            patron += ' - '
            j += 1
        print(patron)
        if c != num:
            c += 1
            print('* ' * c)
        num1 -= 1
    i += 1

num = int(input('Introduce un numero: '))
i = 1
c = num
listapatron = []
patron = str(i) + ' - '
listapatron.append(patron)
i += 1
while i <= num:
    if c > 1:
        listapatron.append('* ' * c)
    c -= 1
    patron = patron.replace(str(i-1),str(i))
    patron += str(i) * i + ' - '
    listapatron.append(patron)
    i += 1
print('\n'.join(listapatron))
listapatron.reverse()
print('\n'.join(listapatron[1:len(listapatron)]))
# 4 - Cuarto ejercicio:
'''Crea un programa que realitzi el següent patró en funció d’un nombre 
“n” introduït. L’exemple següent es mostra el patró per al nombre 5.'''
'''
5 * * * * 5 * * * 5 * * 5 * 5
4 %%% 4 %% 4 % 4
3 * * 3 * 3
2 % 2
1
2 * 2
3 %% 3 % 3
4 * * * 4 * * 4 * 4
5 %%%% 5 %%% 5 %% 5 % 5
'''
num = int(input('Introduce un numero: '))
i = 1
listapatron = []
listapatron2 = []
patron = str(i)
listapatron.append(patron)
patron2 = str(i)
i += 1
while i <= num:
    patron = patron.replace(str(i-1), str(i))
    patron2 = patron2.replace(str(i-1), str(i))
    if i % 2 == 0:
        patron2 = patron2.replace('%', '*')
        patron2 = str(i) + ' ' + '* ' * i + patron2
        patron = patron.replace('*', '%')
        patron = str(i) + ' ' + '% ' * i + patron
    else:
        patron2 = patron2.replace('*', '%')
        patron2 = str(i) + ' ' + '% ' * i + ' ' + patron2
        patron = patron.replace('%', '*')
        patron = str(i) + ' ' + '* ' * i + patron
    listapatron.append(patron)
    listapatron2.append(patron2)
    i += 1
listapatron.reverse()
print(f'\n'.join(listapatron[0:len(listapatron)]))
print(f'\n'.join(listapatron2[0:len(listapatron2)]))
# 5 - Quinto ejercicio:
'''
Imaginaos que se os ha introducido el número n = 5
El patrón a crear será:'''
'''
    1        
   2*2       
  3-3-3
 4*4*4*4
5-5-5-5-5
 4*4*4*4
  3-3-3
   2*2
    1
'''
num = int(input('Introduce un numero: '))
i = 1
listapatron = []
patron = ''
patron += ' ' * (num-i) + str(i)
listapatron.append(patron)
i += 1
while i <= num: 
    patron = patron.replace(' ', '', 1)
    patron = patron.replace(str(i-1), str(i))
    if i % 2 == 0:
        patron = patron.replace('-', '*')
        patron += '*' + str(i)
    else:
        patron = patron.replace('*', '-')
        patron += '-' + str(i)
    listapatron.append(patron)
    i += 1
print(f'{'\n'.join(listapatron)}')
listapatron.reverse()
print(f'{'\n'.join(listapatron[1:len(listapatron)])}')
# 6 - Sexto ejercicio:
# Crea un código que realice el siguiente patrón en función de
# un número n introducido y una palabra introducida:
# Ejemplo del patrón para el número n = 5

'''
    1 2 2 2 2 2 2 2 2 2 2 1
    1 2 3 3 3 3 3 3 3 3 2 1
    1 2 3 4 4 4 4 4 4 3 2 1
    1 2 3 4 palabra 4 3 2 1
    1 2 3 4 4 4 4 4 4 3 2 1
    1 2 3 3 3 3 3 3 3 3 2 1
    1 2 2 2 2 2 2 2 2 2 2 1
'''

# 2n - 2 + 2n - 2 = 4n - 4 --> 4n - 4 + n_palabra
# El ejemplo del patrón para el número n = 6 y palabra = hola
'''
    1 2 2 2 2 2  2 2 2 2 2 1
    1 2 3 3 3 3  3 3 3 3 2 1
    1 2 3 4 4 4  4 4 4 3 2 1
    1 2 3 4 5 5  5 5 4 3 2 1
    1 2 3 4 5 hola 5 4 3 2 1
    1 2 3 4 5 5  5 5 4 3 2 1
    1 2 3 4 4 4  4 4 4 3 2 1
    1 2 3 3 3 3  3 3 3 3 2 1
    1 2 2 2 2 2  2 2 2 2 2 1
'''

# El ejemplo del patrón para el número n = 6 y palabra = adios
'''
    1 2 2 2 2 2 2 2 2 2 2 2 1
    1 2 3 3 3 3 3 3 3 3 3 2 1
    1 2 3 4 4 4 4 4 4 4 3 2 1
    1 2 3 4 5 5 5 5 5 4 3 2 1
    1 2 3 4 5 adios 5 4 3 2 1
    1 2 3 4 5 5 5 5 5 4 3 2 1
    1 2 3 4 4 4 4 4 4 4 3 2 1
    1 2 3 3 3 3 3 3 3 3 3 2 1
    1 2 2 2 2 2 2 2 2 2 2 2 1
'''
num = int(input('Introduce un numero: '))
palabra = input('Introduce una palabra: ')
i = 1
j = 1
listapatron = []
patron = ''
listapatron.append(patron)
while i <= num - 1:
    patron = str(i)
    i += 1
    listapatron.append(patron)
patron = ' '.join(listapatron) + ' ' + palabra + ' '
listapatron.reverse()
print(patron + ' '.join(listapatron))
listapatron.reverse()
listapatron.append((str(i-1) + ' ') * (len(palabra) / 2).__round__())
print(' '.join(listapatron))
# 7 - Séptimo ejercicio: Crear una aplicación que pida:
# 1 string que represente un nombre de como mucho 15 caracteres.
# 1 carácter de relleno y,
# represente el siguiente patrón en el caso de haber introducido 'nombre' y 
# el carácter '#':
'''
     e n o m b r e n
    r ############# o
   b ############### m
  m ################# b
 o ################### r
n #### n o m b r e #### e
'''

# 8 - Octavo ejercicio:
# El programa pide una palabra de como máximo 9 caracteres y 2 caracteres de relleno (se # pide cada uno por separado).
# En el caso de que la palabra introducida fuera “palabra”, el primer caracter de relleno 
# fuera “*” y el segundo carácter de relleno fuera “-”, el patrón generado (por pasos sería)
import time
palabra = input('Introduce una palabra de maximo 9 caracteres: ')
caracter1 = input('Introduce el primer caracter: ')
caracter2 = input('Introduce el segundo caracter: ')
i = 0
patronesp = ''
while i < 3:
    patron = caracter1 + (caracter2 * (len(palabra) + (i*2))) + caracter1
    patronpalabra = caracter1 + ' ' * i + palabra + ' ' * i  + caracter1
    print("\033[2J\033[H", end="")
    if i == 0:
        time.sleep(0.5)
        print(patron +'\n' + patronpalabra)
        print(patron)
        time.sleep(2)
        print("\033[2J\033[H", end="")
        patron = patron.replace(caracter1, ' ')
        patron = patron.replace(caracter2, caracter1)
        patron = patron.replace(' ', caracter2)
        patronpalabra = patronpalabra.replace(caracter1, caracter2)
        print(patron + '\n' + patronpalabra)
        print(patron)
        time.sleep(2)
    else:
        time.sleep(0.5)
        print(patron + '\n' + patronesp + patronpalabra)
        print(patronesp + patron)
        time.sleep(2)
        print("\033[2J\033[H", end="")
        patron = patron.replace(caracter1, ' ')
        patron = patron.replace(caracter2, caracter1)
        patron = patron.replace(' ', caracter2)
        patronesp = patronesp.replace(caracter1, caracter2)
        patronpalabra = patronpalabra.replace(caracter1, caracter2)
        print(patron + '\n' + patronesp + patronpalabra)
        print(patronesp + patron)
        time.sleep(2)
        patronesp = patronesp.replace(caracter2, caracter1)
    i += 1
    patronesp = patronesp.replace(' ' + caracter1, (' ' * (i + 1)) + caracter1, 1)
    patronesp += caracter1 + ' ' * (len(palabra) + (2*i)) + caracter1 + '\n' 


# 9 - Noveno ejercicio:
# En el caso de introducir el número n = 3 y la palabra introducida fuera palabra = feo.
# La evolución del patrón sería la siguiente.
# EL número de movimientos a la derecha de la palabra tienen que ser cinco.
# Límite de longitud de palabra de 9 caracteres, número mínimo introducido el n=3.
# La primera línea tiene que tener como último carácter el número introducido - 1.
'''
1er paso:
1 1 1 1 2
feo 1 2 3
1 1 2 3 3

2o paso:
1 1 1 2 3
1 feo 3 3
1 2 3 3 3

3er paso:
1 1 2 3 3
1 3 feo 3
2 3 3 3 3 

4o paso:
1 2 3 3 3
2 3 3 feo
3 3 3 3 3
'''

# En el caso de introducir en número n = 9 y la palabra = feo, la 
# evolución del patrón sería la siguiente:

'''
1er paso:
1 1 1 1 2 3 4 5 6 7 8
feo 1 2 3 4 5 6 7 8 9
1 1 2 3 4 5 6 7 8 9 9 

2º paso:
1 1 1 2 3 4 5 6 7 8 9
1 feo 3 4 5 6 7 8 9 9
1 2 3 4 5 6 7 8 9 9 9

3er paso:
1 1 2 3 4 5 6 7 8 9 9
1 2 feo 5 6 7 8 9 9 9
2 3 4 5 6 7 8 9 9 9 9

4º paso:
1 2 3 4 5 6 7 8 9 9 9
2 3 4 feo 7 8 9 9 9 9
3 4 5 6 7 8 9 9 9 9 9

5º paso:
2 3 4 5 6 7 8 9 9 9 9
3 4 5 6 feo 9 9 9 9 9
4 5 6 7 8 9 9 9 9 9 9

6º paso:
3 4 5 6 7 8 9 9 9 9 9
4 5 6 7 8 feo 9 9 9 9
5 6 7 8 9 9 9 9 9 9 9

7º paso:
4 5 6 7 8 9 9 9 9 9 9
5 6 7 8 9 9 feo 9 9 9
6 7 8 9 9 9 9 9 9 9 9

8º paso:
5 6 7 8 9 9 9 9 9 9 9
6 7 8 9 9 9 9 feo 9 9
7 8 9 9 9 9 9 9 9 9 9

9º paso:
6 7 8 9 9 9 9 9 9 9 9
7 8 9 9 9 9 9 9 feo 9
8 9 9 9 9 9 9 9 9 9 9

10º paso:
7 8 9 9 9 9 9 9 9 9 9
8 9 9 9 9 9 9 9 9 feo
9 9 9 9 9 9 9 9 9 9 9
'''

