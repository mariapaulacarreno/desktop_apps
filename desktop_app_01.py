from tkinter import *

# Ventana principal de la desktop app
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Sistemas Guanenta")

# tamaño de la ventana 
ventana_principal.geometry("500x500")

# color de fondo de la ventana
ventana_principal.config(bg="green")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# agregamos un objeto tipo Frame sobre la ventana
frame_1 = Frame(ventana_principal)
frame_1.config(bg="blue", width=480, height=240)
frame_1.place(x=10,y=10)

# Agregamos una imagen al frame
escudo = PhotoImage(file="ing/escudoColegio.png")
lb_escudo = Label(frame_1, image=escudo)
lb_escudo.place(x=10, y=20)

# bucle principal
ventana_principal.mainloop()



