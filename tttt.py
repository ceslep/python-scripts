import turtle

# Configuración inicial de la pantalla y la tortuga
pantalla = turtle.Screen()
pantalla.bgcolor("white")  # Fondo blanco

tortuga = turtle.Turtle()
tortuga.speed(5)  # Velocidad media

# Función para dibujar el contorno del sombrero vueltiao
def dibujar_sombrero():
    tortuga.penup()
    tortuga.goto(-100, -100)
    tortuga.pendown()
    tortuga.begin_fill()
    tortuga.color("black")
    tortuga.circle(100, 180)  # Dibuja la base del sombrero (una semicírculo)
    tortuga.end_fill()

# Función para crear los detalles del sombrero vueltiao
def dibujar_detalles():
    tortuga.penup()
    tortuga.goto(-100, -100)  # Regresa a la base del sombrero
    tortuga.pendown()
    tortuga.setheading(45)  # Cambia la orientación
    tortuga.pensize(2)

    # Dibujar líneas diagonales para simular el diseño tradicional del sombrero vueltiao
    for i in range(8):
        tortuga.forward(200)
        tortuga.backward(200)
        tortuga.left(45)  # Gira para la siguiente línea diagonal

# Función para agregar las líneas verticales para dar la textura del sombrero
def dibujar_lineas_verticales():
    tortuga.penup()
    tortuga.goto(-80, -50)
    tortuga.pendown()
    tortuga.setheading(0)  # Alineamos las líneas verticalmente
    tortuga.pensize(1)

    # Dibujar líneas verticales para la textura del sombrero vueltiao
    for _ in range(9):
        tortuga.forward(200)
        tortuga.backward(200)
        tortuga.left(20)

# Función para el mensaje cultural
def mensaje_cultural():
    tortuga.penup()
    tortuga.goto(-200, -200)
    tortuga.pendown()
    tortuga.write("El Sombrero Vueltiao es un símbolo\n"
                   "cultural de la afrocolombianidad.\n"
                   "Representa las tradiciones de la región\n"
                   "Caribe colombiana, especialmente en la\n"
                   "música, danza y la cultura cumbiera.", font=("Arial", 12, "normal"))

# Dibujo del sombrero vueltiao
dibujar_sombrero()
dibujar_detalles()
dibujar_lineas_verticales()

# Mostrar el mensaje cultural
mensaje_cultural()

# Finaliza el dibujo
turtle.done()
