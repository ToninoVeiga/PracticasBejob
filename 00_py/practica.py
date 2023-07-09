import random

# Solicitar el número de filas y columnas al usuario

try:
    num_dimension = int(input("Introducir dimension de matriz: "))

# Crear la matriz y rellenarla con valores enteros aleatorios
    matriz = [[random.randint(0, 9) for _ in range(num_dimension)] for _ in range(num_dimension)]

# Imprimir la matriz
    for fila in matriz:
        print(fila)


# Sumar los valores de cada fila e imprimir el número de fila
    for i, fila in enumerate(matriz, 1):
        suma_fila = sum(fila)
        print("Suma de la fila", i, ":", suma_fila)

# Sumar los valores de cada columna
    for columna in range(num_dimension):
        suma_columna = sum(matriz[fila][columna] for fila in range(num_dimension))
        print("Suma de la columna ", columna+1 , ":" , suma_columna)
    
except ValueError:
    print("The input is not a valid integer.")
