import ctypes

# Define manualmente la estructura COORD
class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

# Función para mover el cursor a una posición específica
def gotoxy(x, y):
    handle = ctypes.windll.kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
    coord = COORD(x, y)  # Utiliza la estructura COORD definida manualmente
    ctypes.windll.kernel32.SetConsoleCursorPosition(handle, coord)

# Dibuja un cuadro
def dibujarCuadro(x1, y1, x2, y2):
    for i in range(x1, x2):
        gotoxy(i, y1)
        print("-")  # Línea horizontal superior
        gotoxy(i, y2)
        print("-")  # Línea horizontal inferior

    for i in range(y1, y2):
        gotoxy(x1, i)
        print("|")  # Línea vertical izquierda
        gotoxy(x2, i)
        print("|")  # Línea vertical derecha

    gotoxy(x1, y1)
    print("|")
    gotoxy(x1, y2)
    print("|")
    gotoxy(x2, y1)
    print("|")
    gotoxy(x2, y2)
    print("|")

# Función para limpiar la pantalla o eliminar los cuadros
def limpia():
    for i in range(5, 24):
        for j in range(3, 77):
            gotoxy(j, i)
            print(" ")

class CONSOLE_CURSOR_INFO(ctypes.Structure):
    _fields_ = [("dwSize", ctypes.c_ulong), ("bVisible", ctypes.c_bool)]

# Función para ocultar el cursor
def CursorOff():
    cursor_info = CONSOLE_CURSOR_INFO(100, False)  # Tamaño arbitrario y visible=False
    handle = ctypes.windll.kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(cursor_info))

# Función para mostrar el cursor
def CursorOn(visible=True, size=20):
    cursor_info = CONSOLE_CURSOR_INFO(size, visible)
    handle = ctypes.windll.kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(cursor_info))





