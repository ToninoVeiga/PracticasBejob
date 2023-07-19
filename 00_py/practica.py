import random
"""
Constantes globales 
"""
di_mensajes = {
            0: "Sin información adicional",
            1: "La dimensión debe ser un número en el rango solicitado", 
            2: "Entrada inválida. Introduce una dimensión entera de acuerdo al rango indicado.",
            3: "Proceso Abortado",
            4: "Proceso Ejecutado",
        }

"""
definicion de clases 
"""
class Matriz:

    def __init__(self):
        self.size = None
        self.matriz = None
        self.n_max_random = 20

    def __str__(self):
        """
        Print la matriz con las celdas justificadas a la derecha respetando la longitud mayor
        """
        lista_aplanada = [item for sublist in self.matriz for item in sublist]
        top = max(lista_aplanada)
        string = str(top)
        number_of_digits = max(len(string), 4)

        matrix_string = ""
        for row in self.matriz:
            row_string = " ".join(str(value).rjust(number_of_digits) for value in row)
            matrix_string += row_string + "\n"
        return matrix_string
    
    def get_element(self, row, column):
        return self.matriz[row][column]
    
    def set_element(self, row, column, value):
        self.matriz[row][column] = value
    
    def get_size(self):
        return self.size
    
    def carga_matriz(self , n):
        """
        Salida: Se rellena la matriz con números enteros aleatorios
        """
        self.size = n
        self.matriz = [[random.randint(0, self.n_max_random) for _ in range(n)] for _ in range(n)]
        return self.matriz
        
    # Sumar los valores de cada fila
    def obtener_suma_filas(self):
        """
        Salida: Lista con la suma de cada fila de la matriz.
        """
        sums = []
        for row in range(self.get_size()):
            sums.append(sum(self.matriz[row]))
        return sums
    
    # Sumar los valores de cada columna
    def obtener_suma_columnas(self):
        """
        Salida: Lista con la suma de cada columna de la matriz
        """
        sums = []
        for col in range(len(self.matriz[0])):
            x = 0
            for row in range(len(self.matriz)):
                x += self.matriz[row][col]
            sums.append(x)
        return sums
       
    # Añade una fila y una columa a la matriz
    def incrementar_dimension(self, l1, l2):
        # Añadir una nueva columna a la matriz desde la lista L1
        for i in range(len(self.matriz)):
            self.matriz[i].append(l1[i])

        # Añadir una nueva fila a la matriz desde la lista L2
        last_cell_value = sum(l1) + sum(l2)
        self.matriz.append(l2 + [last_cell_value]) 
        self.size +=1    

class Peticion:
    def __init__(self):
        self.dimension = None
        self.n_max_dimension = 50
        self.estado = "Parado"
    # Solicitar al usuario el valor para actualizar la dimensión de la matriz
    def obtener_dimension(self):
        """
        Salida: 
        """
        while True:
            entrada = input(f"Introduce una dimensión entera del 1 al {self.n_max_dimension} (x para abortar): ")
            if entrada.lower() == "x":
                self.estado = "Abortado"
                return

            try:
                dimension = int(entrada)
                if 1 <= dimension <= self.n_max_dimension:
                    self.dimension = dimension
                    self.estado = "En proceso"
                    break
                else:
                    print(di_mensajes[1])
            except ValueError:   
                print(di_mensajes[2])
"""
main 
"""
def main():
    matriz = Matriz()
    peticion = Peticion()
    peticion.obtener_dimension()
    if peticion.estado == "En proceso":
#   if peticion.dimension is not None:
#        print("\nPresiona cualquier tecla para continuar...")
#        input()
        matriz.carga_matriz(peticion.dimension)
        # Imprimir matriz generado
        print("\n\nLa matriz inicial es \n\n")
        print(matriz)    
#        print("\nPresiona cualquier tecla para continuar...")
#        input()

        # Obtener suma de las filas de la matriz
        sumr = matriz.obtener_suma_filas()

        # Obtener suma de las columnas de la matriz
        sumc = matriz.obtener_suma_columnas()        

        # Incrementar dimensión con los valores correspondientes a la suma de cada fila y cada columna inicial
        matriz.incrementar_dimension(sumr,sumc)

        for i, sum in enumerate(sumr):
            print("La suma de la fila {} de la matriz inicial es {}".format(i+1, sum))
#        print("\nPresiona cualquier tecla para continuar...")
#        input()
        print("\n")

        for i, sum in enumerate(sumc):
            print("La suma de la columna {} de la matriz inicial es {}".format(i+1, sum))
#        print("\nPresiona cualquier tecla para continuar...")
#        input()
        
        print(f"\n\nLa matriz final de dimension {matriz.size} es \n\n")
        print(matriz)
#        print("\nPresiona cualquier tecla para continuar...")
#        input()

        print(di_mensajes[4])

    elif peticion.estado == "Abortado":
        print(di_mensajes[3])

# Verificar si el archivo se ejecuta directamente como un programa
if __name__ == "__main__":
    # Llamar a la función main()
    main()

