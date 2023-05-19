import turtle


win = turtle.Screen()
win.bgcolor("white")
win.setup(width=800, height=600)
win.tracer(0)

player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("red")
player.penup()
player.goto(-350, 0)


def up():
    y = player.ycor()
    y += 20
    player.sety(y)


def down():
    y = player.ycor()
    y -= 20
    player.sety(y)


def left():
    x = player.xcor()
    x += 20
    player.setx(x)


def right():
    x = player.xcor()
    x -= 20
    player.setx(x)


win.listen()
win.onkeypress(up, "w")
win.onkeypress(down, "s")
win.onkeypress(left, "a")
win.onkeypress(right, "s")

while True:
    win.update()
