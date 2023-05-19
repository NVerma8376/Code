import tkinter
window = tkinter.Tk()
tkinter.Scale(window,bg="red",from_=0,to_=100,orient=tkinter.HORIZONTAL).grid(row=2,column=2)
window.mainloop()