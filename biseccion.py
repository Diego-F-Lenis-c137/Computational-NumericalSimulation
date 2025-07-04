import sympy as sp
import f_inputs as fin

ans = 0
def biseccion():
    print(
        """
        __________.__                           .__               
        \______   \__| ______ ____   ____  ____ |__| ____   ____  
         |    |  _/  |/  ___// __ \_/ ___\/ ___\|  |/  _ \ /    \ 
         |    |   \  |\___ \\\  ___/\  \__\  \___|  (  <_> )   |  \\
         |______  /__/____  >\___  >\___  >___  >__|\____/|___|  /
                \/        \/     \/     \/    \/               \/ 
        """
    )
    print("La tecnica de biseccion permite aproximar la solucion a una ecuacion no lineal \nbasandose en el teorema de valor intermedio, \nse requiere evaluar la ecuacion en un intervalo [a,b] \ntal que uno de estos valores sea positivo y el otro negativo, \nse asume que existira un punto en este intervalo para el que f(x) = 0")
    input("/")
    global fun, x
    x = sp.symbols('x')
    fun = fin.parse_user_input()
    
    print("Para aproximar a una solucion correctamente ingrese un intervalo para evaluar f(x)")
    print(" - <a> debe ser menor que <b>")
    print(" - f(a) * f(b) debe ser < 0")
    
    while(True):
        a = float(input("valor incial 'a' //:"))
        b = float(input("valor final 'b' //:"))
        fa = fun.evalf(subs={x: a})
        print(f"f(a) = {fa}")
        fb = fun.evalf(subs={x: b})
        print(f"f(b) = {fb}")

        if ((fa*fb) < 0):
            print(f"f(a)*f(b) = {fa*fb}")
            print("ok ✔")
            break
        else:
            print("❌ Intervalo inválido, reintentalo")
        
    while(True):
        t = int(input("ingresa una cantidad de decimales para aproximar el resultado //:"))
        if (t.is_integer()):
            break
        else:
            print("Debe ser un entero positivo")
            
    t = 0*(10 ** t)
    midpoint(a, b, t, 50)
    print("la raiz de la expresion es :")
    print(ans)

def midpoint(a, b, t, depth):
    if (depth <= 0):
        c = ((a + b)/2)
        fc =  fun.evalf(subs={x: c})
        global ans
        ans = fc
    else:
        c = ((a + b)/2) 
        print(f"punto medio x: {c}")
        fa =  fun.evalf(subs={x: a})
        fb =  fun.evalf(subs={x: b})
        fc =  fun.evalf(subs={x: c})
        if ((fc*fa)<0):
            midpoint(a, c, t, depth-1)
        elif ((fc*fb) < 0):
            midpoint(c, b, t, depth-1)

biseccion()