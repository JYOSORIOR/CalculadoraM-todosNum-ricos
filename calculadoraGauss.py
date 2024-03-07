import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import numpy as np

"""-2 -1 2
1 1 1
-1 4 1

4,3,2"""


def salir(cuadro):
    cuadro.destroy()
    import menuPrincipal
    menuPrincipal.main(cuadro)

def borrar():
    MatrizEntrada.delete(1.0, END)
    vectorV.set("")
    resulUnoVar.set("")
    resulDosVar.set("")
    resulTresVar.set("")
    resulCuatroVar.set("")


def ordenar_2(msj):
    lista = msj.split(sep='\n')
    lista_final = []
    for x in lista:
        lista_final.append(x)
    print("Lista 1: ", lista_final)
    return lista_final


def to_matriz(msj):
    mat = []
    for x in msj:
        fila = x.split(sep=' ')
        mat.append(fila)
    return mat


def to_float(msj):
    mat = []
    aux = []
    for x in msj:
        for y in x:
            aux.append(float(y))
        mat.append(aux.copy())
        aux.clear()
    return mat


def saberDeCuantoPorCuantoEs(matriz):
    aux = 0
    filas = len(matriz)
    for i in range(0, len(matriz)):
        if aux < len(matriz[i]):
            aux = len(matriz[i])

    return aux, filas


def rellenarLosEspacios(matriz):
    numerosFaltan, filas = saberDeCuantoPorCuantoEs(matriz)
    for i in range(0, len(matriz)):
        if numerosFaltan > len(matriz[i]):
            matriz[i].append(0)
    return matriz


def solucionar_ecuacion_lineal(mat, b):
    a = np.array(mat)
    v_sol = np.array(b)
    x = np.linalg.solve(a, v_sol)
    final = retornar_impresion_ecu_lineal(x)
    print(final)
    print(len(final))
    return final


def retornar_impresion_ecu_lineal(arreglo):
    msj = []
    for x in range(len(arreglo)):
        msj.append(str(arreglo[x]))
    return msj


def delimitaComas(msj):
    msj1 = msj.split(sep='\n')
    lista_final = []
    for x in msj1:
        lista_final.append(float(x))
    return lista_final


def resolver_ecu_lineales():
    vectorSolucion = vectorEntrada.get("1.0", "end-1c")
    matriz = delimitaCuadros()
    m = ordenar_2(matriz)
    a = to_matriz(m)
    print(a)
    t = to_float(a)
    mat = rellenarLosEspacios(t)
    b = delimitaComas(vectorSolucion)
    x = solucionar_ecuacion_lineal(mat, b)

    if len(x) == 2:
        xStrUno = str(x[0])
        xStrDos = str(x[1])
        resulUnoVar.set(xStrUno)
        resulDosVar.set(xStrDos)
    if len(x) == 3:
        xStrUno = str(x[0])
        xStrDos = str(x[1])
        xStrTres = str(x[2])
        resulUnoVar.set(xStrUno)
        resulDosVar.set(xStrDos)
        resulTresVar.set(xStrTres)
    if len(x) == 4:
        xStrUno = str(x[0])
        xStrDos = str(x[1])
        xStrTres = str(x[2])
        xStrCuatro = str(x[3])
        resulUnoVar.set(xStrUno)
        resulDosVar.set(xStrDos)
        resulTresVar.set(xStrTres)
        resulCuatroVar.set(xStrCuatro)
    if len(x) ==6:
        xStrUno = str(x[0])
        xStrDos = str(x[1])
        xStrTres = str(x[2])
        xStrCuatro = str(x[3])
        resulUnoVar.set(xStrUno)
        resulDosVar.set(xStrDos)
        resulTresVar.set(xStrTres)
        resulCuatroVar.set(xStrCuatro)






