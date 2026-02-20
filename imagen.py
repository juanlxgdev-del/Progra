import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Imagen en Tkinter")
imagen = Image.open("images.jpg")
imagen = imagen.resize((400,200))
imagen_tk= ImageTK.PhotoImage(imagen)
label_imagen = tk.Label(root, image=imagen_tk)
label_imagen.pack(pady=20)

root.mainloop()

ven1 = tk.Tk()
ven1.title("Mi primera aplicacion con Tkinter")
ven1.geometry("600x450")

etiqueta = tk.Label(ven1,
                    text="Hola, grupo de programacion basica!",
                    font=("Arial", 14, "bold"),
                    fg="black",
                    bg="yellow",
                    padx=20,
                    pady=10)
etiqueta.place(x=100, y=50)

etiqueta2 = tk.Label(ven1,
                     text="Mi nombre es Juan",
                     font=("Arial", 12, "bold"),
                     padx=20,
                     pady=10)
etiqueta2.place(x=100, y=150)

etiqueta3 = tk.Label(ven1,
                     text="Mi comida favorita son los tacos al pastor",
                     font=("Arial", 11, "bold"),
                     padx=20,
                     pady=10)
etiqueta3.place(x=100, y=250)

etiqueta4 = tk.Label(ven1,
                     text="Mi animal favorito son los perros",
                     font=("Arial", 11, "bold"),
                     padx=20,
                     pady=10)
etiqueta4.place(x=100, y=350)
ven1.mainloop()





