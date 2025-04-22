from colorama import Fore, Back, Style, init
from os import system
init(autoreset=True)

system('cls')

# Simulación de la bandera de Colombia (2 líneas amarillas, 1 azul, 1 roja)
print(Back.YELLOW + " " * 50)


# Texto opcional
print(Style.RESET_ALL + "\n" + Fore.WHITE + Style.BRIGHT + "¡Esta es la bandera de Colombia!")
