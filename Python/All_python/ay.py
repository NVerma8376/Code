import turtle
win=turtle.Screen()
robot = turtle.Turtle("turtle")

robot.speed(0)

for i in range(10):
    for i in range(10):
        robot.forward(100)
        robot.lt(360/4)
    robot.lt(1)

while True:
    win.update()
    
n=5
k=5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=" ")
    print()