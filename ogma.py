import speech_recognition as sr
from tts_watson.TtsWatson import TtsWatson


# initiaze Watson text to Speech
ttsWatson = TtsWatson('oskik313@gmail.com', 'MamNaImieOskar313.', 'en-US_AllisonVoice')
ttsWatson.play("Hello World")


# get audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)
try:
    print("You said " + r.recognize_google(audio))
    command = r.recognize_google(audio)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

