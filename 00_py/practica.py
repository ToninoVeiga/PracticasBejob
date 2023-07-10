import random

def is_valid_integer(string):
  """
Verificar que una cadena sea un número entero entre 1 y 20 o sea el literal "x" (sin distinción entre mayúsculas y minúsculas).
   Entrada:
     string: La cadena a verificar.
   Salida:
     True si la cadena es válida, False en caso contrario.
     "string" / "integer" : En caso de True indica si se trata de un numero válido o del caracter de finalización
  """
  if string.lower() == "x":
    return True, "string"
  try:
    int(string)
  except ValueError:
    return False, "string"
  if int(string) < 1 or int(string) > 20:
    return False, "string"
  return True, "integer"

#Bucle principal
while True:
    # Solicitar al usuario el valor de dimensión
    str_dimension = (input("Introducir dimension de matriz: "))
    itsok , valor = is_valid_integer(str_dimension)
    if itsok:
        if valor == "integer":
        # Si se ha introducido un integer ok:
            num_dimension = int(str_dimension) 
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
            print("Cálculo finalizado")
            break
        else:
            print("Proceso finalizado a petición")
            break
    else: 
       print("Enter an integer between 2 or 20 to process matrix or 'x' to exit")

