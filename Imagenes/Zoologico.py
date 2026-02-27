import tkinter as tk
from PIL import Image, ImageTk

def ventana():
    global ven1
    ven1 = tk.Tk()
    ven1.title("Reino animal")
    ven1.geometry("800x700")
    ven1.config(bg="white")
    
    ventana = tk.Tk()
    imagen = Image.open("1.jpg")   
    imagen = imagen.resize((800,600))
    imagen_tk= ImageTk.PhotoImage(imagen)
    label_imagen = tk.Label(ventana, image=imagen_tk)
    label_imagen.pack(pady=20)

    eti1 = tk.Label(ven1, text="Reino animal",font=("Comic Sans",30))
    eti1.pack()
    
    boton_ir_2 = tk.Button(ven1, text="Elefante", command=ventana_2)
    boton_ir_2.pack(pady=20)
    
    boton_ir_3 = tk.Button(ven1, text="Jirafa", command=ventana_3)
    boton_ir_3.pack(pady=20)
    
    boton_ir_4 = tk.Button(ven1, text="Castor", command=ventana_4)
    boton_ir_4.pack(pady=20)

    ven1.mainloop()

def destruir_ventana(ventana_actual):
    ventana_actual.destroy()
    ventana()
def destruir_ventana(ventana_2):
    ventana_2.destroy()
def destruir_ventana(ventana_3):
    ventana_3.destroy()
def destruir_ventana(ventana_4):
    ventana_4.destroy()
    
def ventana_2():
    global ven2

    ven2 = tk.Tk()
    ven2.title("Elefante")
    ven2.geometry("800x700")
    ven2.config(bg="grey")

    eti2 = tk.Label(ven2, text="Elefante")
    eti2.pack()
    
    boton2 = tk.Button(ven2, text="Regresar",command=lambda: destruir_ventana(ven2))
    boton2.pack(pady=20)

    ven2.mainloop()

def ventana_3():
    global ven3
    ven3 = tk.Tk()
    ven3.title("Jirafa")
    ven3.geometry("800x700")
    ven3.config(bg="yellow")

    eti3 = tk.Label(ven3, text="Jirafa")
    eti3.pack()

    boton3 = tk.Button(ven3, text="Regresar",command=lambda: destruir_ventana(ven3))
    boton3.pack(pady=20)

    ven3.mainloop()

def ventana_4():
    global ven4
    ven4 = tk.Tk()
    ven4.title("Castor")
    ven4.geometry("800x700")
    ven4.config(bg="brown")

    eti4 = tk.Label(ven4, text="Castor")
    eti4.pack()

    boton4 = tk.Button(ven4, text="Regresar",command=lambda: destruir_ventana(ven4))
    boton4.pack(pady=20)

    ven4.mainloop()

ventana()