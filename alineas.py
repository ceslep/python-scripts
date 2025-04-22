import turtle
import random

pantalla = turtle.Screen()
pantalla.title("Lineas Curvas")

colores = ["red", "blue", "green", "yellow", "purple", "orange"]

tortuga = turtle.Turtle()
# Velocidad de la tortuga (1 = lento, 10 = rápido, 0 = sin animación)
tortuga.speed(0)
tortuga.color("blue")     # Color para dibujar el polígono

ancho = pantalla.window_width()
alto = pantalla.window_height()

cantidad = 30
margen = 10

xinicial = (-ancho // 2)+margen
xfinal = (ancho // 2)-margen
yinicial = (alto // 2)-margen
yfinal = (-alto // 2)+margen

nlineas = ancho // cantidad


for i in range(2*nlineas):
    tortuga.color(random.choice(colores))
    tortuga.penup()
    tortuga.goto(xinicial, yinicial-i*nlineas)
    tortuga.pendown()
    tortuga.goto(xinicial+i*nlineas, yfinal)
   


turtle.done()
