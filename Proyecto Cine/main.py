from models import *
# Peliculas
peliculas = [
    Pelicula(1, "Avatar", 192, "PG-13", "Ciencia Ficcion", "Un soldado infiltrado en el planeta Pandora"),
    Pelicula(2, "Titanic", 194, "PG-13", "Drama", "Historia de amor en el navio Titanic"),
    Pelicula(3, "Buscando a Nemo", 100, "G", "Animacion", "Un pez payaso cruza el oceano para encontrar a su hijo"),
    Pelicula(4, "Toy Story", 81, "G", "Animacion", "Los juguetes cobran vida cuando los humanos no estan"),
    Pelicula(5, "Mi Pobre Angelito", 103, "PG", "Comedia", "Un niño se queda solo en casa y debe protegerla de ladrones"),
    Pelicula(6, "E.T.", 115, "PG", "Ciencia Ficcion", "Un niño ayuda a un extraterrestre a regresar a su hogar"),
    Pelicula(7, "El Rey Leon", 88, "G", "Animacion", "Un cachorro de leon debe reclamar su lugar como rey"),
    Pelicula(8, "Los Pitufos", 103, "PG", "Animacion", "Las criaturas azules llegan a Nueva York"),
    Pelicula(9, "Paddington", 95, "PG", "Comedia", "Un oso de Peru busca un hogar en Londres"),
    Pelicula(10, "La Dama y el Vagabundo", 76, "G", "Animacion", "Historia de amor entre dos perros de diferentes clases"),
]

# Crear salas
salas = [
    Sala(1, "Sala 1", "Piso 1", "2D", 80, False),
    Sala(2, "Sala 2", "Piso 1", "3D", 80, False),
    Sala(3, "Sala 3", "Piso 2", "IMAX", 80, True),
    Sala(4, "Sala 4", "Piso 2", "2D", 70, False),
    Sala(5, "Sala 5", "Piso 1", "3D", 85, False),
    Sala(6, "Sala 6", "Piso 3", "IMAX", 90, True),
    Sala(7, "Sala 7", "Piso 2", "2D", 75, True),
    Sala(8, "Sala 8", "Piso 1", "3D", 80, True),
    Sala(9, "Sala 9", "Piso 3", "2D", 60, False),
    Sala(10, "Sala 10", "Piso 2", "3D", 80, False),
]

# Crear funciones
funciones = [
    Funcion(1, peliculas[0], salas[0], "14:00", 12.50),
    Funcion(2, peliculas[0], salas[1], "16:00", 14.00),
    Funcion(3, peliculas[1], salas[2], "18:00", 16.50),
    Funcion(4, peliculas[1], salas[0], "20:00", 14.50),
    Funcion(5, peliculas[2], salas[3], "15:30", 12.00),
    Funcion(6, peliculas[2], salas[4], "17:30", 13.50),
    Funcion(7, peliculas[3], salas[5], "19:30", 16.00),
    Funcion(8, peliculas[3], salas[1], "21:30", 14.00),
    Funcion(9, peliculas[4], salas[6], "16:15", 17.50),
    Funcion(10, peliculas[4], salas[2], "18:45", 16.50),
]

# Crear promociones
promociones = [
    Promo("PROMOARIZA", "20% descuento para los que han sobrevivido con Ariza", 20, "2026-03-31"),
    Promo("PROMOJIMMY", "15% descuento estudiantes", 15, "2026-03-31"),
    Promo("PROMONOVIOS", "25% descuento en pareja", 25, "2026-08-31"),
    Promo("PROMOFAMILIA", "30% descuento para grupos familiares", 30, "2026-12-31"),
    Promo("PROMOCALCULO", "35% descuento para estudiantes de cálculo", 35, "2026-09-30"),
    Promo("PROMOPRIMERSEMESTRE", "10% descuento para nuevos estudiantes", 10, "2026-04-30"),
    Promo("PROMOEMPRESA", "18% descuento para empleados de empresas", 18, "2026-05-31"),
    Promo("PROMOFINDE", "15% descuento fines de semana", 15, "2026-06-30"),
    Promo("PROMONAVIDAD", "40% descuento preventa navideña", 40, "2026-11-30"),
    Promo("PROMOCUMAÑO", "22% descuento mes de cumpleaños", 22, "2026-12-31"),
]

