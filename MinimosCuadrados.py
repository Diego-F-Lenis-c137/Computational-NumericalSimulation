import numpy as np
import sympy as sp
from tabulate import tabulate

def aproximacion_minimos_cuadrados_cuadratica(x_data, y_data, mostrar_detalles=True):
    """
    Realiza aproximación por mínimos cuadrados para función cuadrática f(x) = ax² + bx + c
    
    Parámetros:
    x_data: array de valores x
    y_data: array de valores y
    mostrar_detalles: bool, si mostrar el proceso paso a paso
    
    Retorna:
    dict con coeficientes, función aproximada
    """
    
    # Convertir los datos a arreglos de NumPy
    x = np.array(x_data)
    y = np.array(y_data) 
    n = len(x)
    
    # Prints iniciales
    if mostrar_detalles:
        print("=" * 60)
        print("APROXIMACIÓN POR MÍNIMOS CUADRADOS - FUNCIÓN CUADRÁTICA")
        print("=" * 60)
        print(f"Función objetivo: f(x) = ax² + bx + c")
        print(f"Número de puntos: {n}")
        print()
    
    # Crear tabla de datos
    tabla_datos = []
    for i in range(n):
        tabla_datos.append([i+1, x[i], y[i], x[i]**2, x[i]**3, x[i]**4, x[i]*y[i], x[i]**2*y[i]])
    
    # Encabezados de la tabla
    headers = ["i", "xᵢ", "yᵢ", "xᵢ²", "xᵢ³", "xᵢ⁴", "xᵢyᵢ", "xᵢ²yᵢ"]
    
    # Mostrar tabla de datos si se solicita
    if mostrar_detalles:
        print("Tabla de datos:")
        print(tabulate(tabla_datos, headers=headers, tablefmt="grid", floatfmt=".4f"))
        print()
    
    # Calcular sumas necesarias
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_x3 = np.sum(x**3)
    sum_x4 = np.sum(x**4)
    sum_xy = np.sum(x*y)
    sum_x2y = np.sum(x**2*y)
    
    # Diccionario de las sumatorias
    sumas = [
        ["Σxᵢ", sum_x],
        ["Σyᵢ", sum_y],
        ["Σxᵢ²", sum_x2],
        ["Σxᵢ³", sum_x3],
        ["Σxᵢ⁴", sum_x4],
        ["Σxᵢyᵢ", sum_xy],
        ["Σxᵢ²yᵢ", sum_x2y]
    ]
    
    if mostrar_detalles:
        print("Sumas necesarias:")
        print(tabulate(sumas, headers=["Suma", "Valor"], tablefmt="grid", floatfmt=".4f"))
        print()
    
    # Formar el sistema de ecuaciones normales
    # Para f(x) = ax² + bx + c:
    # Σyᵢ = na + bΣxᵢ + cΣxᵢ²
    # Σxᵢyᵢ = aΣxᵢ + bΣxᵢ² + cΣxᵢ³
    # Σxᵢ²yᵢ = aΣxᵢ² + bΣxᵢ³ + cΣxᵢ⁴
    
    # Matriz de coeficientes A
    A = np.array([
        [n, sum_x, sum_x2],
        [sum_x, sum_x2, sum_x3],
        [sum_x2, sum_x3, sum_x4]
    ])
    
    # Vector de términos independientes b
    b = np.array([sum_y, sum_xy, sum_x2y])
    
    if mostrar_detalles:
        print("Sistema de ecuaciones normales:")
        print("⎡{:8.4f} {:8.4f} {:8.4f}⎤    ⎡c⎤   ⎡{:8.4f}⎤".format(A[0,0], A[0,1], A[0,2], b[0]))
        print("⎢{:8.4f} {:8.4f} {:8.4f}⎥   ⎢b⎥ = ⎢{:8.4f}⎥".format(A[1,0], A[1,1], A[1,2], b[1]))
        print("⎣{:8.4f} {:8.4f} {:8.4f}⎦ ⎣a⎦   ⎣{:8.4f}⎦".format(A[2,0], A[2,1], A[2,2], b[2]))
        print()
    
    # Resolver el sistema usando numpy
    try:
        # Resolver el sistema de ecuaciones normales
        coeficientes = np.linalg.solve(A, b)
        c, b_coef, a = coeficientes
        
        if mostrar_detalles:
            print("Solución del sistema:")
            print(f"c = {c:.6f}")
            print(f"b = {b_coef:.6f}")
            print(f"a = {a:.6f}")
            print()
            print(f"Función aproximada: f(x) = {a:.6f}x² + {b_coef:.6f}x + {c:.6f}")
            
    
    except np.linalg.LinAlgError:
        print("Error: El sistema no tiene solución única")
        return None
    
    # Usar SymPy para expresión simbólica
    x_sym = sp.Symbol('x')
    funcion_aproximada = a*x_sym**2 + b_coef*x_sym + c
    
    # Calcular valores aproximados y errores
    y_aprox = a*x**2 + b_coef*x + c
    errores = y - y_aprox
    errores_cuadrados = errores**2

    return {
        'coeficientes': {'a': a, 'b': b_coef, 'c': c},
        'funcion_sympy': funcion_aproximada,
        'y_aproximado': y_aprox,
        'errores': errores,
        'matriz_coeficientes': A,
        'vector_terminos': b
    }

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo
    x_datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_datos = [1.3, 3.5, 4.2, 5, 7, 8.8, 10.1, 12.5, 13, 15.6]
    
    print("EJEMPLO: Aproximación cuadrática")
    print("Datos:")
    print(f"x = {x_datos}")
    print(f"y = {y_datos}")
    
    # Realizar aproximación
    resultado = aproximacion_minimos_cuadrados_cuadratica(x_datos, y_datos)
            
    print("\nEjemplo de evaluación:")
    x_eval = 2.5
    a, b, c = resultado['coeficientes']['a'], resultado['coeficientes']['b'], resultado['coeficientes']['c']
    y_eval = a*x_eval**2 + b*x_eval + c
    print(f"f({x_eval}) = {y_eval:.6f}")