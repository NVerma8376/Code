from tkinter import *
import random
window = Tk()
def rect():
    x1 = random.randint(20,40)
    y1 = random.randint(20,40)
    x2 = random.randint(50,400)
    y2 = random.randint(50,400)
    canvas = Canvas(window, width=500, height=500)
    canvas.pack()
    canvas.create_rectangle(x1, y1, x2, y2)
    mainloop()
rect()