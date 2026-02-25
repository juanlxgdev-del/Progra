import tkinter as tk
from tkinter import messagebox

def ventanas():
    if vet1.get()==1:
        messagebox.showinfo("Ventana de informacion","Aca puedes escribir info al usuario")
    elif vet1.get()==2:
        messagebox.showwarning("Ventana de informacion","Esta es una advertencia")
    elif vet1.get()==3:
        messagebox.showerror("Ventana de informacion","Has cometido un error")
    elif vet1.get()==4:
        messagebox.askyesno("Ventana de informacion","Te gusta esta clase")
        if respuesta:
            messagebox.showinfo("Ventana de respuesta","Ta bien")
        else:
            messagebox.showinfo("Ventana de respuesta","No ta bien")
    elif vet1.get()==5:
        messagebox.askquestion("Ventana de informacion","¿Me darias tu alma?")
        if respuesta:
            messagebox.showinfo("Ventana de respuesta","Apoco si")
        else:
            messagebox.showinfo("Ventana de respuesta","¿Porque?")


vet1=tk.Tk()
vet1.title("Uso de las diferentes messagebox")
vet1.geometry("400x500")
vet1.config(bg="lightblue")
etiqueta1=tk.Label(vet1,text="Veremos el uso de las messagebox")
etiqueta1.pack(pady=20)

var=tk.IntVar()
rad1=tk.Radiobutton(vet1,text="Mostrar informacion",variable=var,value=1)
rad1.pack()
rad2=tk.Radiobutton(vet1,text="Advertencias",variable=var,value=2)
rad2.pack()
rad3=tk.Radiobutton(vet1,text="Error",variable=var,value=3)
rad3.pack()
rad4=tk.Radiobutton(vet1,text="Preguntar si o no",variable=var,value=4)
rad4.pack()
rad5=tk.Radiobutton(vet1,text="Preguntar aceptar o cancelar",variable=var,value=5)
rad5.pack()

boton1=tk.Button(vet1,text="Sacar ventana",command=ventanas)
boton1.pack(pady=30)

vet1.mainloop()