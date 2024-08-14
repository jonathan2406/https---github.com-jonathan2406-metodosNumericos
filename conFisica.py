import numpy as np

# Definimos los arreglos de tiempo y distancia
tiempo = np.array([0, 3, 5, 8, 10, 13])  # en segundos
distancia = np.array([0, 225, 383, 623, 742, 993])  # en metros

# Calculamos la velocidad media entre cada par de puntos consecutivos
velocidades = np.diff(distancia) / np.diff(tiempo)

# Imprimimos los resultados de manera ordenada
for i in range(len(velocidades)):
    print(f"Velocidad t = {tiempo[i]} s: {velocidades[i]:.2f} m/s")
