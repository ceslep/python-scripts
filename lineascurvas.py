import turtle,random,keyboard

t=turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
turtle.title("Lineas Curvas")
turtle.setup(800,800)
turtle.hideturtle()
for i in range(0,610,20):
    t.penup()
    t.color(random.choice(["red", "orange", "yellow", "green", "blue",  "cyan", "white", "magenta", "lime"]))
    t.goto(-300,300-i)
    t.pendown()
    t.goto(-300+i,-300)
    t.penup()
    t.color(random.choice(["red", "orange", "yellow", "green", "blue",  "cyan", "white", "magenta", "lime"]))
    t.goto(300,-300+i)
    t.pendown()
    t.goto(300-i,300)
    t.penup()
    t.color(random.choice(["red", "orange", "yellow", "green", "blue",  "cyan", "white", "magenta", "lime"]))
    t.goto(0,-i)
    t.pendown()
    t.circle(i)
    if keyboard.is_pressed("q"):
        break
turtle.done()