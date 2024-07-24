import ollama

def ans(quess, ai):
    response = ollama.chat(model=ai, messages=[{'role':'user', 'content':quess}])
    answer = response['message']['content']
    return answer