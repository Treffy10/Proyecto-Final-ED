import Caja
import os
import Tienda
import getpass
import time
import Producto
import msvcrt

def leerPasw():
    print("Clave: ", end="", flush=True)  # Mostrar "Clave: "
    password = []
    while True:
        char = msvcrt.getch()
        char = char.decode('utf-8')  # Convertir a cadena
        if char == '\r':  # Si es Enter, termina la entrada
            break
        elif char == '\b':  # Si es retroceso, elimina el último carácter
            if password:
                password.pop()
                print("\b \b", end="", flush=True)
        else:
            password.append(char)
            print("*", end="", flush=True)

    print()  # Salto de línea después de ingresar la contraseña
    return ''.join(password)


def guardarCajas(cajas):
    try:
        with open("caja.txt", 'w') as archivo:
            for caja in cajas:
                archivo.write(f"{caja.getID()}, {caja.getProductoVendido()}\n")
        print("Cajas guardadas correctamente")
    except FileNotFoundError:
        print(f"El archivo {'caja.txt'} no fue encontrado.")

def cargarCajas():
    cajas = []
    try:
        with open("caja.txt", "r") as archivo:
            for linea in archivo:
                id_str, producto = linea.strip().split(',')
                id = int(id_str)
                caja = Caja.Caja(id)
                caja.setProductoVendido(producto)
                cajas.append(caja)

        print("Cajas cargadas correctamente.")
    except FileNotFoundError:
        print("Error al abrir el archivo. No se cargaron cajas.")

    return cajas

