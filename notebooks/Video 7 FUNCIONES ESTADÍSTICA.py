# Importa la librería NumPy y la usa con el alias 'np' para escribir menos código.
import numpy as np

# Crea una matriz 3x3 con los números del 1 al 9 y la guarda en la variable 'm'.
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Muestra la matriz creada en la consola.
print(m)

# Imprime una línea en blanco para separar la salida.
print("")

# Calcula la media de todos los elementos de la matriz y la muestra en pantalla.
print(np.mean(m))
