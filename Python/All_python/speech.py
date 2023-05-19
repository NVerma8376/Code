from gtts import gTTS
import os
text = str(input("text"))

tts = gTTS(text=text, lang='en')
tts.save("j.mp3")

os.system("start j.mp3")

