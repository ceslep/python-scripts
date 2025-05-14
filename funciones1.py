import turtle,os,math,random
os.system("cls")

t=turtle.Turtle()
t.speed(0)

def circulo(radio,centro_x,centro_y,grosor, color,relleno):
    t.penup()
    t.goto(centro_x,centro_y-radio)
    t.pendown()
    if relleno:
        t.begin_fill()
    t.color(color)
    t.circle(radio)
    if relleno:
        t.end_fill()

for _ in range(24):
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    r=random.randint(10,100)
    g=random.randint(1,10)
    c=random.choice(["blue","red","green","purple"])
    circulo(r,x,y,g,c,True)

turtle.done()