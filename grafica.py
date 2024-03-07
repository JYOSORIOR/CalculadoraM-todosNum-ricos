import numpy as np
from matplotlib import pyplot as plt
import sympy as sp
import tkinter
from tkinter import *
from sympy import integrate, exp, sin, cos, pi

def salir(ventanita):
    ventanita.destroy()
    import menuPrincipal
    menuPrincipal.main(ventanita)


def borrar():
    funcionesEntrada.delete(1.0, END)

def evaluar(funcion, x):
    evaluada= eval(funcion)
    return evaluada


lX=[]
lY=[]
xCP = np.arange(0.001, 20000, 0.01)#paso de 0.01 hasta 20000 desde 0.001 para pos
xCN = np.arange(-20000, 0, 0.01)#paso de 0.01 hasta 20000 desde 0.001 para neg
var = (-20000, 20000, 0.01)# intervalo para coger valores desde -20k hasta 20k
ecuacionEje = 'x*0'

def graficar():
    funciones = funcionesEntrada.get("1.0", "end-1c")
    lf = guardarListas(funciones)
    print(lf)

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




def guardarListas(msj):
    lista = msj.split(sep='\n')
    lista_final = []
    for x in lista:
        lista_final.append(x)
    print("Lista de funciones: ", lista_final)
    return lista_final

def main(ventanita):
    ventanita.destroy()
    ventanita = Tk()
    ventanita.title("Graficadora")
    ventanita.geometry("680x162")
    global funcionesEntrada
    #Ventana
    # Labels de la parte izquierda
    metodoLabel = Label(ventanita, text="GRAFICADORA", width="63", font=("helvetica", 12, "bold"),
                        padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
    metodoLabel.place(x=15, y=12)

    funcionLabel = Label(ventanita, text="Introduzca las\nfunciones a\ngraficar :", width="10", height="5", font=("helvetica", 11, "bold italic"),
                         padx=5, pady=5, fg="black")
    funcionLabel.place(x=15, y=45)

    #entrys

    funcionesEntrada = Text(ventanita, width=53, height=5, font=("helvetica", 11, "bold italic"), bg="gray91")
    funcionesEntrada.place(x=130, y=50)


    #botones
    btnCalcular = Button(ventanita, text="Graficar", width="8", font=("helvetica", 10, "bold"),
                         bg="LightSkyBlue1", fg="black", command=graficar)
    btnCalcular.place(x=570, y=50)

    btnBorrar = Button(ventanita, text="Borrar", width="8", font=("helvetica", 10, "bold"),
                       bg="LightSkyBlue1", fg="black", command=borrar)
    btnBorrar.place(x=570, y=80)

    btnSalir = Button(ventanita, text="Salir", width="8", font=("helvetica", 10, "bold"),
                      bg="LightSkyBlue1", fg="black",  command=lambda:salir(ventanita))
    btnSalir.place(x=570, y=110)

