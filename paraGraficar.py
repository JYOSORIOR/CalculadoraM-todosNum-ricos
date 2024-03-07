import numpy as np
from numpy import sqrt
from matplotlib import pyplot as plt
def evaluar(funcion, x):
    var2=eval(funcion)
    return var2

lf=["0.5*x*np.exp(-x**2*0.5)+np.cos(3.1415926*np.sqrt(x))"]
#0.5*x*np.exp(-x**2*0.5)+np.cos(3.1415926*np.sqrt(x))
lX=[]
lY=[]
xCP = np.arange(0.001, 20000, 0.01)#paso de 0.01 hasta 20000 desde 0.001 para pos
xCN = np.arange(-20000, 0, 0.01)#paso de 0.01 hasta 20000 desde 0.001 para neg
var = (-20000, 20000, 0.01)# intervalo para coger valores desde -20k hasta 20k
ecuacionEje = 'x*0'
def graficar():

        print('grafico')

        print(lX)
        print(lY)
        for i in range(0, len(lf)):
            print(lf[i])
            plt.plot(var, [evaluar(ecuacionEje, j) for j in var], color='black', label=lf[i])
            plt.plot([evaluar(ecuacionEje, j) for j in var], var, color='black')
            plt.plot(xCN, [evaluar(lf[i], j) for j in xCN], color='black')
            plt.plot(xCP, [evaluar(lf[i], j) for j in xCP], color='black')
        plt.grid()
        plt.legend(loc='upper left')
        plt.xlim(-50, 50)
        plt.ylim(-50, 50)
        plt.show()







graficar()