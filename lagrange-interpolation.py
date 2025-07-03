import sympy as sp


lagrange_pol = 0
point_count = 0
points : list = list()

def get_points_and_pol():
    global lagrange_pol, points
    lagrange_pol = 0
    x = sp.symbols("x")

    while(True):
        print("Ingrese el numero de puntos del polinomio de lagranje")
        point_count = int(input(": "))
        if point_count < 2 : 
            print("No puedes ingresar menos de 2 puntos")
            continue
        print("Ahora ingrese los puntos")
        for i in range(0, point_count):
            xp = int(input(f"Ingrese x_{i}: "))
            yp = int(input(f"Ingrese y_{i}: "))
            points.append((xp,yp))
        print(points)

        for k in range(0, point_count) :
            l = 1
            for j in range(0, point_count) :
                if k == j: continue 
                l = l * ((x - points[j][0])/(points[k][0] - points[j][0])) 
            lagrange_pol += l*points[k][1]
        break

def show_pol():
    print()
    print("El polinomio de lagrange es :")
    sp.pprint(sp.simplify(lagrange_pol), use_unicode=True)
    print()

def test_vals():
    while (True):
        value = int(input("Ingrese el valor de x: "))
        x = sp.Symbol("x")
        print(f"f({value}) = {lagrange_pol.subs(x, value)}")

def menu():
    while (True):
        print("1- Ingresar puntos para interpolar")
        print("2- Ver polinomio de lagrange")
        print("3- Probar valores en la funcion actual")
        print("0- salir")
        print()
        ans = int(input(": "))
        if (ans < 0 or ans > 3):
            print("Valor incorrecto")
            continue
        if ans == 1:
            get_points_and_pol()
        elif (ans == 2):
            show_pol()
        elif (ans == 3):
            test_vals()



if __name__ == "__main__":
    menu()

