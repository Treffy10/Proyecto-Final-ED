from tabulate import tabulate
import datetime
import os
import locale
import copy
from Producto import Producto
import Caja
class Tienda:
    productos = []
    def __init__(self, archivo):
        self.nombreArchivo = archivo
        self.productos = self.leerProductosDesdeArchivo()

    def guardarProductosEnArchivo(self):
        try:
            with open(self.nombreArchivo, 'w') as archivo:
                for producto in self.productos:
                    archivo.write(
                        f"{producto.nombre} {producto.codigo} {producto.precio} {producto.preciocomp} {producto.cantidad}\n")
        except Exception as e:
            print(f"Se produjo un error al guardar los productos en el archivo: {str(e)}")
    def leerProductosDesdeArchivo(self):
        productos = []  # Inicializa una lista vacía para almacenar los productos
        try:
            with open(self.nombreArchivo, 'r') as archivo:
                for linea in archivo:
                    nombre, codigo, precio, preciocomp, cantidad = linea.strip().split()
                    producto = Producto(nombre, codigo, float(precio), float(preciocomp), int(cantidad))
                    productos.append(producto)
            print(f"Productos leídos desde el archivo {self.nombreArchivo}.")
        except FileNotFoundError:
            print(f"El archivo {self.nombreArchivo} no fue encontrado.")
        except Exception as e:
            print(f"Se produjo un error al leer los productos desde el archivo: {str(e)}")
        return productos

    def mostrarRegistro(self):
        print("=== REGISTRO DE PRODUCTOS ===")
        if not self.productos:
            print("No hay productos registrados")
            return
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}")
            print(f"Codigo: {producto.codigo}")
            print(f"Precio: {producto.precio}")
            print(f"Precio de Compra: {producto.preciocomp}")
            print(f"Cantidad: {producto.cantidad}")
            print("-------------------------")

    def hacer_descuento(self, totalVenta):
        intentos = 3  # Límite de intentos para ingresar datos válidos
        while intentos > 0:
            descuento = input("¿Desea aplicar un descuento? (s/n): ").lower()
            if descuento == "s":
                porcentaje = int(input("Ingrese el porcentaje del descuento (0-100): "))
                if 0 <= porcentaje <= 100:
                    descuento_total = totalVenta * porcentaje / 100
                    totalVenta -= descuento_total
                    return totalVenta
                else:
                    print("El porcentaje debe estar entre 0 y 100.")
            elif descuento == "n":
                print("No se aplicó descuento.")
                return totalVenta
            else:
                print("Entrada no válida. Por favor, ingrese 's' o 'n'.")
                intentos -= 1

        print("Límite de intentos alcanzado. No se aplicó descuento.")
        return totalVenta

    def buscarProducto(self, codigo):
        for i, producto in enumerate(self.productos):
            if producto.codigo == codigo:
                return i
        return -1

    def modificarProducto(self, codigo):
        indice = self.buscarProducto(codigo)

        if indice != -1:
            print("Producto encontrado")
            print(f"Nombre del producto actual: {self.productos[indice].nombre}")
            print(f"Precio del producto actual: {self.productos[indice].precio}\n")
            producto = self.productos[indice]

            producto.nombre = str(input("Nuevo nombre: "))
            producto.precio = float(input("Nuevo precio: "))
            print("Producto modificado exitosamente")
        else:
            print("Producto no encontrado")

    def eliminarProducto(self, codigo):
        indice = self.buscarProducto(codigo)

        if indice != 1:
            print("Producto encontrado")
            del self.productos[indice]
            print("Producto eliminado correctamente")
        else:
            print("Producto no encontrado")

    def mostrarBoleta(self, carrito):
        # Crear una lista para almacenar los datos de los productos en formato de lista
        data = []
        for producto in carrito:
            data.append([producto.codigo, producto.nombre, producto.precio, producto.cantidad,
                         producto.precio * producto.cantidad])

        # Utilizar tabulate para mostrar la tabla
        print("Productos comprados:")
        print(tabulate(data, headers=["Codigo", "Nombre", "Precio", "Cantidad", "Total"], tablefmt="fancy_grid"))

    def vender(self):
        fecha_hora_actual = datetime.datetime.now()
        locale.setlocale(locale.LC_ALL, 'es_PE.UTF-8')
        terminar_compra = False
        carrito = []  # Crear una lista separada para el carrito de compras
        indice = 0

        while not terminar_compra:
            codigo_producto = str(input("Ingrese el código del producto (0 para finalizar la compra): "))

            if codigo_producto == "0":
                break  # Salir del bucle si el usuario ingresa "0"

            # Validar si el código de producto existe en la lista de productos
            indice = self.buscarProducto(codigo_producto)
            if indice is None:
                print("Producto no encontrado. Por favor, ingrese un código válido.")
                continue  # Vuelve al inicio del bucle

            try:
                cantidad_producto = int(input("Ingrese la cantidad del producto: "))
            except ValueError:
                print("Cantidad no válida. Debe ingresar un número entero.")
                continue  # Vuelve al inicio del bucle

            if cantidad_producto <= self.productos[indice].cantidad:
                producto = copy.deepcopy(
                    self.productos[indice])  # Crear una copia profunda del producto para el carrito
                producto.cantidad = cantidad_producto
                carrito.append(producto)  # Agregar copia del producto al carrito después de la validación
            else:
                print(
                    "La cantidad ingresada es mayor a la disponible en inventario. Por favor, ingrese una cantidad válida.")
                continue  # Vuelve al inicio del bucle para que el usuario ingrese una cantidad válida

        nom_cliente = str(input("Ingrese el nombre del cliente: "))

        # Solicitar descuento antes de mostrar la boleta
        totalVenta = sum(producto.precio * producto.cantidad for producto in carrito)
        total_venta = self.hacer_descuento(totalVenta)

        os.system("cls" if os.name == "nt" else "clear")  # Borra la pantalla (Windows o Unix)

        print("/////////////////////////////////////////")
        print("\tHUANUCO - Leoncio Prado - Rupa Rupa")
        print("\tAV.JULIO BURGA - TINGO MARIA")
        print("\t---------- Boleta de Venta ------------")
        print(f"\tCliente: {nom_cliente}")
        print(f"\tFecha y hora: {fecha_hora_actual}")

        formatted_total = locale.currency(total_venta, grouping=True)
        formatted_total = f"S/. {formatted_total}"
        self.mostrarBoleta(carrito)

        # Resta la cantidad en la lista de productos después de completar la compra
        for producto in carrito:
            indice = self.buscarProducto(producto.codigo)
            self.productos[indice].cantidad -= producto.cantidad

        carrito.clear()

        self.guardarProductosEnArchivo()
        print(f"Costo Total: {total_venta}")  # Mostrar el total de venta

        print("Venta registrada correctamente.")
        input("Presiona para continuar...")

    def calcularGastos(self):
        gastos = 0.0
        for producto in self.productos:
            gastos += producto.preciocomp * producto.cantidad
        return gastos

    def calcularIngresos(self):
        ingresos = 0.0
        for producto in self.productos:
            ingresos += producto.precio * producto.cantidad  # Suma los ingresos en lugar de sobrescribir
        return ingresos

    def calcularGanancias(self):
        gastos = self.calcularGastos()
        ingresos = self.calcularIngresos()
        return ingresos - gastos

    def mostrarGastosIngresosGanancias(self):
        gastos = self.calcularGastos()
        ingresos = self.calcularIngresos()
        ganancias = self.calcularGanancias()

        locale.setlocale(locale.LC_ALL, 'es_PE.UTF-8')
        gastos_total = locale.currency(gastos, grouping=True)
        gastos_total = f"S/. {gastos_total}"
        ingresos_total = locale.currency(ingresos, grouping=True)
        ingresos_total = f"S/. {ingresos_total}"
        ganancias_total = locale.currency(ganancias, grouping=True)
        ganancias_total = f"S/. {ganancias_total}"
        print("===== GASTOS, INGRESOS Y GANANCIAS =====")
        print(f"Gastos totales: {gastos_total}")
        print(f"Ingresos totales: {ingresos_total}")
        print(f"Ganancias totales: {ganancias_total}")

    def agregarProducto(self, nuevoProducto):
        self.productos.append(nuevoProducto)
        print("Producto agregado exitosamente.")