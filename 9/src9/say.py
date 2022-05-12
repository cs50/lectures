import cowsay
import pyttsx3

engine = pyttsx3.init()
cowsay.cow("This was CS50")
engine.say("This was CS50")
engine.runAndWait()
