import tkinter as tk

def crear_grilla():
    try:
        filas = int(entry_filas.get())
        columnas = int(entry_columnas.get())
    except ValueError:
        print("Por favor ingrese valores numéricos válidos.")
        return

    # Oculta la sección de ingreso de filas y columnas
    frame_config.destroy()

    # Crea un nuevo frame para la grilla
    frame_grilla = tk.Frame(root)
    frame_grilla.pack(padx=10, pady=10)

    # Lista para almacenar las celdas de entrada
    entradas = []
    for i in range(filas):
        fila_entries = []
        for j in range(columnas):
            celda = tk.Entry(frame_grilla, width=10)
            celda.grid(row=i, column=j, padx=2, pady=2)
            fila_entries.append(celda)
        entradas.append(fila_entries)

    # Función para recopilar e imprimir la matriz completa
    def imprimir_matriz():
        matriz = []
        for i in range(filas):
            fila_valores = []
            for j in range(columnas):
                valor = entradas[i][j].get()
                fila_valores.append(valor)
            matriz.append(fila_valores)
        print("Matriz:")
        for fila in matriz:
            print(fila)

    btn_guardar = tk.Button(root, text="Imprimir Matriz", command=imprimir_matriz)
    btn_guardar.pack(pady=10)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Crear Grilla de Datos")

# Frame para pedir el número de filas y columnas
frame_config = tk.Frame(root)
frame_config.pack(padx=10, pady=10)

label_filas = tk.Label(frame_config, text="Número de filas:")
label_filas.grid(row=0, column=0, padx=5, pady=5)
entry_filas = tk.Entry(frame_config)
entry_filas.grid(row=0, column=1, padx=5, pady=5)

label_columnas = tk.Label(frame_config, text="Número de columnas:")
label_columnas.grid(row=1, column=0, padx=5, pady=5)
entry_columnas = tk.Entry(frame_config)
entry_columnas.grid(row=1, column=1, padx=5, pady=5)

btn_crear = tk.Button(frame_config, text="Crear Grilla", command=crear_grilla)
btn_crear.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
