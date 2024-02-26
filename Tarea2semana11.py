def ordenar_fila(matriz, numero_fila):
    # Verificar si la fila especificada existe en la matriz
    if numero_fila < 0 or numero_fila >= len(matriz):
        print("Número de fila inválido.")
        return

    # Aplicar el algoritmo de ordenación de selección a la fila específica
    matriz[numero_fila] = sorted(matriz[numero_fila])

# Ejemplo de una matriz 3x3
mi_matriz = [
    [3, 1, 2],
    [6, 5, 4],
    [9, 7, 8]
]

# Número de fila a ordenar
fila_a_ordenar = 1

# Mostrar la matriz original
print("Matriz Original:")
for fila in mi_matriz:
    print(fila)

# Ordenar la fila especificada
ordenar_fila(mi_matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con Fila Ordenada:")
for fila in mi_matriz:
    print(fila)
