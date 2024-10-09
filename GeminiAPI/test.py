import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")
text = input("Enter a prompt: ")
response = model.generate_content(text)
print(response.text)



