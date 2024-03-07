import sympy as sp
import tkinter
from tkinter import *
import numpy as np
import sympy as sym
from tkinter import ttk, messagebox
import tkinter as tk

# 0.377358490566038*x + 0.424528301886792 -----F
# cc ----- r
valorescc=[]
valoresexp=[]
text_var = []
entries = []
#7 1 10 5 4 3 13 10 2 x
#2 9 2 5 7 11 2 5 14 y
#[[7 1 10 5 4 3 13 10 2] [2 9 2 5 7 11 2 5 14]]
def salir(root):
    root.destroy()
    import menuPrincipal
    menuPrincipal.main(root)

def calcular():
    matriz=convertirMatriz()
    aX = np.array(matriz[0])
    aY = np.array(matriz[1])
    n= int(puntosEntry.get())
    sets = ['gradoDosVar', 'gradoTresVar', 'gradoCuatroVar', 'gradoCincoVar', 'gradoSeisVar']
    gr1= grUno(aX, aY, n )
    gradoUnoo = gradoUno(aX, aY, n)
    expCC(aX, aY, n)
    print(valorescc)
    gradoUnoVar.set(gradoUnoo)
    gradoDosVar.set(valoresexp[0])
    gradoTresVar.set(valoresexp[1])
    gradoCuatroVar.set(valoresexp[2])
    gradoCincoVar.set(valoresexp[3])
    gradoSeisVar.set(valoresexp[4])
    ccG1Var.set(gr1)
    ccG2Var.set(valorescc[0])
    ccG3Var.set(valorescc[1])
    ccG4Var.set(valorescc[2])
    ccG5Var.set(valorescc[3])
    ccG6Var.set(valorescc[4])




def grUno(xi, yi, n):
    xi = np.array(xi, dtype=float)
    yi = np.array(yi, dtype=float)
    xm = np.mean(xi)
    ym = np.mean(yi)
    sx = np.sum(xi)
    sy = np.sum(yi)
    sxy = np.sum(xi * yi)
    sx2 = np.sum(xi ** 2)
    sy2 = np.sum(yi ** 2)
    a1 = (n * sxy - sx * sy) / (n * sx2 - sx ** 2)
    a0 = ym - a1 * xm
    x = sym.Symbol('x')
    f = a0 + a1 * x
    fx = sym.lambdify(x, f)
    fi = fx(xi)
    numerador = n * sxy - sx * sy
    raiz1 = np.sqrt(n * sx2 - sx ** 2)
    raiz2 = np.sqrt(n * sy2 - sy ** 2)
    r = numerador / (raiz1 * raiz2)
    r2 = r ** 2
    return r

def gradoUno(xi, yi, n):
    xi = np.array(xi, dtype=float)
    yi = np.array(yi, dtype=float)
    xm = np.mean(xi)
    ym = np.mean(yi)
    sx = np.sum(xi)
    sy = np.sum(yi)
    sxy = np.sum(xi * yi)
    sx2 = np.sum(xi ** 2)
    sy2 = np.sum(yi ** 2)
    a1 = (n * sxy - sx * sy) / (n * sx2 - sx ** 2)
    a0 = ym - a1 * xm
    x = sym.Symbol('x')
    f = a0 + a1 * x
    fx = sym.lambdify(x, f)
    fi = fx(xi)
    numerador = n * sxy - sx * sy
    raiz1 = np.sqrt(n * sx2 - sx ** 2)
    raiz2 = np.sqrt(n * sy2 - sy ** 2)
    r = numerador / (raiz1 * raiz2)
    r2 = r ** 2
    print(f)
    return f

def expCC(xi, yi, n):
    for m in [2, 3, 4, 5, 6]:
        xi = np.array(xi)
        yi = np.array(yi)
        k = m + 1
        A = np.zeros(shape=(k, k), dtype=float)
        B = np.zeros(k, dtype=float)
        for i in range(0, k, 1):
            for j in range(0, i + 1, 1):
                coeficiente = np.sum(xi ** (i + j))
                A[i, j] = coeficiente
                A[j, i] = coeficiente
            B[i] = np.sum(yi * (xi ** i))
        C = np.linalg.solve(A, B)
        x = sym.Symbol('x')
        f = 0
        fetiq = 0
        for i in range(0, k, 1):
            f = f + C[i] * (x ** i)
            fetiq = fetiq + np.around(C[i], 4) * (x ** i)

        fx = sym.lambdify(x, f)
        fi = fx(xi)
        ym = np.mean(yi)
        xm = np.mean(xi)
        errado = fi - yi
        sr = np.sum((yi - fi) ** 2)
        st = np.sum((yi - ym) ** 2)
        r = (st - sr) / st
        valoresexp.append(f)
        valorescc.append(r)
    print(valoresexp)
    return f


