import turtle,random,keyboard

turtle.speed(0)
t=turtle.Turtle()
turtle.bgcolor("black")
t.color("cyan")
t.pensize(2)
colors=["red", "orange", "yellow", "green", "blue",  "cyan", "white", "magenta", "lime"]
turtle.title("Lineas Curvas")
screen=turtle.Screen()
t.speed(0)
w,h=300,300
t.penup()
t.goto(-w,h)
print(-w+10)

while True:
        screen.clear()
        screen.bgcolor("black")
        for i in range(0,2*w,20):
            t.penup()
            t.color(random.choice(colors))
            t.goto(-w+10,h-10-i)
            t.pendown()
            t.goto(-w+10+i,-h+10)
        if keyboard.is_pressed("esc"):
            print("Escape presionado. Saliendo...")
            break