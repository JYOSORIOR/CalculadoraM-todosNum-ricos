from tkinter import *
import tkinter
from tkinter import ttk
import numpy
import operacionesMatrices
import re

def salir(root):
    root.destroy()
    import menuPrincipal
    menuPrincipal.main(root)

def main(root):
    #VENTANA PRINCIPAL
    root.title("Calculadora Matrices")
    root.geometry("1200x1000")


    #FRAME SUPERIOR

    frameSuperior = Frame(root, height=400, width=1000)
    #frameSuperior.config(bg="black")
    frameSuperior.grid(row=0, column=0)

    #FRAME MEDIO

    frameMedio = Frame(root, height=300, width=1000, highlightbackground="gray", highlightthickness=1)
    #frameMedio.config(bg="gray")
    frameMedio.grid(row=1, column=0)

    #FRAME INFERIOR

    frameInferior = Frame(root, height=400, width=1000)
    #frameInferior.config(bg="lightblue")
    frameInferior.grid(row=2, column=0, pady= 20)

    #FRAME "MATRICES"

    frameMatrices = Frame(frameSuperior, height=400, width=400)
    #frameMatrices.config(bg="red")
    frameMatrices.grid(row=0, column=0)

    #labelMatrices = Label(frameMatrices, text="SOY EL FRAME DE MATRICES :)").place(x=0, y=0)

    #FRAME BOTONES FUNCIONES

    frameBotones = Frame(frameSuperior, height=400, width=300, highlightbackground="gray", highlightthickness=2)
    #frameBotones.config(bg="yellow")
    frameBotones.grid(row=0, column=1)

    #labelBotones = Label(frameBotones, text="SOY EL FRAME DE BOTONES :)").place(x=0, y=0)

    #FRAME "EDITOR"

    frameEditor = Frame(frameSuperior, height=400, width=400)
    #frameEditor.config(bg="blue")
    frameEditor.grid(row=0, column=2)

    #labelEditor = Label(frameEditor, text="SOY EL FRAME EDITOR :)").place(x=0, y=0)

    #FRAME "OPERACIONES"

    #labelOperaciones = Label(frameMedio, text="SOY EL FRAME DE OPERACIONES :)").place(x=0, y=0)

    frameOperacion = Frame(frameMedio, height=150, width=400)
    frameOperacion.grid(row=0)

    labelBarraOperacion = Label(frameOperacion, text="Operación: ", width="20", font=("helvetica", 12, "bold"),
                        padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
    labelBarraOperacion.grid(row=0, column=0, pady= 20)

    operacionVar = StringVar()
    entryOperacion = Entry(frameOperacion, textvariable=operacionVar, width=40, font=15)
    entryOperacion.grid(row= 0, column= 1, padx=20)




    #FRAME OPERACIONES BOTONES

    frameOperacionBotones = Frame(frameMedio, height=150, width=400)
    frameOperacionBotones.grid(row=1)


    #-----------------------------------------------------------------
    #TABLAS
    columns = ('Id', 'Nombre')
    tablaMatrices = ttk.Treeview(frameMatrices, columns=columns, show='headings')

    tablaMatrices.heading('Id', text='Id')
    tablaMatrices.heading('Nombre', text='Nombre')

    tablaMatrices.grid(row=0,column=0, padx=20)

    datosTabla = []

    def paraLaTabla(iteraciones, raiz, errorRela, extremoInfe, extremoSupe):
        datosTabla.append()

    #PRUEBA
    def destructor(arrayFrames):
        frameDestruir = arrayFrames[len(arrayFrames)-1]
        frameDestruir.destroy()
        arrayFrames.clear()

    text_var = []
    entries = []
    variasMatrices=[]
    frames = []
    tamanosArray = []

    def obtenerNumerosPrueba():
        print("1. ")
        print(entriesFinal)
        print("2. ")
        print(entriesFinal[0])
        print("3. ")
        print(entriesFinal[0][0])

    def obtenerNumeros():

        frameDestruir = frames[len(frames)-1]
        frameDestruir.destroy()
        frames.clear()

        print(entriesFinal)

        ultimaMatriz = len(entriesFinal)-1
        filas =len(entriesFinal[ultimaMatriz][0][0])

        print(entriesFinal[ultimaMatriz])
        columnas = len(entriesFinal[ultimaMatriz])


        matriz = []

        for i in range(columnas):
            matriz.append([])
            for j in range(filas):
                matriz[i].append(text_var[i][j].get())
        variasMatrices.append(matriz)

        print(matriz)
        print(len(matriz))
        print("Son varias: ",variasMatrices)
        print(len(variasMatrices))
        print(len(variasMatrices[0]))
        print(len(variasMatrices[0][0]))
        #print(len(variasMatrices[0][0][0]))

        entries.clear()
        text_var.clear()
        actualizarMatrices()


    entriesFinal = []
    def crearBoxes():
        nX = int(tamanosArray[0])
        nY = int(tamanosArray[1])
        tamanosArray.clear()

        print(tamanosArray)
        print(nX)
        print(nY)
        frameDestruir = frames[len(frames)-1]
        frameDestruir.destroy()
        frames.clear()

        x2 = 0
        y2 = 0

        matriz = []

        frameConstructor1 = tkinter.Frame(frameSuperior, width=400, height=400, highlightbackground="gray", highlightthickness=1)
        #frameConstructor1.config(bg="green")
        frameConstructor1.grid(row=0, column=2)

        #frames.append(frameEditor1)
        saveData(frames, frameConstructor1)

        frame = tkinter.Frame(frameConstructor1, width=400, height=400)
        #frame.config(bg="green")
        frame.grid(row=1, column=0)

        frameNombre = tkinter.Frame(frameConstructor1, width=400, height=100)
        #frameNombre.config(bg="orange")
        frameNombre.grid(row=0, column=0, pady=10)


        varNombre = tkinter.StringVar()
        entryNombre = Entry(frameNombre, textvariable=varNombre, width=10, font=15)
        entryNombre.grid(row=0,column=1, padx=20)

        nombreMatriz = varNombre.get()

        labelEditor = Label(frameNombre, text="Nombre: ")
        labelEditor.grid(row=0, column=0)

        for y in range(nY):
            text_var.append([])
            entries.append([])
            fila = []
            columna = []

            for x in range(nX):
                text_var[y].append(StringVar())
                entryX = Entry(frame, textvariable=text_var[y][x], width=5, font=15)
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

        btnGuardarMatriz = Button(frameNombre, text="Guardar", width="6", font=("helvetica", 12, "bold"),
                                  bg="LightSkyBlue1", fg="black", command=obtenerNumeros)
        btnGuardarMatriz.grid(row=0, column=2, padx=5)

        # SE AÑADE LA MATRIZ ENTERA A UNA LISTA
        #matrizCompleta = []

        #matrizCompleta.append(nombreMatriz)
        #matrizCompleta.append(matriz)

        entriesFinal.append(matriz)

        #print("TAMAÑO MATRIZ: ")
        #print(len(matriz))

        #print("CANTIDAD DE COLUMNAS: ")
        #print(len(columna))

        #print("CANTIDAD DE FILAS: ")
        #print(len(matriz[0][0]))

        #print("------------------------------------------")
        #print(matriz)
        #print("------------------------------------------")
        #print(matriz[0][0])

    def actualizarMatrices():
        tablaMatrices.delete(*tablaMatrices.get_children())
        for i in range(len(variasMatrices)):
            matriz = variasMatrices[i]
            dato = [i, matriz]
            tablaMatrices.insert('', tkinter.END, values=dato)

        print("TABLA ACTUALIZADA")

    def saveData(array, data):
        array.append(data)
        print(array)
        print("DATA HAS BEEN SAVED SUCCESFULLY")

    def abrirCreador():

        frameEditor1 = tkinter.Frame(frameSuperior, width=400, height=400)
        #frameEditor1.config(bg="red")
        frameEditor1.grid(row=0, column=2)

        #frames.append(frameEditor1)
        saveData(frames, frameEditor1)

        frame = tkinter.Frame(frameEditor1, width=400, height=400)
        #frame.config(bg="red")

        labelEditor = Label(frameEditor1, text="EDITOR")

        labelX = Label(frame, text="X", width="5", height="1", font=("helvetica", 10, "bold"),
                       padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=1, relief="ridge")
        labelY = Label(frame, text="Y", width="5", height="1", font=("helvetica", 10, "bold"),
                       padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=1, relief="ridge")

        numParticionesX = tkinter.IntVar()
        numParticionesY = tkinter.IntVar()

        funcCampoTextoX = Entry(frame, textvariable=numParticionesX, font=10, width=10)

        funcCampoTextoY = Entry(frame, textvariable=numParticionesY, font=10, width=10)

        def saveSizes():
            tamanosArray.append(funcCampoTextoX.get())
            tamanosArray.append(funcCampoTextoY.get())
            crearBoxes()

        btnCrearBoxes = Button(frame, text="Crear", width="15", font=("helvetica", 12, "bold"),
                                bg="LightSkyBlue1", fg="black", command=saveSizes)
        #frame.bind("<Return>", saveSizes())

        labelEditor.place(x=20, y=20)
        labelX.place(x=40, y=60)
        labelY.place(x=40, y=120)
        funcCampoTextoX.place(x=120, y=62)
        funcCampoTextoY.place(x=120, y=122)
        btnCrearBoxes.place(x=150, y=170)

        frame.pack()

    def abrirEditor():

        frameConstructor1 = tkinter.Frame(frameSuperior, width=400, height=400, highlightbackground="gray", highlightthickness=1)
        #frameConstructor1.config(bg="pink")
        frameConstructor1.grid(row=0, column=2)

        # frames.append(frameEditor1)
        saveData(frames, frameConstructor1)

        frame = tkinter.Frame(frameConstructor1, width=400, height=400)
        #frame.config(bg="green")
        frame.grid(row=1, column=0)

        frameNombre = tkinter.Frame(frameConstructor1, width=400, height=100)
        #frameNombre.config(bg="orange")
        frameNombre.grid(row=0, column=0, pady=10)

        varNombre = tkinter.StringVar()
        entryNombre = Entry(frameNombre, textvariable=varNombre, width=10, font=15)
        entryNombre.grid(row=0, column=1, padx=20)

        nombreMatriz = varNombre.get()

        labelEditor = Label(frameNombre, text="Nombre: ")
        labelEditor.grid(row=0, column=0)

        data = verMatrizSeleccionada()
        id = data[0]
        matrizSeleccionada = data[1]
        filas = len(matrizSeleccionada[0])
        columnas = len(matrizSeleccionada)
        x2 = 0
        y2 = 0

        print("ID: ")
        print(id)

        print("FILAS: ")
        print(filas)
        print("COLUMNAS: ")
        print(columnas)

        for y in range(columnas):
            text_var.append([])
            entries.append([])
            fila = []
            columna = []
            matriz = []
            for x in range(filas):
                text_var[y].append(StringVar())
                entryX = Entry(frame, textvariable=text_var[y][x], width=5, font=15)
                entries[y].append(entryX)
                #entryX.insert(matrizSeleccionada[x][y])
                entries[y][x].grid(column=x + x2, row=y + y2, padx=10, pady=10)
                # entries.append(entryX)
                entryX.insert(0, matrizSeleccionada[y][x])
                print(matrizSeleccionada[y][x])
                fila.append(entryX)
                x2 += 30
            columna.append(fila)
            matriz.append(columna)
            # append your StringVar and Entry

            y2 += 30
            x2 = 0

        def guardarMatrizEditada():
            matrizEditada = []
            for i in range(columnas):
                matrizEditada.append([])
                for j in range(filas):
                    matrizEditada[i].append(text_var[i][j].get())
                    print("---------------------------------------")
                    print(text_var[i][j].get())
            variasMatrices[id] = matrizEditada
            entries.clear()
            text_var.clear()
            frameDestruir = frames[len(frames) - 1]
            frameDestruir.destroy()
            frames.clear()
            actualizarMatrices()

            print("NUEVA MATRIZ")
            print(len(matrizEditada[0]))
            print(len(matrizEditada))
            print(matrizEditada)
            #variasMatrices.append(matriz)

        btnGuardarMatriz = Button(frameNombre, text="Guardar", width="6", font=("helvetica", 12, "bold"),
                                  bg="LightSkyBlue1", fg="black", command=guardarMatrizEditada)
        btnGuardarMatriz.grid(row=0, column=2, padx=5)

    def abrirVisualizadorMatriz():
        frameConstructor1 = tkinter.Frame(frameSuperior, width=400, height=400, highlightbackground="gray", highlightthickness=1)
        #frameConstructor1.config(bg="pink")
        frameConstructor1.grid(row=0, column=2)

        # frames.append(frameEditor1)
        saveData(frames, frameConstructor1)

        frame = tkinter.Frame(frameConstructor1, width=400, height=400)
        #frame.config(bg="green")
        frame.grid(row=1, column=0)

        frameNombre = tkinter.Frame(frameConstructor1, width=400, height=100)
        #frameNombre.config(bg="orange")
        frameNombre.grid(row=0, column=0, pady=10)

        data = verMatrizSeleccionada()
        id = data[0]
        matrizSeleccionada = data[1]
        filas = len(matrizSeleccionada[0])
        columnas = len(matrizSeleccionada)
        x2 = 0
        y2 = 0

        print("ID: ")
        print(id)

        textLabel = "Matriz " +  str(id) + ": "
        #labelEditor = Label(frameNombre, text=textLabel)
        labelEditor = Label(frameNombre, text=textLabel, width="20", font=("helvetica", 12, "bold"),
                            padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
        labelEditor.grid(row=0, column=0)

        print("FILAS: ")
        print(filas)
        print("COLUMNAS: ")
        print(columnas)

        for y in range(columnas):
            text_var.append([])
            entries.append([])
            fila = []
            columna = []
            matriz = []
            for x in range(filas):
                text_var[y].append(StringVar())
                entryX = Entry(frame, textvariable=text_var[y][x], width=5, font=15)
                entries[y].append(entryX)
                #entryX.insert(matrizSeleccionada[x][y])
                entries[y][x].grid(column=x + x2, row=y + y2, padx=10, pady=10)
                # entries.append(entryX)
                entryX.insert(0, matrizSeleccionada[y][x])
                entryX.config(state=DISABLED)
                print(matrizSeleccionada[y][x])
                fila.append(entryX)
                x2 += 30
            columna.append(fila)
            matriz.append(columna)
            # append your StringVar and Entry

            y2 += 30
            x2 = 0

        def cerrarVisualizador():
            entries.clear()
            text_var.clear()
            frameDestruir = frames[len(frames) - 1]
            frameDestruir.destroy()
            frames.clear()

        btnGuardarMatriz = Button(frameNombre, text="Cerrar", width="6", font=("helvetica", 12, "bold"),
                                  bg="LightSkyBlue1", fg="black", command=cerrarVisualizador)
        btnGuardarMatriz.grid(row=0, column=2, padx=5)

    def abrirEliminadorMatrices():
        frameConstructor1 = tkinter.Frame(frameSuperior, width=400, height=400, highlightbackground="gray", highlightthickness=1)
        #frameConstructor1.config(bg="pink")
        frameConstructor1.grid(row=0, column=2)

        # frames.append(frameEditor1)
        saveData(frames, frameConstructor1)

        frame = tkinter.Frame(frameConstructor1, width=400, height=400, highlightbackground="gray", highlightthickness=1)
        #frame.config(bg="green")
        frame.grid(row=1, column=0)

        frameNombre = tkinter.Frame(frameConstructor1, width=400, height=100)
        #frameNombre.config(bg="orange")
        frameNombre.grid(row=0, column=0, pady=10)

        frameOpciones = tkinter.Frame(frameConstructor1, width=400, height=100)
        #frameOpciones.config(bg="brown")
        frameOpciones.grid(row=3, column=0, pady=10)

        data = verMatrizSeleccionada()
        id = data[0]
        matrizSeleccionada = data[1]
        filas = len(matrizSeleccionada[0])
        columnas = len(matrizSeleccionada)
        x2 = 0
        y2 = 0

        print("ID: ")
        print(id)

        textLabel = "Matriz " +  str(id) + ": "
        labelEditor = Label(frameNombre, text=textLabel, width="20", font=("helvetica", 12, "bold"),
                            padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
        labelEditor.grid(row=0, column=0)

        labelOpciones = Label(frameOpciones, text="¿Desea eliminar esta matriz?", width="30", font=("helvetica", 12, "bold"),
                            padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
        labelOpciones.grid(row=0, column=0)

        print("FILAS: ")
        print(filas)
        print("COLUMNAS: ")
        print(columnas)

        for y in range(columnas):
            text_var.append([])
            entries.append([])
            fila = []
            columna = []
            matriz = []
            for x in range(filas):
                text_var[y].append(StringVar())
                entryX = Entry(frame, textvariable=text_var[y][x], width=5, font=15)
                entries[y].append(entryX)
                #entryX.insert(matrizSeleccionada[x][y])
                entries[y][x].grid(column=x + x2, row=y + y2, padx=10, pady=10)
                # entries.append(entryX)
                entryX.insert(0, matrizSeleccionada[y][x])
                entryX.config(state=DISABLED)
                print(matrizSeleccionada[y][x])
                fila.append(entryX)
                x2 += 30
            columna.append(fila)
            matriz.append(columna)
            # append your StringVar and Entry

            y2 += 30
            x2 = 0

        frameDestruir = frames[len(frames) - 1]
        def eliminarMatriz():
            variasMatrices.pop(id)
            cerrarVisualizador()
            actualizarMatrices()

            frameDestruir.destroy()
            frames.clear()


        def cerrarVisualizador():
            entries.clear()
            text_var.clear()

            frameDestruir.destroy()
            frames.clear()

        btnSI = Button(frameOpciones, text="Sí", width="6", font=("helvetica", 12, "bold"),
                                  bg="LightSkyBlue1", fg="black", command=eliminarMatriz)
        btnSI.grid(row=1, column=0, padx=5, pady=5)

        btnNO = Button(frameOpciones, text="No", width="6", font=("helvetica", 12, "bold"),
                                  bg="LightSkyBlue1", fg="black", command=cerrarVisualizador)
        btnNO.grid(row=2, column=0, padx=5, pady=5)


    def verMatrizSeleccionada():
        data = []
        tablaSelec = tablaMatrices.focus()
        detalles = tablaMatrices.item(tablaSelec)
        id = int(detalles["values"][0])
        data.append(id)
        #id = detalles.get("Id")
        #print("---------------------------------")
        #print("LA ID ES: " + str(id))

        matriz = variasMatrices[id]
        data.append(matriz)
        matrizNumpy = numpy.array(variasMatrices[id])
        print(matriz)
        return data

    def calcularDeterminante():
        matrizSeleccionada = verMatrizSeleccionada()[1]
        matrizNumpy = numpy.array(matrizSeleccionada, dtype=numpy.float64)
        #print(matrizNumpy)

        resultado = operacionesMatrices.determinante(matrizNumpy)
        #print(resultado)

        frameConstructor1 = tkinter.Frame(frameInferior, width=600, height=300, highlightbackground="gray", highlightthickness=1)
        frameConstructor1.grid(row=1, column=0)

        saveData(framesSolucion, frameConstructor1)

        text = "La determinante es: " + str(resultado)

        labelEditor = Label(frameConstructor1, text=text, width="40", font=("helvetica", 12, "bold"),
                            padx=5, pady=10, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
        labelEditor.grid(row=0, column=0)

        def clearSolucionador():
            for i in range(len(framesSolucion)):
                frameDestruir = framesSolucion[len(frames) - 1]
                frameDestruir.destroy()
            frames.clear()
            entries_solution.clear()
            text_var_solution.clear()
            labelEditor.destroy()

        btnLimpiarSolucion = Button(frameConstructor1, text="Cerrar", width="15", font=("helvetica", 12, "bold"),
                                    bg="LightSkyBlue1", fg="black", command=clearSolucionador).grid(row=1, column=0,
                                                                                                    pady=15,
                                                                                                    padx=80)


    def calcularInversa():
        matrizSeleccionada = verMatrizSeleccionada()[1]
        matrizNumpy = numpy.array(matrizSeleccionada, dtype=numpy.float64)

        #resultado = determinante(matrizSeleccionada)
        resultado = operacionesMatrices.inversa(matrizNumpy)
        #print(resultado)

        frameConstructor1 = tkinter.Frame(frameInferior, width=600, height=300, highlightbackground="gray", highlightthickness=1)
        frameConstructor1.grid(row=1, column=0)

        saveData(framesSolucion, frameConstructor1)

        frameGuardar = tkinter.Frame(frameInferior, width=600, height=300)
        frameGuardar.grid(row=2, column=0)

        # frames.append(frameEditor1)
        saveData(framesSolucion, frameGuardar)

        text = "Inversa de la matriz: "

        labelEditor = Label(frameInferior, text=text, width="40", font=("helvetica", 12, "bold"),
                            padx=5, pady=10, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
        labelEditor.grid(row=0, column=0)

        filas = len(resultado[0])
        columnas = len(resultado)
        x2 = 0
        y2 = 0

        labelOpciones = Label(frameGuardar, text="¿Desea guardar esta matriz?", width="30",
                              font=("helvetica", 12, "bold"),
                              padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")

        for y in range(columnas):
            text_var_solution.append([])
            entries_solution.append([])
            fila = []
            columna = []
            matriz = []
            for x in range(filas):
                text_var_solution[y].append(StringVar())
                entryX = Entry(frameConstructor1, textvariable=text_var_solution[y][x], width=5, font=15)
                entries_solution[y].append(entryX)
                #entryX.insert(matrizSeleccionada[x][y])
                entries_solution[y][x].grid(column=x + x2, row=y + y2, padx=10, pady=10)
                # entries.append(entryX)
                entryX.insert(0, resultado[y][x])
                entryX.config(state=DISABLED)
                print(resultado[y][x])
                fila.append(entryX)
                x2 += 30
            columna.append(fila)
            matriz.append(columna)
            # append your StringVar and Entry

            y2 += 30
            x2 = 0

            def clearSolucionador():
                for i in range(len(framesSolucion)):
                    frameDestruir = framesSolucion[len(frames) - 1]
                    frameDestruir.destroy()
                frames.clear()
                entries_solution.clear()
                text_var_solution.clear()
                labelEditor.destroy()
                frameGuardar.destroy()
                #labelOpciones.destroy()
                #btnLimpiarSolucion.destroy()

            def guardarResultado():

                matrizResultado = []
                for i in range(columnas):
                    matrizResultado.append([])
                    for j in range(filas):
                        matrizResultado[i].append(resultado[i][j])
                        print("---------------------------------------")
                        print(resultado[i][j])
                variasMatrices.append(matrizResultado)

                actualizarMatrices()
                print("RESULTADO GUARDADO")
                clearSolucionador()

            labelOpciones.grid(row=2, column=0, pady= 10)

            btnSI = Button(frameGuardar, text="Sí", width="6", font=("helvetica", 12, "bold"),
                           bg="LightSkyBlue1", fg="black", command=guardarResultado)
            btnSI.grid(row=3, column=0, padx=5, pady=5)

            btnNO = Button(frameGuardar, text="No", width="6", font=("helvetica", 12, "bold"),
                           bg="LightSkyBlue1", fg="black", command=clearSolucionador)
            btnNO.grid(row=4, column=0, padx=5, pady=5)

            btnLimpiarSolucion = Button(frameGuardar, text="Cerrar", width="15", font=("helvetica", 12, "bold"),
                                  bg="LightSkyBlue1", fg="black", command=clearSolucionador).grid(row=0, column=0, pady=15,
                                                                                             padx=80)


    def calcularTranspuesta():
        matrizSeleccionada = verMatrizSeleccionada()[1]
        matrizNumpy = numpy.array(matrizSeleccionada, dtype=numpy.float64)
        #print(matrizNumpy)

        #resultado = determinante(matrizSeleccionada)
        resultado = operacionesMatrices.transpuesta(matrizNumpy)
        #print(resultado)

        frameConstructor1 = tkinter.Frame(frameInferior, width=600, height=300, highlightbackground="gray", highlightthickness=1)
        frameConstructor1.grid(row=1, column=0)

        saveData(framesSolucion, frameConstructor1)

        frameGuardar = tkinter.Frame(frameInferior, width=600, height=300)
        frameGuardar.grid(row=2, column=0)

        # frames.append(frameEditor1)
        saveData(framesSolucion, frameGuardar)

        text = "Transpuesta de la matriz: "

        labelEditor = Label(frameInferior, text=text, width="40", font=("helvetica", 12, "bold"),
                            padx=5, pady=10, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
        labelEditor.grid(row=0, column=0)

        filas = len(resultado[0])
        columnas = len(resultado)
        x2 = 0
        y2 = 0

        labelOpciones = Label(frameGuardar, text="¿Desea guardar esta matriz?", width="30",
                              font=("helvetica", 12, "bold"),
                              padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")

        for y in range(columnas):
            text_var_solution.append([])
            entries_solution.append([])
            fila = []
            columna = []
            matriz = []
            for x in range(filas):
                text_var_solution[y].append(StringVar())
                entryX = Entry(frameConstructor1, textvariable=text_var_solution[y][x], width=5, font=15)
                entries_solution[y].append(entryX)
                #entryX.insert(matrizSeleccionada[x][y])
                entries_solution[y][x].grid(column=x + x2, row=y + y2, padx=10, pady=10)
                # entries.append(entryX)
                entryX.insert(0, resultado[y][x])
                entryX.config(state=DISABLED)
                print(resultado[y][x])
                fila.append(entryX)
                x2 += 30
            columna.append(fila)
            matriz.append(columna)
            # append your StringVar and Entry

            y2 += 30
            x2 = 0

            def clearSolucionador():
                for i in range(len(framesSolucion)):
                    frameDestruir = framesSolucion[len(frames) - 1]
                    frameDestruir.destroy()
                frames.clear()
                entries_solution.clear()
                text_var_solution.clear()
                labelEditor.destroy()
                frameGuardar.destroy()
                #labelOpciones.destroy()
                #btnLimpiarSolucion.destroy()

            def guardarResultado():

                matrizResultado = []
                for i in range(columnas):
                    matrizResultado.append([])
                    for j in range(filas):
                        matrizResultado[i].append(resultado[i][j])
                        print("---------------------------------------")
                        print(resultado[i][j])
                variasMatrices.append(matrizResultado)

                actualizarMatrices()
                print("RESULTADO GUARDADO")
                clearSolucionador()

            labelOpciones.grid(row=2, column=0, pady= 10)

            btnSI = Button(frameGuardar, text="Sí", width="6", font=("helvetica", 12, "bold"),
                           bg="LightSkyBlue1", fg="black", command=guardarResultado)
            btnSI.grid(row=3, column=0, padx=5, pady=5)

            btnNO = Button(frameGuardar, text="No", width="6", font=("helvetica", 12, "bold"),
                           bg="LightSkyBlue1", fg="black", command=clearSolucionador)
            btnNO.grid(row=4, column=0, padx=5, pady=5)

            btnLimpiarSolucion = Button(frameGuardar, text="Cerrar", width="15", font=("helvetica", 12, "bold"),
                                  bg="LightSkyBlue1", fg="black", command=clearSolucionador).grid(row=0, column=0, pady=15,
                                                                                             padx=80)

    framesSolucion = []
    text_var_solution = []
    entries_solution = []

    def calcularOperacion():

        operacion = str(entryOperacion.get())
        print(operacion)
        resultado = []
        textResult = ""

        frameConstructor1 = tkinter.Frame(frameInferior, width=600, height=300, highlightbackground="gray", highlightthickness=1)
        frameConstructor1.grid(row=1, column=0)

        frameGuardar = tkinter.Frame(frameInferior, width=600, height=300)
        frameGuardar.grid(row=2, column=0)

        # frames.append(frameEditor1)
        saveData(framesSolucion, frameGuardar)

        # frames.append(frameEditor1)
        saveData(framesSolucion, frameConstructor1)

        if "+" in operacion:

            pattern = "(\d+)?\+(\d+)"
            result = re.match(pattern, operacion)
            data = result.groups()
            data1 = int(data[0])
            data2 = int(data[1])

            array1 = variasMatrices[data1]
            array2 = variasMatrices[data2]
            resultado = operacionesMatrices.suma(array1,array2)

            textResult = "Suma entre la matriz " + str(data1) + " y la matriz " + str(data2)

        elif "-" in operacion:

            pattern = "(\d+)?\-(\d+)"
            result = re.match(pattern, operacion)
            data = result.groups()
            data1 = int(data[0])
            data2 = int(data[1])

            array1 = variasMatrices[data1]
            array2 = variasMatrices[data2]
            resultado = operacionesMatrices.resta(array1, array2)

            textResult = "Resta entre la matriz " + str(data1) + " y la matriz " + str(data2)

        elif "*" in operacion:

            pattern = "(\d+)?\*(\d+)"
            result = re.match(pattern, operacion)
            data = result.groups()
            data1 = int(data[0])
            data2 = int(data[1])

            array1 = variasMatrices[data1]
            array2 = variasMatrices[data2]
            resultado = operacionesMatrices.productoPunto(array1, array2)

            textResult = "Producto punto entre la matriz " + str(data1) + " y la matriz " + str(data2)

        else:
            print("Ingrese una operación válida.")

        print(resultado[0])
        print(resultado[0][0])
        print(resultado)

        filas = len(resultado[0])
        columnas = len(resultado)
        x2 = 0
        y2 = 0

        labelEditor = Label(frameInferior, text=textResult, width="40", font=("helvetica", 12, "bold"),
                            padx=5, pady=10, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
        labelEditor.grid(row=0, column=0)

        labelOpciones = Label(frameGuardar, text="¿Desea guardar esta matriz?", width="30",
                              font=("helvetica", 12, "bold"),
                              padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")

        for y in range(columnas):
            text_var_solution.append([])
            entries_solution.append([])
            fila = []
            columna = []
            matriz = []
            for x in range(filas):
                text_var_solution[y].append(StringVar())
                entryX = Entry(frameConstructor1, textvariable=text_var_solution[y][x], width=5, font=15)
                entries_solution[y].append(entryX)
                #entryX.insert(matrizSeleccionada[x][y])
                entries_solution[y][x].grid(column=x + x2, row=y + y2, padx=10, pady=10)
                # entries.append(entryX)
                entryX.insert(0, resultado[y][x])
                entryX.config(state=DISABLED)
                print(resultado[y][x])
                fila.append(entryX)
                x2 += 30
            columna.append(fila)
            matriz.append(columna)
            # append your StringVar and Entry

            y2 += 30
            x2 = 0

            def clearSolucionador():
                for i in range(len(framesSolucion)):
                    frameDestruir = framesSolucion[len(frames) - 1]
                    frameDestruir.destroy()
                frames.clear()

                entries_solution.clear()
                text_var_solution.clear()
                labelEditor.destroy()
                frameGuardar.destroy()
                #labelOpciones.destroy()
                #btnLimpiarSolucion.destroy()

            def guardarResultado():
                #variasMatrices.append(resultado)

                matrizResultado = []
                for i in range(columnas):
                    matrizResultado.append([])
                    for j in range(filas):
                        matrizResultado[i].append(resultado[i][j])
                        print("---------------------------------------")
                        print(resultado[i][j])
                variasMatrices.append(matrizResultado)

                actualizarMatrices()
                print("RESULTADO GUARDADO")
                clearSolucionador()

            labelOpciones.grid(row=2, column=0, pady= 10)

            btnSI = Button(frameGuardar, text="Sí", width="6", font=("helvetica", 12, "bold"),
                           bg="LightSkyBlue1", fg="black", command=guardarResultado)
            btnSI.grid(row=3, column=0, padx=5, pady=5)

            btnNO = Button(frameGuardar, text="No", width="6", font=("helvetica", 12, "bold"),
                           bg="LightSkyBlue1", fg="black", command=clearSolucionador)
            btnNO.grid(row=4, column=0, padx=5, pady=5)

            btnLimpiarSolucion = Button(frameGuardar, text="Cerrar", width="15", font=("helvetica", 12, "bold"),
                                  bg="LightSkyBlue1", fg="black", command=clearSolucionador).grid(row=0, column=0, pady=15,
                                                                                             padx=80)



    #BOTONES
    btnAddMatriz = Button(frameBotones, text="Añadir matriz", width="15", font=("helvetica", 12, "bold"),
                             bg="LightSkyBlue1", fg="black", command=abrirCreador).grid(row=0, column=0, pady=15, padx=80)


    btnEditarMatriz = Button(frameBotones, text="Editar matriz", width="15", font=("helvetica", 12, "bold"),
                             bg="LightSkyBlue1", fg="black", command=abrirEditor).grid(row=1, column=0, pady=15, padx=80)

    btnEliminarMatriz = Button(frameBotones, text="Eliminar matriz", width="15", font=("helvetica", 12, "bold"),
                             bg="LightSkyBlue1", fg="black", command=abrirEliminadorMatrices).grid(row=2, column=0, pady= 15, padx=80)

    btnVerMatriz = Button(frameBotones, text="Ver matriz", width="15", font=("helvetica", 12, "bold"),
                             bg="LightSkyBlue1", fg="black", command=abrirVisualizadorMatriz).grid(row=3, column=0, pady= 15, padx=80)

    btnActualizarMatrices = Button(frameBotones, text="Actualizar matrices", width="15", font=("helvetica", 12, "bold"),
                             bg="LightSkyBlue1", fg="black", command=actualizarMatrices).grid(row=4, column=0, pady= 10, padx=80)

    #BOTONES FUNCIONES

    btnCalcular = Button(frameOperacion, text="Calcular", width="10", font=("helvetica", 12, "bold"),
                              bg="LightSkyBlue1", fg="black", command=calcularOperacion)
    btnCalcular.grid(row=0, column=2, padx=10)

    btnDeterminante = Button(frameOperacionBotones, text="Determinante", width="10", font=("helvetica", 12, "bold"),
                              bg="LightSkyBlue1", fg="black", command= calcularDeterminante)
    btnDeterminante.grid(row=0, column=0, padx=10)

    btnInversa = Button(frameOperacionBotones, text="Inversa", width="10", font=("helvetica", 12, "bold"),
                              bg="LightSkyBlue1", fg="black", command=calcularInversa)
    btnInversa.grid(row=0, column=1, padx=10)

    btnTranspuesta = Button(frameOperacionBotones, text="Transpuesta", width="10", font=("helvetica", 12, "bold"),
                              bg="LightSkyBlue1", fg="black", command=calcularTranspuesta)
    btnTranspuesta.grid(row=0, column=2, padx=10)

    btnSalir = Button(frameOperacionBotones, text="Salir", width="10", font=("helvetica", 12, "bold"),
                            bg="LightSkyBlue1", fg="black", command=lambda:salir(root))
    btnSalir.grid(row=0, column=3, padx=10)