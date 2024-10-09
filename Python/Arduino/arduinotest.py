import serial
import time
import stt
import ollama
import pyttsx3

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

def TTS(text):
    newVoiceRate = 145
    engine.setProperty('rate',newVoiceRate)
    engine.setProperty('voice', 4)
    engine.say(text)
    engine.runAndWait()

def button():
    global ispressed, answer, question
    command = serial1.read(2)
    if len(command) == 2:
        if command == b"B1" and not ispressed:
            print("Button is pressed")
            question = stt.listen()
            print(question)
            ispressed = True
            time.sleep(1)  # Debounce time for button press and release
            for i in range(3):
                serial1.write(b"H")
                time.sleep(0.2)
                serial1.write(b"L")

        elif command == b"B2" and ispressed:
            print("Button is released")
            response = ollama.chat(model="phi", messages=[{'role': 'user', 'content': question}], stream=False)
            answer = response['message']['content']
            print(answer)
            TTS(answer)  # Call the TTS function here
            
            ispressed = False

while True:
    button()
