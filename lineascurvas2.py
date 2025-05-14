import turtle,os,random
os.system("cls")
colores=["red", "orange", "yellow", "green", "blue",  "cyan", "white", "magenta", "lime"]
e=turtle.Turtle()
e.speed(0)
for i in range(0,600,10):
    e.penup()
    e.color(random.choice(colores))
    e.goto(-300,300-i)
    e.pendown()
    e.goto(-300+i,-300)

turtle.done()