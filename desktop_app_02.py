from tkinter import *
from tkinter import messagebox

# ------------------------------------------
# funciones de la app
# ------------------------------------------
def salir():
    messagebox.showinfo("Suma 1.0","hizo click en el boton salir")
    ventana_principal.destroy()

def borrar():
    messagebox.showinfo("Suma 1.0","los datos seran borrados")
    x.set("")
    y.set("")
    t_resultados.delete("1.0", "end")

def sumar():
    messagebox.showinfo("Suma 1.0","hizo click en el boton sumar")
    z=int(entry_x.get()) + int(entry_y.get())
    t_resultados.insert(INSERT, "la suma de " + entry_x.get() + " y " + entry_y.get()
    + " casi siempre es " + str(z) + "\n")

# ------------------------------------------
# configuracion ventana principal
# ----------------------------------
# Ventana principal de la desktop app
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Sistemas Guanentá")

# tamaño de la ventana 
ventana_principal.geometry("500x500")

# color de fondo a la ventana
ventana_principal.config(bg="black")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# ------------------------------------------
# variables globales de la app
# ------------------------------------------
x=StringVar()
y=StringVar()

# ------------------------------------------
# Frame entrada de datos
# ------------------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="green", width=480, height=240)
frame_entrada.place(x=10,y=10)

# Agregamos una imagen al frame
escudo = PhotoImage(file="ing/escudoColegio.png")
lb_escudo = Label(frame_entrada, image=escudo)
lb_escudo.place(x=10, y=20)

# label para titulo de la app
titulo=Label(frame_entrada, text="Suma numeros enteros")
titulo.config(bg="yellow", fg="blue", font=("Arial", 16))
titulo.place(x=220, y=20)

aviso=Label(frame_entrada, text="ingrese 5 digitos para cada variable")
aviso.config(bg="yellow", fg="blue", font=("Arial", 12))
aviso.place(x=205, y=50)

# label para titulo de la app
lb_x=Label(frame_entrada, text="X=")
lb_x.config(bg="yellow", fg="blue", font=("Arial", 16))
lb_x.place(x=180, y=90)

entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(bg="white", fg="black", font=("Times New Roman",16))
entry_x.focus_set()
entry_x.place(x=220, y=90, width=100, height=30)

lb_y=Label(frame_entrada, text="Y=")
lb_y.config(bg="yellow", fg="blue", font=("Arial", 16))
lb_y.place(x=180, y=140)

entry_y = Entry(frame_entrada, textvariable=y)
entry_y.config(bg="white", fg="black", font=("Times New Roman",16))
entry_y.place(x=220, y=140, width=100, height=30)
# ------------------------------------------
# Frame operaciones
# ------------------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="green", width=480, height=120)
frame_operaciones.place(x=10,y=260)

# boton para sumar
bt_sumar = Button(frame_operaciones, text="Sumar", command=sumar)
bt_sumar.place(x=45,y =45, width=100, height=30)

# boton para borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=180,y =45, width=100, height=30)

# boton para salir
bt_salir = Button(frame_operaciones, text="Salir", command=salir)
bt_salir.place(x=315,y =45, width=100, height=30)

# ------------------------------------------
# Frame resultados
# ------------------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="green", width=480, height=100)
frame_resultados.place(x=10,y=390)

# area de texto para mostrar resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="yellow", fg="black", font=("Arial",16))
t_resultados.place(x=10, y=10, width=460, height=80)

# bucle principal
ventana_principal.mainloop()