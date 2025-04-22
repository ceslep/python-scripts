import turtle,random
# Configurar la ventana
screen = turtle.Screen()
screen.bgcolor("black")
# Crear la tortuga
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
w, h = screen.window_width(), screen.window_height()
# Colores para los cuadrados
colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "white"]
# Dibujar cuadrados concéntricos
for side in range(0, w, 20):
    pen.penup()
    # Mover a la esquina superior izquierda del cuadrado
    pen.goto(-side/2, side/2)
    pen.pendown()
    pen.color(random.choice(colors))
    for _ in range(4):
        pen.forward(side)
        pen.right(90)

pen.hideturtle()
screen.exitonclick()
