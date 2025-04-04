from signal import SIG_DFL
import serial
import time
import stt
import os
from ollama import *
import google.generativeai as genai

# Set up the serial connection
arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)  # Update '/dev/ttyUSB0' to your Arduino port
time.sleep(2)  # Allow time for the connection to initialize

print("Python connected to Arduino")

def gen(input):
    response: ChatResponse = chat(model='phi', messages=[
      {
        'role': 'user',
        'content': input,
      },
    ])
    return response['message']['content']
    # or access fields directly from the response object
    # print(response.message.content)

try:

    while True:
        # Read data from the Arduino
        if arduino.in_waiting > 0:
            data = arduino.readline().decode().strip()
            if data:
                if data == "B1":
                    print("Button pressed!")
                    input = stt.listen()
                    ans = gen(input)
                    stt.text_to_speech(ans)
except KeyboardInterrupt:
    print("\nExiting on user interrupt...")

finally:
    arduino.close()
    print("Connection closed.")



    