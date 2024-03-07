import tkinter
from tkinter import *
from tkinter import messagebox
import math
#x=round(mynumber, 2)

def salir(root):
    root.destroy()
    root.destroy()


# no root
def basesConversor():
    import interfazConFracciones
    interfazConFracciones.main()


# est[a
def conversosIEEE(root):
    import formatosIEEE754
    formatosIEEE754.main(root)


def biseccion(root):
    import calculadoraBiseccion
    calculadoraBiseccion.main(root)


def reglaFalsa(root):
    import calculadoraReglaFalsa
    calculadoraReglaFalsa.main(root)


def newton(root):
    import calculadoraMetNewRaphson
    calculadoraMetNewRaphson.main(root)


# yopi
def secante(root):
    import CalculadoraMetSeante
    CalculadoraMetSeante.main(root)


def polinomios(root):
    import calciladoraMetPolinomios
    calciladoraMetPolinomios.main(root)


def derivadas(root):
    import calculadoraDerivadas
    calculadoraDerivadas.main(root)


# *************************
def rectangulos(root):
    import metodoRectangulo
    metodoRectangulo.main(root)


def trapecio(root):
    import metodoTrapecio
    metodoTrapecio.main(root)


def simp13(root):
    import calculadoraSimpson13
    calculadoraSimpson13.main(root)


def simp38(root):
    import calculadoraSimpson38
    calculadoraSimpson38.main(root)


def montecarlo(root):
    import montecarlo
    montecarlo.main(root)


# eta
def matrices(root):
    import calculadoraMatrices
    calculadoraMatrices.main(root)


def ecuaciones(root):
    import calculadoraGauss
    calculadoraGauss.main(root)


def ajusteCurva(root):
    import ajusteDeCurvas
    ajusteDeCurvas.main(root)


def graficadoraLinda(root):
    import grafica
    grafica.main(root)


