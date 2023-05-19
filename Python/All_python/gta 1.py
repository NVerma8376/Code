import turtle
import random
import random
win = turtle.Screen()
win.title("GTA 1")
win.bgcolor("black")
win.setup(800, 600)
win.tracer(0)

player = turtle.Turtle()
player.penup()
player.speed(0)
player.color("blue")
player.shape("square")


def up():
    y = player.ycor()
    y += 20
    player.sety(y)


def down():
    y = player.ycor()
    y -= 20
    player.sety(y)


def right():
    x = player.xcor()
    x += 20
    player.setx(x)


def left():
    x = player.xcor()
    x -= 20
    player.setx(x)


y = random.randint(1, 800)
x = random.randint(1, 600)

npc = turtle.Turtle()
npc.speed(0)
npc.shape("square")
npc.color("blue")
npc.penup()
npc.goto(360, 0)

npc2 = turtle.Turtle()
npc2.speed(0)
npc2.shape("square")
npc2.color("blue")
npc2.penup()
npc2.goto(0, 360)

npc3 = turtle.Turtle()
npc3.speed(0)
npc3.shape("square")
npc3.color("blue")
npc3.penup()
npc3.goto(-360, 0)


win.listen()
win.onkeypress(up, "w")
win.onkeypress(down, "s")
win.onkeypress(right, "d")
win.onkeypress(left, "a")


while True:
    win.update()
    factor = random.randint(20, 80)

    if player.ycor() == npc2.ycor() and player.xcor() == npc2.xcor():
        y = npc2.ycor()
        y -= 40
        x = npc2.ycor()
        x = random.randint(20, factor)
        npc2.sety(y)
        npc2.setx(x)
