import turtle
my_wn = turtle.Screen()
turtle.speed(0)
for i in range(30):
    turtle.circle(2*i)
    turtle.circle(-2*i)
    turtle.left(i)
turtle.exitonclick()
