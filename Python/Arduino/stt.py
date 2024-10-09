import speech_recognition as sr
import pyttsx3

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

def tts(answer):
  engine = pyttsx3.init()
  text = answer
  engine.say(text)
  engine.runAndWait()