# Crear productos comida
productos = [
    Producto(1, "Palomitas Grandes", 8.50, 50),
    Producto(2, "Bebida Refrescante", 5.00, 75),
    Producto(3, "Hot Dog", 7.50, 30),
    Producto(4, "Nachos con Queso", 9.50, 40),
    Producto(5, "Agua Mineral", 4.00, 100),
    Producto(6, "Cerveza Artesanal", 7.00, 60),
    Producto(7, "Palomitas Saladas", 7.50, 45),
    Producto(8, "Refresco Light", 5.00, 80),
    Producto(9, "Perrito Completo", 8.50, 25),
    Producto(10, "Golosinas Variadas", 3.50, 120),
]

# Crear usuarios
usuarios = [
    Usuario(1, "Doom Slayer", "doom@infierno.com", "+1 555-666-7777"),
    Usuario(2, "Dante", "dante@devilmaycry.com", "+39 345 678 9012"),
    Usuario(3, "Leon S. Kennedy", "leon@bsaa.com", "+1 202-555-0199"),
    Usuario(4, "CJ", "cj@grovestreet.com", "+1 213-555-8923"),
    Usuario(5, "Michael De Santa", "michael@vapid.com", "+1 310-555-4721"),
    Usuario(6, "Franklin Clinton", "franklin@chop.com", "+1 323-555-1684"),
    Usuario(7, "Steve", "steve@minecraft.com", "+44 20 7946 0123"),
    Usuario(8, "Trevor Philips", "trevor@tpi.com", "+1 559-555-3287"),
    Usuario(9, "Nick", "nick@left4dead.com", "+1 702-555-2165"),
    Usuario(10, "Peter Parker", "spiderman@dailybugle.com", "+1 212-555-8976"),
]

# Crear empleados
empleados = [
    Empleado(1, "Natanael Cano", "nata@auracine.com", "6621234567", "EMP101", "ADMIN", "16:00-00:00"),
    Empleado(2, "Peso Pluma", "hassan@auracine.com", "3312345678", "EMP102", "TAQUILLERO", "18:00-02:00"),
    Empleado(3, "Luis Miguel", "elsol@auracine.com", "5551234567", "EMP103", "ADMIN", "20:00-04:00"),
    Empleado(4, "Christian Nodal", "nodal@auracine.com", "6371234567", "EMP104", "LIMPIEZA", "09:00-17:00"),
    Empleado(5, "Carín León", "carin@auracine.com", "6629876543", "EMP105", "TAQUILLERO", "10:00-18:00"),
    Empleado(6, "Juan Gabriel", "juanga@auracine.com", "6561112222", "EMP106", "ADMIN", "14:00-22:00"),
    Empleado(7, "Vicente Fernández", "chente@auracine.com", "3334445555", "EMP107", "LIMPIEZA", "06:00-14:00"),
    Empleado(8, "Thalía", "thalia@auracine.com", "5512223333", "EMP108", "TAQUILLERO", "08:00-16:00"),
    Empleado(9, "Junior H", "juniorh@auracine.com", "6645556666", "EMP109", "LIMPIEZA", "22:00-06:00"),
    Empleado(10, "Paulina Rubio", "pau@auracine.com", "5598887777", "EMP110", "TAQUILLERO", "11:00-19:00"),
]
# login
# login del cliente usando solo email
def login_usuario():
    global usuario_actual
    email=input("Email: ")
    for u in usuarios:
        if u.email==email:
            usuario_actual=u
            print("Bienvenido",u.nombre)
            return True
    print("Usuario no encontrado")
    return False

# login empleados y marcar asistencia
def login_empleado():
    global empleado_actual
    email=input("Email: ")
    for e in empleados:
        if e.email==email:
            empleado_actual=e
            print("Bienvenido",e.nombre,"-",e.rol)
            print(empleado_actual.marcar_entrada())
            return True
    print("Empleado no encontrado")
    return False

# usuario
# mostrar peliculas
def ver_peliculas():
    for i,p in enumerate(peliculas,1):
        print(i,"-",p)

# mostrar funciones y asientos disponibles
def ver_funciones():
    for i,f in enumerate(funciones,1):
        disp=f.calcular_asientos_disponibles()
        print(i,"-",f)
        print("Sala:",f.sala.nombre)
        print("Disponibles:",disp)
        print("Precio:",f.precio_base)
        print()

# alimentos del cine
def ver_alimentos():
    print("\nALIMENTOS DISPONIBLES")
    for p in productos:
        print("-",p)
    print()

