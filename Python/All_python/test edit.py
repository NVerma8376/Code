import turtle
import random

win = turtle.Screen()
win.bgcolor("red")
win.title("physics sim in a vacum chamber with the balls having 0 weight with the black chamber slowing down or pulling the ball")
win.tracer(0)

balls=[]
colors=["Blue", "Cyan", "Yellow", "magenta"]


pull= turtle.Turtle()



for i in range(25):
    balls.append(turtle.Turtle())

for ball in balls:
    ball.color(random.choice(colors))
    ball.penup()
    ball.shape("circle")
    ball.speed(0)
    x=random.randint(-300, 300)
    y= random.randint(200, 300)
    ball.goto(x, y)
    ball.dx=random.randint(-5, 5)
    ball.dy=0

box = turtle.Turtle()
box.hideturtle()
box.pencolor("white")
box.speed(0)
box.penup()
box.goto(-380,-315)
box.pendown()

box.fd(752)
box.lt(90)
box.fd(635)
box.lt(90)
box.fd(750)
box.lt(90)
box.fd(635)




gravity=0.3

while True:
    win.update()
    
    for ball in balls:
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)
    
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.dy *= -1
            
        if ball.xcor() > 360:
            ball.dx *= -1
            
        if ball.xcor() < -360:
            ball.dx *= -1     

win.mainloop()
