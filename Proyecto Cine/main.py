from models import *

# PELICULAS
peliculas = [
    Pelicula(1, "Zootopia 2", 105, "A", "Animacion", "Continuacion de Zootopia"),
    Pelicula(2, "Kimetsu no yaiba", 100, "B", "Animacion", "Demon Slayer pelicula"),
    Pelicula(3, "Lejos de ti", 180, "A", "Drama", "Drama romantico intenso"),
    Pelicula(4, "Spiderman", 130, "B", "Accion", "El hombre arana regresa"),
    Pelicula(5, "Avengers", 190, "B", "Accion", "Los vengadores se reúnen"),
    Pelicula(6, "GHOST", 70, "C", "Terror", "Historias de suspenso"),
    Pelicula(7, "rOBOTS", 30, "A", "Animacion", "Robots y su mundo"),
    Pelicula(8, "Glowbert", 110, "A", "Animacion", "Una aventura brillante"),
    Pelicula(9, "Viaje de Chihiro", 65, "A", "Animacion", "Viaje magico al otro mundo"),
    Pelicula(10, "Castillo vagabundo", 88, "A", "Animacion", "El castillo se mueve"),
]

# SALAS
salas = [
    Sala(1, "04", "IMAX", 100, True),
    Sala(2, "05", "3D", 90, True),
    Sala(3, "06", "2D", 80, False),
    Sala(4, "07", "2D", 80, False),
    Sala(5, "08", "3D", 85, False),
    Sala(6, "09", "IMAX", 95, True),
    Sala(7, "10", "2D", 75, False),
    Sala(8, "11", "3D", 80, False),
    Sala(9, "12", "2D", 60, False),
    Sala(10, "13", "3D", 70, False),
]

# FUNCIONES
funciones = [
    Funcion(101, peliculas[0], salas[0], "14:00", 150),
    Funcion(102, peliculas[0], salas[1], "16:00", 140),
    Funcion(103, peliculas[1], salas[2], "18:00", 130),
    Funcion(104, peliculas[1], salas[3], "20:00", 140),
    Funcion(105, peliculas[2], salas[4], "15:30", 160),
    Funcion(106, peliculas[2], salas[5], "17:30", 170),
    Funcion(107, peliculas[3], salas[6], "19:30", 150),
    Funcion(108, peliculas[3], salas[7], "21:30", 140),
    Funcion(109, peliculas[4], salas[8], "16:15", 180),
    Funcion(110, peliculas[4], salas[9], "18:45", 160),
]

# PROMOCIONES
promociones = [
    Promocion("PROMO_ESTUDIANTE", "20% estudiantes", 20, "2026-05-31"),
    Promocion("PROMO_PAREJA", "25% en pareja", 25, "2026-08-31"),
    Promocion("PROMO_FAMILIA", "30% familias", 30, "2026-12-31"),
    Promocion("PROMO_LUNES", "15% los lunes", 15, "2026-06-30"),
    Promocion("PROMO_MATINE", "10% matinés", 10, "2026-07-31"),
    Promocion("PROMO_SENIOR", "20% mayores", 20, "2026-09-30"),
    Promocion("PROMO_CUMPLEAÑOS", "35% cumpleaños", 35, "2026-12-31"),
    Promocion("PROMO_REFERIDO", "12% referido", 12, "2026-04-30"),
    Promocion("PROMO_CARNET", "18% carnet joven", 18, "2026-08-31"),
    Promocion("PROMO_FIDELIDAD", "5% fidelidad", 5, "2026-10-31"),
]

# PRODUCTOS
productos = [
    Producto(1, "Palomitas", 85, 10),
    Producto(2, "Refresco", 45, 10),
    Producto(3, "Nachos", 70, 10),
    Producto(4, "HotDog", 60, 10),
    Producto(5, "Chocolates", 35, 10),
    Producto(6, "Agua", 30, 10),
    Producto(7, "Gomitas", 25, 10),
    Producto(8, "Pizza", 90, 10),
    Producto(9, "Crepa", 55, 10),
    Producto(10, "Combo1", 250, 10),
]

# ZONA COMIDA
zona = ZonaComida(1, "Dulceria nwn", productos)

# USUARIOS
usuarios = [
    Usuario(1, "Jax", "jax@gmail.com", "3535"),
    Usuario(2, "Pomni", "pompom@gmail.com", "36546"),
    Usuario(3, "Ragatha", "ragaa@gmail.com", "65765"),
    Usuario(4, "Zooble", "zooble@gmail.com", "45677"),
    Usuario(5, "Gangle", "loveanime@gmail.com", "87568"),
    Usuario(6, "Kinger", "kinger@gmail.com", "5346"),
    Usuario(7, "Majo", "majitoo@gmail.com", "734667"),
    Usuario(8, "Rafa", "rafaelf@gmail.com", "823418"),
    Usuario(9, "Osvaldo", "osvaldof@gmail.com", "75348"),
    Usuario(10, "Andree", "andreelet@gmail.com", "928485"),
]

# EMPLEADOS
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
usuarioActual = None
empleadoActual = None

# LOGIN
def loginUsuario():
    global usuarioActual
    email = input("Email: ")
    for u in usuarios:
        if u.email == email:
            usuarioActual = u
            u.login()
            return True
    print("[ERROR]: Usuario no encontrado")
    return False

