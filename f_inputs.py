import sympy as sp

def parse_user_input():
    print("\n Como ingresar funciones:")
    print(" - Usa 'x' como variable.")
    print(" - Usa ** para potencias (ej. x**2 para x al cuadrado).")
    print(" - Escribe \"E\" para usar el numero de euler")
    print(" - Puedes usar funciones como sin(x), cos(x), exp(x), log(x), etc.")
    print(" - Para funciones como 4x^2 + 3x - 5, escribe: 4*x**2 + 3*x - 5")
    print("Ejemplo válido: exp(-x) - x\n")

    funcion_usuario = input("Escribe tu función f(x): ")
    
    #comentar este bloque para inspeccionar el valor de la funcion introducida
    try:
        f = sp.sympify(funcion_usuario)

    except Exception as e:
        print("❌ Función inválida:", str(e))
        return
   
    '''
    #descomentar esto para inspeccionar el valor de la funcion introducida
    try:
        x = sp.symbols('x')
        xeval = int(input("Valor para evaluar x :"))
        func = sp.sympify(funcion_usuario)
        print("Funcion", func)
        solved = func.subs(x, xeval).evalf()
        print("Funcion resuelta: ", solved)

    except Exception as e:
        print("Entrada Invalida: ", str(e))
    '''
    return f
