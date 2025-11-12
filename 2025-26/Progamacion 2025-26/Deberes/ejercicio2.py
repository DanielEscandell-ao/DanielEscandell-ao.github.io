# Para el próximo día me váis a investigar qué hacen los siguientes métodos e las listas.
# list.append() Sirve para añadir un valor nuevo al final de la lista.
frutas = ["manzana", "pera", "uva"]
frutas.append("naranja")
print(frutas)
# list.clear() Sirve para eliminar todos los valores de una lista.
numeros = [1, 2, 3, 4]
numeros.clear()
print(numeros)
# list.count() Sirve para contar las veces que aparece un valor en la lista.
numeros = [1, 2, 2, 3, 2, 4]
print(numeros.count(2))
# list.extend() Este es como el append pero para añadir varios valores a la vez.
animales = ["gato", "perro"]
animales.extend(["loro", "pez"])
print(animales)
# list.insert() Sirve para añadir un valor nuevo en una posicion especifica dentro de la lista.
colores = ["rojo", "azul", "verde"]
colores.insert(1, "amarillo")
print(colores)
# list.remove() Sirve para quitar la primera aparicion de un valor en especifico.
nombres = ["Ana", "Juan", "Ana", "Luis"]
nombres.remove("Ana")
print(nombres)
# list.reverse() Sirve para darle la vuelta a la lista.
letras = ["a", "b", "c", "d"]
letras.reverse()
print(letras)