from tkinter import *
import win32com.client as wincl


def speak(text):

    print(text)
    speak1 = wincl.Dispatch("SAPI.SpVoice")
    speak1.Speak(text)


top = Tk()
L1 = Label(top, text="User Name")
L1.pack(side=LEFT)
E1 = Entry(top, bd=5)
E1.pack(side=RIGHT)
text1 = E1.get()
B1 = Button(top, text="speak", command=speak(text1))
B1.pack(side=RIGHT)

top.mainloop()
