import speech_recognition as sr
import pyttsx3

import os

speech_engine = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Please say something:")
        audio = speech_engine.listen(source, phrase_time_limit=5)  # Set a 5-second limit
        print("Recognizing...")
        try:
            text = speech_engine.recognize_google(audio, language="en-IN")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")


def text_to_speech(text):
    com = f"espeak-ng '{text}'"
    os.system(com)


