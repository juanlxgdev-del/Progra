#Antes de empezar, profe jimmy, se que no he sido el mejor alumno, asi que preparese para ver un codigo con errores
#Porque claro, al listo de juan luis le encanta hacerlo de ultima hora, asi que, tome asiento , leea lineas feas y
#Lea con atencion estos comentarios, porque la verdad solo falta media hora para entregar el proyecto
#y probablemente haya cosas medio raras aqui.

# Nota adicional profe Jimmy:
# Este codigo fue escrito mientras tambien estaba pensando en el examen de Ariza
# y en cálculo diferencial con Zamora, asi que mi cerebro estaba alternando
# entre matrices, derivadas y Python. No recomiendo esa combinacion.


class Persona:
    def __init__(self, id, nom, ema, tel):
        self.id = id
        self.nom = nom
        self.ema = ema
        self.tel = tel
        self.activo = False
        self.email = ema
        self.nombre = nom
        self.telefono = tel

    # Si este login funciona a la primera voy a fingir que siempre supe hacerlo
    # si no funciona… bueno, culpare al sueño acumulado.

    def login(self):
        self.activo = True
        return f"{self.nom} entró"

    def logout(self):
        self.activo = False
        return f'{self.nom} se fue'

    # Esta parte es para actualizar datos
    # sinceramente aqui la logica si la tengo clara
    # milagro considerando que llevo varias horas con esto.

    def actualizar_datos(self, nom, ema, tel):
        self.nom = nom
        self.ema = ema
        self.tel = tel
        self.email = ema
        self.nombre = nom
        self.telefono = tel
        return f"datos actualizados bla bla para {self.nom}"


# Aqui empieza Usuario
# en teoria esto hereda de Persona
# en la practica espero no haber roto nada con el super()

class Usuario(Persona):
    def __init__(self, id, nom, ema, tel):
        super().__init__(id, nom, ema, tel)
        self.puntos = 0
        self.reservas_viejas = []
        self.reservas_activas = []
        self.puntos_fidelidad = 0
        self.historial_reservas = []

    # Esta funcion crea reservas
    # no voy a mentir, esta parte me hizo pensar mas de lo que esperaba.

    def hacer_reserva(self, func, cant_asientos):

        if not self.activo:
            return None
        
        disponibles = func.dame_asientos_libres()

        # Si alguien pide mas asientos de los que hay, pues no se puede
        # logica simple, milagrosamente.

        if cant_asientos > disponibles:
            return None
        
        asientos_que_le_toco = func.dame_asientos(cant_asientos)

        precio_total = func.precio * cant_asientos

        res = Reserva(len(self.reservas_viejas) + 1, self, func, asientos_que_le_toco, precio_total)
        
        self.reservas_viejas.append(res)
        self.reservas_activas.append(res)
        self.historial_reservas.append(res)

        # puntos de fidelidad
        # creo que esto esta bien… CREO.

        self.puntos += int((func.precio * cant_asientos) / 10)
        self.puntos_fidelidad = self.puntos
        
        return res

    def crear_reserva(self, func, cant_asientos):
        return self.hacer_reserva(func, cant_asientos)

    # Mostrar puntos
    # aqui ya estaba medio cansado pero queria que funcionara.

    def ver_puntos(self):
        return f"{self.nom} tiene {self.puntos} puntos"
    
    # Cancelar reserva
    # esta parte la revise como tres veces porque me daba miedo romper algo.

    def cancelar(self, id_res):
        for r in self.reservas_activas:
            if r.id == id_res:
                r.estado = 'CANCELADA'
                self.reservas_activas.remove(r)
                self.puntos -= int(r.precio_total / 10)
                self.puntos_fidelidad = self.puntos
                return True
        return False

    def cancelar_reserva(self, id_res):
        return self.cancelar(id_res)

    def marcar_entrada(self):
        return self.login()


# Cambio de clase
# honestamente aqui ya estaba un poco confundido entre UML,
# clases, herencia y todo lo que vimos.

class Empleado(Persona):
    def __init__(self, id, nom, ema, tel, id_emp, rol, hor):
        super().__init__(id, nom, ema, tel)
        self.id_emp = id_emp
        self.rol = rol
        self.hor = hor
    
    def entrada(self):
        return f"{self.nom} ({self.rol}) llegó - {self.hor}"
    
    def marcar_entrada(self):
        return self.entrada()
    
    # Aqui solo el admin puede gestionar funciones
    # logica sencilla para no complicarme la vida mas de lo necesario.

    def puede_gestionar(self, funcion):
        if self.rol == "ADMIN":
            return f"Función {funcion.id} ({funcion.peli.titulo}) gestionada"
        return f'{self.nom} no puede'

    def gestionar_funciones(self, funcion):
        return self.puede_gestionar(funcion)


