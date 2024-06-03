import tkinter as tk
from tkinter import filedialog, messagebox, font as tkfont
import ollama

class TextEditor:
    def __init__(self):
        global AImodel
        global background_color, foreground_color
        self.window = tk.Tk()
        self.window.title("Text Editor")
        
        
        background_color = "black"
        foreground_color = "white"
        
        AImodel = "phi3"
        self.text_area = tk.Text(self.window, wrap=tk.WORD, bg=background_color, fg=foreground_color, insertbackground=foreground_color, selectbackground="lightblue")
        self.text_area.pack(expand=tk.YES, fill=tk.BOTH)

        self.text_area.bind("<Return>", self.ask_last_question)

        self.create_menu()
        self.create_toolbar()

        self.history = []
        self.history_index = -1

        self.window.mainloop()

    def create_menu(self):
        global background_color, foreground_color
        menu = tk.Menu(self.window, bg=background_color, fg=foreground_color)
        self.window.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_editor)

        edit_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Ai", menu=edit_menu)
        edit_menu.add_command(label="phi", command=self.phi_ai)
        edit_menu.add_command(label="wizard-math", command=self.wizard_math_ai)
        edit_menu.add_command(label="llama3", command=self.llama3_ai)
        edit_menu.add_command(label="mistral", command=self.mistral_ai)
        edit_menu.add_command(label="PiratePhi", command=self.PiratePhi_ai)
        edit_menu.add_command(label="summarizer", command=self.summarizer_ai)

        format_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Format", menu=format_menu)
        format_menu.add_command(label="Font", command=self.change_font)

        tools_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Word Count", command=self.word_count)

        theme_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Theme", menu=theme_menu)
        theme_menu.add_command(label="Light", command=self.light_theme)
        theme_menu.add_command(label="Dark", command=self.dark_theme)
        theme_menu.add_command(label="Blue", command=self.blue_theme)
        theme_menu.add_command(label="Hacker", command=self.Hacker_theme)
        theme_menu.add_command(label="Barbie", command=self.Barbie_theme)

    def light_theme(self):
        global foreground_color, background_color
        foreground_color = "black"
        background_color = "white"
        self.text_area.config(bg=background_color, fg=foreground_color, insertbackground=foreground_color)

    def dark_theme(self):
        global foreground_color, background_color
        foreground_color = "white"
        background_color = "black"
        self.text_area.config(bg=background_color, fg=foreground_color, insertbackground=foreground_color)

    def blue_theme(self):
        global foreground_color, background_color
        foreground_color = "light blue"
        background_color = "black"
        self.text_area.config(bg=background_color, fg=foreground_color, insertbackground=foreground_color)

    def Hacker_theme(self):
        global foreground_color, background_color
        foreground_color = "dark green"
        background_color = "black"
        self.text_area.config(bg=background_color, fg=foreground_color, insertbackground=foreground_color)

    def Barbie_theme(self):
        global foreground_color, background_color
        foreground_color = "#f8098c"
        background_color = "light pink"
        self.text_area.config(bg=background_color, fg=foreground_color, insertbackground=foreground_color)

    def create_toolbar(self):
        global background_color
        toolbar = tk.Frame(self.window, bg=background_color)
        toolbar.pack(side=tk.TOP, fill=tk.X)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file = filedialog.askopenfilename(defaultextension=".chapri", filetypes=[("Chapri Files", "*.chapri"), ("All Files", "*.*")])
        if file:
            self.window.title(f"Python Text Editor - {file}")
            self.text_area.delete(1.0, tk.END)
            with open(file, "r") as file_handler:
                self.text_area.insert(tk.INSERT, file_handler.read())

    def save_file(self):
        file = filedialog.asksaveasfilename(defaultextension=".chapri", filetypes=[("Chapri Files", "*.chapri"), ("All Files", "*.*")])
        if file:
            with open(file, "w") as file_handler:
                file_handler.write(self.text_area.get(1.0, tk.END))
            self.window.title(f"Python Text Editor - {file}")

    def exit_editor(self):
        self.window.quit()
    
    def wizard_math_ai(self):
        global AImodel
        AImodel = "wizard-math"

    def phi_ai(self):
        global AImodel
        AImodel = "phi3"
    
    def llama3_ai(self):
        global AImodel
        AImodel = "llama3"

    def mistral_ai(self):    
        global AImodel
        AImodel = "mistral"

    def PiratePhi_ai(self):
        global AImodel
        AImodel = "PiratePhi"

    def summarizer_ai(self):
        global AImodel
        AImodel = "summarizer"

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
    global AImodel
    response = ollama.chat(model=AImodel, messages=[{'role': 'user', 'content': question}], stream=False)
    answer = response['message']['content']
    return answer

if __name__ == "__main__":
    text_editor = TextEditor()