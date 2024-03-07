import struct
import tkinter
from tkinter import *
from tkinter import messagebox

bina = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]


def flotante_a_binario(valor):
    val = struct.unpack('Q', struct.pack('d', valor))[0]
    return bina(val)


def binario_a_flotante(valor):
    hx = hex(int(valor, 2))
    return struct.unpack("d", struct.pack("q", int(hx, 16)))[0]


# Los flotantes están representados por el formato de punto flotante IEEE 754 que tiene una longitud de 64 bits

# flotate a binario
binstr = flotante_a_binario(13.265)
print('Binario de 13:')
print(binstr + '\n')
print(len(binstr))
print(type(binstr), "---> tipo")

# binario a flotnte
fl = binario_a_flotante(binstr)
print('Decimal de  ' + binstr)
print(fl)
print(type(fl), "---> tipo")


# -------------
def decimalBinario32(decimal):
    bin32 = float_to_bin32(float(decimal))
    return bin32
def float_to_bin32(num):
    bits, = struct.unpack('!I', struct.pack('!f', num))
    return "{:032b}".format(bits)

#-----

def binarioDecimal32():
    entrada = IEEE32Entry.get()
    signo = entrada[0]
    exponente = entrada[1:9]
    mantiza = entrada[9:23]
    binario = numero_to_str(signo, exponente, mantiza, 32)
    print(binario)
    numero = bin_to_float32(binario)
    return numero


def numero_to_str(signo, exponente, mantiza, bits):
    numero = ""
    if (bits == 32):
        if len(exponente) < 8:
            exponente += '0' * (8 - len(exponente))
        if len(mantiza) < 23:
            mantiza += '0' * (23 - len(mantiza))
            numero += signo
            numero += exponente
            numero += mantiza
    elif bits == 64:
        if len(exponente) < 11:
            exponente += '0' * (11 - len(exponente))
        if len(mantiza) < 52:
            mantiza += '0' * (52 - len(mantiza))
            numero += signo
            numero += exponente
            numero += mantiza
    return numero


def bin_to_float64(binary):
    return struct.unpack('d', struct.pack('Q', int(binary, 2)))[0]


def bin_to_float32(binary):
    return struct.unpack('!f', struct.pack('!I', int(binary, 2)))[0]


# -----------

def salir(roota):
    roota.destroy()
    import menuPrincipal
    menuPrincipal.main(roota)


def borrar():
    decimalEntry.delete(0, END)
    binariaEntry.delete(0, END)
    IEEE32Entry.delete(0, END)
    mantisa64Var.set("")
    signo64Var.set("")
    exponente64Var.set("")
    mantisa32Var.set("")
    signo32Var.set("")
    exponente32Var.set("")



def calcular():
    if decimalEntry.get() != "":
        decimal = float(decimalEntry.get())
        binariaEntry.insert(0, flotante_a_binario(decimal))
        variable = flotante_a_binario(decimal)
        signo64Var.set(variable[1])
        exponente64Var.set(variable[1:12])
        mantisa64Var.set(variable[13:63])
        otrica=str(decimalBinario32(decimal))
        IEEE32Entry.insert(0,otrica)
        signo32Var.set(otrica[0])
        exponente32Var.set(otrica[1:9])
        mantisa32Var.set(otrica[9:35])
    elif binariaEntry.get() != "":
        binario = str(binariaEntry.get())
        if len(binario) == 63:
            decimalEntry.insert(0, binario_a_flotante(binario))
        else:
            messagebox.showerror(message="Ingrese la cantidad correcta de números", title="Error")
    elif IEEE32Entry.get() != "":
        decimalEntry.insert(0, binarioDecimal32())
    else:
        messagebox.showwarning(message="Ingrese algun valor a calcular", title="Error")


