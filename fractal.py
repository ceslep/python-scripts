import turtle

def sierpinski(tortuga, orden, tamano):
    if orden == 0:
        for _ in range(3):
            tortuga.forward(tamano)
            tortuga.left(120)
    else:
        sierpinski(tortuga, orden-1, tamano/2)
        tortuga.forward(tamano/2)
        sierpinski(tortuga, orden-1, tamano/2)
        tortuga.backward(tamano/2)
        tortuga.left(60)
        tortuga.forward(tamano/2)
        tortuga.right(60)
        sierpinski(tortuga, orden-1, tamano/2)
        tortuga.left(60)
        tortuga.backward(tamano/2)
        tortuga.right(60)

pantalla = turtle.Screen()
pantalla.bgcolor("white")
tortuga = turtle.Turtle()
tortuga.speed(0)

# Dibuja el Triángulo de Sierpinski de orden 4
sierpinski(tortuga, 4, 200)

turtle.done()
