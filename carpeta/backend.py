class Usuario():
    lista=[]
    def __init__(self,name,age,food):
        self.nombre=name
        self.edad=age
        self.comida=food
        if self not in Usuario.lista:
            Usuario.lista.append(self)

    def mostrar_datos(self):
        return f"El usuario {self.nombre} tiene {self.edad} y le gusta {self.comida}"

    @classmethod
    def mostrar_lista(cls):
        for u in Usuario.lista:
            print(u.mostrar_datos())