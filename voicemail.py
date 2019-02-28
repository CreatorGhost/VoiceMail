import smtplib
import speech_recognition as sr
'''def mymail(email,passwd,mssg):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email,passwd)
	server.sendmail(email, "assassinsadi@gmail.com", mssg)
	server.quit()

mymail("wantech010@gmail.com", "Googleapj", "Its Me Adii")
print("done")'''
r=sr.Recognizer()
with sr.Microphone() as ss:
	print("speak")
	listen = r.listen(ss)
	try:
		text = r.recognize_google(audio)
		print("you said : {}".format(text))
	except:
		print("fuck")
