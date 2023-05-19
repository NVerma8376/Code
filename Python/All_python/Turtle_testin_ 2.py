import turtle
import random
import time

FONT = ("Arial", 14, "bold")

#global Score

win = turtle.Screen()
win.bgcolor("white")
win.setup(width=800, height=600)
win.tracer(0)

player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("red")
player.penup()
player.goto(0, 0)
player.shapesize(1, 1, 1)

npc2 = turtle.Turtle()
npc2.speed(0)
npc2.shape("square")
npc2.color("blue")
npc2.penup()
npc2.goto(0, 20)
npc2.shapesize(1, 1, 1)

npc3 = turtle.Turtle()
npc3.speed(0)
npc3.shape("square")
npc3.color("blue")
npc3.penup()
npc3.goto(0, -20)
npc3.shapesize(1, 1, 1)

write = turtle.Turtle(visible=False)
write.speed("fastest")
write.penup()
write.goto(0, 225)
write.write("0", font=FONT)

#start = "y"
# if start == "y":
#    timeLoop = True
#
# Variables to keep track and display
#Sec = 3
#
# Begin Process
#timeLoop = start
# while timeLoop:
#    Sec -= 1
#    write.write(Sec, font=FONT)
#    time.sleep(1)
#    if Sec == 0:
#        Sec = 3
#


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


win.listen()

win.onkeypress(up, "w")
win.onkeypress(down, "s")
win.onkeypress(right, "d")
win.onkeypress(left, "a")


Score = 0


class Move(turtle.Turtle, Score):
    def __init__(self, *args, **kwargs):
        super(Move, self).__init__(*args, **kwargs)

    def move(turtle, npc, nps, fact, Score, self):

        if npc.ycor() == nps.ycor() and npc.xcor() == nps.xcor():
            y = nps.ycor()
            x = nps.ycor()
            x = random.randint(20, fact)
            y = random.randint(20, fact)
            for Score in range(0, 1):
                Score += 1

            if x % 20 == 0 and y % 20 == 0:
                nps.sety(y)
                nps.setx(x)
                write.clear()
                write.write(Score, font=FONT)


while True:
    try:
        win.update()
    except Exception:
        break

    # def __init__(self):

    i = None
    for i in range(1, 4):
        i = i-1

    MOVe = Move()

    factor = random.randint(40, 200)

    MOVe.move(player, npc2, factor, Score)
    MOVe.move(player, npc3, factor, Score)
    MOVe.move(npc2, npc3, factor, Score)

    # if player.ycor() == npc2.ycor() and player.xcor() == npc2.xcor():
    #    y = npc2.ycor()
    #    x = npc2.ycor()
    #    x = random.randint(20, factor)
    #    y = random.randint(20, factor)
    #    if x % 20 == 0 and y % 20 == 0:
    #        npc2.sety(y)
    #        npc2.setx(x)

    # if player.ycor() == npc3.ycor() and player.xcor() == npc3.xcor():
    #    y = npc3.ycor()
    #    x = npc3.ycor()
    #    x = random.randint(20, factor)
    #    y = random.randint(20, factor)
    #    if x % 20 == 0 and y % 20 == 0:
    #        npc3.sety(y)
    #        npc3.setx(x)
#
    # if npc3.ycor() == npc2.ycor() and npc3.xcor() == npc2.xcor():
    #    y = npc3.ycor()
    #    x = npc3.ycor()
    #    x = random.randint(20, factor)
    #    y = random.randint(20, factor)
    #    if x % 20 == 0 and y % 20 == 0:
    #        npc3.sety(y)
    #        npc3.setx(x)