# Interfaz gráfica
def main(roota):
    roota.destroy()
    roota=Tk()
    roota.title("Calculadora IEEE754 bit")
    roota.geometry("950x450")
    # Labels de la parte izquierda
    baseLabel = Label(roota, text="Base", width="15", font=("helvetica", 12, "bold"),
                      padx=5, pady=5, bg="LightSkyBlue2", fg="black", borderwidth=2, relief="groove")
    baseLabel.place(x=15, y=12)

    decimalLabel = Label(roota, text="Decimal", width="15", font=("helvetica", 12, "bold"),
                         padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    decimalLabel.place(x=15, y=48)

    binariaLabel = Label(roota, text="IEEE754 64 Bytes", width="15", font=("helvetica", 12, "bold"),
                         padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    binariaLabel.place(x=15, y=78)

    signoLabel = Label(roota, text="Signo", width="5", font=("helvetica", 12, "bold"),
                       padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    signoLabel.place(x=15, y=118)

    exponenteLabel = Label(roota, text="Exponente", width="8", font=("helvetica", 12, "bold"),
                           padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    exponenteLabel.place(x=110, y=118)

    mantisaLabel = Label(roota, text="Mantisa", width="8", font=("helvetica", 12, "bold"),
                         padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    mantisaLabel.place(x=322, y=118)

    signo32Label = Label(roota, text="Signo", width="5", font=("helvetica", 12, "bold"),
                         padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    signo32Label.place(x=15, y=265)

    exponente32Label = Label(roota, text="Exponente", width="8", font=("helvetica", 12, "bold"),
                             padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    exponente32Label.place(x=110, y=265)

    mantisa32Label = Label(roota, text="Mantisa", width="8", font=("helvetica", 12, "bold"),
                           padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    mantisa32Label.place(x=322, y=265)

    IEEE32Label = Label(roota, text="IEEE754 32 Bytes", width="15", font=("helvetica", 12, "bold"),
                        padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
    IEEE32Label.place(x=15, y=200)

    # Label de la parte derecha

    NumLabel = Label(roota, text="Numero", width="57", font=("helvetica", 12, "bold"),
                     padx=5, pady=5, bg="LightSkyBlue2", fg="black", borderwidth=2, relief="groove")
    NumLabel.place(x=180, y=12)
    global mantisa64Var,exponente64Var, signo64Var, signo32Var, exponente32Var, mantisa32Var
    # Campos de texto
    decimalVar = tkinter.IntVar()
    binariaVar = tkinter.DoubleVar()

    signo64Var = tkinter.StringVar()
    exponente64Var = tkinter.StringVar()

    mantisa64Var = tkinter.StringVar()

    signo32Var = tkinter.StringVar()
    exponente32Var = tkinter.StringVar()
    mantisa32Var = tkinter.StringVar()
    IEEE32Var = tkinter.DoubleVar()
    global decimalEntry
    decimalEntry = Entry(roota, textvariable=decimalVar, font=10, width=64)
    decimalEntry.place(x=180, y=53)
    global binariaEntry
    binariaEntry = Entry(roota, textvariable=binariaVar, font=10, width=64)
    binariaEntry.place(x=180, y=83)
    global signo64Entry
    signo64Entry = Entry(roota, textvariable=signo64Var, font=10, width=2, state="readonly")
    signo64Entry.place(x=83, y=123)
    global exponente64Entry
    exponente64Entry = Entry(roota, textvariable=exponente64Var, font=12, width=11, state="readonly")
    exponente64Entry.place(x=210, y=123)
    global mantisa64Entry
    mantisa64Entry = Entry(roota, textvariable=mantisa64Var, font=10, width=55, state="readonly")
    mantisa64Entry.place(x=420, y=123)
    global signo32Entry
    signo32Entry = Entry(roota, textvariable=signo32Var, font=10, width=2, state="readonly")
    signo32Entry.place(x=83, y=270)
    global exponente32Entry
    exponente32Entry = Entry(roota, textvariable=exponente32Var, font=10, width=11, state="readonly")
    exponente32Entry.place(x=210, y=270)
    global mantisa32Entry
    mantisa32Entry = Entry(roota, textvariable=mantisa32Var, font=10, width=55, state="readonly")
    mantisa32Entry.place(x=420, y=270)
    global IEEE32Entry
    IEEE32Entry = Entry(roota, textvariable=IEEE32Var, width=64, font=10)
    IEEE32Entry.place(x=182, y=205)

    # Botones

    btnCalcular = Button(roota, text="Calcular", width="8", font=("helvetica", 12, "bold"),
                         bg="LightSkyBlue2", fg="black", command=calcular)
    btnCalcular.place(x=150, y=400)

    btnBorrar = Button(roota, text="Borrar", width="8", font=("helvetica", 12, "bold"),
                       bg="LightSkyBlue2", fg="black", command=borrar)
    btnBorrar.place(x=325, y=400)

    btnSalir = Button(roota, text="Salir", width="8", font=("helvetica", 12, "bold"),
                      bg="LightSkyBlue2", fg="black", command=lambda:salir(roota))
    btnSalir.place(x=500, y=400)

    borrar()