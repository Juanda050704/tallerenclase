# Solicitar al usuario que ingrese su edad
try:
    edad = int(input("Por favor, ingresa tu edad: "))
except ValueError:
    print("Edad no válida. Debes ingresar un número.")
    exit()

# Definir las etapas de la vida
etapas = {
    'bebé': (0, 2),
    'niño pequeño': (3, 5),
    'niño': (6, 12),
    'adolescente': (13, 17),
    'adulto joven': (18, 35),
    'adulto': (36, 64),
    'adulto mayor': (65, 120)
}

# Determinar la etapa de la vida
etapa = None
for nombre_etapa, (edad_inicio, edad_fin) in etapas.items():
    if edad_inicio <= edad <= edad_fin:
        etapa = nombre_etapa
        break

if etapa:
    print(f"Tú estás en la etapa de '{etapa}'.")
else:
    print("No se pudo determinar la etapa de la vida para esta edad.")
