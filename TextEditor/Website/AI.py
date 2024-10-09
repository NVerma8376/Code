import ollama
import google.generativeai as genai
import os

def ans(quess, ai, mode):
    if mode == "offline":
        response = ollama.chat(model=ai, messages=[{'role':'user', 'content':quess}])
        answer = response['message']['content']
        return answer
    elif mode == "online":
        genai.configure(api_key=os.environ["API_KEY"])
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(quess)
        answer = (response.text)
        return answer