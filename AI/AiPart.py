import ollama

def giveansofques(question):

    response = ollama.chat(model='phi', messages=[
    {
        'role': 'user',
        'content': question,
    },
    ])
    return (response['message']['content'])