import pyttsx3



def tts(lines):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 130)
    engine.setProperty('voice', voices[10].id)
    engine.say(lines)
    engine.runAndWait()

