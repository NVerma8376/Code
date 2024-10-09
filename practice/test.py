from tkinter import *
import ollama
import google.generativeai as genai
import os


# GUI
root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#89ABE3"
TEXT_COLOR = "#00246B"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Send function
def send():
	send = "You -> " + e.get()
	txt.insert(END, "\n" + send)

	user = e.get().lower()

	answer = ans(user)
	txt.insert(END, "\n" + f"Bot -> {answer}")

	e.delete(0, END)

def ans(quess):
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(quess)
    answer = (response.text)
    return answer


txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)



e = Entry(root, bg="#89ABE3", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="➜", font=FONT_BOLD, bg="#EA738D",
			command=send).grid(row=2, column=1)

root.mainloop()
