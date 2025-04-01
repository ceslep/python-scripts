from colorama import Fore, Back, Style, init
init(autoreset=True)  # Resetea automáticamente después de cada print

# Listas de colores de texto (Fore) y fondo (Back)
text_colors = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
bg_colors = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
color_names = ['BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']

# Mostrar colores de texto
print(Style.BRIGHT + "== Colores de texto ==")
for color, name in zip(text_colors, color_names):
    print(color + f"Texto en {name}")

# Mostrar colores de fondo
print(Style.BRIGHT + "\n== Colores de fondo ==")
for color, name in zip(bg_colors, color_names):
    print(color + f" Fondo en {name} ", end=' ')  # Mostrar en una sola línea
    print(Style.RESET_ALL)  # Reseteo manual para separar

# Combinación de colores de texto y fondo
print(Style.BRIGHT + "\n== Combinaciones ==")
for f_color, f_name in zip(text_colors, color_names):
    for b_color, b_name in zip(bg_colors, color_names):
        print(f"{f_color}{b_color}Texto: {f_name} | Fondo: {b_name}", end='  ')
        print(Style.RESET_ALL)
