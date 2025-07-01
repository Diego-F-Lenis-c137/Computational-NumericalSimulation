import sympy as sp
from tabulate import tabulate

def diferencias_divididas():
    x = sp.Symbol('x')

    # Funciones predefinidas
    funciones = {
        "1": sp.sin(x),
        "2": sp.cos(x),
        "3": sp.exp(x),
        "4": x**3 - 2*x + 1,
        "5": 1 / (1 + x**2)
    }

    print("Seleccione la función a interpolar:")
    print("1. sin(x)")
    print("2. cos(x)")
    print("3. e^x")
    print("4. x^3 - 2x + 1")
    print("5. 1 / (1 + x^2)")
    print("6. Ingresar una función personalizada")

    eleccion = input("Ingrese el número de la función: ")

    if eleccion == "6":
        print("\n Guía rápida para ingresar funciones:")
        print(" - Usa 'x' como variable.")
        print(" - Usa ** para potencias (ej. x**2 para x al cuadrado).")
        print(" - Puedes usar funciones como sin(x), cos(x), exp(x), log(x), etc.")
        print(" - Para funciones como 4x^2 + 3x - 5, escribe: 4*x**2 + 3*x - 5")
        print("Ejemplo válido: exp(-x) - x\n")
        funcion_usuario = input("Escribe tu función f(x): ")
        try:
            f = sp.sympify(funcion_usuario)
        except Exception as e:
            print("❌ Función inválida:", str(e))
            return
    elif eleccion in funciones:
        f = funciones[eleccion]
    else:
        print("❌ Opción no válida.")
        return

    f_leiblexd = sp.lambdify(x, f, 'math')

    try:
        n = int(input("Ingrese el número de puntos: "))
        xi = []
        for i in range(n):
            val = float(input(f"Ingrese x{i}: "))
            xi.append(val)
    except Exception as e:
        print("❌ Error en la entrada:", str(e))
        return

    try:
        yi = [f_leiblexd(val) for val in xi]
    except Exception as e:
        print("❌ Error al evaluar la función:", str(e))
        return

    # Crear tabla de diferencias divididas
    dd_tabla = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dd_tabla[i][0] = yi[i]

    for j in range(1, n):
        for i in range(n - j):
            num = dd_tabla[i + 1][j - 1] - dd_tabla[i][j - 1]
            den = xi[i + j] - xi[i]
            dd_tabla[i][j] = num / den

    # Construcción de la tabla para imprimir
    tabla_tabulate = []
    for i in range(n):
        fila = [xi[i], dd_tabla[i][0]]
        for j in range(1, n - i):
            fila.append(dd_tabla[i][j])
        tabla_tabulate.append(fila)

    headers = ["x", "f(x)"] + [f"dd{i}f" for i in range(1, n)]
    print("\n📊 Tabla de Diferencias Divididas:\n")
    print(tabulate(tabla_tabulate, headers=headers, tablefmt="fancy_grid"))

    # Valor de x a evaluar
    try:
        x_eval = float(input("\nIngrese el valor de x para aproximar f(x): "))
    except:
        print(" Entrada inválida para x.")
        return

    if x_eval < min(xi) or x_eval > max(xi):
        print(" ADVERTENCIA: Está realizando una extrapolación fuera del rango de los datos.")

    # Polinomio simbólico
    polinomio = dd_tabla[0][0]
    term = 1
    for i in range(1, n):
        term *= (x - xi[i - 1])
        polinomio += dd_tabla[0][i] * term

    approx = sp.N(polinomio.subs(x, x_eval))
    print(f"\n✅ Aproximación f({x_eval}) ≈ {approx}")

    try:
        real = f_leiblexd(x_eval)
        error = abs(real - approx)
        print(f" Valor real f({x_eval}) = {real}")
        print(f" Error absoluto = {error}")
    except:
        pass

    print("\n Polinomio construido:")
    print(sp.simplify(polinomio))

# Ejecutar función principal
if __name__ == "__main__":
    diferencias_divididas()
