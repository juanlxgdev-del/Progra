class Producto ():
    def __init__(self,nombre,precio_base,stock):
        self.nombre=nombre
        self.precio_base=precio_base
        self.stock=stock

    def aplicar_descuento(self,porcentaje):
        self.precio_base*=(1-porcentaje)
        print(f"El nuevo precio del prodcutro {self.nombre} es {self.precio_base}")

    def actualiza_stock(self,cantidad):
        if(self.stock+cantidad)<0:
            print("No hay suficiente stock")
        else:
            self.stock+=cantidad
            print(f"El nuevo stick de {self.nombre} es {self.stock}")

class Categoria():
    def __init__(self,nombre_categoria):
        self.nombre_categoria=nombre_categoria
        self.list=[]
    
    def agregar_producto(self,producto):
        self.list.append(producto)
        print(f"El producto {producto.nombre} se agrego a la lista")

    def valor_total_categoria(self):
        suma=0
        for m in self.list:
            suma+=m.precio_base*m.stock
        print(f"El precio total de la categoria {self.nombre_categoria} es {suma} pesos")
