import turtle
import random
FONT = ("Arial", 14, "bold")
Score = 0

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

try:
    class Move():
        def move(turtle, npc, nps, fact):
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

        def __init__(self, *args, **kwargs):
            #super(Move, self).__init__(*args, **kwargs)
            a = 0
except Exception:
    pass


MOVe = Move()


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


while True:
    try:
        win.update()
    except Exception:
        break

    def __init__(self, *args, **kwargs):
        super(Move, self).__init__(*args, **kwargs)
        i = 5
        for Score in range(1, i):
            i += 1
            Score += 1
            write.write(Score, font=FONT)

    factor = random.randint(40, 200)
    MOVe.move(player, npc2, factor)
    MOVe.move(player, npc3, factor)
    MOVe.move(npc2, npc3, factor)
