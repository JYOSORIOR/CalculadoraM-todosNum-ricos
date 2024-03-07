from tkinter import Tk, PhotoImage, Label, Button
# from tkinter import PhotoImage

def mainIni(root):
    root.destroy()
    import menuPrincipal
    menuPrincipal.main(root)

app = Tk()
app.title("calcBlue")
app.geometry("500x350")

# Lees la imagen:
# He colocado ruta relativa, es decir, la imagen a la misma
# altura de la aplicación. Si prefieres, puedes colocar una
# ruta absoluta.
imagen = PhotoImage(file = "imagenLogo.png")

# Con Label y la opción image, puedes mostrar una imagen en el widget:
background = Label(image = imagen, text = "Imagen S.O de fondo")

# Con place puedes organizar el widget de la imagen posicionandolo
# donde lo necesites (relwidth y relheight son alto y ancho en píxeles):
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)


# Por defecto el fondo es blaco. Accediendo al método config
# de Label podrías, por ejemplo, establecer un color de fondo distinto:
# background.config(bg = "gray")

btnGraficar = Button(app, text="→",width="3", font=("helvetica", 10, "bold"),bg="ivory2", fg="black", command=lambda:mainIni(app))
btnGraficar.place(x=450, y=300)

app.mainloop()
#0.5*x*exp(-x**2*0.5)+cos(3.1415926*sqrt(x))