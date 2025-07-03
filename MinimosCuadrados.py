import numpy as np
import sympy as sp
from tabulate import tabulate
import matplotlib.pyplot as plt

def aproximacion_minimos_cuadrados_cuadratica(x_data, y_data, mostrar_detalles=True):
    """
    Realiza aproximación por mínimos cuadrados para función cuadrática f(x) = ax² + bx + c
    
    Parámetros:
    x_data: array de valores x
    y_data: array de valores y
    mostrar_detalles: bool, si mostrar el proceso paso a paso
    
    Retorna:
    dict con coeficientes, función aproximada y estadísticas
    """
    
    # Convertir a arrays de numpy
    x = np.array(x_data)
    y = np.array(y_data) 
    n = len(x)
    
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
    
    headers = ["i", "xᵢ", "yᵢ", "xᵢ²", "xᵢ³", "xᵢ⁴", "xᵢyᵢ", "xᵢ²yᵢ"]
    
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
        print("⎡{:8.4f} {:8.4f} {:8.4f}⎤ ⎡c⎤   ⎡{:8.4f}⎤".format(A[0,0], A[0,1], A[0,2], b[0]))
        print("⎢{:8.4f} {:8.4f} {:8.4f}⎥ ⎢b⎥ = ⎢{:8.4f}⎥".format(A[1,0], A[1,1], A[1,2], b[1]))
        print("⎣{:8.4f} {:8.4f} {:8.4f}⎦ ⎣a⎦   ⎣{:8.4f}⎦".format(A[2,0], A[2,1], A[2,2], b[2]))
        print()
    
    # Resolver el sistema usando numpy
    try:
        coeficientes = np.linalg.solve(A, b)
        c, b_coef, a = coeficientes
        
        if mostrar_detalles:
            print("Solución del sistema:")
            print(f"c = {c:.6f}")
            print(f"b = {b_coef:.6f}")
            print(f"a = {a:.6f}")
            print()
            print(f"Función aproximada: f(x) = {a:.6f}x² + {b_coef:.6f}x + {c:.6f}")
            print()
    
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
    
    # Tabla de resultados
    tabla_resultados = []
    for i in range(n):
        tabla_resultados.append([
            i+1, x[i], y[i], y_aprox[i], errores[i], errores_cuadrados[i]
        ])
    
    if mostrar_detalles:
        print("Tabla de resultados:")
        headers_res = ["i", "xᵢ", "yᵢ", "f(xᵢ)", "Error", "Error²"]
        print(tabulate(tabla_resultados, headers=headers_res, tablefmt="grid", floatfmt=".6f"))
        print()
    
    # Calcular estadísticas del error
    error_cuadratico_medio = np.sqrt(np.mean(errores_cuadrados))
    suma_errores_cuadrados = np.sum(errores_cuadrados)
    
    # Calcular coeficiente de determinación R²
    y_media = np.mean(y)
    ss_tot = np.sum((y - y_media)**2)
    ss_res = np.sum((y - y_aprox)**2)
    r_squared = 1 - (ss_res / ss_tot)
    
    return {
        'coeficientes': {'a': a, 'b': b_coef, 'c': c},
        'funcion_sympy': funcion_aproximada,
        'y_aproximado': y_aprox,
        'errores': errores,
        'error_cuadratico_medio': error_cuadratico_medio,
        'suma_errores_cuadrados': suma_errores_cuadrados,
        'r_squared': r_squared,
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
    print()
    
    # Realizar aproximación
    resultado = aproximacion_minimos_cuadrados_cuadratica(x_datos, y_datos)
    
    if resultado:
        print("\n" + "="*60)
        print("EXPRESIÓN SIMBÓLICA CON SYMPY:")
        print("="*60)
        print(f"f(x) = {resultado['funcion_sympy']}")
        
        # Graficar (descomenta si tienes matplotlib instalado)
        # graficar_aproximacion(x_datos, y_datos, resultado)
        
        print("\nEjemplo de evaluación:")
        x_eval = 2.5
        a, b, c = resultado['coeficientes']['a'], resultado['coeficientes']['b'], resultado['coeficientes']['c']
        y_eval = a*x_eval**2 + b*x_eval + c
        print(f"f({x_eval}) = {y_eval:.6f}")