# promociones disponibles
def ver_promos():
    print("PROMOCIONES")
    for p in promociones:
        print("-",p)

# reservar asientos
def reservar():
    ver_funciones()
    f=int(input("Funcion: "))-1
    if f<0 or f>=len(funciones):
        print("Funcion invalida")
        return
    cantidad=int(input("Cuantos asientos: "))
    funcion=funciones[f]
    reserva=usuario_actual.crear_reserva(funcion,cantidad)
    if reserva:
        print("Reserva creada")
        print("Asientos:",reserva.asientos)
        pagar=input("Pagar ahora? si/no ")
        if pagar=="si":
            reserva.confirmar_pago()
            print("Pago realizado")
            print(reserva.generar_ticket())
    else:
        print("No hay suficientes asientos")

# cancelar reserva
def cancelar():
    if not usuario_actual.reservas_activas:
        print("No tienes reservas")
        return
    for i,r in enumerate(usuario_actual.reservas_activas,1):
        print(i,"-",r)
    x=int(input("Cancelar cual: "))-1
    reserva=usuario_actual.reservas_activas[x]
    usuario_actual.cancelar_reserva(reserva.id_reserva)
    reserva.funcion.sala.liberar_asientos(reserva.asientos)
    print("Reserva cancelada")

# menu usuario
def menu_usuario():
    while True:
        print("\nCINE AURORA")
        print("1 Ver peliculas")
        print("2 Ver funciones")
        print("3 Ver alimentos")
        print("4 Ver promociones")
        print("5 Reservar asientos")
        print("6 Cancelar reserva")
        print("7 Salir")
        op=input("> ")
        if op=="1":ver_peliculas()
        elif op=="2":ver_funciones()
        elif op=="3":ver_alimentos()
        elif op=="4":ver_promos()
        elif op=="5":reservar()
        elif op=="6":cancelar()
        elif op=="7":break

# empleado
# agregar pelicula
def agregar_pelicula():
    nombre=input("Nombre: ")
    dur=int(input("Duracion: "))
    clas=input("Clasificacion: ")
    gen=input("Genero: ")
    sin=input("Sinopsis: ")
    nueva=Pelicula(len(peliculas)+1,nombre,dur,clas,gen,sin)
    peliculas.append(nueva)
    print("Pelicula agregada")

# crear funcion
def agregar_funcion():
    print("Peliculas:")
    for i,p in enumerate(peliculas,1):
        print(i,p)
    p=int(input("Pelicula: "))-1
    print("Salas:")
    for i,s in enumerate(salas,1):
        print(i,s)
    s=int(input("Sala: "))-1
    hora=input("Hora: ")
    precio=float(input("Precio: "))
    nueva=Funcion(len(funciones)+1,peliculas[p],salas[s],hora,precio)
    funciones.append(nueva)
    print("Funcion agregada")

# agregar promo
def agregar_promocion():
    cod=input("Codigo: ")
    desc=input("Descripcion: ")
    porc=int(input("Descuento %: "))
    fecha=input("Fecha fin: ")
    nueva=Promo(cod,desc,porc,fecha)
    promociones.append(nueva)
    print("Promo agregada")

# menu empleado
def menu_empleado():
    while True:
        print("\nMENU EMPLEADO")
        print("1 Ver funciones")
        print("2 Limpiar sala")
        print("3 Ver reservas")
        print("4 Agregar pelicula")
        print("5 Agregar funcion")
        print("6 Agregar promocion")
        print("7 Salir")
        op=input("> ")
        if op=="1":ver_funciones()
        elif op=="2":
            for i,s in enumerate(salas,1):
                print(i,s)
            x=int(input("Sala: "))-1
            print(salas[x].limpiar())
        elif op=="3":
            for u in usuarios:
                for r in u.historial_reservas:
                    print(r)
        elif op=="4":agregar_pelicula()
        elif op=="5":agregar_funcion()
        elif op=="6":agregar_promocion()
        elif op=="7":break

# menu
# entrada del sistema
def menu_principal():
    while True:
        print("\nCINE AURORA")
        print("1 Login usuario")
        print("2 Login empleado")
        print("3 Salir")
        op=input("> ")
        if op=="1":
            if login_usuario():menu_usuario()
        elif op=="2":
            if login_empleado():menu_empleado()
        elif op=="3":break

# iniciar programa
menu_principal()
