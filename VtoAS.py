#Visual to Speech Impaired
#same code as VtoIMP
import speech_recognition as sr
from PIL import ImageTk
import pyttsx3
import csv 
import os

import keyboard
import pyttsx3
import win32clipboard
import pyttsx3

filename="Speech to sign.txt"

def SpeakText(command):
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
    
    
def speech():
    r = sr.Recognizer()
    try:
            
    	#SpeakText("Say start to begin")
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
    			#Text(MyText)
        
    except sr.RequestError as e:
    	print("Could not request results; {0}".format(e))
    		
    except sr.UnknownValueError:
    	print("unknown error occurred")
    
    return MyText

   

#def get_clipboard_text():
 #   win32clipboard.OpenClipboard()
  #  text = win32clipboard.GetClipboardData()
   # win32clipboard.CloseClipboard()
   # return text

def speak(text):
   engine = pyttsx3.init()
   engine.say(text)
   engine.runAndWait()

    
def TTS():
    f = open(filename, "ro")
    text = f.read()
    speak(text)
    return

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
    speech_word= MyText.lower()
    if speech_word == "yes":
        TTS()
    elif speech_word == "no":
        return
    else:
        SpeakText("Invalid")
    return 
  
def Sign_language_View():
    import Misc.py

def Sign_language_Interpreter():
    import app.py
    
def user_visual():
    SpeakText("Do you wish to speak or listen?")
    MyText = speech()
    speech_boolean= MyText.lower()

    if speech_boolean =="speak":
        speaker()
    elif speech_boolean == "listen":
        listener()
    else:
        SpeakText("Invalid")
        
def user_speech_auditory():
    SpeakText("Do you wish to speak or listen?")
    MyText = speech()
    speech_boolean= MyText.lower()

    if speech_boolean =="speak":
        Sign_language_Interpreter()
    elif speech_boolean == "listen":
        Sign_language_View()
    else:
        SpeakText("Invalid")
        
SpeakText("Please choose user type: 1 for visual impaired 2 for speech and auditory impaired")
MyText = speech()
choice = MyText.lower()
if choice =="one":
    user_visual()
elif choice == "two" or "2":
    user_speech_auditory()
else:
    SpeakText("Invalid user type")
   