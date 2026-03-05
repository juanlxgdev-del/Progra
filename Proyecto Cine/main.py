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

# Crear zona de comida
zona_comida = ZonaComida(1, "Concesion Principal", "Entrada principal")
for productoo in productos:
    zona_comida.agregar_producto(productoo)

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

# Variables chachipistachis para el manejo de sesiones (ayuda profe jimmy, esto esta hecho horrible)
usuario_actual = None
empleado_actual = None

def login_usuario():
    global usuario_actual
    
    print("\n" + "="*60)
    print("LOGIN USUARIO")
    print("="*60)
    emaill = input("Ingresa tu email: ")
    
    for i in range(len(usuarios)):
        if usuarios[i].email == emaill:
            print("Bienvendiio " + usuarios[i].nombre)
            usuarios[i].login()
            usuario_actual = usuarios[i] # Arreglo discreto: si no lo asignaba, lo de abajo reventaba
            return True  
    return False

def login_empleado():
    global empleado_actual
    
    print("\n" + "="*60)
    print("LOGIN EMPLEADO")
    print("="*60)
    emaill = input("Ingresa tu email: ")
    
    for i in range(len(empleados)):
        if empleados[i].email == emaill:
            print(f"Bienvendiio " + empleados[i].nombre + " (" + empleados[i].rol + ")")
            empleados[i].login()
            empleado_actual = empleados[i] # Otro fix necesario para que corra
            return True

    print("Email no encontrado")
    return False

# ===== MENU USUARIO =====
def menu_ver_peliculas():
    print("\n" + "="*60)
    print("PELICULAS DISPONIBLES")
    print("="*60)
    for i, peliculaa in enumerate(peliculas, 1):
        print(f"{i}. {peliculaa}")
        print(f"   Duracion: {peliculaa.duracion} minutos")
        print(f"   Sinopsis: {peliculaa.obtener_sinopsis()}")
        print()

def menu_ver_funciones():
    print("\n" + "="*60)
    print("FUNCIONES DISPONIBLES")
    print("="*60)
    for i, funcionn in enumerate(funciones, 1):
        disponibless = funcionn.calcular_asientos_disponibles()
        print(f"{i}. {funcionn}")
        print(f"   Sala: {funcionn.sala.nombre} ({funcionn.sala.tipo})")
        print(f"   Asientos disponibles: {disponibless}")
        print(f"   Precio: ${funcionn.precio_base}")
        print()

def menu_ver_alimentos():
    print("\n" + "="*60)
    print(f"ALIMENTOS - {zona_comida.nombre}")
    print("="*60)
    for productoo in zona_comida.lista_productos:
        print(f"- {productoo}")
    print()

def menu_realizar_reserva():
    if not usuario_actual:
        print("Debes iniciar sesion")
        return
    
    menu_ver_funciones()

# Seleccionar función
    entrada_funcion = input("Selecciona una funcion (numero): ")
    if entrada_funcion.isdigit():
        funcion_idx = int(entrada_funcion) - 1
        if funcion_idx >= 0 and funcion_idx < len(funciones):
            funcionn = funciones[funcion_idx]
        
        # Cantidad de asientos
        entrada_cantidad = input("Cantidad de asientos: ")
        if entrada_cantidad.isdigit():
            cantidadd = int(entrada_cantidad)
            
            reservaa = usuario_actual.crear_reserva(funcionn, cantidadd)
            
            if reservaa:
                print("\nReserva creada exitosamente")
                print("ID Reserva: " + str(reservaa.id_reserva)) # fix crucial
                print("Asientos: " + ", ".join(reservaa.asientos))
                print("Costo: $" + str(reservaa.costo_total))
                
                confirmarr = input("\nDeseas confirmar el pago? (si/no): ")
                if confirmarr.lower() == "si":
                    reservaa.confirmar_pago()
                    print("Pago confirmado")
                    print(reservaa.generar_ticket())
                else:
                    print("No hay suficientes asientos disponibles")
            else:
                print("Cantidad invalida")
        else:
            print("Opcion invalida")
    else:
        print("Opcion invalida")

def menu_cancelar_reserva():
    if not usuario_actual: print("Debes iniciar sesion"); return
    if not usuario_actual.reservas_activas: print("No tienes reservas activas"); return

    print("\n" + "="*60 + "\nTUS RESERVAS\n" + "="*60)
    i=1
    for r in usuario_actual.reservas_activas: print(str(i) + ". " + str(r)); i+=1

    e = input("Selecciona reserva a cancelar (numero): ")
    if e.isdigit():
        idx = int(e)-1
        if 0<=idx<len(usuario_actual.reservas_activas):
            r = usuario_actual.reservas_activas[idx]
            usuario_actual.cancelar_reserva(r.id_reserva)
            r.funcion.sala.liberar_asientos(r.asientos)
            print("Reserva cancelada exitosamente")
        else: print("Numero invalido")
    else: print("Error en la cancelacion")

