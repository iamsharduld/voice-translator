import pyttsx

def run(text):
	engine = pyttsx.init()
	engine.say(text)
	#engine.say('The quick brown fox jumped over the lazy dog.')
	engine.runAndWait()

