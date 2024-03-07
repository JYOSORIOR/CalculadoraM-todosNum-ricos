import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import math

#x = np.linspace(-2,6, 101)
#plt.plot(x, x**2 - 4*x)
#plt.grid()
#plt.show()




#--------------------------------------------------------------------------------------------------------

#FUNCIONES



def borrar():
    funcCampoTexto.delete(0, END)
    extremoIzqText.delete(0, END)
    extremoDerText.delete(0, END)
    numParticionesTexto.delete(0, END)


    extremoIzqSalidaText.config(state=NORMAL)
    extremoIzqSalidaText.delete(0, END)
    extremoIzqSalidaText.config(state='readonly')




def salir(ventana):
    ventana.destroy()


#-------------------------------------------------------------------------------------------------

def determinar_func(func, valor):
    ecuacion = sp.sympify(func)
    simbolo = sp.symbols('x')
    result = ecuacion.evalf(subs={simbolo: float(valor)})
    #print(result)
    return result

def integracionPuntoIzq(func, a, b, n):
    muestras = n + 1

    suma = 0

    h = (b-a) / n

    for i in range(n):
        a += h
        suma += determinar_func(func,a)

        integr = h/2 * (determinar_func(func, a) + 2 * suma + determinar_func(func, b))

    return integr


    print(suma)
    return suma

def graf(func, a, b, n):
    muestras = n + 1
    xi = np.linspace(a, b, muestras)
    fi = determinar_func(func, xi)

    muestraslinea = muestras*10
    xk = np.linspace(a, b, muestraslinea)
    fk = determinar_func(func, xk)

    plt.plot(xi, fi, 'ro')
    plt.plot(xk, fk)

    plt.fill_between(xi, 0, fi, color= 'g')
    for i in range(0, muestras, 1):
        plt.axvline(xi[i], color='w')

    plt.show()

def integracionGeneral():

    func = funcCampoTexto.get()
    a = float(extremoIzqText.get())
    b = float(extremoDerText.get())
    n = int(numParticionesTexto.get())

    puntoIzq = integracionPuntoIzq(func, a, b , n)

    extremoIzqSalidaText.config(state=NORMAL)
    extremoIzqSalidaText.insert(0, puntoIzq)
    extremoIzqSalidaText.config(state=DISABLED)

    graf(func,a,b,n)


#-------------------------------------------------------------------------------------------
def main(ventana):
    #Creación ventana
    ventana = tkinter.Tk()
    ventana.geometry("500x500")
    global funcCampoTexto, extremoIzqText, extremoDerText, numParticionesTexto, extremoIzqSalidaText

    #Título
    integracionLabel = Label(ventana, text="Integración por trapecios", width="40", font=("helvetica", 12, "bold"),
                         padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove").place(x=15, y=12)

    #Declaración de Labels Entrada
    entradaLabel = Label(ventana, text="Entrada", width="15", font=("helvetica", 12, "bold"),
                      padx=5, pady=5, fg="black", borderwidth=2).place(x=15, y= 50)

    funcLabel = Label(ventana, text="Función", width="15", font=("helvetica", 12, "bold"),
                      padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(x=15, y= 90)

    intervaloLabel = Label(ventana, text="Intervalo", width="15", font=("helvetica", 12, "bold"),
                      padx=5, pady=5).place(x=15, y= 125)

    extremoIzqLabel = Label(ventana, text="Extremo Izquierdo", width="15", font=("helvetica", 12, "bold"),
                      padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(x=15, y= 160)
    extremoDerLabel = Label(ventana, text="Extremo Derecho", width="15", font=("helvetica", 12, "bold"),
                      padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(x=15, y= 200)

    numParticionesLabel = Label(ventana, text="Núm de particiones", width="15", font=("helvetica", 12, "bold"),
                      padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(x=15, y= 240)
    #---------------------------------------------------------------------------------------------------------------------------
    #Declaración de Labels Salida
    salidaLabel = Label(ventana, text="Salida", width="15", font=("helvetica", 12, "bold"),
                      padx=5, pady=5, fg="black", borderwidth=2).place(x=15, y= 340)

    integralLabel = Label(ventana, text="Integral", width="15", font=("helvetica", 12, "bold"),
                      padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(x=15, y= 380)

    extremoIzqSalidaLabel = Label(ventana, text="Valor de la integral", width="15", font=("helvetica", 12, "bold"),
                      padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(x=15, y= 420)


    #VARIABLES CAMP TEXTO
    funcVar = tkinter.StringVar()
    extremoIzq = tkinter.DoubleVar()
    extremoDer = tkinter.DoubleVar()
    numParticiones = tkinter.IntVar()

    #ENTRADA
    funcCampoTexto = Entry(ventana, textvariable=funcVar, font=10, width=26)
    funcCampoTexto.place(x=185, y=90)

    extremoIzqText = Entry(ventana, textvariable=extremoIzq, font=10, width=26)
    extremoIzqText.place(x=185, y=160)

    extremoDerText = Entry(ventana, textvariable=extremoDer, font=10, width=26)
    extremoDerText.place(x=185, y=200)

    numParticionesTexto = Entry(ventana, textvariable=numParticiones, font=10, width=26)
    numParticionesTexto.place(x=185, y=240)


    #----------------------------------------------------------------------------------------------------------------------------

    #VARIABLES CAMP TEXTO
    extremoIzqSalida = tkinter.DoubleVar()
    extremoDerSalida = tkinter.DoubleVar()
    puntoMedioSalida = tkinter.DoubleVar()

    #SALIDA
    extremoIzqSalidaText = Entry(ventana, textvariable=extremoIzqSalida, font=10, width=26, state='readonly')
    extremoIzqSalidaText.place(x=185, y=420)
    #BOTONES

    btnCalcular = Button(ventana, text="Calcular", width="10", font=("helvetica", 12, "bold"),
                         bg="LightSkyBlue1", fg="black", command=integracionGeneral)
    btnCalcular.place(x=15, y=300)

    btnBorrar = Button(ventana, text="Borrar", width="10", font=("helvetica", 12, "bold"),
                       bg="LightSkyBlue1", fg="black", command=borrar)
    btnBorrar.place(x=155, y=300)

    btnSalir = Button(ventana, text="Salir", width="10", font=("helvetica", 12, "bold"),
                      bg="LightSkyBlue1", fg="black", command=lambda:salir(ventana))
    btnSalir.place(x=295, y=300)
