import sympy as sp

def Polinomio_Taylor():
    # Declaramos símbolo
    x = sp.symbols('x')

    # Funciones disponibles
    funciones_disponibles = {
        "1": sp.sin(x),
        "2": sp.cos(x),
        "3": sp.exp(x),
        "4": sp.ln(1 + x),
        "5": 1 / (1 - x)
    }

    # Mostrar opciones
    print("Seleccione la función:")
    print("1. sin(x)")
    print("2. cos(x)")
    print("3. e^x")
    print("4. ln(1 + x)")
    print("5. 1 / (1 - x)")

    # Entrada del usuario
    eleccion = input("Ingrese el número de la función: ")
    if eleccion not in funciones_disponibles:
        print("Opción no válida.")
        return

    f = funciones_disponibles[eleccion]
    x0 = float(input("Ingrese el valor de x0: "))
    n = int(input("Ingrese el orden del polinomio de Taylor (ej. 5): "))

    # Calcular el polinomio de Taylor
    polinomio_de_taylor = 0
    for i in range(n + 1):
        derivada = f.diff(x, i)
        termino_aux = (derivada.subs(x, x0) / sp.factorial(i)) * (x - x0)**i
        polinomio_de_taylor += termino_aux

    print("\nPolinomio de Taylor de orden", n, "alrededor de x0 =", x0, ":")
    print(sp.simplify(polinomio_de_taylor))

    # Evaluación en un punto
    x_eval = float(input("\nIngrese el valor de x en el que desea evaluar la función y el polinomio: "))

    # Evaluar función real y polinomio
    f_real = f.subs(x, x_eval).evalf()
    taylor_val = polinomio_de_taylor.subs(x, x_eval).evalf()
    error_abs = abs(f_real - taylor_val)

    print(f"\nValor real f({x_eval}) = {f_real}")
    print(f"Valor del polinomio de Taylor T({x_eval}) = {taylor_val}")
    print(f"Error absoluto = {error_abs}")

# Ejecutar la función
Polinomio_Taylor()