def loginEmpleado():
    global empleadoActual
    email = input("Email: ")
    for e in empleados:
        if e.email == email:
            empleadoActual = e
            e.login()
            print(empleadoActual.marcarEntrada())
            return True
    print("[ERROR]: Empleado no encontrado")
    return False

# USUARIO
def verPeliculas():
    print("\n--- CARTELERA ---")
    for p in peliculas:
        print(p)
    print()

def verFunciones():
    print("\n--- FUNCIONES ---")
    for f in funciones:
        print(f, "| Sala:", f.sala.nombre, "| Disponibles:", f.sala.obtenerLibres(), "| Precio: $", f.precio)

def verProductos():
    print("\n--- MENU DULCERIA ---")
    for p in zona.productos:
        print(p)

def verPromos():
    print("\n--- PROMOCIONES ---")
    for p in promociones:
        print(p)

def reservar():
    verFunciones()
    try:
        f = int(input("\nFuncion: ")) - 101
        cantidad = int(input("Asientos: "))
        funcion = funciones[f]
        reserva = usuarioActual.crearReserva(funcion, cantidad)
        
        if reserva:
            print("[SISTEMA]: Boletos apartados")
            print("Asientos:", reserva.asientos)
            
            # Comida
            print("\n¿Comida? (pon ID o 'n'): ", end="")
            opc = input()
            if opc != 'n':
                precio = zona.venderPorId(int(opc))
                if precio > 0:
                    reserva.comida += precio
                    print(">> Comida: $", reserva.comida)
            
            # Promo
            print("¿Codigo promocional? (s/n): ", end="")
            if input().lower() == 's':
                cod = input("Codigo: ")
                for p in promociones:
                    if p.codigo == cod:
                        reserva.precio = p.aplicar(reserva.precio)
                        print("[EXITO]: Descuento aplicado")
                        break
            
            # Pago
            print("¿Pagar? (s/n): ", end="")
            if input().lower() == 's':
                reserva.estado = "PAGADA"
                print(reserva.generarTicket())
        else:
            print("[ERROR]: No hay asientos")
    except:
        print("[ERROR]: Entrada invalida")

def menuUsuario():
    while True:
        print("\n" + "="*30)
        print("CINE")
        print("="*30)
        print("1 Ver peliculas")
        print("2 Ver funciones")
        print("3 Ver comida")
        print("4 Ver promociones")
        print("5 Reservar")
        print("6 Ver puntos")
        print("7 Salir")
        op = input("> ")
        
        if op == "1":
            verPeliculas()
        elif op == "2":
            verFunciones()
        elif op == "3":
            verProductos()
        elif op == "4":
            verPromos()
        elif op == "5":
            reservar()
        elif op == "6":
            print(f"\nPuntos: {usuarioActual.puntosFidelidad}")
        elif op == "7":
            usuarioActual.logout()
            break

# EMPLEADO
def agregarPelicula():
    titulo = input("Titulo: ")
    duracion = int(input("Duracion: "))
    clasif = input("Clasificacion: ")
    genero = input("Genero: ")
    sinopsis = input("Sinopsis: ")
    nueva = Pelicula(len(peliculas) + 1, titulo, duracion, clasif, genero, sinopsis)
    peliculas.append(nueva)
    print("[EXITO]: Pelicula agregada")

def agregarFuncion():
    print("\nPeliculas:")
    for i, p in enumerate(peliculas, 1):
        print(i, p.titulo)
    p = int(input("Pelicula: ")) - 1
    
    print("Salas:")
    for i, s in enumerate(salas, 1):
        print(i, s.nombre)
    s = int(input("Sala: ")) - 1
    
    hora = input("Hora: ")
    precio = int(input("Precio: "))
    nueva = Funcion(len(funciones) + 101, peliculas[p], salas[s], hora, precio)
    funciones.append(nueva)
    print("[EXITO]: Funcion agregada")

def agregarPromocion():
    cod = input("Codigo: ")
    desc = input("Descripcion: ")
    porc = int(input("Descuento %: "))
    fecha = input("Fecha fin: ")
    nueva = Promocion(cod, desc, porc, fecha)
    promociones.append(nueva)
    print("[EXITO]: Promo agregada")

def menuEmpleado():
    while True:
        print("\n" + "="*30)
        print("MENU EMPLEADO")
        print("="*30)
        print("1 Ver funciones")
        print("2 Agregar pelicula")
        print("3 Agregar funcion")
        print("4 Agregar promocion")
        print("5 Ver reservas")
        print("6 Salir")
        op = input("> ")
        
        if op == "1":
            verFunciones()
        elif op == "2":
            agregarPelicula()
        elif op == "3":
            agregarFuncion()
        elif op == "4":
            agregarPromocion()
        elif op == "5":
            for u in usuarios:
                if u.reservas:
                    print(f"\n{u.nombre}:")
                    for r in u.reservas:
                        print(f"  {r}")
        elif op == "6":
            empleadoActual.logout()
            break

# MENU PRINCIPAL
def menuPrincipal():
    while True:
        print("\n" + "="*30)
        print("BIENVENIDO CINE AURORA")
        print("="*30)
        print("1 Login usuario")
        print("2 Login empleado")
        print("3 Salir")
        op = input("> ")
        
        if op == "1":
            if loginUsuario():
                menuUsuario()
        elif op == "2":
            if loginEmpleado():
                menuEmpleado()
        elif op == "3":
            break

menuPrincipal()