#Visual to Speech Impaired
# dont know same code as VtoIMP
import speech_recognition as sr
from PIL import ImageTk
import pyttsx3
import csv 
import os
import keyboard
import pyttsx3
import win32clipboard 

filename = "Speech to sign.txt"

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

def speak(text):
   engine = pyttsx3.init()
   engine.say(text)
   engine.runAndWait()  

def TTS():
    f = open(filename, "r")
    text = f.read()
    speak(text)
    f.close()

def speaker():
    SpeakText("Please, go ahead")
    MyText = speech()
    f = open(filename, "w")
    f.write(MyText)
    f.close()

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

def listener():
    SpeakText("Do you want me to read a text message for you?")
    MyText = speech()
    speech_word = MyText.lower()
    if speech_word == "yes":
        TTS()
    elif speech_word == "no":
        return
    else:
        SpeakText("Invalid")

def Sign_language_View():
    import Misc
    Misc()

def Sign_language_Interpreter():
    import app
    app()
def user_visual():
    SpeakText("Do you wish to speak or listen?")
    MyText = speech()
    speech_boolean = MyText.lower()
    if speech_boolean == "speak":
        speaker()
    elif speech_boolean == "listen":
        listener()
    else:
        SpeakText("Invalid")   
def user_speech():
    SpeakText("Do you wish to speak or listen?")
    MyText = speech()
    speech_boolean = MyText.lower()
    if speech_boolean == "speak":
        Sign_language_Interpreter()
    elif speech_boolean == "listen":
        listener()
    else:
        SpeakText("Invalid")  
SpeakText("Please choose user type: 1 for visual impaired 2 for speech impaired")
MyText = speech()
choice = int(MyText)
if choice ==1:
    user_visual()
elif choice == 2:
    user_speech()
else:
    SpeakText("Invalid user type")