# Importa la librería NumPy para poder trabajar con matrices y operaciones lineales.
import numpy as np

# Define la matriz A de tamaño 3x3 con los coeficientes del sistema de ecuaciones.
A = np.array([[2, 1, -2], [3, 0, 1], [1, 1, -1]])

# Muestra la matriz A en la consola.
print(A)

# Imprime una línea en blanco para separar la salida.
print("")

# Define el vector columna b con los términos independientes del sistema.
b = np.array([[-3], [5], [-2]])

# Muestra la transpuesta de b, es decir, la convierte en una fila para visualizarla.
print(np.transpose(b))

# Imprime otra línea en blanco para separar la salida.
print("")

# Resuelve el sistema lineal A x = b y guarda la solución en la variable x.
x = np.linalg.solve(A, b)

# Muestra la solución x del sistema.
print(x)

# Comprueba si A @ x es aproximadamente igual a b y muestra True o False.
print(np.allclose(np.dot(A, x), b))
