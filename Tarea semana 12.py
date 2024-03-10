import numpy as np

# Definir las ciudades, días de la semana y semanas
ciudades = ['CiudadA', 'CiudadB', 'CiudadC']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = ['Semana1', 'Semana2', 'Semana3']

# Crear una matriz 3D de temperaturas aleatorias para cada día en cada ciudad y semana
temperaturas = np.random.randint(low=20, high=35, size=(len(ciudades), len(dias_semana), len(semanas)))

# Mostrar la matriz de temperaturas
print("Matriz de temperaturas:")
print(temperaturas)

# Calcular el promedio de temperaturas por semana para cada ciudad
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedio de temperaturas para {ciudad}:")
    for j, semana in enumerate(semanas):
        promedio_semana = np.mean(temperaturas[i, :, j])
        print(f"{semana}: {promedio_semana:.2f}°C")

def temperatura_promedio(datos_temperaturas):
    """
    Calcula la temperatura promedio de una ciudad durante un período de tiempo.

    Args:
    - datos_temperaturas: Un diccionario que contiene datos de temperaturas de múltiples ciudades y semanas.
                          El formato del diccionario debe ser: {'ciudad': {'semana1': [temp1, temp2, ...], 'semana2': [temp1, temp2, ...], ...}, ...}

    Returns:
    - Un diccionario con la temperatura promedio de cada ciudad: {'ciudad': temperatura_promedio, ...}
    """
    temperatura_promedio_ciudades = {}

    for ciudad, datos_semanales in datos_temperaturas.items():
        temperatura_promedio_semanal = 0

        for semana, temperaturas in datos_semanales.items():
            temperatura_promedio_semanal += sum(temperaturas)

        # Calcula el promedio dividiendo la suma total de temperaturas entre el número de semanas
        temperatura_promedio_semanal /= len(datos_semanales)

        temperatura_promedio_ciudades[ciudad] = temperatura_promedio_semanal

    return temperatura_promedio_ciudades

# Ejemplo de datos de temperaturas para 3 ciudades durante 4 semanas
datos_temperaturas_ejemplo = {
    'CiudadA': {'Semana1': [25, 28, 23], 'Semana2': [27, 26, 24], 'Semana3': [26, 29, 28], 'Semana4': [30, 32, 31]},
    'CiudadB': {'Semana1': [18, 20, 19], 'Semana2': [22, 24, 23], 'Semana3': [17, 19, 20], 'Semana4': [21, 23, 22]},
    'CiudadC': {'Semana1': [31, 30, 32], 'Semana2': [29, 28, 30], 'Semana3': [33, 32, 34], 'Semana4': [28, 27, 29]}
}

# Calcula la temperatura promedio de cada ciudad
resultado = temperatura_promedio(datos_temperaturas_ejemplo)

# Imprime los resultados
for ciudad, temp_promedio in resultado.items():
    print(f'Temperatura promedio en {ciudad}: {temp_promedio:.2f} grados Celsius')
