from rich.console import Console
from rich.table import Table
from colorama import init, Fore, Back, Style

# Inicializa Colorama para que funcione correctamente en Windows
init()

console = Console()
table = Table(title="Ejemplo de Tabla")

table.add_column("Nombre", style="cyan", no_wrap=True)
table.add_column("Edad", style="magenta")
table.add_row("Alice", "30")
table.add_row("Bob", "25")

console.print(table)


# Texto con colores de primer plano (Fore) y fondo (Back)
print(Fore.RED + "Este texto es rojo")
print(Back.GREEN + "Este texto tiene fondo verde")

# Combina estilos y luego restablece al formato por defecto
print(Style.BRIGHT + "Texto brillante" + Style.RESET_ALL)
print("Texto con formato normal")
