import pyaudio
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Say Somthing");
    audio = r.listen(source)
    print("Times Up...")
    
    
try:
    text = r.recognize_google(audio)
    print("you said : {}".format(text))
except:
    print("fuck") 