# Parte de peliculas
# despues de las matrices de Ariza esto se sintio hasta relajante.

class Pelicula:
    def __init__(self, id, tit, dur, clas, gen, sin):
        self.id = id
        self.titulo = tit
        self.dur = dur
        self.clas = clas
        self.gen = gen
        self.sin = sin
        self.duracion = dur
        self.obtener_sinopsis = lambda: self.sinopsis()
    
    def sinopsis(self):
        return f"{self.titulo}: {self.sin}"
    
    def es_para_niños(self):
        return self.clas in ["G", 'PG']
    
    def __str__(self):
        return f"{self.titulo} ({self.gen}) [{self.clas}]"


# Clase espacio general
# aqui empieza la parte de lugares dentro del cine.

class Espacio:
    def __init__(self, id, nom, ubi):
        self.id = id
        self.nom = nom
        self.ubi = ubi
        self.ok = True
        self.nombre = nom

    def esta_ok(self):
        return self.ok
    
    def limpiar(self):
        self.ok = True
        return f"{self.nom} limpio"


# Esta parte de las salas fue de las que mas tiempo me tomo entender
# no es dificil, pero cuando llevas muchas horas programando
# hasta un for parece sospechoso.

class Sala(Espacio):
    def __init__(self, id, nom, ubi, tip, cap, vip):
        super().__init__(id, nom, ubi)
        self.tip = tip
        self.cap = cap
        self.vip = vip
        self.asientos = self._generar()
        self.tipo = tip

    # Generar asientos automaticamente fue idea para no escribirlos uno por uno
    # porque si lo hacia manual probablemente seguiria aqui mañana.

    def _generar(self):
        asientos = {}
        filas = ['A', 'B', "C", 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        cols = 10
        
        for fila in filas:
            for col in range(1, cols + 1):
                asiento = f"{fila}{col}"
                asientos[asiento] = "ok"
        
        return asientos
    
    def libres(self):
        return sum(1 for e in self.asientos.values() if e == "ok")
    
    def dame_asientos(self, cant):
        sacados = []
        for key, val in self.asientos.items():
            if val == "ok" and len(sacados) < cant:
                self.asientos[key] = "ocupado"
                sacados.append(key)
        
        return sacados
    
    def dame_asientos_libres(self):
        return self.libres()
    
    # liberar asientos en caso de cancelacion

    def devolver_asientos(self, lista):
        for a in lista:
            if a in self.asientos:
                self.asientos[a] = "ok"

    def liberar_asientos(self, lista):
        return self.devolver_asientos(lista)
    
    def calcular_asientos_disponibles(self):
        return self.libres()

    def __str__(self):
        libres = self.libres()
        tipo_vip = "VIP" if self.vip else "normal"
        return f"Sala {self.nom} ({self.tip}) {tipo_vip} - {libres} libres"


# Cambio de seccion: comida
# honestamente aqui ya estaba un poco cansado
# pero queria que el sistema tuviera tambien esta parte.

class ZonaComida(Espacio):
    def __init__(self, id, nom, ubi):
        super().__init__(id, nom, ubi)
        self.productos = []
        self.stock = {}
        self.lista_productos = []
    
    def agregar(self, prod):
        self.productos.append(prod)
        self.lista_productos.append(prod)
        self.stock[prod.id] = prod.cant
    
    def vender(self, id_prod, cant):
        for p in self.productos:
            if p.id == id_prod and self.stock[id_prod] >= cant:
                self.stock[id_prod] -= cant
                p.cant -= cant
                return True
        return False
    
    def reponer(self, id_prod, cant):
        for p in self.productos:
            if p.id == id_prod:
                self.stock[id_prod] += cant
                p.cant += cant
                return True
        return False
    
    def __str__(self):
        return f"{self.nom} - {len(self.productos)} cosas"


class Producto:
    def __init__(self, id, nom, pre, cant):
        self.id = id
        self.nom = nom
        self.pre = pre
        self.cant = cant
    
    def __str__(self):
        return f"{self.nom} - ${self.pre} ({self.cant})"


# Funciones de cine
# en este punto del codigo ya llevaba bastante rato
# asi que si algo se ve raro probablemente era el sueño.

class Funcion:
    def __init__(self, id, peli, sala, hor, precio):
        self.id = id
        self.peli = peli
        self.sala = sala
        self.hor = hor
        self.precio = precio
        self.precio_base = precio
    
    def dame_asientos_libres(self):
        return self.sala.libres()
    
    def dame_asientos(self, cant):
        return self.sala.dame_asientos(cant)

    def calcular_asientos_disponibles(self):
        return self.dame_asientos_libres()
    
    def info(self):
        return f'{self.peli.titulo} - {self.hor} - Sala {self.sala.nom} - ${self.precio}'
    
    def __str__(self):
        return f"[{self.id}] {self.peli.titulo} - {self.hor}"


# Promociones
# esta parte la investigue un poco porque no estaba tan clara en mis notas.

class Promo:
    def __init__(self, cod, des, desc, exp):
        self.cod = cod
        self.des = des
        self.desc = desc
        self.exp = exp
    
    def aplicar(self, monto):
        return monto * (1 - self.desc / 100)
    
    def __str__(self):
        return f"{self.cod} - {self.desc}% - {self.des} (hasta: {self.exp})"


# Ultima clase grande: Reserva
# si el programa llega hasta aqui sin explotar ya es victoria personal.

class Reserva:
    def __init__(self, id, usr, func, asi, precio):
        self.id = id
        self.usr = usr
        self.func = func
        self.asi = asi
        self.precio_total = precio
        self.estado = 'PENDIENTE'
        self.asientos = asi
        self.costo_total = precio
        self.id_reserva = id
        self.funcion = func
    
    def pagar(self):
        if self.estado == "PENDIENTE":
            self.estado = "PAGADA"
            return True
        return False

    def confirmar_pago(self):
        return self.pagar()
    
    # generar ticket sencillo

    def ticket(self):
        ticket = f"""
    ================================
            TICKET DEL CINE
    ================================
    
    Reserva: {self.id}
    Cliente: {self.usr.nom}
    Email: {self.usr.ema}
    
    Pelicula: {self.func.peli.titulo}
    Sala: {self.func.sala.nom}
    Hora: {self.func.hor}
    Asientos: {', '.join(self.asi)}
    Total: ${self.precio_total:.2f}
    Estado: {self.estado}
    
    ================================
"""
        return ticket

    def generar_ticket(self):
        return self.ticket()
    
    def usar_promo(self, promo):
        desc = self.precio_total - promo.aplicar(self.precio_total)
        self.precio_total = promo.aplicar(self.precio_total)
        return desc
    
    def cambiar_estado(self, est):
        self.estado = est
    
    def __str__(self):
        return f"Reserva {self.id} - {self.usr.nom} - {self.func.peli.titulo} - {self.estado}"


# Fin del archivo
# Profe Jimmy, gracias por revisar el codigo.
# Despues de entregar esto me voy directo a estudiar
# para Ariza y calculo diferencial con Zamora.
# Deséeme suerte.

class Reserva:
    def __init__(self, id, usr, func, asi, precio):
        self.id = id
        self.usr = usr
        self.func = func
        self.asi = asi
        self.precio_total = precio
        self.estado = 'PENDIENTE'
    
    def pagar(self):
        if self.estado == "PENDIENTE":
            self.estado = "PAGADA"
            return True
        return False
    
    # generar ticket sencillo

    def ticket(self):
        ticket = f"""
    ================================
            TICKET DEL CINE
    ================================
    
    Reserva: {self.id}
    Cliente: {self.usr.nom}
    Email: {self.usr.ema}
    
    Pelicula: {self.func.peli.titulo}
    Sala: {self.func.sala.nom}
    Hora: {self.func.hor}
    Asientos: {', '.join(self.asi)}
    Total: ${self.precio_total:.2f}
    Estado: {self.estado}
    
    ================================
"""
        return ticket
    
    def usar_promo(self, promo):
        desc = self.precio_total - promo.aplicar(self.precio_total)
        self.precio_total = promo.aplicar(self.precio_total)
        return desc
    
    def cambiar_estado(self, est):
        self.estado = est
    
    def __str__(self):
        return f"Reserva {self.id} - {self.usr.nom} - {self.func.peli.titulo} - {self.estado}"


# Fin del archivo
# Profe Jimmy, gracias por revisar el codigo.
# Despues de entregar esto me voy directo a estudiar
# para Ariza y calculo diferencial con Zamora.

# Deséeme suerte.
