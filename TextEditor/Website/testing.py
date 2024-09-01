# Assuming ollamaAI is correctly installed and importable
import ollamaAI

questions = []
answers = []

def chat():
    question = input("What is your question? ")
    answer = ollamaAI.ans(question, "phi")  # Ensure "phi" is a valid parameter for ollamaAI.ans()
    answers.append(answer)
    questions.append(question)

for _ in range(3):  # Collecting 3 sets of questions and answers
    chat()

# Printing all questions and answers in an orderly format
for i, (question, answer) in enumerate(zip(questions, answers), start=1):
    print(f"{i}. Question: {question}\n   Answer: {answer}\n")
