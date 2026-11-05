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
import time as t
num = int(input('Introduce un numero mayor a 3: '))
palabra = input('Introduce una palabra de no mas de 9 caracteres: ')
contpasos = 1
pasos = num + 1
patron = palabra + ' '
print("\033[2J\033[H", end="")
j = 1
while j <= num:
        patron += str(j) + ' '
        j += 1
while contpasos <= pasos:
    print(patron)
    t.sleep(2)
    patron = patron.replace(str(contpasos), palabra, 1)
    patron = patron.replace(palabra, str(contpasos), 1)
    patron = patron.replace(str(contpasos + 1), str(contpasos + 2), 1)
    contpasos += 1