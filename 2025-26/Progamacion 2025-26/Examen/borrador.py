import math

num = 2
numero = int(input('Introduce un numero: '))
objetivo = 1
lista = []
esprimo = True

while objetivo <= numero:
    while num <= int(math.sqrt(objetivo) + 1):
        if objetivo % num == 0:
            esprimo = False
            break
        num += 1
    
    objetivo += 1 
print(lista)