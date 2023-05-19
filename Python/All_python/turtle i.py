import turtle as t
import tkinter as tk
root = tk.Tk()


def rect(horz, vert, color):
    t.pendown()
    t.pensize(2)
    t.color(color)
    t.begin_fill()
    for i in range(1, 3):
        t.fd(horz)
        t.lt(90)
        t.fd(vert)
        t.lt(90)
    t.penup()
    t.end_fill()
    t.speed("slow")


rect(100, 50, "red")

root.mainloop()
