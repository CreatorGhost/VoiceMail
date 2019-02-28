import pyaudio

import speech_recognition as sr  

def voice():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Somthing");
        audio = r.listen(source)
        print("Times Up...")
    try:
        text = r.recognize_google(audio)
        print("you said : {}".format(text))
        k = ("{}".format(text))
        return k
    except:
        print("nopee")
      
    
    
voice()    


import smtplib

def mymail(email,passwd,mssg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email,passwd)
    server.sendmail(email, "assassinsadi@gmail.com", mssg)
    server.quit()


if k == "send mail":
        print("Sending Mail.....")
        print ("Please Provide the message..")
        message = voice()
        mymail("wantech010@gmail.com", "Googleapj", message)
else:
    print("Say Send Mail")
