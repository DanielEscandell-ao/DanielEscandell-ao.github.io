# 1. Contar consonantes
frase = input('Introduce una frase: ')
frase = frase.lower()
contador = 0
consonantes = 0
vocal = 0
while contador < len(frase):
    if frase[contador] == 'a' or frase[contador] == 'e' or frase[contador] == 'i' or frase[contador] == 'o' or frase[contador] == 'u':
        vocal += 1
    else:
        consonantes += 1
    contador += 1
print(consonantes)
# 2. Multiplos de 3
num = int(input('Introduce un numero: '))
cont = 1
multiplos = []
while cont <= num:
    if cont % 3 == 0:
        multiplos.append(cont)
    cont += 1
print(f'Los multiplos de 3 hasta {num} son: {multiplos}')
# 3. Triangulo rectangulo
num = int(input('Introduce un numero: '))
cont = num
car = '*'
while cont >= 1:
    print(car*cont)
    cont -= 1
# 4. Suma de numeros
num = int(input('Introduce un numero: '))
suma = 0
while num > 0:
    suma += num
    num = int(input('Introduce un numero: '))
print(suma)
# 5. Invertir frase
frase = input('Introduce una frase: ')
palabras = frase.split()  
contador = len(palabras) - 1
resultado = []
while contador >= 0:
    resultado.append(palabras[contador])
    contador -= 1
print(" ".join(resultado))
# 6. Suma de numeros
num = input('Introduce los numeros a sumar juntos: ')
suma = 0
cont = 0
while cont < len(num):
    suma += int(num[cont])
    cont += 1
print(f'La suma de los numeros es: {suma}')
# 7. Palabras pares
frase = input('Introduce una frase: ')
palabras = frase.split()
cont = 0
palabraspar = []
while cont < len(palabras):
    if len(palabras[cont]) % 2 == 0:
        palabraspar.append(palabras[cont])
    cont += 1
print(' '.join(palabraspar))
# 8. Numeros pares
num = int(input('Introduce un numero: '))
cont = num
while cont >= 0:
    if num % 2 == 0:
        print(cont)
    else:
        print(cont - 1)
    cont -= 2
# 10. Triangulo rectangulo invertido
num = int(input('Introduce un numero: '))
car = '*'
numcar = 1
numesp = num - 1
cont = 0
patron = ''
while cont < num:
    patron += ' ' * numesp
    patron += car * numcar
    numesp -= 1
    numcar += 1
    cont += 1
    print(patron)
# 11.
num = input('Introduce un numero: ')
cont = len(num) - 1
capicua = ''
while cont >= 0:
    capicua += num[cont]
    cont -= 1
if num == capicua:
    print('El numero es capicua.')
else:
    print('El numero no es capicua.')
# 12.
frase = input('Introduce una frase: ')
letra = input('Introduce una letra: ')
cont = 0
contletra = 0
while cont < len(frase):
    if frase[cont] == letra:
        contletra += 1
    cont += 1
print(f'La letra aparece {contletra}')
# 13. 
num = int(input('Introduce un numero: '))
cont = 1
patron = []
while cont <= num:
    patron.append(str(cont))
    print(''.join(patron))
    cont += 1
# 14. 
num = int(input('Introduce un numero: '))
divisores = []
cont = 1
while cont <= num:
    if num % cont == 0:
        divisores.append(str(cont))
    cont += 1
print(f'Divisores: {' '.join(divisores)}')
print(f'Tiene {len(divisores)} divisores')
# 15.
num = int(input('Introduce un numero: '))
cont = num
car = '*'
while cont > 1:
    print(car * cont)
    cont -= 1
while cont <= num:
    print(car * cont)
    cont += 1
# 16. 
num = int(input('Introduce un numero: '))
cont = 1
car = ' '
mult = num - 1
patron = []
while cont <= num:
    patron.append(str(cont))
    print(mult * car + ''.join(patron))
    cont += 1
    mult -= 1
# 17. 
num = int(input('Introduce un numero: '))
cont = 1
car = '*'
mult = 0
while cont < num:
    print(f'{cont}{car * mult}')
    cont += 1
    mult += 1
while cont > 0:
    print(f'{cont}{car * mult}')
    cont -= 1
    mult -= 1
# 18. IMPOSIBLE
# 19.
palabra = input('Introduce una palabra: ')
cont = 0
patron = []
while cont < len(palabra):
    patron.append(palabra[cont])
    cont += 1
    print(''.join(patron))
while cont > 1:
    patron.pop()
    print(''.join(patron))
    cont -= 1
# 20. IMPOSIBLE