listaejemplo = [15, 12, 34, 56, 12, 12, 3, 4, 6, 5, 7, 8]
# 1 Imprime por pantalla cuantas veces aparece el numero 12
# ej de impresion: "El numeoro 12 aparece x veces"
print("El numero de veces que aparece 12 es", listaejemplo.count(12))
# 2 Inserta un numero leido por teclado en la posicion 4 de la lista.
listaejemplo.insert(3, int(input("Introducce un numero: ")))
print(listaejemplo)
# 3 Imprime la lista con los elementos invertidos de posicion.
listaejemplo.reverse()
print(listaejemplo)
# 4 Tienes otra lista: [1, 2, 3]. Añadela como unico elemento al final de listaejemplo.
listaejemplo2 = [1, 2, 3]
listaejemplo.append(listaejemplo2)
print(listaejemplo)
# 5 Extiende la lista listaejemplo coin los elementos de la lista del puntoanterior
listaejemplo.extend(listaejemplo2)
print(listaejemplo)
# 6 Extrae el elemento 12 de la lista (Una vez) y imprime como queda la lista despues de extraerlo
listaejemplo.remove(12)
print(listaejemplo)



# Ejercicio rapido
# Crea una lista que tenga 3 dimensiones en las que cada sublista contenga al menos 3 elementos. 
# Quiero que imprimais el 3er elemento de la lista que esta dentro del 3er elemento de la lista
# que se encuentra en la 3a posicion de la lista principoal "listatri"
listatri = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
print(f"El tercer elemento de la lista que esta debtro del tercer elemento de la lista que se encuentra en la tercera posicion de la lista principal es: {listatri[2][2][2]}")