def crearBoxes():
    print(tamanoArray)
    size = int(tamanoArray[0])
    frameBoxes = tkinter.Frame(frameUno, width=800, height=60)
    frameBoxes.config()
    frameBoxes.grid(row=1, column=0)
    x2 = 0
    y2 = 0
    matriz = []
    for y in range(size):
        text_var.append([])
        entries.append([])
        fila = []
        columna = []

        for x in range(size):
            text_var[y].append(StringVar())
            entryX = Entry(frameBoxes, textvariable=text_var[y][x], width=5, font=15)
            entries[y].append(entryX)
            entries[y][x].grid(column=x + x2, row=y + y2, padx=10, pady=10)
            # entries.append(entryX)
            fila.append(entryX)
            x2 += 30
        columna.append(fila)
        matriz.append(columna)
        # append your StringVar and Entry

        y2 += 30
        x2 = 0

        entriesFinal.append(matriz)


def abrirCreador():
    ocultar()
    frameCreador = tkinter.Frame(frameUno, width=300, height=60)
    frameCreador.config()
    frameCreador.grid(column=0, row=1)

    labelX = Label(frameCreador, text="Ingrese el tamaño de la matriz ", width="20", height="1",
                   font=("helvetica", 10, "bold"),
                   padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=1, relief="ridge")
    labelX.grid(column=0, row=0)

    numParticionesX = tkinter.IntVar()

    funcCampoTextoX = Entry(frameCreador, textvariable=numParticionesX, font=10, width=10)
    funcCampoTextoX.grid(column=0, row=1)

    def guardarTamano():
        tamano = funcCampoTextoX.get()
        tamanoArray.append(tamano)
        frameCreador.destroy()
        crearBoxes()

    btnCrearBoxes = Button(frameCreador, text="Ok", width="7", font=("helvetica", 12, "bold"),
                           bg="LightSkyBlue1", fg="black", command=guardarTamano)
    btnCrearBoxes.grid(column=1, row=1)


def delimitaCuadros():
    entriesFinal, variasMatrices = prueba()
    concatenacion = ""
    numero = 0
    filas = 0
    while filas < len(entriesFinal):
        while numero < len(entriesFinal):
            concatenacion = concatenacion + variasMatrices[0][filas][numero]
            if numero <= len(entriesFinal) - 2:
                concatenacion = concatenacion + " "
            numero = numero + 1
        if filas <= len(entriesFinal) - 2:
            concatenacion = concatenacion + "\n"
        filas = filas + 1
        numero = 0
    return concatenacion


def prueba():
    ultimaMatriz = len(entriesFinal) - 1
    filas = len(entriesFinal[ultimaMatriz][0][0])
    columnas = len(entriesFinal[ultimaMatriz])
    matriz = []
    for i in range(columnas):
        matriz.append([])
        for j in range(filas):
            matriz[i].append(text_var[i][j].get())
    variasMatrices.append(matriz)
    return (entriesFinal, variasMatrices)


def ocultar():
    btnCrearMatriz.destroy()

    # interfaz
