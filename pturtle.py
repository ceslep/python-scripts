import turtle

# Crear una pantalla y configurar la tortuga
pantalla = turtle.Screen()
pantalla.title("Polígono con líneas al centro")

tortuga = turtle.Turtle()
tortuga.speed(3)          # Velocidad de la tortuga (1 = lento, 10 = rápido, 0 = sin animación)
tortuga.color("blue")     # Color para dibujar el polígono

# Parámetros del polígono
n_lados = 12               # Cambia este valor para probar con distintos polígonos (3=triángulo, 4=cuadrado, etc.)
distancia = 50           # Longitud de cada lado
angulo = 360 / n_lados    # Ángulo de giro para un polígono regular

# Lista para guardar los vértices
vertices = []

# DIBUJAR EL POLÍGONO
for _ in range(n_lados):
    # Guardamos la posición actual (vértice)
    vertices.append(tortuga.pos())
    # Avanzamos y giramos para dibujar el siguiente lado
    tortuga.forward(distancia)
    tortuga.right(angulo)

# CAMBIAMOS DE COLOR PARA LAS LÍNEAS AL CENTRO
tortuga.color("red")

# LLEVAMOS A LA TORTUGA AL CENTRO (0, 0) SIN DIBUJAR
tortuga.penup()
tortuga.home()  # (0, 0)
tortuga.pendown()

# DIBUJAMOS LÍNEAS DESDE EL CENTRO A CADA VÉRTICE
for vertice in vertices:
    tortuga.goto(vertice)  
    tortuga.goto(0, 0)

turtle.done()
