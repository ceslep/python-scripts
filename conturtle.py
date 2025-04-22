import random
import turtle

# Configuración de la ventana
# `ventana = turtle.Screen()` is creating a window for drawing using the Turtle graphics library in
# Python. It initializes a screen object that represents the drawing window where you can create
# graphics using the Turtle module.
ventana = turtle.Screen()
ventana.setup(width=500, height=500)
ventana.title("Dibujo con Turtle")
ventana.bgcolor("lightblue")

# Crear la tortuga
t = turtle.Turtle()
t.color("darkgreen")
t.pensize(1)
t.speed(2)


ancho = (ventana.window_width()) // 2
j = 0

# Dibujar una cuadrícula rápidamente con colores aleatorios
t.speed(0)  # Establecer la velocidad al máximo
for x in range(-ancho,ancho,10):
    t.color(random.random(), random.random(), random.random())  # Color aleatorio
    t.penup()
    t.goto(-ancho,x)
    t.pendown()
    t.goto(x, ancho)

for x in range(-ancho,ancho,10):
    t.color(random.random(), random.random(), random.random())  # Color aleatorio
    t.penup()
    t.goto(ancho,-x)
    t.pendown()
    t.goto(x, ancho)    



# Finaliza al hacer clic en la ventana
ventana.exitonclick()