def main(cuadro):
    cuadro.destroy()
    cuadro = Tk()
    cuadro.title("Calculadora conversión de matrices")
    cuadro.geometry("740x450")
    global frameUno
    frameUno = tkinter.Frame(cuadro, width=300, height=150)
    # frame.config(bg="green")
    frameUno.grid(row=1, column=0)

    frameDos = tkinter.Frame(cuadro, width=400, height=100)
    # frame.config(bg="green")
    frameDos.grid(row=2, column=0)
    frameTres = tkinter.Frame(cuadro, width=400, height=100)
    # frame.config(bg="green")
    frameTres.grid(row=4, column=0)

    frameCuatro = tkinter.Frame(cuadro, width=400, height=100)
    # frame.config(bg="green")
    frameCuatro.grid(row=3, column=0)
    frameQuinto = tkinter.Frame(cuadro, width=400, height=100)
    # frame.config(bg="green")
    frameQuinto.grid(row=0, column=0)
    # Labels nombres
    metodo = Label(frameQuinto, text="SISTEMA DE ECUCIONES LINEALES", width="80", font=("helvetica", 12, "bold"),
                   padx=5,
                   pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
    metodo.grid(row=0, column=0)

    matriz = Label(frameUno, text="matriz", width="14", font=("helvetica", 12, "bold"), padx=5, pady=5, bg="ivory2",
                   fg="black", borderwidth=2, relief="groove")
    matriz.grid(row=0, column=0)

    vector = Label(frameUno, text="vector", width="17", font=("helvetica", 12, "bold"), padx=5, pady=5, bg="ivory2",
                   fg="black", borderwidth=2, relief="groove")
    vector.grid(row=0, column=1)

    # label resultados
    x1Label = Label(frameTres, text="x1", width="17", font=("helvetica", 12, "bold"),
                    padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    x1Label.grid(row=0, column=0)

    x2Label = Label(frameTres, text="x2", width="17", font=("helvetica", 12, "bold"),
                    padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    x2Label.grid(row=1, column=0)

    x3Label = Label(frameTres, text="x3", width="17", font=("helvetica", 12, "bold"),
                    padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    x3Label.grid(row=2, column=0)

    x4Label = Label(frameTres, text="x4", width="17", font=("helvetica", 12, "bold"),
                    padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    x4Label.grid(row=3, column=0)
    global MatrizEntrada,vectorEntrada,btnCrearMatriz,variasMatrices,entriesFinal,entries,matrizV,vectorV,resultadoV,resulUnoVar,resulDosVar,resulTresVar,resulCuatroVar,tamanoArray,text_var
    # espacios de entradas
    matrizV = tkinter.StringVar()
    vectorV = tkinter.StringVar()
    resultadoV = tkinter.StringVar()
    resulUnoVar = tkinter.StringVar()
    resulDosVar = tkinter.StringVar()
    resulTresVar = tkinter.StringVar()
    resulCuatroVar = tkinter.StringVar()
    tamanoArray = []
    text_var = []
    entries = []
    entriesFinal = []
    variasMatrices = []
    btnCrearMatriz = Button(cuadro, text="+", width="4", font=("helvetica", 12, "bold"),
                            bg="LightSkyBlue1", fg="black", command=abrirCreador)
    btnCrearMatriz.place(x=300, y=70)

    vectorEntrada = Text(frameUno, font=1, width=4, height=4)
    vectorEntrada.grid(row=1, column=1)

    resultadoUnoEntrada = Entry(frameTres, textvariable=resulUnoVar, font=10, width=30, state="readonly")
    resultadoUnoEntrada.grid(row=0, column=1)

    resultadoDosEntrada = Entry(frameTres, textvariable=resulDosVar, font=10, width=30, state="readonly")
    resultadoDosEntrada.grid(row=1, column=1)

    resultadoTresEntrada = Entry(frameTres, textvariable=resulTresVar, font=10, width=30, state="readonly")
    resultadoTresEntrada.grid(row=2, column=1)

    resultadoCuatroEntrada = Entry(frameTres, textvariable=resulCuatroVar, font=10, width=30, state="readonly")
    resultadoCuatroEntrada.grid(row=3, column=1)

    """resultadoEntrada = Text(cuadro, width=28, height=8, font=15)
    resultadoEntrada.place(x=200, y=270)"""

    # botones

    btnCalcular = Button(frameCuatro, text="Calcular", width="10", font=("helvetica", 12, "bold"),
                         bg="LightSkyBlue1", fg="black", command=resolver_ecu_lineales)
    btnCalcular.grid(row=0, column=0)

    btnBorrar = Button(frameCuatro, text="Borrar", width="10", font=("helvetica", 12, "bold"),
                       bg="LightSkyBlue1", fg="black", command=borrar)
    btnBorrar.grid(row=0, column=2)

    btnSalir = Button(frameCuatro, text="Salir", width="10", font=("helvetica", 12, "bold"),
                      bg="LightSkyBlue1", fg="black", command=lambda:salir(cuadro))
    btnSalir.grid(row=0, column=3)

