import sympy as sp
import f_inputs as fin

import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

def minimos_cuadrados(x, y, n):
    sum_x = np.sum(x)
    print(sum_x)
    sum_y = np.sum(y)
    print(sum_y)
    sum_xy = 0
    sum_x2 = 0
    for i in range(n):
        sum_xy = sum_xy + (x[i] * y[i])
        sum_x2 = sum_x2 + (x[i] ** 2)

    m = ((n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)) 
    b = (sum_y - m * sum_x) / n

    return m, b

def main():
    n = int(input("Ingrese el número de puntos: "))
    x = np.zeros(n)
    y = np.zeros(n)

    for i in range(n):
        x[i], y[i] = map(float, input(f"Ingrese el punto {i+1} (x y): ").split(sep=","))

    m, b = minimos_cuadrados(x, y, n)

    print("Ecuación de la recta:")
    print(f"y = {m:.4f}x + {b:.4f}")

    print("Puntos y valores ajustados:")
    y_ajustados = np.zeros(n)
    for i in range(n):

        y_ajustados[i] = (m * x[i]) + b
    
    print(tabulate(list(zip(x, y, y_ajustados)), headers=["x", "y", "y ajustado"], tablefmt="fancy_grid"))

    plt.scatter(x, y, label="Puntos")
    plt.plot(x, y_ajustados, label=f"y = {m:.4f}x + {b:.4f}", color="red")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    '''n = int(input("Ingrese el número de puntos: "))
    x = []
    y = []
    for i in range(n):
        point = input(f"Ingrese el punto {i+1} (x y): ")
        x_val, y_val = map(float, point.split( sep=","))
        x.append(x_val)
        y.append(y_val)

    m, b = minimos_cuadrados(x, y, n)'''

    print(
    '''
       _____  .__                   /\  ________  
      /     \ |__| ____            /  \ \_____  \ 
     /  \ /  \|  |/    \   ______  \/\/  /  ____/ 
    /    Y    \  |   |  \ /_____/       /       \ 
    \____|__  /__|___|  /               \_______ \\
            \/        \/                        \/
    .____    .__                     .__          
    |    |   |__| ____   ____ _____  |  |         
    |    |   |  |/    \_/ __ \\\__  \ |  |         
    |    |___|  |   |  \  ___/ / __ \|  |__       
    |_______ \__|___|  /\___  >____  /____/       
            \/       \/     \/     \/             
    ''')
    print("El método de mínimos cuadrados lineal es una técnica estadística \nque busca encontrar la línea recta que mejor se ajusta a un conjunto de datos, \nminimizando la suma de los cuadrados de las diferencias entre puntos ")
    main()