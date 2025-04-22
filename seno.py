import turtle,math,random

# Configurar la ventana
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Seno")
w, h = 800, 600
screen.setup(width=w, height=h)

seno = turtle.Turtle()
seno.speed("fastest")
seno.pensize(2)
seno.color("cyan")
seno.penup()
ancho=(w//2)
alto=(h//2-20)
seno.goto(-ancho,0)
seno.pendown()
for i in range(0,w,10):
    seno.goto(i-ancho,alto*math.sin(6*i*math.pi/(w)))
    seno.color(random.choice(["red", "orange", "yellow", "green", "blue",  "cyan", "white", "magenta", "lime"]))
    

screen.exitonclick()