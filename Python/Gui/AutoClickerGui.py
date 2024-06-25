import tkinter
import AutoClicker
import threading

window = tkinter.Tk()  

window.title("Auto Clicker")

cps = tkinter.StringVar()

window.geometry('350x200')

lbl = tkinter.Label(window, text="Auto Clicker", font=("Arial Bold", 20))

def autoautoclicker():
    create_autoclicker = AutoClicker.start_autoclicker()

autoautoclickerstart = threading.Thread(target=autoautoclicker)


def submit():

    autoautoclickerstart.start()
    CPS = cps.get()
    AutoClicker(cps,True)
    cps.set("")


def stop():
    AutoClicker.autoclick(cps,False)
    cps.set("")
    window.destroy()


#Gui
CPS = tkinter.Entry(window,textvariable = cps, font=('calibre',10,'normal')).pack(padx=20, pady=20)
btn = tkinter.Button(window, text="Start", bg="green", fg="white", command=submit).pack(padx=20, pady=20)
btn2 = tkinter.Button(window, text="Stop", bg="green", fg="white", command=stop).pack(padx=20, pady=20)


window.mainloop()