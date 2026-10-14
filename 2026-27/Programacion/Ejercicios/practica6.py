# 1. Crea un programa que determini si un número introduït des de teclat és positiu, negatiu o zero.
num = int(input('Introduce un numero: '))
if num > 0:
    print('El numero introducido es positivo.')
elif num < 0:
    print('El numero introducido es negativo.')
else:
    print('El numero es cero.')
# 2. Escriu un programa que escrigui per pantalla si una fruita es "cítrica", "dolça", "fruit sec" o "altra" utilitzant entrada per teclat 
# (utiliza una llista per cada tipus de fruita, conjunt o tupla per la comprovació).
frutas = {'Manzana':'Dulce', 'Naranja':'Citrica', 'Cacahuete':'Fruto Seco'}
fruta = input(f'Introduce una fruta: ')
match fruta:
    case 'Manzana':
        print(f'La fruta {fruta} es {frutas[fruta]}')
    case 'Naranja':
        print(f'La fruta {fruta} es {frutas[fruta]}')
    case 'Cacahuete':
        print(f'La fruta {fruta} es {frutas[fruta]}')
    case _:
        print(f'La fruta {fruta} no esta en la lista, es otro tipo de fruta.')
# 3. Crea un programa que determini si una persona té menys de 18 anys (menor), té més o igual a 18 anys 
# (si té entre 18 y 30 -inclosos- és un adult jove, si te entre 31 y 65 anys és un adult, si té més de 65 anys és un adult senior) 
# i m’imprimeixi per pantalla el tipus de persona.
años = int(input('Introduce tu edad: '))
if años < 18:
    print('Eres menor de edad.')
elif (años >= 18) and (años <= 30):
    print('Eres un adulto joven.')
elif (años >= 31) and (años < 65):
    print('Eres un adulto.')
else: 
    print('Eres un adulto senior.')
# 4. Creeu un programa que determini el dia de la setmana a partir d'un número de l'1 al 7 (1 Dilluns…i finalment 7 Diumenge).
dia = int(input('Introduce un numero del 1 al 7: '))
match dia:
    case 1:
        print('Hoy es lunes.')
    case 2:
        print('Hoy es martes.')
    case 3:
        print('Hoy es miercoles.')
    case 4:
        print('Hoy es jueves.')
    case 5:
        print('Hoy es viernes.')
    case 6:
        print('Hoy es sabado.')
    case 7:
        print('Hoy es domingo.')
    case _:
        print('No has introducido un numero del 1 al 7.')
# 5. Escriu un programa que classifiqui un animal en "mamífer", "au", "rèptil" o "un altre" .
animales = {'castor':'mamifero', 'colibri':'ave', 'camaleon':'reptil'}
animal = input('Introduce un animal: ')
match animal:
    case 'castor':
        print(f'El animal {animal} es un {animales[animal]}')
    case 'colibri':
        print(f'El animal {animal} es un {animales[animal]}')
    case 'camaleon':
        print(f'El animal {animal} es un {animales[animal]}')
    case _:
        print(f'El animal {animal} es otro tipo de animal')
# 6. Creeu un programa que calculi el cost d'enviament d’un paquet segons la distància: fins a 10 km, 10-50 km, o més de 50 km.
coste = int(input('Introduce el coste de envio: '))
distancia = int(input('Introduce la distancia: '))
if distancia < 10:
    print(f'El coste de envio es: {coste * 1}')
elif distancia >= 10 and distancia <= 50:
    print(f'El coste de envio es: {coste * 1.5}')
else:
    print(f'El coste de envio es: {coste * 2}')
# 7. Crea un programa que assigni una qualificació a una nota numèrica (A, B, C, D o F) en funció d’una nota numérica donada per teclat 
# (A = entre 9 i 10 -ambdós inclosos-, B = entre 7 i 9 -incloent el 7 però no el 9- , C = entre 5 i 7 -incloent el 5 però no el 7-, 
# F = menys de 5).
nota = int(input('Introduce tu nota: '))
if nota > 10:
    print('No has introducido una nota valida.')
elif nota == 10 or nota == 9:
    print('Tu nota es A.')
elif nota >= 7:
    print('Tu nota es B')
elif nota >= 5:
    print('Tu nota es C')
else:
    print('Tu nota es F')
# 8. Escriu un programa que classifiqui un dia de la setmana a "laborable" o "cap de setmana".
dia = input('Introduce un dia: ').lower()
dias = {'lunes':'laborable', 'martes':'laborable', 'miercoles':'laborable', 'jueves':'laborable', 'viernes':'laborable', 'sabado':'fin de semana', 'domingo':'fin de semana'}
if dias[dia] == 'laborable':
    print(f'El dia {dia} es {dias[dia]}')
elif dias[dia] == 'fin de semana':
    print(f'El dia {dia} es {dias[dia]}')
else: 
    print('No has introducido un dia de la semana.')
# 9. Escriu un programa que emmagatzemi la cadena de caràcters contrasenya en una variable, 
# pregunteu a l'usuari per la contrasenya i imprimiu per pantalla si la contrasenya 
# introduïda per l'usuari coincideix amb la desada a la variable sense tenir en compte majúscules i minúscules.
contra = 'contraseña'
verificacion = input('Introduce la contraseña: ').lower()
if verificacion == contra:
    print('La contraseña es correcta.')
