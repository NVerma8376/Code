from customtkinter import *

app = CTk()
app.geometry('500x400')
app.title("Watch Selection")

def click():
    vid = input.get()

# Create a frame for the input field and button
input_frame = CTkFrame(master=app, corner_radius=10)
input_frame.pack(pady=20, fill="x", expand=True)

# Create the input field
input = CTkEntry(master=input_frame, width=350, corner_radius=10)
input.pack(side="left", fill="x")

# Create the button
btn = CTkButton(master=app, text="click me", corner_radius=20, hover_color="#4682b4", command=click)
btn.place(relx=0.5, rely=0.75, anchor='center')

# Create the label
text = CTkLabel(master=app, text="What do you want to watch?", font=('Helvetica', 30, 'bold'))
text.place(relx=0.5, rely=0.05, anchor='center')

app.mainloop()