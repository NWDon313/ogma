from pynput.keyboard import Key
from pynput import keyboard
import speech_recognition as sr
import pyttsx3
from commands import analyzeString

# get audio from the microphone
def voiceRecognizer():
    # Initiaze TtoS
    xengine = pyttsx3.init()
    # Initiaze voice recording
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
        xengine.say('One moment , sir. ')
        xengine.runAndWait()
    try:
        command = r.recognize_google(audio)
        analyzeString(command)
        print(command)
    except sr.UnknownValueError:
        print("Could not understand audio")
        xengine.say('Could you repeat that?. ')
        xengine.runAndWait()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

# listen for button pressed
def on_press(key):
    try:
        if key == Key.insert:
            print("so far so good")
            voiceRecognizer()
    except AttributeError:
       print("some error occured")


#Key listener
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
