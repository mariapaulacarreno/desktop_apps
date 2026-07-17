from tkinter import *

# Ventana principal
ventana_principal = Tk()
ventana_principal.title("Bandera de Noruega")
ventana_principal.geometry("500x350")
ventana_principal.config(bg="white")
ventana_principal.resizable(0, 0)

# Frame principal de la bandera (rojo)
frame_1 = Frame(ventana_principal, bg="red", width=440, height=280)
frame_1.place(x=30, y=30)

# Cruz blanca 
Frame(frame_1, bg="white", width=60, height=280).place(x=100, y=0)
Frame(frame_1, bg="white", width=440, height=60).place(x=0, y=110)

# Cruz azul 
Frame(frame_1, bg="blue", width=30, height=280).place(x=115, y=0)
Frame(frame_1, bg="blue", width=440, height=30).place(x=0, y=125)

# Bucle principal
ventana_principal.mainloop()