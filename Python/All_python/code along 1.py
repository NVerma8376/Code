import tkinter
window =tkinter.Tk()
window.title("codi")
button = tkinter.Button(window,text="hi",width=40)
button.pack(padx=20, pady=20)

global NO
NO=0
def funct(event):
    
    No = No + 1
    if No == 1:
        button.configure(text="1")
    elif No == 2:
        button.configure(text="2")
    else:
        button.pack_forget()
button.bind("<ButtonRelease-1>",funct)
window.mainloop() 