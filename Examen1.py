import random
import math

# Define el rango de búsqueda (1 a 1,000,000)
min_number = 1
max_number = int(input("Ingrese el número al que se le va a encontrar el número primo más cercano: "))

# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

# Función para calcular la aptitud (fitness) de un número
def aptitud(numero):
    return abs(numero - max_number) if es_primo(numero) else numero

# Función para generar una cadena de bits aleatoria
def generar_cadena_bits(longitud):
    return ''.join(random.choice('01') for _ in range(longitud))

# Función para realizar el cruce entre dos cadenas de bits
def cruce(padre1, padre2):
    punto_cruce = random.randint(1, min(len(padre1), len(padre2)) - 1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

# Función para realizar la mutación en una cadena de bits
def mutacion(cadena_bits, tasa_mutacion):
    cadena_mutada = ''
    for bit in cadena_bits:
        if random.random() < tasa_mutacion:
            cadena_mutada += '1' if bit == '0' else '0'
        else:
            cadena_mutada += bit
    return cadena_mutada

# Función principal para encontrar el número primo más cercano
def encontrar_primo_cercano():
    poblacion_tamano = 100
    longitud_cadena_bits = int(math.log2(max_number)) + 1
    tasa_mutacion = 0.01

    poblacion = [generar_cadena_bits(longitud_cadena_bits) for _ in range(poblacion_tamano)]

    for _ in range(100):  # Número de generaciones
        fitness_values = [aptitud(int(cadena, 2)) for cadena in poblacion]
        poblacion = sorted(poblacion, key=lambda x: aptitud(int(x, 2)))[:poblacion_tamano // 2]
        nueva_generacion = []

        while len(nueva_generacion) < poblacion_tamano // 2:
            padre1, padre2 = random.choices(poblacion, k=2)
            hijo1, hijo2 = cruce(padre1, padre2)
            hijo1 = mutacion(hijo1, tasa_mutacion)
            hijo2 = mutacion(hijo2, tasa_mutacion)
            nueva_generacion.extend([hijo1, hijo2])

        poblacion.extend(nueva_generacion)

    mejor_cadena = poblacion[0]
    mejor_numero = int(mejor_cadena, 2)
    return mejor_numero

# Encuentra el número primo más cercano
if max_number > 1000000:
    print("El número ingresado es mayor a 1,000,000. Por favor, ingrese un número menor.")
    exit()
numero_primo_cercano = encontrar_primo_cercano()
print(f"El número primo más cercano a {max_number} es {numero_primo_cercano}.")
