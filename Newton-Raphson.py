import sympy as sp
from tabulate import tabulate

def newton_raphson():
    x = sp.symbols('x')

    # Funciones disponibles (ahora con opción 6 para función personalizada)
    functions = {
        "1": sp.sin(x),
        "2": sp.cos(x),
        "3": sp.exp(x),
        "4": sp.exp(-x) - x,
        "5": x**2 - 2
    }

    print("Seleccione la función para encontrar la raíz:")
    print("1. sin(x)")
    print("2. cos(x)")
    print("3. e^x")
    print("4. e^(-x) - x")
    print("5. x^2 - 2")
    print("6. Ingresar una función personalizada")

    choice = input("Ingrese el número de la función: ")

    # Función personalizada
    if choice == "6":
        print("\n Guía rápida para ingresar funciones:")
        print(" - Usa 'x' como variable.")
        print(" - Usa ** para potencias (ej. x**2 para x al cuadrado).")
        print(" - Puedes usar funciones como sin(x), cos(x), exp(x), log(x), etc.")
        print(" - Para funciones como 4x^2 + 3x - 5, escribe: 4*x**2 + 3*x - 5")
        print("Ejemplo válido: exp(-x) - x\n")

        user_input = input("Escribe tu función f(x): ")
        try:
            f = sp.sympify(user_input)
        except Exception as e:
            print(" Función inválida:", str(e))
            return
    elif choice in functions:
        f = functions[choice]
    else:
        print(" Opción no válida.")
        return

    f_prime = sp.diff(f, x)

    f_lamb = sp.lambdify(x, f, 'math')
    f_prime_lamb = sp.lambdify(x, f_prime, 'math')

    x0 = float(input("Ingrese el valor inicial x0: "))
    tol = float(input("Ingrese la tolerancia (ej. 1e-6): "))
    max_iter = int(input("Ingrese el número máximo de iteraciones: "))

    iter_count = 0
    tabla = []

    while iter_count < max_iter:
        try:
            fx = f_lamb(x0)
            dfx = f_prime_lamb(x0)
            if dfx == 0:
                print("La derivada es cero.")
                return

            x1 = x0 - fx / dfx
            error = abs(x1 - x0)

            tabla.append([
                iter_count + 1,
                f"{x1:.10f}",
                f"{f_lamb(x1):.10f}",
                f"{error:.10f}"
            ])

            if error < tol:
                break

            x0 = x1
            iter_count += 1

        except Exception as e:
            print(f"Error en la iteración {iter_count + 1}: {e}")
            return

    print("\n Resultados de la iteración (Newton-Raphson):\n")
    print(tabulate(tabla, headers=["Iteración", "Valor de X", "Fx", "Error"], tablefmt="fancy_grid"))

    if error < tol:
        print(f"\n Raíz aproximada encontrada: x = {x1}")
        print(f" Total de iteraciones: {iter_count + 1}")
    else:
        print("\n Se alcanzó el número máximo de iteraciones sin alcanzar la tolerancia.")

if __name__ == "__main__":
    newton_raphson()