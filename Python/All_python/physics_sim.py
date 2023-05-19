import turtle
import random

win=turtle.Screen()
win.bgcolor("black")
win.title("physics sim in a vacum chamber with the balls having 0 weight")
win.tracer(0)

box = turtle.Turtle()
box.hideturtle()
box.pencolor("white")
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


balls =[]

for _ in range(25):
    balls.append(turtle.Turtle())

color=["red","blue","green","orange", "yellow", "cyan"]
shape=["circle","square"]  
    
for ball in balls:
    ball.shape(random.choice(shape))
    ball.color(random.choice(color))
    ball.penup()
    ball.speed(0)
    x = random.randint(-300, 300)
    y = random.randint(200,300)
    ball.goto(x,y)
    ball.dy = 0
    ball.dx = random.randint(-4,4)
    ball.da=random.randint(-5,5)

gravity = 0.1

while True:
    win.update()
    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)
        
        ball.setx(ball.xcor() + ball.dx)

        if ball.xcor() > 360:
            ball.dx *= -1
            ball.da *= -1
            
        if ball.xcor() < -360:
            ball.dx *= -1
            ball.da *= -1
        
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.dy *= -1
            ball.da *= -1
        



win.mainloop()