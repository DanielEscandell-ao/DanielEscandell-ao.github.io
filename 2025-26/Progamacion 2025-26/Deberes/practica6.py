# Determinar si un numero es positivo, negativo o cero
num = float(input("Introduce un numero: "))

if num > 0: 
    print("El numero es positivo")
elif num < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")

# Determinar si una fruta es citrica, dulce, fruto seco o otra
citricos = {"limon", "naranja", "lima"}
dulces = {"manzana", "pera", "platano"}
frutoseco = {"pistacho", "nuez", "almendra"}

fruta = input("Introduce una fruta: ").lower()

if fruta in citricos:
    print("Es una fruta citrica")
elif fruta in dulces:
    print("Es una fruta dulce")
elif fruta in frutoseco:
    print("Es un fruto seco")
else:
    print("Es otro tipo de fruta")

# Classificar una persona segun su edad
edad = int(input("Introduce tu edad: "))

if edad < 18:
    print("Eres menor de edad")
elif 18 <= edad <= 30:
    print("Eres un adulto joven")
elif 31 <= edad <= 65:
    print("Eres un adulto")
else:
    print("Eres un adulto senior")

# Determinar el dia de la semana segun el numero
num = int(input("Introduce un numero del 1 al 7: "))

dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miercoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sabado",
    7: "Domingo"
}

if num in dias:
    print(f"El dia es {dias[num]}")
else:
    print("Numero invalido. Introduce un numero del 1 al 7")

# Clasifica un animal
mamiferos = {"perro", "gato", "vaca"}
aves = {"gaviola", "pinguino", "aguila"}
reptiles = {"serpiente", "cocodrilo", "tortuga"}

animal = input("Introduce un animal: ").lower()

if animal in mamiferos:
    print("Es un mamifero")
elif animal in aves:
    print("Es una ave")
elif animal in reptiles:
    print("Es un reptil")
else:
    print("Es otro tipo de animal")