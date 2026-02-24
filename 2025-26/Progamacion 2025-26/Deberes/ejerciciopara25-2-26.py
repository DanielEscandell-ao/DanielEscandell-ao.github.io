# 2
frase = input('Introduce una frase: ')
palabras = frase.split()
contador = 0
contenedor = ''
while contador < len(palabras):
    contenedor += palabras[contador] + ' '
    print(contenedor)
    contador = contador + 1
palabras.reverse()
while contador > 0:
    print(" ".join(palabras[:contador]))
    contador = contador - 1

# 3
numero = int(input('Introduce un numero: '))
contador = 1
while contador <= numero:
    print(contador + '-')
    print({numero}*'* ')
    contador += 1