def convertirMatriz():
    filas = 2
    columna = int(puntosEntry.get())

    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columna):
            matriz[i].append(float(text_var[i][j].get()))
            print(text_var[i][j].get())
    return matriz

def borrar():
    puntosEntry.delete(0, END)
    numeroEntry.delete(0, END)
    text_var.clear()
    entries.clear()
    ajusteVar.set("")
    gradoUnoVar.set("")
    gradoDosVar.set("")
    gradoTresVar.set("")
    gradoCuatroVar.set("")
    gradoCincoVar.set("")
    gradoSeisVar.set("")



def crearBoxes(root):
    x2 = 0
    y2 = 0
    filas = 2
    columna = int(puntosEntry.get())
    for i in range(filas):
        # append an empty list to your two arrays
        # so you can append to those later
        text_var.append([])
        entries.append([])
        for j in range(columna):
            # append your StringVar and Entry
            text_var[i].append(StringVar())
            entries[i].append(Entry(root, textvariable=text_var[i][j], width=4))
            entries[i][j].place(x=68 + x2, y=102 + y2)
            x2 += 30
        y2 += 30
        x2 = 0


# Interfaz gráfica
def main(root):
    root.destroy()
    root = Tk()
    root.title("Ajuste por mínimos cuadrados")
    root.geometry("1350x600")

    # Labels de la parte izquierda
    metodoLabel = Label(root, text="Ajuste de curvas por mínimos cuadrados", width="110", font=("helvetica", 14, "bold"),
                        padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
    metodoLabel.place(x=15, y=12)

    puntosLabel = Label(root, text="Número de puntos", width="15", font=("helvetica", 12, "bold"),
                         padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    puntosLabel.place(x=15, y=52)

    x_Label = Label(root, text="x", width="2", font=("helvetica", 12, "bold"),
                    padx=2, pady=2, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    x_Label.place(x=25, y=98)

    y_Label = Label(root, text="y", width="2", font=("helvetica", 12, "bold"),
                    padx=2, pady=2, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    y_Label.place(x=25, y=128)

    # Solo para mostrar


    gradoUnoLabel = Label(root, text="Grado Uno", width="17", font=("helvetica", 12, "bold"),
                                 padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    gradoUnoLabel.place(x=15, y=290)

    gradoDosLabel = Label(root, text="Grado Dos", width="17", font=("helvetica", 12, "bold"),
                                 padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    gradoDosLabel.place(x=15, y=330)

    gradoTresLabel = Label(root, text="Grado Tres", width="17", font=("helvetica", 12, "bold"),
                                 padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    gradoTresLabel.place(x=15, y=370)

    gradoCuatroLabel = Label(root, text="Grado Cuatro", width="17", font=("helvetica", 12, "bold"),
                                 padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    gradoCuatroLabel.place(x=15, y=410)

    gradoCincoLabel = Label(root, text="Grado Cinco", width="17", font=("helvetica", 12, "bold"),
                                 padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    gradoCincoLabel.place(x=15, y=450)

    gradoSeisLabel = Label(root, text="Grado Seis", width="17", font=("helvetica", 12, "bold"),
                                 padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    gradoSeisLabel.place(x=15, y=490)



    #Label de CC

    ccG1Label = Label(root, text="CC", width="2", font=("helvetica", 7, "bold"),
                                 padx=4, pady=4, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    ccG1Label.place(x=1067, y=292)

    ccG2Label = Label(root, text="CC", width="2", font=("helvetica", 7, "bold"),
                                 padx=4, pady=4, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    ccG2Label.place(x=1067, y=332)

    ccG3Label = Label(root, text="CC", width="2", font=("helvetica", 7, "bold"),
                                 padx=4, pady=4, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    ccG3Label.place(x=1067, y=372)

    ccG4Label = Label(root, text="CC", width="2", font=("helvetica", 7, "bold"),
                                 padx=4, pady=4, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    ccG4Label.place(x=1067, y=412)

    ccG5Label = Label(root, text="CC", width="2", font=("helvetica", 7, "bold"),
                                 padx=4, pady=4, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    ccG5Label.place(x=1067, y=452)

    ccG6Label = Label(root, text="CC", width="2", font=("helvetica", 7, "bold"),
                                 padx=4, pady=4, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    ccG6Label.place(x=1067, y=492)
    global ccG1Var, ccG2Var,ccG3Var, ccG4Var, ccG5Var, ccG6Var,puntosEntry, numeroEntry, ajusteVar, gradoUnoVar, gradoDosVar, gradoTresVar, gradoCuatroVar, gradoCincoVar, gradoSeisVar
    # Campos de texto
    cantPuntosVar = tkinter.IntVar()
    numeroVar = tkinter.DoubleVar()

    ajusteVar = StringVar()
    gradoUnoVar = StringVar()
    gradoDosVar = StringVar()
    gradoTresVar = StringVar()
    gradoCuatroVar = StringVar()
    gradoCincoVar = StringVar()
    gradoSeisVar = StringVar()

    ccG1Var= StringVar()
    ccG2Var= StringVar()
    ccG3Var= StringVar()
    ccG4Var= StringVar()
    ccG5Var= StringVar()
    ccG6Var= StringVar()



    puntosEntry = Entry(root, textvariable=cantPuntosVar, font=10, width=30)
    puntosEntry.place(x=180, y=56)



    # Solo para mostrar

    gradoUnoEntry = Entry(root, textvariable=gradoUnoVar, font=10, width=95, state="readonly")
    gradoUnoEntry.place(x=200, y=293)

    gradoDosEntry = Entry(root, textvariable=gradoDosVar, font=10, width=95, state="readonly")
    gradoDosEntry.place(x=200, y=333)

    gradoTresEntry = Entry(root, textvariable=gradoTresVar, font=10, width=95, state="readonly")
    gradoTresEntry.place(x=200, y=373)

    gradoCuatroEntry = Entry(root, textvariable=gradoCuatroVar, font=10, width=95, state="readonly")
    gradoCuatroEntry.place(x=200, y=413)

    gradoCincoEntry = Entry(root, textvariable=gradoCincoVar, font=10, width=95, state="readonly")
    gradoCincoEntry.place(x=200, y=453)

    gradoSeisEntry = Entry(root, textvariable=gradoSeisVar, font=10, width=95, state="readonly")
    gradoSeisEntry.place(x=200, y=493)


    #solo para mostrar cc

    ccG1Entry = Entry(root, textvariable=ccG1Var, font=10, width=25, state="readonly")
    ccG1Entry.place(x=1092, y=292)

    ccG2Entry = Entry(root, textvariable=ccG2Var, font=10, width=25, state="readonly")
    ccG2Entry.place(x=1092, y=332)

    ccG3Entry = Entry(root, textvariable=ccG3Var, font=10, width=25, state="readonly")
    ccG3Entry.place(x=1092, y=372)

    ccG4Entry = Entry(root, textvariable=ccG4Var, font=10, width=25, state="readonly")
    ccG4Entry.place(x=1092, y=412)

    ccG5Entry = Entry(root, textvariable=ccG5Var, font=10, width=25, state="readonly")
    ccG5Entry.place(x=1092, y=452)

    ccG6Entry = Entry(root, textvariable=ccG6Var, font=10, width=25, state="readonly")
    ccG6Entry.place(x=1092, y=492)

    # Botones

    btnCalcular = Button(root, text="Calcular", width="10", font=("helvetica", 12, "bold"),
                         bg="LightSkyBlue1", fg="black", command=calcular)
    btnCalcular.place(x=450, y=215)

    btnBorrar = Button(root, text="Borrar", width="10", font=("helvetica", 12, "bold"),
                       bg="LightSkyBlue1", fg="black", command=borrar)
    btnBorrar.place(x=650, y=215)

    btnSalir = Button(root, text="Salir", width="10", font=("helvetica", 12, "bold"),
                      bg="LightSkyBlue1", fg="black", command=lambda:salir(root))
    btnSalir.place(x=850, y=215)



    btnOK = Button(root, text="OK", width="3", font=("helvetica", 8, "bold"),
                      bg="LightSkyBlue1", fg="black", command=lambda:crearBoxes(root))
    btnOK.place(x=460, y=54)

    borrar()