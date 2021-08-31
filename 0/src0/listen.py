import pyttsx3
import speech_recognition

print("What's your name? ")
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    audio = recognizer.listen(source)
name = recognizer.recognize_google(audio)

engine = pyttsx3.init()
engine.say(f"hello, {name}")
engine.runAndWait()
