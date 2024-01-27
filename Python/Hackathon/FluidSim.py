import tkinter as tk
import random

class Ball:
    def __init__(self, canvas, x, y, radius, color):
        self.canvas = canvas
        self.radius = radius
        self.color = color
        self.id = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)
        self.x = x
        self.y = y
        self.dx = random.randint(-2, 2)
        self.dy = random.randint(-2, 2)

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x - self.radius < 0 or self.x + self.radius > self.canvas.winfo_width():
            self.dx *= -1
        if self.y - self.radius < 0 or self.y + self.radius > self.canvas.winfo_height():
            self.dy *= -1

        self.canvas.coords(self.id, self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius)

    def check_collision(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx * dx + dy * dy) ** 0.5
        if distance < self.radius + other.radius:
            return True
        return False

def update():
    for i in balls:
        i.move()
        for j in balls:
            if i != j and i.check_collision(j):
                temp_dx = i.dx
                i.dx = j.dx
                j.dx = temp_dx
                temp_dy = i.dy
                i.dy = j.dy
                j.dy = temp_dy
    root.after(10, update)

root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

balls = []
for _ in range(10):
    balls.append(Ball(canvas, random.randint(0, 800), random.randint(0, 600), random.randint(10, 30), 'blue'))

update()
root.mainloop()
