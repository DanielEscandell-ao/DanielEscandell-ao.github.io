# Empecemos con las estructuras de control de flujo condicional.
# Operandos que nos permiten determinar si una condición es verdadera o falsa:
# Operandos lógicos aplicables a tipos compatibles y quer resultan siempre en un booleano:
# Igualdad:
# ==
print('Ejecutamos la comparación lógiga: "5 == 5", resultando:')
print(f'{5 == 5}')
print('Ejecutamos la comparación lógiga: "4 == 5", resultando:')
print(f'{4 == 5}')
print('Ejecutamos la comparación lógiga: "4 == \'4\'", resultando:')
print(f'{4 == "4"}')

# Diferencia:
# !=
print()
print('Ejecutamos la comparación lógiga: "5 != 5", resultando:')
print(f'{5 != 5}')
print('Ejecutamos la comparación lógiga: "4 != 5", resultando:')
print(f'{4 != 5}')
print('Ejecutamos la comparación lógiga: "4 != \'4\'", resultando:')
print(f'{4 != "4"}')

# Mayor que:
# >
print()
print('Ejecutamos la comparación lógiga: "5 > 5", resultando:')
print(f'{5 > 5}')
print('Ejecutamos la comparación lógiga: "4 > 5", resultando:')
print(f'{4 > 5}')
# print('Ejecutamos la comparación lógiga: "4 > \'4\'", resultando:')
# print(f'{4 > "4"}') -> Nos va a dar una exceción!
print('Ejecutamos la comparación lógiga: "4 > len(\"4\")", resultando:')
print(f'{4 > len("4")}')

# Menor que:
# <
print()
print('Ejecutamos la comparación lógiga: "5 < 5", resultando:')
print(f'{5 < 5}')
print('Ejecutamos la comparación lógiga: "4 < 5", resultando:')
print(f'{4 < 5}')
# print('Ejecutamos la comparación lógiga: "4 < \'4\'", resultando:')
# print(f'{4 < "4"}') -> Nos va a dar una exceción!
print('Ejecutamos la comparación lógiga: "4 < len(\"4\")", resultando:')
print(f'{4 < len("4")}')

# Mayor o igual que:
# >=
print()
print('Ejecutamos la comparación lógiga: "5 >= 5", resultando:')
print(f'{5 >= 5}')
print('Ejecutamos la comparación lógiga: "4 >= 5", resultando:')
print(f'{4 >= 5}')
# print('Ejecutamos la comparación lógiga: "4 >= \'4\'", resultando:')
# print(f'{4 >= "4"}') -> Nos va a dar una exceción!
print('Ejecutamos la comparación lógiga: "4 >= len(\"4\")", resultando:')
print(f'{4 >= len("4")}')

# Menor o igual que:
# <=
print()
print('Ejecutamos la comparación lógiga: "5 <= 5", resultando:')
print(f'{5 <= 5}')
print('Ejecutamos la comparación lógiga: "4 <= 5", resultando:')
print(f'{4 <= 5}')
# print('Ejecutamos la comparación lógiga: "4 <= \'4\'", resultando:')
# print(f'{4 <= "4"}') -> Nos va a dar una exceción!
print('Ejecutamos la comparación lógiga: "4 <= len(\"4\")", resultando:')
print(f'{4 <= len("4")}')

# Ejemplos de funcionamiento con casting:
print()
print(f'{4 > int("4")}')
print(f'{str(4) > "4"}')
print(f'{str(5) > "4"}')

# Operadores lógicos que nos permiten enlazar los booleanos (resultados de las comparaciones anteriores).
# Estos operadores solo pueden operar con BOOLEANOS.
# Operador lógico o (español) -> or
# Funcionamiento: basta que uno de los operadores sea True para que toda la operación resulte True.
# Ejemplos:
edad = 17
nota = 6
pagado = True
print(f'{(edad > 16) or (nota >= 5) or (pagado == True)}')

# Realmente lo anterior no cumple con lo que deseamos obtener ya que todas las condiciones son
# NECESARIAS, por tanto, ya que todas se tienen que cumplir, usaremos el otro operador lógico:
# y (español) -> and
print(f'{(edad > 16) and (nota >= 5) and (pagado == True)}')

# operadores de control de flujo de ejecución.
# si se cumple una condición hago "a", si no se cumple, hago "b".
# Traducción a comandos -> 
# if (condicion):
#   "código" -> El código está separado una tabulación.
# else:
#   "otro código" -> El código está separado una tabulación.     
# Ejemplo:
# Imaginemos que queremos comprobar que se cumplen los condicionantes anteriores para
# mostrar un mensaje en pantalla que nos diga: "Enhorabuena, puedes matricularte a segundo"
# si se cumplen las condiciones o "Vago de las narices, estudia y aprueba primero!" si no
# se cumplen.

nombre = input('Introduce tu nombre: ')
if (edad > 16) and (nota >= 5) and (pagado == True):
    # Todas las variables o objetos creados dentro de este contexto de if, no 
    # serán accesibles desde fuera de él, se eliminan cuando se termina la ejecución
    # de código de este contexto.
    # Se pueden usar todas las variables de fuera de este contexto y modificarlas, luego
    # su valor no desaparecerá cuando termine de ejecutarse el código de este contexto.
    nombre = input('Introduce tu nombre: ')
    print(f'Enhorabuena, puedes matricularte a segundo {nombre}.')
else:
    print("Vago de las narices, estudia y aprueba primero!")

print(f'Hola {nombre}, ¡Melón!')