import random

class Matrix:
    def __init__(self, n):
        self.n = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
    # Rellenar matriz con valores enteros aleatorios
    def generate(self):
        for i in range(self.n):
            for j in range(self.n):
                self.matrix[i][j] = random.randint(0, 9)
    # Imprimir la matriz
    def print(self):
        for row in self.matrix:
            print(row)
    # Sumar los valores de cada fila e imprime resultado
    def add_rows(self):
        for row in range(len(self.matrix)):
            sum = 0
            for element in self.matrix[row]:
                sum += element
            print(f"The sum of row", int(row)+1, "is" , {sum} )
    # Sumar los valores de cada columna e imprime resultado
    def add_cols(self):
        for col in range(len(self.matrix[0])):
            sum = 0
            for row in range(len(self.matrix)):
                sum += self.matrix[row][col]
            print(f"The sum of column" , int(col)+1 , "is" , {sum})
    # Solicitar al usuario el valor de dimensión
    def get_matrix_dimension():
        while True:
            dimension = input("Enter the dimension of the matrix: ")
            try:
                dimension = int(dimension)
                if dimension > 0:
                    return dimension
            except ValueError:
                print("Please enter a valid integer.")

dimension = Matrix.get_matrix_dimension()
matrix = Matrix(dimension)
matrix.generate()
matrix.print()
matrix.add_rows()
matrix.add_cols()