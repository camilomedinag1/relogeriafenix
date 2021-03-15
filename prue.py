from tkinter import *
import tkinter


def funcion():
    otra_ventana = tkinter.Toplevel(root)
    root.iconify()

root = tkinter.Tk()
boton = tkinter.Button(root, text="Abrir otra ventana", command=funcion)
boton.pack()
root.mainloop()