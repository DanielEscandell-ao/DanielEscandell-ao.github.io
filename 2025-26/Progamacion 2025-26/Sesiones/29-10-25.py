# Correcció del exercici del darrer dia:
# Fes un input d'un nombre y imprimeix el seu valor multiplicat per 2 per pantalla.

numero = input('Introduce un número: ')
numpordos = numero*2
cadena = 'hola'
cadena = cadena*5
print('El número introducido y multiplicado por dos es: ',numpordos)
print(cadena)
# Introducción a los tipos de datos básicos en programación.
# 1 Las cadenas de caracteres: el tipo "string" y en Python se llama 'str'
# En el ejemplo de arriba: input() siempre me va a devover un dato de tipo 'str'

# Tenemos que pensar que en la primera instrucción en la línea 4 de este documento,
# la variable numero apuntará a un objeto de tipo 'str', entonces, no podremos hacer
# ninguna operación matemática on él.
# Solución = transformar el tipo de dato 'str' en un tipo de dato numérico.
# Los dos tipos de datos numéricos que nos bastarán en Python y son nativos al lenguaje son:
# Tipo Entero -> en Python recibe el nombre de 'int' (aquellos números que no tienen decimales positivos y negativos)
# Tipo Decimal (números reales) -> en Python reciben e nombre de 'float' 

# Existe una manera de convertir datos de un tipo a otro SI ES POSIBLE (NO SIEMPRE LO ES).
# A esto anterior se le conoce como CASTING (es lo mismo que transformación de tipos)
# '45' -> Si se puede transformar a int o a float
# '%&/&%' -> No tiene sentido transformarlo en un número...y por tanto, tampoco se va a poder.

# El modod de hacer CASTING es poniendo delante de la variable el LITERAL del tipo que quiero
# transformar el nombre del otro tipo al que se transforma y luego cerrarlo entre paréntesis.
# Ejemplo
print()
numero = int(input('Introduce un número: ')) 
numpordos = numero*2
print('El número introducido y multiplicado por dos es: ',numpordos)

# Si introducimos un valor en el input que no se puede traducir a numérico, a la hora de hacer
# el CASTING nos producira una EXCEPCIÓN, que detiene la ejecución completamente.
# Una EXCEPCIÓN se produce cuando hacemos un uso inesperado e incorrecto del código
# pero no se trata de un error de sintaxis, si es un error de sintaxis, ni si quiera empezará a  
# ejecutarse el código.

# Próximo día:
# Repasad este código y jugad con él porque habrá preguntas.