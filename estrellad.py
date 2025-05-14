import math,random
import turtle as t

def dibujar_figura(radio, origen_x, origen_y, color):
    # Calcular las coordenadas x e y
    x = int(radio * math.cos(math.radians(-30)))
    y = int(radio * math.sin(math.radians(-30)))

    # Configurar el color del lápiz
    t.color(color)
    t.penup()

    # Moverse al origen especificado
    t.goto(origen_x, origen_y)

    # Dibujar la figura
    t.goto(origen_x + x, origen_y + y)
    t.pendown()
    t.goto(origen_x - x, origen_y + y)
    t.goto(origen_x, origen_y + radio)
    t.goto(origen_x + x, origen_y + y)

    t.penup()
    t.goto(origen_x + x, origen_y - y)
    t.pendown()
    t.goto(origen_x - x, origen_y - y)
    t.goto(origen_x, origen_y - radio)
    t.goto(origen_x + x, origen_y - y)

# Configuración inicial y ejecución
t.speed(0)
""" dibujar_figura(100, 50, 50, "blue")  # Llamar a la función con un radio de 100, origen en (50, 50) y color azul
dibujar_figura(100, -150, 50, "red")
dibujar_figura(100, -150, -150, "green") 
dibujar_figura(100, 50, -150, "purple") """

t.bgcolor("black")  # Cambiar el color de fondo
for _ in range(24):
    dibujar_figura(random.randint(100, 100), random.randint(-200, 200), random.randint(-200, 200), random.choice(["blue", "red", "green", "purple"]))

t.hideturtle()  # Ocultar la tortuga
t.done()
