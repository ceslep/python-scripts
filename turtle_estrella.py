import turtle
import random

# Configuración de la ventana
ventana = turtle.Screen()
ventana.bgcolor("black")
ventana.title("Dibujar una estrella personalizada")

# Crear el objeto tortuga
estrella = turtle.Turtle()
estrella.color("cyan")
estrella.pensize(2)
estrella.speed(3)

colores=["red", "blue", "green", "yellow", "purple", "orange"]

lados = 20
tamaño = 200
angulo=120
estrella.speed(0)
    
for _ in range(lados):
        estrella.color(random.choice(colores))
        estrella.forward(tamaño)
        estrella.color(random.choice(colores))
        estrella.circle(20)
        estrella.right(100)

estrella.penup()
estrella.goto(-100, -100)
estrella.pendown()
estrella.color("red")

for _ in range(lados):
        estrella.color(random.choice(colores))
        estrella.forward(tamaño)
        estrella.color(random.choice(colores))
        estrella.circle(20)
        estrella.right(100)   

# Solicitar al usuario los parámetros

# Dibujar la estrella

# Finalizar
turtle.done()
