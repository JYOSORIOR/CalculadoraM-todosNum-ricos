import sympy as sp
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk


def salir(rootinini):
    rootinini.destroy()
    import menuPrincipal
    menuPrincipal.main(rootinini)


def calcular():
    funcion = str(funcionEntry.get())

    numero = float(numeroEntry.get())

    x = sp.symbols('x')
    p_d = sp.diff(funcion, x)
    s_d = sp.diff(funcion, x, 2)
    r_pd = float(sp.diff(funcion, x).evalf(subs={x: numero}))
    r_sd = float(sp.diff(funcion, x, 2).evalf(subs={x: numero}))
    # p_d es primera derivada
    # s_d es Segunda derivada
    # r_pd resultado primera
    # r_sd resultado segunda
    primeraVar.set(str(r_pd))
    segundaVar.set(str(r_sd))



def borrar():
    funcionEntry.delete(0, END)
    numeroEntry.delete(0, END)
    primeraVar.set("")
    segundaVar.set("")


def main(rootinini):
    rootinini.destroy()
    rootinini = Tk()
    # Interfaz gráfica
    rootinini.title("Calculadora de derivadas")
    rootinini.geometry("500x290")
    global funcionEntry, numeroEntry, primeraVar, segundaVar

    # Labels de la parte izquierda
    metodoLabel = Label(rootinini, text="DERIVADAS", width="45", font=("helvetica", 12, "bold"),
                        padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
    metodoLabel.place(x=15, y=12)

    funcionLabel = Label(rootinini, text="Función", width="17", font=("helvetica", 12, "bold"),
                         padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    funcionLabel.place(x=15, y=48)

    x0Label = Label(rootinini, text="Número (xₒ)", width="17", font=("helvetica", 12, "bold"),
                    padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    x0Label.place(x=15, y=80)

    # Solo para mostrar

    primeraDerivadaLabel = Label(rootinini, text="Primera derivada", width="17", font=("helvetica", 12, "bold"),
                                 padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    primeraDerivadaLabel.place(x=15, y=190)

    segundaDerivadaLabel = Label(rootinini, text="Segunda derivada", width="17", font=("helvetica", 12, "bold"),
                                 padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    segundaDerivadaLabel.place(x=15, y=220)

    # Campos de texto
    funcionVar = tkinter.StringVar()
    numeroVar = tkinter.DoubleVar()

    primeraVar = StringVar()
    segundaVar = StringVar()

    funcionEntry = Entry(rootinini, textvariable=funcionVar, font=10, width=30)
    funcionEntry.place(x=200, y=53)

    numeroEntry = Entry(rootinini, textvariable=numeroVar, font=10, width=30)
    numeroEntry.place(x=200, y=83)

    # Solo para mostrar
    primeraDerivadaEntry = Entry(rootinini, textvariable=primeraVar, font=10, width=30, state="readonly")
    primeraDerivadaEntry.place(x=200, y=190)

    segundaDerivadaEntry = Entry(rootinini, textvariable=segundaVar, font=10, width=30, state="readonly")
    segundaDerivadaEntry.place(x=200, y=220)

    # Botones

    btnCalcular = Button(rootinini, text="Calcular", width="10", font=("helvetica", 12, "bold"),
                         bg="LightSkyBlue1", fg="black", command=calcular)
    btnCalcular.place(x=60, y=130)

    btnBorrar = Button(rootinini, text="Borrar", width="10", font=("helvetica", 12, "bold"),
                       bg="LightSkyBlue1", fg="black", command=borrar)
    btnBorrar.place(x=200, y=130)

    btnSalir = Button(rootinini, text="Salir", width="10", font=("helvetica", 12, "bold"),
                      bg="LightSkyBlue1", fg="black", command=lambda:salir(rootinini))
    btnSalir.place(x=340, y=130)

    borrar()

