import turtle

win = turtle.Screen()
win.title("pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")

paddle1.penup()
paddle1.goto(-350, 0)
paddle1.shapesize(stretch_wid=5, stretch_len=1)

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("blue")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)


ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2


def paddle1up():
    y = paddle1.ycor()
    y += 30
    paddle1.sety(y)


def paddle1down():
    y = paddle1.ycor()
    y -= 30
    paddle1.sety(y)


def paddle2up():
    y = paddle2.ycor()
    y += 30
    paddle2.sety(y)


def paddle2down():
    y = paddle2.ycor()
    y -= 30
    paddle2.sety(y)


win.listen()
win.onkeypress(paddle1up, "w")
win.onkeypress(paddle1down, "s")

win.onkeypress(paddle2up, "Up")
win.onkeypress(paddle2down, "Down")

while True:
    win.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
