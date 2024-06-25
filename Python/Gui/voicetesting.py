import pyttsx3

engine = pyttsx3.init()

voice = engine.getProperty("voices")
for i in voice:
    print(i)

engine.say("Hello, I am a text to speech engine")