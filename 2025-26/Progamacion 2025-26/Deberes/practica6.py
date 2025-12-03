# Ejercicio 1: Determinar si un numero es positivo, negativo o cero
num = float(input("Introduce un numero: "))

if num > 0: 
    print("El numero es positivo")
elif num < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")

# Ejercicio 2: Determinar si una fruta es citrica, dulce, fruto seco o otra
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

# Ejercicio 4: Determinar el dia de la semana segun el numero
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

# Ejercicio 5: Clasifica un animal
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

# Ejercicio 6: calcular coste de envío según distancia
dist = float(input("Introduce la distancia en km: "))
if dist <= 10:
    print("Coste: 5€")
elif dist <= 50:
    print("Coste: 10€")
else:
    print("Coste: 20€")

# Ejercicio 7: clasificación de nota escolar
nota = float(input("Introduce la nota: "))
if 9 <= nota <= 10:
    print("A")
elif 7 <= nota < 9:
    print("B")
elif 5 <= nota < 7:
    print("C")
else:
    print("F")

# Ejercicio 8: clasificar día como laborable o fin de semana
dia = input("Introduce un día de la semana: ").lower()
if dia in {"lunes", "martes", "miercoles", "jueves", "viernes"}:
    print("Laborable")
elif dia in {"sabado", "domingo"}:
    print("Cap de setmana")
else:
    print("Dia no válido")

# Ejercicio 9: comprobar contraseña sin distinguir mayúsculas
contrasena = "python123"
entrada = input("Introduce la contraseña: ")
if entrada.lower() == contrasena.lower():
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

# Ejercicio 10: división con control de divisor 0
a = float(input("Introduce el primer numero: "))
b = float(input("Introduce el segundo numero: "))
if b == 0:
    print("Error: no se puede dividir entre 0")
else:
    print(a / b)

# Ejercicio 11: determinar si debe tributar
edad = int(input("Introduce tu edad: "))
ingresos = float(input("Introduce tus ingresos mensuales: "))
if edad > 16 and ingresos >= 1000:
    print("Debes tributar")
else:
    print("No debes tributar")

# Ejercicio 12: asignar grupo según nombre y sexo
nombre = input("Introduce tu nombre: ").capitalize()
sexo = input("Introduce tu sexo (H/M): ").upper()

if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre > "N"):
    print("Grupo A")
else:
    print("Grupo B")

# Ejercicio 13: calcular tipo impositivo según renta anual
renda = float(input("Introduce tu renta anual: "))
if renda < 10000:
    print("5%")
elif renda < 20000:
    print("15%")
elif renda < 35000:
    print("20%")
elif renda < 60000:
    print("30%")
else:
    print("45%")

# Ejercicio 14: match para fruta
fruta = input("Introduce una fruta: ").lower()
match fruta:
    case "poma":
        print("Es una poma")
    case "platan" | "plàtan":
        print("Es un plàtan")
    case _:
        print("És una altra fruita")

# Ejercicio 15: match para día de la semana por número
num = int(input("Introduce un número del 1 al 7: "))
match num:
    case 1: print("Dilluns")
    case 2: print("Dimarts")
    case 3: print("Dimecres")
    case 4: print("Dijous")
    case 5: print("Divendres")
    case 6: print("Dissabte")
    case 7: print("Diumenge")
    case _: print("Número invàlid")

# Ejercicio 16: match para códigos HTTP
code = input("Introduce un código: ")

match code:
    case "200": print("Tot ok")
    case "301": print("Moviment permanent de la pàgina")
    case "302": print("Moviment temporal de la pàgina")
    case "404": print("Pàgina no trobada")
    case "500": print("Error intern del servidor")
    case "503": print("Servidor no disponible")
    case _: print("Missatge desconegut")