import tkinter as tk
from tkinter import messagebox

def opcion ():
    if var.get()==1:
        messagebox.showinfo("Eleccion","Te gustan los Tacos")
    elif var.get()==2:
        messagebox.showinfo("Eleccion","Te gustan las Clanchas")
    elif var.get()==3:
        messagebox.showinfo("Eleccion","Te gustan las Milanesa")
    elif var.get()==4:
        messagebox.showinfo("Eleccion","Te gustan las Pizza")

vent1=tk.Tk()
vent1.title("Radio Button")
vent1.geometry("300x400")
etiqueta1=tk.Label(vent1,text="¿Cual es tu comida favorita?")
etiqueta1.pack(pady=20)

var=tk.IntVar()
rad1=tk.Radiobutton(vent1,text="Tacos",variable=var,value=1)
rad1.pack()
rad2=tk.Radiobutton(vent1,text="Clanchas",variable=var,value=2)
rad2.pack()
rad3=tk.Radiobutton(vent1,text="Milanesa",variable=var,value=3)
rad3.pack()
rad4=tk.Radiobutton(vent1,text="Pizza",variable=var,value=4)
rad4.pack()

boton1=tk.Button(vent1,text="Verificar",command=opcion)
boton1.pack(pady=30)

vent1.mainloop()