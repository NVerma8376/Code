import serial
import time
import stt
import ollama
import pyttsx3

from ollama import chat
from ollama import ChatResponse

# Initialize pyttsx3 engine at the start of the script
engine = pyttsx3.init()

global ispressed
ispressed = False
global answer, question
answer = ""
question = ""

# Set up the serial connection to the Arduino
serial1 = serial.Serial('/dev/ttyUSB0', 9600)
print("connected to: " + serial1.portstr)
def ai(text):
    response: ChatResponse = chat(model='phi', messages=[
        {
            'role': 'user',
            'content': text,
        },
    ])
    return (response['message']['content'])

def button():
    global ispressed
    command = serial1.read(2)
    if len(command) == 2:
        if command == b"B1" and not ispressed:
            print("B1 pressed")
            text = stt.tts()
            say = ai(text)
            stt.text_to_speech(say)
            ispressed = True
        elif command == b"B2" and ispressed:
            print("B2 released")
            ispressed = False

while True:
    button()