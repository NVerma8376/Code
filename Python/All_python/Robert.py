import random
import win32com.client as wincl


print("I am a chat bot and your friend.")
print("say (bye)to end the chat")
print("My name is Robert")


while 1 == 1:
    print("Say something.")

    word = str(input("-"))

    if word == "bye":
        break

    if word == "Robert do math":
        print("Robert does math")
        mathtype = input("sign=")
        if mathtype == "+":
            print("add")
            num = int(input("num1="))
            num2 = int(input("num2="))
            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak(num+num2)

        if mathtype == "-":
            print("subtract")
            num = int(input("num1="))
            num2 = int(input("num2="))
            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak(num-num2)

        if mathtype == "*":
            print("multiply")
            num = int(input("num1="))
            num2 = int(input("num2="))
            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak(num*num2)

        if mathtype == "/":
            print("divide")
            num = int(input("num1="))
            num2 = int(input("num2="))
            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak(num/num2)

    if word == "hello":
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak("hello what is your name")

    if word == "naitik":
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak(
            "I am Robert if you want me to do something,just say (Robert do)and what ever you want me to do.")

    if word == "how are you":
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak("fine")

    magic_ball = ["Certainly", "Yes", "No", "Why not", "Please say it again", "Fine",
                  "Hello", "What", "What is your name", "My name is Robert", "I code!!", "thanks"]
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(random.choice(magic_ball))
