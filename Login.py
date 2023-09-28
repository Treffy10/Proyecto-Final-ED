import Funciones_adicionales
import time
import Menu
import msvcrt

MAX_ATTEMPTS = 3 # Numero de intentos

# Función para cambiar una cadena en un arreglo de caracteres
def cambio(a):
    a = a[:10]  # Limita la cadena a 10 caracteres
    return a

# Función para leer la contraseña sin mostrarla en pantalla
def leerPasw():
    Funciones_adicionales.gotoxy(23, 13)
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

# Función de inicio de sesión
def login():
    Funciones_adicionales.CursorOn(1, 10)
    try:
        with open("credencial.txt", 'r') as archivo:
            titulo = archivo.readline().strip()
            usuario = archivo.readline().strip()
            clave = archivo.readline().strip()
            usuaadmi = archivo.readline().strip()
            claveadmi = archivo.readline().strip()
    except FileNotFoundError:
        print("El archivo 'credencial.txt' no fue encontrado.")

    usuario = cambio(usuario)
    clave = cambio(clave)

    user2 = ''
    contra2 = ''
    x = 1
    f = 33

    Funciones_adicionales.gotoxy(35, 6)
    print("ACCESO")
    Funciones_adicionales.dibujarCuadro(18, 9, 60, 15)
    Funciones_adicionales.gotoxy(23, 11)
    print("Usuario: ", end="")
    user2 = str(input())
    user2 = cambio(user2)

    Funciones_adicionales.gotoxy(23, 13)
    contra2 = leerPasw()

    Funciones_adicionales.CursorOff()

    for _ in range(3):
        Funciones_adicionales.gotoxy(33, 19)
        print("Cargando", end="")
        Funciones_adicionales.gotoxy(f, 19)
        print(".", end="")
        f += 1
        time.sleep(x)

    if user2 == usuario and contra2 == clave:
        for _ in range(3):
            Funciones_adicionales.gotoxy(33, 19)
            print("Cargando", end="")
            Funciones_adicionales.gotoxy(f, 19)
            print(".", end="")
            f += 1
            time.sleep(x)
        print("\nAccediendo al Sistema...")
        Funciones_adicionales.limpia()
        Menu.menu()
    else:
        Funciones_adicionales.gotoxy(35, 19)
        print("                                     ")
        Funciones_adicionales.gotoxy(30, 19)
        print("Datos incorrectos")
        Funciones_adicionales.gotoxy(18, 20)
        input("Presione Enter para volver a ingresar...")
        Funciones_adicionales.limpia()
        login()







