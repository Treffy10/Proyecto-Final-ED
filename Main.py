import Login
import Funciones_adicionales
import os

os.system("cls" if os.name == "nt" else "clear") # limpia la pantalla
if os.name == "nt":   # Cambia el color de la consola (Windows)
    os.system("color 70")
Funciones_adicionales.dibujarCuadro(0, 0, 78, 24) # Dibuja cuadro grande
Funciones_adicionales.dibujarCuadro(1, 1, 77, 3) # Dibuja cuadro chico
Funciones_adicionales.CursorOff() # apaga el cursor
Funciones_adicionales.gotoxy(16, 2) # establece la posicion del titulo

with open("credencial.txt", 'r') as archivo:
    # Lee las líneas desde el archivo
    titulo = archivo.readline().strip()
    usuario = archivo.readline().strip()
    clave = archivo.readline().strip()
    usuaadmi = archivo.readline().strip()
    claveadmi = archivo.readline().strip()
print(f"\t\t {titulo}")
Login.login()