def main(root):
    # Interfaz gráfica

    root = Tk()
    root.title("Calculadora conversión de bases")
    root.geometry("875x350")

    # Líneas de la calculadora para separar apartados
    """canvasUno = Canvas(root, bg="LightSkyBlue4", height=2, width=640)
    canvasUno.place(x=215, y=46)

    canvasDos = Canvas(root, bg="LightSkyBlue4", height=2, width=640)
    canvasDos.place(x=215, y=82)

    canvasTres = Canvas(root, bg="LightSkyBlue4", height=2, width=640)
    canvasTres.place(x=215, y=120)

    canvasCuatro = Canvas(root, bg="LightSkyBlue4", height=2, width=640)
    canvasCuatro.place(x=215, y=158)

    canvasCinco = Canvas(root, bg="LightSkyBlue4", height=2, width=640)
    canvasCinco.place(x=215, y=198)

    canvaSeis = Canvas(root, bg="LightSkyBlue4", height=2, width=640)
    canvaSeis.place(x=215, y=238)

    canvaSiete = Canvas(root, bg="LightSkyBlue4", height=2, width=640)
    canvaSiete.place(x=215, y=278)"""

    # Labels de la parte izquierda
    nombreLabel = Label(root, text="Calculadora Métodos Numéricos", width="83", font=("helvetica", 12, "bold"),
                        padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
    nombreLabel.place(x=15, y=12)

    baseLabel = Label(root, text="Calculadora bases", width="18", font=("helvetica", 12, "bold"),
                      padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    baseLabel.place(x=15, y=50)

    ecuacionesLabel = Label(root, text="Solución de ecuaciones", width="18", font=("helvetica", 12, "bold"),
                            padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    ecuacionesLabel.place(x=15, y=88)

    derivadasLabel = Label(root, text="Derivadas", width="18", font=("helvetica", 12, "bold"),
                           padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    derivadasLabel.place(x=15, y=126)

    integraleslLabel = Label(root, text="Integrales", width="18", font=("helvetica", 12, "bold"),
                             padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    integraleslLabel.place(x=15, y=164)

    algebralLabel = Label(root, text="Álgebra lineal", width="18", font=("helvetica", 12, "bold"),
                          padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    algebralLabel.place(x=15, y=206)

    graficadoralLabel = Label(root, text="Graficadora", width="18", font=("helvetica", 12, "bold"),
                              padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    graficadoralLabel.place(x=15, y=244)

    # botones BASES

    btnConverBases = Button(root, text="Conversor Bases", width="14", font=("helvetica", 10, "bold"),
                            bg="LightSkyBlue1", fg="black", command=lambda: basesConversor())
    btnConverBases.place(x=215, y=51)

    btnConverIEEE = Button(root, text="Conversor IEEE", width="14", font=("helvetica", 10, "bold"),
                           bg="LightSkyBlue1", fg="black", command=lambda: conversosIEEE(root))
    btnConverIEEE.place(x=345, y=51)

    # Botones solucion ecuaciones

    btnBiseccion = Button(root, text="Bisección", width="14", font=("helvetica", 10, "bold"),
                          bg="LightSkyBlue1", fg="black", command=lambda: biseccion(root))
    btnBiseccion.place(x=215, y=89)

    btnreglaFalsa = Button(root, text="Regla Falsa", width="14", font=("helvetica", 10, "bold"),
                           bg="LightSkyBlue1", fg="black", command=lambda: reglaFalsa(root))
    btnreglaFalsa.place(x=345, y=89)

    btnNewton = Button(root, text="Newton Raphson", width="14", font=("helvetica", 10, "bold"),
                       bg="LightSkyBlue1", fg="black", command=lambda: newton(root))
    btnNewton.place(x=475, y=89)

    btnSecante = Button(root, text="Secante", width="14", font=("helvetica", 10, "bold"),
                        bg="LightSkyBlue1", fg="black", command=lambda: secante(root))
    btnSecante.place(x=605, y=89)

    btnPolinomios = Button(root, text="Polinomios", width="14", font=("helvetica", 10, "bold"),
                           bg="LightSkyBlue1", fg="black", command=lambda: polinomios(root))
    btnPolinomios.place(x=735, y=89)

    # Botones derivadas

    btnDerivadas = Button(root, text="Derivadas", width="14", font=("helvetica", 10, "bold"),
                          bg="LightSkyBlue1", fg="black", command=lambda: derivadas(root))
    btnDerivadas.place(x=215, y=127)

    # Botones Integrales

    btnRectangulo = Button(root, text="Rectángulos", width="14", font=("helvetica", 10, "bold"),
                           bg="LightSkyBlue1", fg="black", command=lambda: rectangulos(root))
    btnRectangulo.place(x=215, y=165)

    btnTrapecio = Button(root, text="Trapecio", width="14", font=("helvetica", 10, "bold"),
                         bg="LightSkyBlue1", fg="black", command=lambda: trapecio(root))
    btnTrapecio.place(x=345, y=165)

    btnSimpson13 = Button(root, text="Simpson 1/3", width="14", font=("helvetica", 10, "bold"),
                          bg="LightSkyBlue1", fg="black", command=lambda: simp13(root))
    btnSimpson13.place(x=475, y=165)

    btnSimpson38 = Button(root, text="Simpson 3/8", width="14", font=("helvetica", 10, "bold"),
                          bg="LightSkyBlue1", fg="black", command=lambda: simp38(root))
    btnSimpson38.place(x=605, y=165)

    btnMontecarlo = Button(root, text="Montecarlo", width="14", font=("helvetica", 10, "bold"),
                           bg="LightSkyBlue1", fg="black", command=lambda: montecarlo(root))
    btnMontecarlo.place(x=735, y=165)

    # Botones algebra

    btnMatrices = Button(root, text="Matrices", width="14", font=("helvetica", 10, "bold"),
                         bg="LightSkyBlue1", fg="black", command=lambda: matrices(root))
    btnMatrices.place(x=215, y=206)

    btnSistemaEL = Button(root, text="Ecuación Lineal", width="14", font=("helvetica", 10, "bold"),
                          bg="LightSkyBlue1", fg="black", command=lambda: ecuaciones(root))
    btnSistemaEL.place(x=345, y=206)

    btnAjusteCurva = Button(root, text="Ajuste Curva", width="14", font=("helvetica", 10, "bold"),
                            bg="LightSkyBlue1", fg="black", command=lambda: ajusteCurva(root))
    btnAjusteCurva.place(x=475, y=206)

    # botones graficadora
    btnGraficar = Button(root, text="Graficador", width="14", font=("helvetica", 10, "bold"),
                         bg="LightSkyBlue1", fg="black", command=lambda: graficadoraLinda(root))
    btnGraficar.place(x=215, y=244)

    # Botones
    btnSalir = Button(root, text="SALIR", width="8", font=("helvetica", 13, "bold"),
                      bg="LightSkyBlue1", fg="black", command=lambda: salir(root))
    btnSalir.place(x=435, y=290)



    """btnCalcular = Button(root, text="Calcular", width="8", font=("helvetica", 12, "bold"),
                         bg="LightSkyBlue1", fg="black", command="")
    btnCalcular.place(x=80, y=190)

    btnBorrar = Button(root, text="Borrar", width="8", font=("helvetica", 12, "bold"),
                       bg="LightSkyBlue1", fg="black", command="")
    btnBorrar.place(x=210, y=190)

    btnSalir = Button(root, text="Salir", width="8", font=("helvetica", 12, "bold"),
                      bg="LightSkyBlue1", fg="black", command=salir)
    btnSalir.place(x=340, y=190)
    """

    root.mainloop()


