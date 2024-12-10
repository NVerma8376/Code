import customtkinter as ctk
import google.generativeai as genai
import os
from tkinter import filedialog, messagebox


# Configure API Key
def configure_api():
    genai.configure(api_key=os.environ["API_KEY"])

# Function to upload and extract text from a .txt file
def extract_text_from_txt(txt_file):
    with open(txt_file, "r") as file:
        return file.read()

# Function to upload and extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    import PyPDF2
    with open(pdf_file, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

# Function to handle file upload and extraction
def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf")])
    if file_path:
        if file_path.endswith(".pdf"):
            file_text = extract_text_from_pdf(file_path)
        elif file_path.endswith(".txt"):
            file_text = extract_text_from_txt(file_path)
        else:
            messagebox.showerror("File Error", "Please upload a valid .txt or .pdf file.")
            return
        text_area.delete(1.0, ctk.END)  # Clear previous text
        text_area.insert(ctk.END, file_text)
        generate_questions(file_text)

# Function to generate questions using Gemini API
def generate_questions(text):
    try:
        prompt = f"Please generate questions from the following text:\n\n{text}\n\nThe questions should be concise and informative."
        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
        questions = response.text.strip().split("\n")
        if questions:
            question_area.delete(1.0, ctk.END)  # Clear previous questions
            for question in questions:
                question_area.insert(ctk.END, f"{question}\n\n")
            ask_question(questions[0])  # Start with the first question
        else:
            messagebox.showinfo("No Questions", "No questions were generated.")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred while generating questions: {e}")

# Function to ask the user a question
def ask_question(question):
    answer = ctk.simpledialog.askstring("Answer", question)
    if answer:
        check_answer(question, answer)

# Function to check the user's answer using the Gemini API
def check_answer(question, answer):
    try:
        prompt = f"Is the following answer correct for the question: '{question}'?\nAnswer: {answer}\n\nPlease respond with 'Yes' or 'No'."
        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
        result = response.text.strip()
        messagebox.showinfo("Answer Check", f"Gemini Response: {result}")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred while checking the answer: {e}")

# Set up the GUI
root = ctk.CTk()
root.title("AI Flashcards")
root.geometry("600x400")

# Text area for displaying the content of the file
text_area = ctk.CTkTextbox(root, height=10, width=50)
text_area.grid(row=0, column=0, padx=20, pady=20)

# Area for displaying generated questions
question_area = ctk.CTkTextbox(root, height=10, width=50)
question_area.grid(row=1, column=0, padx=20, pady=20)

# Button to upload the file
upload_button = ctk.CTkButton(root, text="Upload File", command=upload_file)
upload_button.grid(row=2, column=0, pady=20)

# Initialize the Gemini API with the correct API key
configure_api()

# Start the GUI
root.mainloop()
