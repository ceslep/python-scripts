import turtle
import math
import random

# Configurar la ventana de turtle con fondo negro
turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(2)
colors = ["red", "blue", "green", "purple", "yellow", "orange", "pink", "cyan", "magenta", "lime", "brown", "gray"]

# Función para dibujar el corazón usando coordenadas paramétricas con relleno rojo
def dibujar_corazon(ancho=10, offset_x=0, offset_y=0):
    t.penup()
    t.goto(0, -ancho)  # Comienza un poco más abajo para centrar el corazón
    t.begin_fill()  # Iniciar el relleno con el color seleccionado
    c=random.choice(colors)  # Elegir un color aleatorio de la lista
    t.fillcolor(c)  # Establecer el color de relleno a rojo
    t.color(c)  # Establecer el color del borde a rojo
    
    for t_val in range(0, 360,2):  # Usamos 360 grados para cubrir un ciclo completo
        t_val = math.radians(t_val)  # Convertir grados a radianes
        x = 16 * math.sin(t_val)**3
        y = 13 * math.cos(t_val) - 5 * math.cos(2 * t_val) - 2 * math.cos(3 * t_val) - math.cos(4 * t_val)
        
        t.goto(offset_x+x * ancho,offset_y+ y * ancho)  # Multiplicamos por 10 para escalar la figura
        t.pendown()

    t.end_fill()  # Finalizar el relleno

# Llamar a la función para dibujar el corazón
for i in range(30):
    offset_x=random.randint(-300, 300)
    offset_y=random.randint(-300, 300)
    ancho=random.randint(1, 20)
    dibujar_corazon(ancho,offset_x, offset_y)

# Finalizar
turtle.done()
