# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3 

def listen():
    # Initialize the recognizer 
    r = sr.Recognizer()     

    # Function to convert text to
    # speech
    #def SpeakText(command):    

      # Initialize the engine
    #  engine = pyttsx3.init()
    #  engine.say(command) 
    #  engine.runAndWait()  


    # Loop infinitely for user to
    # speak 
    i = 1
    while(i < 2):   
      i += 1
      # Exception handling to handle
      # exceptions at the runtime
      try:  

        # use the microphone as source for input.
        with sr.Microphone() as source2:    

          # wait for a second to let the recognizer
          # adjust the energy threshold based on
          # the surrounding noise level 
          r.adjust_for_ambient_noise(source2, duration=0.2) 

          #listens for the user's input 
          audio2 = r.listen(source2)    

          # Using google to recognize audio
          MyText = r.recognize_google(audio2)
          MyText = MyText.lower()   

          #print("Did you say ",MyText)
          #SpeakText(MyText)
          engine = pyttsx3.init()
          engine.runAndWait()   
          return MyText 
          

      except sr.RequestError as e:
        print("Could not request results; {0}".format(e))   

      except sr.UnknownValueError:
        print("unknown error occurred") 


