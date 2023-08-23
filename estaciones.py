
mes = input("Por favor, ingresa el nombre del mes: ").lower()
try:
    dia = int(input("Ahora, ingresa el día del mes: "))
except ValueError:
    print("Día no válido. Debes ingresar un número.")

estaciones = {
    'enero': 'invierno',
    'febrero': 'invierno',
    'marzo': 'primavera',
    'abril': 'primavera',
    'mayo': 'primavera',
    'junio': 'verano',
    'julio': 'verano',
    'agosto': 'verano',
    'septiembre': 'otoño',
    'octubre': 'otoño',
    'noviembre': 'otoño',
    'diciembre': 'invierno'
}


if mes in estaciones:
    estacion = estaciones[mes]
    
    if dia >= 1 and dia <= 31: 
        if (mes == 'enero' and dia >= 1) or (mes == 'diciembre' and dia <= 21):
            estacion = 'invierno'
        elif (mes == 'marzo' and dia >= 20) or (mes == 'abril' and dia <= 19):
            estacion = 'primavera'
        elif (mes == 'junio' and dia >= 21) or (mes == 'septiembre' and dia <= 21):
            estacion = 'verano'
        elif (mes == 'diciembre' and dia >= 22) or (mes == 'febrero' and dia <= 19):
            estacion = 'invierno'
        
        print(f"La estación del año para {mes.capitalize()} {dia} es {estacion}.")
    else:
        print("Día no válido. Debes ingresar un día entre 1 y 31.")
else:
    print("Mes no válido. Por favor, ingresa un mes válido.")