def menu_mis_datos():
    if not usuario_actual:
        print("Debes iniciar sesion")
        return
    
    print("\n" + "="*60)
    print("MIS DATOS")
    print("="*60)
    print(f"Nombre: {usuario_actual.nombre}")
    print(f"Email: {usuario_actual.email}")
    print(f"Telefono: {usuario_actual.telefono}")
    print(f"Puntos de fidelidad: {usuario_actual.puntos_fidelidad}")
    print(f"Reservas activas: {len(usuario_actual.reservas_activas)}")
    print()

def menu_usuario_principal():
    while 1:
        print("\n" + "="*60 + "\nMENU USUARIO - " + usuario_actual.nombre + "\n" + "="*60 + "\n1. Ver peliculas\n2. Ver funciones\n3. Ver alimentos\n4. Realizar reserva\n5. Cancelar reserva\n6. Ver mis datos\n7. Cerrar sesion\n" + "="*60)
        
        o = input("Selecciona opcion: ")
        
        if o=="1": menu_ver_peliculas()
        elif o=="2": menu_ver_funciones()
        elif o=="3": menu_ver_alimentos()
        elif o=="4": menu_realizar_reserva()
        elif o=="5": menu_cancelar_reserva()
        elif o=="6": menu_mis_datos()
        elif o=="7": usuario_actual.logout(); print("Sesion cerrada"); break
        else: print("Opcion invalida")

#Agradecimientos especiales para el canal de Marco Vega Gallardo, si profe, me robe ideas de youtube

# MENU EMPLEADO
def menu_empleado_marcar_entrada():
    print("\n" + empleado_actual.marcar_entrada())

def menu_empleado_gestionar_funciones():
    print("\n" + "="*60 + "\nGESTIONAR FUNCIONES\n" + "="*60)
    i=1
    for f in funciones:
        print(str(i) + ". " + str(f) + "\n   Asientos disponibles: " + str(f.calcular_asientos_disponibles()))
        i+=1
    
    e = input("Selecciona una funcion (numero): ")
    if e.isdigit():
        idx = int(e)-1
        if 0<=idx<len(funciones):
            print(empleado_actual.gestionar_funciones(funciones[idx]))
        else: print("Opcion invalida")
    else: print("Opcion invalida") #aqui si, no tengo ningun comentario, me lo robe de https://www.youtube.com/watch?v=B5Q-hKUoceQ&pp=ygUeUHl0aG9uIGluZGljZXMgbGlzdGFzIGVzcGHDsW9s, mejor conocido como pildoras magicas

def menu_empleado_limpiar_sala():
    print("\n" + "="*60 + "\nLIMPIAR SALA\n" + "="*60)
    i=1
    for s in salas:
        print(str(i) + ". " + str(s))
        i+=1
    
    e = input("Selecciona sala a limpiar (numero): ")
    if e.isdigit():
        idx = int(e)-1#en efecto, de donde me robe esto, de codificando y portofoliohttps://www.youtube.com/watch?v=LVI9zw3xCUE&pp=ygUXUHl0aG9uIGlzZGlnaXQoKSBtZXRvZG8%3D:
        if 0<=idx<len(salas):
            print(salas[idx].limpiar())
        else: print("Opcion invalida")
    else: print("Opcion invalida")

def menu_empleado_ver_reservas():
    print("\n" + "="*60 + "\nRESERVAS DEL SISTEMA\n" + "="*60)
    
    totall=0
    for u in usuarios:
        if u.historial_reservas:
            print("\nUsuario: " + u.nombre)
            for r in u.historial_reservas:
                print("  - " + str(r))
                totall+=1
    
    if totall==0: print("No hay reservas en el sistema")

def menu_empleado_principal():
    continuarr = 1
    while continuarr:
        print("\n" + "="*60 + "\nMENU EMPLEADO - " + empleado_actual.nombre + "\nRol: " + empleado_actual.rol + "\n" + "="*60 + "\n1. Marcar entrada\n2. Gestionar funciones\n3. Limpiar sala\n4. Limpiar zona de comida\n5. Ver reservas\n6. Cerrar sesion\n" + "="*60)
        
        o = input("Selecciona opcion: ")
        
        if o=="1": menu_empleado_marcar_entrada()
        elif o=="2": menu_empleado_gestionar_funciones()
        elif o=="3": menu_empleado_limpiar_sala()
        elif o=="4": menu_empleado_ver_reservas()
        elif o=="5": empleado_actual.logout(); print("Sesion cerrada"); continuarr = 0
        else: print("Opcion invalida")
    #Creditos y referencia de https://www.youtube.com/watch?v=pLyy-LzgXaM


#MENU PRINCIPAL
def menu_principal():
    global usuario_actual, empleado_actual
    continuarr = 1
    while continuarr:
        print("\n" + "="*60 + "\nSISTEMA DE CINE\n" + "="*60 + "\n1. Login Usuario\n2. Login Empleado\n3. Salir\n" + "="*60)
        
        o = input("Selecciona opcion: ")
        
        if o=="1":
            if login_usuario():
                menu_usuario_principal()
                usuario_actual = None
        elif o=="2":
            if login_empleado():
                menu_empleado_principal()
                empleado_actual = None
        elif o=="3":
            print("Bye!")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menu_principal()