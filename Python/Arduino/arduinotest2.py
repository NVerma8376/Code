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


def button():
    global ispressed
    command = serial1.read(2)
    if len(command) == 2:
        if command == b"B1" and not ispressed:
            print("B1 pressed")
            exit()
            ispressed = True
        elif command == b"B2" and ispressed:
            print("B2 released")
            ispressed = False

while True:
    button()