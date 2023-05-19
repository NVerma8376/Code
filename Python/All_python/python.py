import turtle
win = turtle.Turtle()
while True:
    syntax = str(input(">>>"))
    def excute():
        if syntax == "print":
            print_what = str(input("="))
            print(print_what)

        elif syntax == "input":
            a=input("=")

win.listen()
win.onclick(excute, "+")
win.mainloop()