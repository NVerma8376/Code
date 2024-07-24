import ollamaAI
data = []

while True:
    question = input("question: ")
    ans = ollamaAI.ans(question, "phi")
    data.append(ans)
    for message in data:
        print(message)



