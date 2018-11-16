r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source,duration=5)
	r.dynamic_energy_thresheld = True
	print("Say something!")
	audio = r.listen(source)



try:
	print("You said: " + r.recognise_google(audio))
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
execpt sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service"(0)".format(e))														