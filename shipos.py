import tkinter as tk
from PIL import Image, ImageTk
def boton_clic():
    print("Hiciste Click!")
ventana = tk.Tk()
ventana.title("Botones en Tkinter")
boton = tk.Button(ventana, text="Haz clic aqui", command=boton_clic,
                font=("Comic Sans",30))
boton.pack(pady="20")
ventana = tk.Tk()
imagen = Image.open("images.jpg")
imagen = imagen.resize((800,600))
imagen_tk= ImageTk.PhotoImage(imagen)
label_imagen = tk.Label(ventana, image=imagen_tk)
label_imagen.pack(pady=20)
ventana.mainloop()

def actualizar_Etiqueta():
    nuevo_texto= entrada.get()
ventana = tk.Tk()
ventana.title("Etiquetas dinamicas")
entrada = tk.Entry(ventana,width=60)
entrada.pack(pady=10)
boton = tk.Button(ventana, text="texto inicial", font =("Arial", 12))
boton.pack()
etiqueta = tk.Label(ventana, text="Texto inicial", font=("Arial", 12))
etiqueta.pack(pady=10)

boton = tk.Button(ventana, text="Haz clic aqui", command=boton_clic,
                font=("Comic Sans",30))
boton.pack(pady="20")
imagen = Image.open("images.jpg")
imagen = imagen.resize((800,600))
imagen_tk= ImageTk.PhotoImage(imagen)
label_imagen = tk.Label(ventana, image=imagen_tk)
label_imagen.pack(pady=20)
ventana.mainloop()
