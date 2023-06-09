import speech_recognition as sr
from PIL import ImageTk
import pyttsx3
import csv 

def SpeakText(command):
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
    
def speech():
    r = sr.Recognizer()
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print("I am listening ")
            #listens for the user's input
            audio2 = r.listen(source2)
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower() 
            print(MyText) 
            SpeakText(MyText)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
    return MyText

def nextPage():
    import Main
    Main()
Mytext = speech()
if (Mytext=="start"):
    nextPage()