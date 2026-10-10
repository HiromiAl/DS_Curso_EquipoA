import numpy as np

# Matriz de ejemplo
matriz = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Matriz:")
print(matriz)

# Suma total
print("\nSuma total:")
print(np.sum(matriz))

# Suma por columnas (axis=0)
print("\nSuma por columnas:")
print(np.sum(matriz, axis=0))

# Suma por filas (axis=1)
print("\nSuma por filas:")
print(np.sum(matriz, axis=1))

# Promedio por columnas
print("\nPromedio por columnas:")
print(np.mean(matriz, axis=0))

# Promedio por filas
print("\nPromedio por filas:")
print(np.mean(matriz, axis=1))

# Valor máximo por columna
print("\nMáximo por columna:")
print(np.max(matriz, axis=0))

# Valor máximo por fila
print("\nMáximo por fila:")
print(np.max(matriz, axis=1))
