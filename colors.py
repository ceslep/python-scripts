from os import system
system("cls")
print("\033[31mhola\033[0m")
import tkinter as tk

def obtener_datos():
    dato1 = entry1.get()
    dato2 = entry2.get()
    print("Dato 1:", dato1)
    print("Dato 2:", dato2)

# Crear la ventana principal
root = tk.Tk()
root.title("Ingreso de Datos")

# Etiqueta y campo de entrada para el primer dato
label1 = tk.Label(root, text="Dato 1:")
label1.grid(row=0, column=0, padx=5, pady=5)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta y campo de entrada para el segundo dato
label2 = tk.Label(root, text="Dato 2:")
label2.grid(row=1, column=0, padx=5, pady=5)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Botón para enviar y procesar los datos
button = tk.Button(root, text="Enviar", command=obtener_datos)
button.grid(row=2, column=0, columnspan=2, pady=10)

# Iniciar el loop de la interfaz
root.mainloop()
