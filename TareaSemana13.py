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
