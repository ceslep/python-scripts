import turtle

pantalla = turtle.Screen()
pantalla.bgcolor("black")
pantalla.title("Superestructura Futurista")

estructura = turtle.Turtle()
estructura.speed(0)
estructura.color("cyan")
estructura.pensize(2)

# Función para dibujar una torre
def torre(x, y, altura):
    estructura.penup()
    estructura.goto(x, y)
    estructura.pendown()
    estructura.begin_fill()
    for _ in range(2):
        estructura.forward(40)
        estructura.left(90)
        estructura.forward(altura)
        estructura.left(90)
    estructura.end_fill()

# Función para dibujar una antena
def antena(x, y, largo):
    estructura.penup()
    estructura.goto(x + 20, y)
    estructura.pendown()
    estructura.color("white")
    estructura.forward(largo)
    estructura.circle(3)
    estructura.color("cyan")

# Función para dibujar un puente
def puente(x1, y1, x2, y2):
    estructura.penup()
    estructura.goto(x1, y1)
    estructura.pendown()
    estructura.goto(x2, y2)

# Dibujar torres principales
torre(-200, -150, 200)
antena(-200, 50, 80)

torre(0, -150, 250)
antena(0, 100, 100)

torre(200, -150, 180)
antena(200, 30, 70)

# Dibujar puentes entre torres
estructura.color("gray")
puente(-160, 50, 40, 100)
puente(40, 100, 240, 30)

# Base de la estructura
estructura.color("cyan")
estructura.penup()
estructura.goto(-250, -150)
estructura.pendown()
estructura.begin_fill()
for _ in range(2):
    estructura.forward(500)
    estructura.right(90)
    estructura.forward(30)
    estructura.right(90)
estructura.end_fill()

estructura.hideturtle()
pantalla.mainloop()
