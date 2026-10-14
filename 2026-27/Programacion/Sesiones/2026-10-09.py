# Exercici 12 de pràctica 6
''' Els alumnes d'un curs s’han dividit en dos grups A i B d’acord amb el sexe i el nom. '
'El grup A està format per les dones amb un nom anterior a la M i els '
'homes amb un nom posterior a la N i el grup B per la resta. Escriu un programa que '
'pregunti a l'usuari el nom i el sexe, i mostri per pantalla el grup que li correspon.'''
'''
nom_alumne = input('Introdueix el teu nom: ')
sexe_alumne = input('Introdueix D si ets dona o M si ets home: ')

abecedario = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
    "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
    "k": 11, "l": 12, "m": 13, "n": 14, "ñ": 15,
    "o": 16, "p": 17, "q": 18, "r": 19, "s": 20,
    "t": 21, "u": 22, "v": 23, "w": 24, "x": 25,
    "y": 26, "z": 27
}

match sexe_alumne:
    case 'D':
        if abecedario[nom_alumne[0].lower()] < 13:
            print(f'Hola {nom_alumne}, estàs assignada al grup A')
        else:
            print(f'Hola {nom_alumne}, estàs assignada al grup B')
    case 'M':
        if abecedario[nom_alumne[0].lower()] > 14:
            print(f'Hola {nom_alumne}, estàs assignat al grup A')
        else:
            print(f'Hola {nom_alumne}, estàs assignat al grup B')
    case _:
        print(f'Hola {nom_alumne}, ets tan inútil que no saps ni introduir una lletra entre dos...')
'''

print()
# Exercici 13 pràctica 6:
'''
Escriu un programa que pregunti a l'usuari la renda anual i mostri per pantalla el tipus impositiu que li correspon.
Els trams impositius per a la declaració de la renda en un país determinat són els següents:
Renda Tipus impositiu
Menys de 10000€ 		5%
Entre 10000€ i 20000€ 	15%
Entre 20000€ i 35000€ 	20%
Entre 35000€ i 60000€ 	30%
Més de 60000€ 		45%
'''
print()
salari_brut = float(input("Indica el teu salari anual brut: "))

irpf = 0

if salari_brut < 10000:
    irpf = salari_brut*0.05
elif salari_brut < 20000:
    irpf = (salari_brut - 10000)*0.15 + 500
elif salari_brut < 35000:
    irpf = (salari_brut - 20000)*0.2 + 2000
elif salari_brut < 60000:
    irpf = (salari_brut - 35000)*0.3 + 5000
else:
    irpf = (salari_brut - 60000)*0.45 + 12500

print(f'En funció del teu salari {salari_brut}€ has de pagar {irpf}€ d\'inpostos')


print()
# Exercici 2 de match-case pràctica 6
'''
Implementa una funció que determini el dia de la setmana a partir d'un número de l'1 al 7 fent servir match.
'''

dia_setmana = input("Introdueix el número del día de la setmana (1 a 7): ")

dias_setmana_dict = {1:'Dilluns', 2:'Dimarts', 3:'Dimecres', 4:'Dijous', 5:'Divendres', 6:'Dissabte', 7:'Diumenge'}

match dia_setmana:
    case "1":
        print(f'Has triat el num. {int(dia_setmana)} que correspon a {dias_setmana_dict[int(dia_setmana)]}')
    case "2":
        print(f'Has triat el num. {int(dia_setmana)} que correspon a {dias_setmana_dict[int(dia_setmana)]}')
    case "3":
        print(f'Has triat el num. {int(dia_setmana)} que correspon a {dias_setmana_dict[int(dia_setmana)]}')
    case "4":
        print(f'Has triat el num. {int(dia_setmana)} que correspon a {dias_setmana_dict[int(dia_setmana)]}')
    case "5":
        print(f'Has triat el num. {int(dia_setmana)} que correspon a {dias_setmana_dict[int(dia_setmana)]}')
    case "6":
        print(f'Has triat el num. {int(dia_setmana)} que correspon a {dias_setmana_dict[int(dia_setmana)]}')
    case "7":
        print(f'Has triat el num. {int(dia_setmana)} que correspon a {dias_setmana_dict[int(dia_setmana)]}')
    case _:
        print(f'Ets tan retrassat que no saps posar un número de l\'1 al 7?????')

# Pel proper dia, haureu de cercar 2 exercicis (buscau problemes de la vida real) més complicats d'els que heu 
# fet a la pràctica 6 i provar de solucionar-los.