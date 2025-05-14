from colorama import Fore, Back, Style, init
import os

os.system("cls")  # Limpia la consola (Windows)
# Inicializa colorama
init(autoreset=True)

# Lista de colores con nombre y fondo
colores = [
    ("Rojo", Back.RED),
    ("Verde", Back.GREEN),
    ("Amarillo", Back.YELLOW),
    ("Azul", Back.BLUE),
    ("Magenta", Back.MAGENTA),
    ("Cian", Back.CYAN),
    ("Blanco", Back.WHITE),
    ("Negro", Back.BLACK),
    ("Gris claro", Back.LIGHTBLACK_EX)
]

# Tamaño del cuadro (puedes ajustarlo)
ancho = 20
alto = 3

# Imprimir cada cuadro
for nombre, fondo in colores:
    print(f"{Style.BRIGHT}{nombre}:")
    for _ in range(alto):
        print(fondo + " " * ancho + Style.RESET_ALL)
    print()  # línea vacía entre cuadros