else:
    print('La contraseña que has introducido no es la correcta.')
# 10. Escriu un programa que demani a l'usuari dos números i en mostri per pantalla la divisió. 
# Si el divisor és zero, el programa ha de mostrar un error.
num1 = int(input('Introduce el dividendo: '))
num2 = int(input('Introduce el divisor: '))
if num2 == 0:
    print('No se puede dividir por cero')
else:
    print(f'La division entre {num1} y {num2} es {num1 / num2}.')
# 11. Per tributar un determinat impost cal ser major de 16 anys i tenir uns ingressos iguals o superiors a 1000 € mensuals. 
# Escriure un programa que pregunti a l’usuari la seva edat i els seus ingressos mensuals i mostri per pantalla si l’usuari 
# ha de tributar o no.
edad = int(input('Introduce tu edad: '))
ingresos = float(input('Introduce tus ingresos mensuales: '))
if edad < 16 or ingresos < 1000:
    print('No tienes que tributar.')
else:
    print('Tienes que tributar.')
# 12. Els alumnes d'un curs s’han dividit en dos grups A i B d’acord amb el sexe i el nom. 
# El grup A està format per les dones amb un nom anterior a la M i els homes amb un nom posterior a la N i el grup B per la resta. 
# Escriu un programa que pregunti a l'usuari el nom i el sexe, i mostri per pantalla el grup que li correspon.
nombre = input('Introduce tu nombre: ').lower()
sexo = input('Introduce tu sexo: ').lower()
match sexo:
    case 'mujer':
        if nombre[0] < 'm':
            print('Tu grupo es el A.')
        else:
            print('Tu grupo es el B')
    case 'hombre':
        if nombre[0] > 'n':
            print('Tu grupo es el A.')
        else:
            print('Tu grupo es el B')
    case _:
        print('Eso no es un genero valido.')
# 13. Escriu un programa que pregunti a l'usuari la renda anual i mostri per pantalla el tipus impositiu que li correspon.
# Els trams impositius per a la declaració de la renda en un país determinat són els següents:
# Renda Tipus impositiu
# Menys de 10000€ 		5%
# Entre 10000€ i 20000€ 	15%
# Entre 20000€ i 35000€ 	20%
# Entre 35000€ i 60000€ 	30%
# Més de 60000€ 		45%
renta = float(input('Introduce tu renta mensual: '))
if renta < 10000:
    print(f'Tu renta mensual es del 5%.')
elif renta >= 10000 and renta < 20000:
    print(f'Tu renta mensual es del 15%.')
elif renta >= 20000 and renta < 35000:
    print(f'Tu renta mensual es del 20%.')
elif renta >= 35000 and renta < 60000:
    print(f'Tu renta mensual es de 30%.')
elif renta >= 60000:
    print(f'Tu renta mensual es de 45%.')
else:
    print(f'No has introducido una renta valida.')
# 14. Implementa un programa que verifiqui si una fruita és "poma", "plàtan" o "una altra" utilitzant match.
fruta = input('Introduce una fruta: ').lower()
match fruta:
    case 'manzana':
        print('Tu fruta es una manzana.')
    case 'platano':
        print('Tu fruta es un platano.')
    case _:
        print('Tu fruta es otra fruta.')
# 15. Implementa una funció que determini el dia de la setmana a partir d'un número de l'1 al 7 fent servir match.
dia = int(input('Introduce un numero del 1 al 7: '))
match dia:
    case 1:
        print('Hoy es lunes.')
    case 2:
        print('Hoy es martes.')
    case 3:
        print('Hoy es miercoles.')
    case 4:
        print('Hoy es jueves.')
    case 5:
        print('Hoy es viernes.')
    case 6:
        print('Hoy es sabado.')
    case 7:
        print('Hoy es domingo.')
    case _:
        print('No has introducido un numero del 1 al 7.')
# 16. Escriu un programa que rebi com a entrada (serà l'entrada per teclat) els codis: 200, 301, 302, 404, 500 i 503. 
# El significat d'aquests codis és el següent: '200' = 'Tot ok', '301' = 'Moviment permanent de la pàgina', 
# '302' = 'Moviment temporal de la pàgina', '404' = 'Pàgina no trobada', '500' = 'Error intern del servidor', 
# '503' = 'Servidor no disponible '. El programa haurà de tornar el missatge corresponent al codi introduït. 
# Si s'introdueix un codi no comprès entre aquests, el programa ha de tornar per pantalla el missatge 'Missatge desconegut'. 
# Tot això ho hauràs de ver fent servir match.
codigo = int(input('Introduce el codigo de error: '))
match codigo:
    case 200:
        print('Todo bien.')
    case 301:
        print('Movimiento permanente de la pagina.')
    case 302:
        print('Movimiento temporal de la pagina.')
    case 404:
        print('Pagina no encontrada.')
    case 500:
        print('Error interno del servidor.')
    case 503:
        print('Servidor no encontrado.')
    case _:
        print('Mensaje desconocido.')