def menu():
    # Limpiar la pantalla
    os.system("cls" if os.name == "nt" else "clear")
    # Cambiar el color de la consola (Windows)
    if os.name == "nt":
        os.system("color 70")

    nprtds = 0
    usuarioValido = False

    with open("credencial.txt", 'r') as archivo:
        # Lee las líneas desde el archivo
        titulo = archivo.readline().strip()
        usuario = archivo.readline().strip()
        clave = archivo.readline().strip()
        usuaadmi = archivo.readline().strip()
        claveadmi = archivo.readline().strip()

    tienda = Tienda.Tienda("producto.txt")
    cajas = cargarCajas()
    carrito = []

    contador = 0
    ingresa = False

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n\t\t\t   SISTEMA DE VENTAS     ")
        print("\t\t\t ----------------------\n")
        print("\t(1) Administrador")
        print("\t(2) Caja")
        print("\t(3) Salir")
        opcion = int(input("\n\tQue desea realizar?: \t"))

        if opcion == 1:
            while True:
                usuarioIngresado = str(input("Ingrese su nombre de usuario: "))
                contrasenaIngresada = leerPasw()

                if usuarioIngresado == usuaadmi and contrasenaIngresada == claveadmi:
                    print("Cargando", end="")
                    for _ in range(3):
                        time.sleep(1)
                        print(".", end="")
                    print("\nBienvenido, " + usuarioIngresado)
                    usuarioValido = True
                    break
                else:
                    print("Nombre de usuario o contraseña incorrectos. Intente nuevamente.")

            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("\n\tADMINISTRADOR")
                print("\t(1) Perfil(Tienda)")
                print("\t(2) Cuenta(Editar)")
                print("\t(3) Establecimiento de Precios")
                print("\t(4) Gestion Financiero")
                print("\t(5) Gestion de Inventario")
                print("\t(6) Editar(Caja)")
                print("\t(7) Atras")
                opcion_prdts = int(input("\n\tQue desea realizar?: \t"))

                if opcion_prdts == 1:
                    while True:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("\n\tPERFIL")
                        print("\t(1) Editar Nombre(Tienda)")
                        print("\t(2) Editar Inicio de Sesion(Usuario y clave)")
                        print("\t(3) Atras")
                        admip = int(input("\n\tElija: \t"))

                        if admip == 1:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("\n\tNombre de Tienda")
                            print(f"Titulo actual: {titulo}")
                            titulo = str(input("Ingrese un nuevo titulo: "))

                            while True:
                                os.system("cls" if os.name == "nt" else "clear")
                                print("\n\t(1) Atras ")
                                opcion3 = int(input())
                                opcion2 = 1
                                if opcion3 == 1:
                                    break

                        if admip == 2:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("\n\t(usuario y contraseña)")
                            print(f"Nombre de usuario actual: {usuario}")
                            print(f"Clave actual: {clave}")
                            usuario = str(input("Ingrese nuevo nombre de usuario: "))
                            clave = str(input("Ingrese nueva clave: "))

                            while True:
                                os.system("cls" if os.name == "nt" else "clear")
                                print("\n\t(1) Atras ")
                                opcion3 = int(input())
                                opcion2 = 1
                                if opcion3 == 1:
                                    break

                        if admip == 3:
                            opcion3 = 2
                            opcion2 = 1
                            break

                if opcion_prdts == 2:
                    while True:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("\n\tCUENTA")
                        print("\t(1) Editar administrador")
                        print("\t(2) Atras")
                        cuentap = int(input("Elije: "))

                        if cuentap == 1:
                            print("\n\tEditar(Administrador)")
                            print("\t(1) Editar administrador")
                            print(f"Nombre de usuario actual: {usuaadmi}")
                            print(f"Clave actual: {claveadmi}")
                            usuaadmi = str(input("Ingrese el nuevo nombre de usuario: "))
                            claveadmi = str(input("Ingrese la nueva clave: "))

                            while True:
                                os.system("cls" if os.name == "nt" else "clear")
                                print("\n\t(1) Atras ")
                                opcion3 = int(input())
                                opcion2 = 1
                                if opcion3 == 1:
                                    break

                        if cuentap == 2:
                            opcion3 = 2
                            opcion2 = 1
                            break

                if opcion_prdts == 3:
                    while True:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("\n\tESTABLECIMIENTO DE PRECIOS(productos)")
                        print("\t(1) Agregar(producto) ")
                        print("\t(2) Modificar(producto) ")
                        print("\t(3) Eliminar(producto) ")
                        print("\t(4) Atras ")
                        ep = int(input("Elija: "))

                        if ep == 1:
                            os.system("cls" if os.name == "nt" else "clear")
                            nombre = str(input("Ingrese el nombre del producto: "))
                            codigo = str(input("Ingrese el codigo del producto: "))
                            precio = float(input("Ingrese el precio: "))
                            preciocomp = float(input("Ingrese el precio de compra del producto: "))
                            cantidad = int(input("Ingrese la cantidad deseada del producto: "))
                            producto = Producto.Producto(nombre, codigo, precio, preciocomp, cantidad)
                            tienda.agregarProducto(producto)
                            print("Producto agregado exitosamente")

                            while True:
                                os.system("cls" if os.name == "nt" else "clear")
                                print("\n\t(1) Atras ")
                                opcion3 = int(input())
                                opcion2 = 1
                                if opcion3 == 1:
                                    break

                        if ep == 2:
                            os.system("cls" if os.name == "nt" else "clear")
                            codigo = str(input("Ingrese el codigo del producto a modificar: "))
                            tienda.modificarProducto(codigo)

                            while True:
                                os.system("cls" if os.name == "nt" else "clear")
                                print("\n\t(1) Atras ")
                                opcion3 = int(input())
                                opcion2 = 1
                                if opcion3 == 1:
                                    break

                        if ep == 3:
                            codigo = str(input("Ingrese el codigo del producto a eliminar: "))
                            tienda.eliminarProducto(codigo)

                        if ep == 4:
                            opcion3 = 2
                            opcion2 = 1
                            break
                if opcion_prdts == 4:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("\n\tGESTION FINANCIERO")
                    print("\t(1) Gastos, Ingreso y Ganancia")
                    print("\t(2) Ver ventas de una caja")
                    print("\t(3) Atras")
                    gf = int(input("Elija: "))

                    if gf == 1:
                        tienda.mostrarGastosIngresosGanancias()
                        input("Presiona Enter para continuar...")
                        while True:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("\n\t(1) Atras ")
                            opcion3 = int(input())
                            opcion2 = 1
                            if opcion3 == 1:
                                break
                    if gf == 2:
                        os.system("cls" if os.name == "nt" else "clear")
                        id = int(input("Ingrese el ID de la caja: "))
                        totalVenta = 0.0
                        resultado = next((caja for caja in cajas if caja.getID() == id), None)

                        # Comprueba si se encontró una coincidencia
                        if resultado is not None:
                            print(f"Ventas de la caja {resultado.getID()}: {resultado.getProductoVendido()}")
                            tienda.mostrarBoleta(carrito)
                        else:
                            print("No se encontró ninguna caja con el ID:", id)
                        input("Presiona Enter para continuar...")

                        while True:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("\n\t(1) Atras ")
                            opcion3 = int(input())
                            opcion2 = 1
                            if opcion3 == 1:
                                break
                    if gf == 3:
                        opcion3 = 2
                        opcion2 = 1
                        break

                if opcion_prdts == 5:

                    os.system("cls" if os.name == "nt" else "clear")
                    tienda.mostrarRegistro()
                    input("Presiona para continuar...")
                    while True:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("\n\t(1) Atras ")
                        opcion3 = int(input())
                        opcion2 = 1
                        if opcion3 == 1:
                            break
                if opcion_prdts == 6:
                    while True:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("\n\tEDITAR(Caja)")
                        print("1. Crear caja")
                        print("2. Borrar caja")
                        print("3. Mostrar cantidad de cajas creadas")
                        print("4. Atras")
                        ec = int(input("Elija: "))

                        if ec == 1:
                            os.system("cls" if os.name == "nt" else "clear")
                            id = int(input("Ingrese el ID de la caja: "))
                            cajas.append(Caja.Caja(id))
                            print("Caja creada correctamente")
                            while True:
                                os.system("cls" if os.name == "nt" else "clear")
                                print("\n\t(1) Atras ")
                                opcion3 = int(input())
                                opcion2 = 1
                                if opcion3 == 1:
                                    break
                        if ec == 2:
                            os.system("cls" if os.name == "nt" else "clear")
                            id = int(input("Ingrese el id de la caja a borrar: "))
                            caja_a_borrar = next((caja for caja in cajas if caja.getID() == id), None)

                            if caja_a_borrar is not None:
                                cajas.remove(caja_a_borrar)
                                print("Caja borrada correctamente.")
                            else:
                                print(f"No se encontró la caja con ID {id}")

                            while True:
                                os.system("cls" if os.name == "nt" else "clear")
                                print("\n\t(1) Atras ")
                                opcion3 = int(input())
                                opcion2 = 1
                                if opcion3 == 1:
                                    break
                        if ec == 3:
                            os.system("cls" if os.name == "nt" else "clear")
                            print(f"Cantidad de cajas creadas: {len(cajas)}")
                            input("Presiona para continuar...")
                            while True:
                                os.system("cls" if os.name == "nt" else "clear")
                                print("\n\t(1) Atras ")
                                opcion3 = int(input())
                                opcion2 = 1
                                if opcion3 == 1:
                                    break
                        if ec == 4:
                            opcion3 = 2
                            opcion2 = 1
                            break
                if opcion_prdts == 7:
                    opcion3 = 2
                    opcion2 = 1
                    break
        if opcion == 2:
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("\n\tCaja")
                print("\t (1) Realizar ventas")
                print("\t (2) Buscar producto")
                print("\t (3) Atras")
                cj = int(input("Elija: "))

                if cj == 1:
                    id = int(input("Ingrese el ID de la caja: "))
                    caja_encontrada = next((caja for caja in cajas if caja.getID() == id), None)

                    if caja_encontrada is not None:
                        tienda.vender()
                        print("Venta registrada correctamente.")
                    else:
                        print(f"No se encontró la caja con ID {id}")
                    input("Presiona para continuar...")

                    while True:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("\n\t(1) Atras ")
                        opcion3 = int(input())
                        opcion2 = 1
                        if opcion3 == 1:
                            break

                if cj == 2:
                    print("Lista de productos:")
                    print("===================================")
                    print("Nombre del Producto   |   Código")
                    print("===================================")
                    for producto in tienda.productos:
                        print(f"{producto.nombre:20} | {producto.codigo}")
                    print("===================================")

                    codigo = str(input("Ingrese el codigo del producto a buscar(caracteristicas): "))
                    indice = tienda.buscarProducto(codigo)
                    if indice != -1:
                        print(f"\nProducto encontrado en el indice: {indice}")
                        print(f"Nombre del producto: {tienda.productos[indice].nombre}")
                        print(f"Codigo del producto: {tienda.productos[indice].codigo}")
                        print(f"Precio del producto: {tienda.productos[indice].precio}")
                        print(f"Cantidad del producto: {tienda.productos[indice].cantidad}")
                        input("Presione para continuar...")
                    else:
                        print("Producto no encontrado")

                    while True:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("\n\t(1) Atras ")
                        opcion3 = int(input())
                        opcion2 = 1
                        if opcion3 == 1:
                            break
                if cj == 3:
                    opcion3 = 2
                    opcion2 = 1
                    break
        if opcion == 3:
            guardarCajas(cajas)
            with open("credencial.txt", 'w') as archivo_salida:
                archivo_salida.write(titulo + '\n')
                archivo_salida.write(usuario + '\n')
                archivo_salida.write(clave + '\n')
                archivo_salida.write(usuaadmi + '\n')
                archivo_salida.write(claveadmi + '\n')
            exit(0)


