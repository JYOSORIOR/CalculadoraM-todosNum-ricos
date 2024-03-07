import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import math

import numpy
import numpy as np
from sympy import *



def borrar():
    funcCampoTexto.delete(0, END)
    gradoCampoTexto.config(state=NORMAL)
    gradoCampoTexto.delete(0, END)
    gradoCampoTexto.config(state=DISABLED)
    tablaD.delete(*tablaD.get_children())
    datosTabla.clear()


def salir(ventana):
    ventana.destroy()


def insert_asterisks(equation):
    return equation.replace('x', '*x')


def separarTerminos(polinomio:str) -> []:

    # quitar los space
    polinomio = polinomio.replace(' ','')

    terminoActual = ''
    terminos = []
    numeroParentesis = 0

    # Por cada caracter en polinomio
    for i in range(len(polinomio)):
        caracterActual = polinomio[i]

        # El primero caracter, siempre se agrega a terminoActual
        if i == 0:
            terminoActual = terminoActual + caracterActual

        # El ultimo caracter
        elif i == len(polinomio) - 1:
            terminoActual = terminoActual + caracterActual
            terminos.append(terminoActual)

        # Otros caracteres
        else:

            # Si se encuentra parentesis, actualizamos el valor de numeroParentesis
            if caracterActual == '(':
                numeroParentesis += 1
                terminoActual = terminoActual + caracterActual
            elif caracterActual == ')':
                numeroParentesis -= 1
                terminoActual = terminoActual + caracterActual

            # Si se encuentra operador '+' o '-'
            elif caracterActual == '+' or caracterActual == '-':

                # Si estamos dentro de parentesis
                if numeroParentesis > 0:
                    terminoActual = terminoActual + caracterActual

                # Si estamos fuera de parentesis, crea un nuevo termino
                else:
                    terminos.append(terminoActual)
                    terminoActual = caracterActual

            # Otros caracteres
            else:
                terminoActual = terminoActual + caracterActual

    return terminos

def encontrarX(termino):
    status = False
    pos = 0
    for i in range(len(termino)):
        if termino[i] == 'x':
            print(termino)
            pos = i
            print(pos)
            status == True
            return pos

    if status == False:
        return False


    #coef = termino[:pos-1]
    #print("COEFICIENTE")
    #print(coef)

    #grado = termino[pos-len(termino)+3:]
    #print("GRADO")
    #print(grado)

def extractorCoeficientes(funcion):
    coeficientes = funcion.all_coeffs()
    return coeficientes

def newtonHorner(grado, xo, poli):
    ite = 0
    tol =  1e-20
    e = 100
    nr = grado
    aux1 = (poli)
    aux2 = (poli)
    j = 1
    r = grado

    for k in range(nr):
        aux1 = (aux2)
        aux2 = ([1]*r)

        aux1[0]=float(poli[0])
        aux2[0]=float(poli[0])

        while e > tol:
            y=float(aux1[0])
            z=float(aux1[0])
            i=1
            while i<r:
                y=((float(xo)*y)+aux1[i])
                aux2[j]=y
                j+=1
                z=(float(xo)*z)+y
                i+=1
            y=(float(xo)*y)+aux1[-1]
            xnuevo=float(xo)-(y/z)
            e = abs((xnuevo-float(xo)))
            xo = xnuevo
            ite+=1
            j=1

        r-=1
        print("La raíz ", k+1, " es: ", xo)
        print("Las iteraciones fueron: ", ite)

        paraLaTabla(xo, ite, "Real")
        e=100
        ite=0


def newtonHornerRoots(poli):
    raices = np.roots(poli)
    print("RAÍCES ROOTS")
    print(raices)

    for i in raices:
        if np.iscomplex(i) == False:
            paraLaTabla(i,  0, "Real")
        elif np.iscomplex(i) == True:
            paraLaTabla(i, 0, "Complejo")


def paraLaTabla(raiz, iteracion, tipo):
    datosTabla.append((raiz, iteracion, tipo))

def tabla():
    for dato in datosTabla:
        tablaD.insert('', tkinter.END, values=dato)

def calcular():
    x,a  = symbols("x,a")

    func = Poly(funcCampoTexto.get())

    expr = 3 + x + x**2 + a*x*2

    #funcion = Poly(expr,x)
    grado= degree(func)

    gradoCampoTexto.config(state=NORMAL)
    gradoCampoTexto.insert(0, grado)
    gradoCampoTexto.config(state=DISABLED)

    print("------------------------------------------")
    #EXTRAER LOS COEFICIENTES EN ORDEN
    coeficientes = extractorCoeficientes(func)
    print(extractorCoeficientes(func))

    #SE EJECUTA EL MÉTODO DE NEWTON - HORNER
    newtonHornerRoots(coeficientes)
    tabla()

def main(ventana):
    #Creación ventana
    ventana = tkinter.Tk()
    ventana.geometry("700x500")

    global funcCampoTexto, gradoCampoTexto, tablaD, datosTabla
    #Título
    metodoLabel = Label(ventana, text="Calculadora de Polinomios", width="40", font=("helvetica", 12, "bold"),
                         padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove").place(x=15, y=12)


    #Declaración de Labels Izquierda
    funcLabel = Label(ventana, text="Ecuación", width="15", font=("helvetica", 12, "bold"),
                      padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(x=15, y= 60)



    gradoLabel = Label(ventana, text="Grado de la función", width="15", font=("helvetica", 12, "bold"),
                      padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(x=15, y= 200)


    #VARIABLES CAMP TEXTO
    funcVar = tkinter.StringVar()
    gradoVar = tkinter.StringVar()



    #ENTRADA
    funcCampoTexto = Entry(ventana, textvariable=funcVar, font=10, width=26)
    funcCampoTexto.place(x=185, y=64)




    #SALIDA
    gradoCampoTexto = Entry(ventana, textvariable=gradoVar, font=10, width=26, state= DISABLED)

    gradoCampoTexto.place(x=185, y=205)


    #2 COMPLEJAS 1 REAL 3*x**3-2

    #BOTONES 1*x**3+7*x**2-6*x-72

    btnCalcular = Button(ventana, text="Calcular", width="8", font=("helvetica", 12, "bold"),
                         bg="LightSkyBlue1", fg="black", command=calcular)
    btnCalcular.place(x=50, y=150)

    btnBorrar = Button(ventana, text="Borrar", width="8", font=("helvetica", 12, "bold"),
                       bg="LightSkyBlue1", fg="black", command=borrar)

    btnBorrar.place(x=190, y=150)

    btnSalir = Button(ventana, text="Salir", width="8", font=("helvetica", 12, "bold"),
                      bg="LightSkyBlue1", fg="black",command=lambda:salir(ventana))
    btnSalir.place(x=330, y=150)



    #Tabla

    #Para la tabla
    columns = ('Raíces', 'Iteraciones', 'Tipo')

    tablaD = ttk.Treeview(ventana, columns=columns, show='headings')

    tablaD.heading('Raíces', text='Raíces')
    tablaD.heading('Iteraciones', text='Iteraciones')
    tablaD.heading('Tipo', text='Tipo')
    datosTabla = []

    #tablaD.grid(padx=0, pady= 5, row=4, column=1)

    scrollbar = ttk.Scrollbar(ventana, orient=tkinter.VERTICAL, command=tablaD.yview)
    tablaD.configure(yscroll=scrollbar.set)
    tablaD.place(x=25, y=260)
    scrollbar.place(x=628,y=261)
