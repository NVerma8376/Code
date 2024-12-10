import tkinter as tk
from tkinter import messagebox

# Set up the main window
root = tk.Tk()
root.title("Modern Blue and Pink Input UI")
root.geometry("500x400")

# Set modern theme
root.configure(bg="#f0f0f0")  # Light gray background

# Create input field
input_frame = tk.Frame(root, bg="#f0f0f0", highlightbackground="#dcdcdc", highlightthickness=1)
input_frame.pack(pady=30)

label = tk.Label(input_frame, text="Enter your message:", font=('Helvetica', 16, 'bold'), bg="#f0f0f0", fg="#333333")
label.pack(side=tk.LEFT, padx=10)

entry = tk.Entry(input_frame, font=('Helvetica', 16), width=40)
entry.pack(side=tk.LEFT, padx=10)

# Create submit button
submit_button = tk.Button(root, text="Submit", command=lambda: submit_message(entry.get()), 
                          bg="#4682b4", fg="#ffffff", font=('Helvetica', 14, 'bold'), relief="flat", bd=0)
submit_button.pack(pady=20)

def submit_message(message):
    messagebox.showinfo("Message", f"You entered:\n\n{message}\n\nThank you for your input!")

if __name__ == "__main__":
    root.mainloop()
