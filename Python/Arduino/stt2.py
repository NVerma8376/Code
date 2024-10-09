import speech_recognition as sr

speech_engine = sr.Recognizer()

def from_mic():
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

print(from_mic())
