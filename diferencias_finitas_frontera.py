import numpy as np
import matplotlib.pyplot as plt

def resolver_problema_frontera():
    """
    Resuelve un problema de frontera usando diferencias finitas
    
    Problema: y'' + p(x)*y' + q(x)*y = f(x)
    Con condiciones de frontera: y(a) = alpha, y(b) = beta
    
    Ejemplo específico:
    y'' - 2y' + y = x*exp(x)
    y(0) = 1, y(1) = 0
    """
    
    # Definir el dominio
    a = 0.0  # frontera izquierda
    b = 1.0  # frontera derecha
    n = 3   # número de puntos interiores
    
    # Condiciones de frontera
    alpha = 1.0  # y(0) = 1
    beta = 0.0   # y(1) = 0
    
    # Crear la malla
    h = (b - a) / (n + 1)
    x = np.linspace(a, b, n + 2)
    
    # Definir las funciones del problema
    def p(x):
        return -2.0  # coeficiente de y'
    
    def q(x):
        return 1.0   # coeficiente de y
    
    def f(x):
        return x * np.exp(x)  # lado derecho
    
    # Crear la matriz del sistema A*y = b
    A = np.zeros((n, n))
    b_vec = np.zeros(n)
    
    # Llenar la matriz A y el vector b
    for i in range(n):
        xi = x[i + 1]  # punto interior i
        
        # Coeficientes de diferencias finitas
        # y''(xi) ≈ (y[i-1] - 2*y[i] + y[i+1]) / h²
        # y'(xi) ≈ (y[i+1] - y[i-1]) / (2*h)
        
        # Coeficiente de y[i-1]
        if i > 0:
            A[i, i-1] = 1/h**2 - p(xi)/(2*h)
        
        # Coeficiente de y[i] (diagonal)
        A[i, i] = -2/h**2 + q(xi)
        
        # Coeficiente de y[i+1]
        if i < n-1:
            A[i, i+1] = 1/h**2 + p(xi)/(2*h)
        
        # Lado derecho
        b_vec[i] = f(xi)
        
        # Ajustar para condiciones de frontera
        if i == 0:  # primer punto interior
            b_vec[i] -= alpha * (1/h**2 - p(xi)/(2*h))
        if i == n-1:  # último punto interior
            b_vec[i] -= beta * (1/h**2 + p(xi)/(2*h))
    
    # Resolver el sistema lineal
    y_interior = np.linalg.solve(A, b_vec)
    
    # Construir la solución completa
    y_completa = np.zeros(n + 2)
    y_completa[0] = alpha
    y_completa[1:-1] = y_interior
    y_completa[-1] = beta
    
    return x, y_completa, A, b_vec

def solucion_exacta(x):
    """
    Solución exacta del problema para comparación
    y'' - 2y' + y = x*exp(x)
    y(0) = 1, y(1) = 0
    """
    # Esta es la solución exacta para este problema específico
    return np.exp(x) * (1 - x + x**2/2)

def graficar_resultados(x, y_numerica, y_exacta):
    """
    Grafica la solución numérica vs exacta
    """
    plt.figure(figsize=(10, 6))
    
    plt.subplot(1, 2, 1)
    plt.plot(x, y_numerica, 'bo-', label='Numérica', markersize=4)
    plt.plot(x, y_exacta, 'r--', label='Exacta', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solución del Problema de Frontera')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    error = abs(y_numerica - y_exacta)
    plt.plot(x, error, 'go-', markersize=4)
    plt.xlabel('x')
    plt.ylabel('Error absoluto')
    plt.title('Error entre Solución Numérica y Exacta')
    plt.grid(True, alpha=0.3)
    plt.yscale('log')
    
    plt.tight_layout()
    plt.show()

# Ejecutar el programa
if __name__ == "__main__":
    print("=== Resolución de Problema de Frontera con Diferencias Finitas ===")
    print("Problema: y'' - 2y' + y = x*exp(x)")
    print("Condiciones: y(0) = 1, y(1) = 0")
    print()
    
    # Resolver el problema
    x, y_num, A, b = resolver_problema_frontera()
    
    # Calcular solución exacta
    y_exact = solucion_exacta(x)
    
    # Mostrar resultados
    print("Resultados:")
    print("x\t\tNumérica\tExacta\t\tError")
    print("-" * 50)
    for i in range(len(x)):
        error = abs(y_num[i] - y_exact[i])
        print(f"{x[i]:.2f}\t\t{y_num[i]:.6f}\t{y_exact[i]:.6f}\t{error:.2e}")
    
    print(f"\nError máximo: {max(abs(y_num - y_exact)):.2e}")
    print(f"Tamaño de paso h: {(x[1] - x[0]):.3f}")
    
    # Mostrar información del sistema
    print(f"\nDimensión del sistema: {A.shape[0]}x{A.shape[1]}")
    print(f"Número de condición: {np.linalg.cond(A):.2e}")
    
    # Graficar
    graficar_resultados(x, y_num, y_exact)
