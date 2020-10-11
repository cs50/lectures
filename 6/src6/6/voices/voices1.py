# Recognizes a voice
# https://pypi.org/project/SpeechRecognition/

import speech_recognition

# Obtain audio from the microphone
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something!")
    audio = recognizer.listen(source)

# Recognize speech using Google Speech Recognition
print("Google Speech Recognition thinks you said:")
print(recognizer.recognize_google(audio))
