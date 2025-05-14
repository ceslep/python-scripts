import turtle,os,random,math

os.system("cls")
t=turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
t.penup()


def draw_shape(ancho,  offset_x=0, offset_y=0,relleno=False):
        i=30
        t.penup()
        t.color(random.choice(["red", "blue", "green", "purple"]))
        x = int(ancho * math.cos(math.radians(-i))) 
        y = int(ancho * math.sin(math.radians(-i))) 
       
        t.goto(offset_x+x, offset_y+y)
        t.pendown()
        if relleno:
            t.begin_fill()
        t.goto(offset_x-x, offset_y+y)
        t.goto(offset_x, offset_y+ancho)
        t.goto(offset_x+x, offset_y+y)
        t.penup()
        t.goto(offset_x+x, offset_y-y)
        t.pendown()
        t.goto(offset_x-x, offset_y-y)
        t.goto(offset_x, offset_y-ancho)
        t.goto(offset_x+x, offset_y-y)
        if relleno:
            t.end_fill()

        i=60
        t.penup()
        t.color(random.choice(["red", "blue", "green", "purple"]))
        x = int(ancho * math.cos(math.radians(-i))) 
        y = int(ancho * math.sin(math.radians(-i))) 
        t.goto(offset_x+x, offset_y+y)
        t.pendown()
        if relleno:
            t.begin_fill()
        t.goto(offset_x+x, offset_y-y)
        t.goto(offset_x-ancho, offset_y)
        t.goto(offset_x+x, offset_y+y)
        t.penup()
        t.goto(offset_x-x, offset_y-y)
        t.pendown()
        t.goto(offset_x-x, offset_y+y)
        t.goto(offset_x+ancho, offset_y)
        t.goto(offset_x-x, offset_y-y)
        if relleno:
            t.end_fill()

        
        t.penup()
        t.color("yellow")
        t.goto(offset_x, offset_y-ancho)

        t.pendown()
        t.circle(ancho)
        t.penup()

for _ in range(60):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    r = random.randint(10, 100)
    g = random.randint(1, 10)
    draw_shape(r, x, y,random.choice([True, False]))


turtle.hideturtle()
turtle.exitonclick()






turtle.done()