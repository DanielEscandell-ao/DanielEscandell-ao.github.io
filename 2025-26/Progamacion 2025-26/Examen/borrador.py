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