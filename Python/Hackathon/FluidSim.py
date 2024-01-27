from tkinter import *
import random

root = Tk()
gravity = 2
canvas = Canvas(root, width=800, height=600)
canvas.pack()

class Ball:
    def __init__(self, canvas, x, y, radius, ux,uy):
        self.canvas = canvas
        self.radius = radius
        self.x = x
        self.y = y
        self.ux = ux
        self.uy = uy
        self.id = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="blue")
        
    def move(self):
        self.x += self.ux
        self.y += self.uy
        self.uy -= gravity
        
        if self.y - self.radius < 0:
            self.uy *-1
        
        self.canvas.coords(self.id, self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius)
        
        
def update():
    for i in balls:
        i.move()        
        
balls = []

for _ in range(2):
    balls.append(Ball(canvas, random.randint(0, 800), random.randint(0, 600), 20, 0,2))

update()
root.mainloop()