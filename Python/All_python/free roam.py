import turtle
win = turtle.Screen()
win.title("free roam")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

square = turtle.Turtle()
square.speed(0)
square.shape("square")
square.color("blue")


def up():
    y = square.ycor()
    y += 20
    square.sety(y)


def down():
    y = square.ycor()
    y -= 20
    square.sety(y)


def right():
    x = square.xcor()
    x += 20
    square.setx(x)


def left():
    x = square.xcor()
    x -= 20
    square.setx(x)


def up1():
    square.penup()


def down2():
    square.pendown()


win.listen()
win.onkeypress(up, "w")
win.onkeypress(down, "s")
win.onkeypress(right, "d")
win.onkeypress(left, "a")
win.onkeypress(up1, "z")
win.onkeypress(down2, "x")

while True:
    win.update()
