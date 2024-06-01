import tkinter as tk
from tkinter import filedialog, messagebox, font as tkfont
import ollama

class TextEditor:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Python Text Editor")

        self.text_area = tk.Text(self.window, wrap=tk.WORD, bg="black", fg="white", insertbackground="white", selectbackground="lightblue")
        self.text_area.pack(expand=tk.YES, fill=tk.BOTH)

        self.text_area.bind("<Return>", self.ask_last_question)

        self.create_menu()
        self.create_toolbar()

        self.history = []
        self.history_index = -1

        self.window.mainloop()

    def create_menu(self):
        menu = tk.Menu(self.window, bg="black", fg="white")
        self.window.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_editor)

        edit_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", menu=edit_menu)
        #edit_menu.add_command(label="Undo", command=self.undo_action, accelerator="Ctrl+Z")
        #edit_menu.add_command(label="Redo", command=self.redo_action, accelerator="Ctrl+Y")
        #self.window.bind_all("<Control-z>", lambda event: self.undo_action())
        #self.window.bind_all("<Control-y>", lambda event: self.redo_action())

        format_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Format", menu=format_menu)
        format_menu.add_command(label="Font", command=self.change_font)

        tools_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Word Count", command=self.word_count)

    def create_toolbar(self):
        toolbar = tk.Frame(self.window, bg="black")
        toolbar.pack(side=tk.TOP, fill=tk.X)

        #undo_button = tk.Button(toolbar, text="Undo", command=self.undo_action, bg="black", fg="white")
        #undo_button.pack(side=tk.LEFT, padx=2, pady=2)

        #redo_button = tk.Button(toolbar, text="Redo", command=self.redo_action, bg="black", fg="white")
        #redo_button.pack(side=tk.LEFT, padx=2, pady=2)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            self.window.title(f"Python Text Editor - {file}")
            self.text_area.delete(1.0, tk.END)
            with open(file, "r") as file_handler:
                self.text_area.insert(tk.INSERT, file_handler.read())

    def save_file(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            with open(file, "w") as file_handler:
                file_handler.write(self.text_area.get(1.0, tk.END))
            self.window.title(f"Python Text Editor - {file}")

    def exit_editor(self):
        self.window.quit()

    def undo_action(self, event=None):
        if self.history_index > 0:
            self.history_index -= 1
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, self.history[self.history_index])

    def redo_action(self, event=None):
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, self.history[self.history_index])

    def change_font(self):
        font_tuple = tkfont.Font(font=self.text_area["font"])
        font = filedialog.askopenfilename()
        if font:
            self.text_area.configure(font=font)

    def word_count(self):
        content = self.text_area.get(1.0, tk.END)
        words = content.split()
        messagebox.showinfo("Word Count", f"Total words: {len(words)}")

    def ask_last_question(self, event):
        lines = self.text_area.get("1.0", tk.END).split("\n")
        last_line = lines[-2] if lines[-1] == "" else lines[-1]
        if last_line.strip().endswith("/ask"):
            question = last_line.strip()[:-4].strip()
            answer = askquestion(question)
            self.text_area.insert(tk.END, f"\nAI: {answer}\n")

def askquestion(question):
    response = ollama.chat(model='phi', messages=[{'role': 'user', 'content': question}])
    answer = response['message']['content']
    return answer

if __name__ == "__main__":
    text_editor = TextEditor()