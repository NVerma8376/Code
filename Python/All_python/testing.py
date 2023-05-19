import turtle
win = turtle.Screen()
win.tracer(0)
win.bgcolor("red")
win.setup(10000,10000)

me = turtle.Turtle()
me.speed(0)
me.shape("circle")
me.color("red","blue")
while True:
    win.update