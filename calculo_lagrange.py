import numpy as np

# Datos recolectados en la FIE (Nodos)
horas = np.array([8.0, 10.0, 14.0, 16.0])
velocidades = np.array([120.0, 45.0, 105.0, 80.0])

def lagrange(x_nodos, y_nodos, x_evaluar):
    """
    Calcula la interpolación polinómica de Lagrange para predecir el ancho de banda.
    """
    n = len(x_nodos)
    resultado_final = 0.0
    
    for i in range(n):
        L_i = 1.0
        for j in range(n):
            if i != j: # Evitar división por cero
                L_i = L_i * ((x_evaluar - x_nodos[j]) / (x_nodos[i] - x_nodos[j]))
        
        resultado_final += y_nodos[i] * L_i
        
    return resultado_final

# Si ejecutamos este script directamente, hacemos una prueba de consola
if __name__ == "__main__":
    hora_prueba = 11.5 
    velocidad_predicha = lagrange(horas, velocidades, hora_prueba)
    print("=== Modelo Predictivo de Ancho de Banda FIE ===")
    print(f"Hora de consulta: {hora_prueba} hrs (11:30 AM)")
    print(f"Velocidad predicha: {velocidad_predicha:.2f} Mbps")
