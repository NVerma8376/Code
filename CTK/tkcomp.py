import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Watch Selection")
root.geometry('500x400')

# Create a label
label = tk.Label(root, text="What do you want to watch?", font=('Helvetica', 16, 'bold'))
label.place(relx=0.5, rely=0.3, anchor='center')

# Create an entry field
entry = tk.Entry(root, width=350)
entry.place(relx=0.5, rely=0.5, anchor='center')

# Create a button
button = tk.Button(root, text="Click me", command=lambda: messagebox.showinfo("Selection", f"You selected: {entry.get()}"))
button.place(relx=0.5, rely=0.75, anchor='center')

# Run the application
root.mainloop()