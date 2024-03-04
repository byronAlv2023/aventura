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
