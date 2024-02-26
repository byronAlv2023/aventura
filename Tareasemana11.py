def buscar_valor(matriz, valor):
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == valor:
                return True, i, j

    return False, None, None

# Ejemplo de una matriz 3x3
mi_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor_a_buscar = 5

# Buscar el valor en la matriz
encontrado, fila, columna = buscar_valor(mi_matriz, valor_a_buscar)

# Mostrar resultados
if encontrado:
    print(f"El valor {valor_a_buscar} se encontró en la posición ({fila}, {columna}) de la matriz.")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
