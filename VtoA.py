#Visual to Speech Impaired
#same code as VtoIMP
import speech_recognition as sr
from PIL import ImageTk
import pyttsx3
from VtoIMP import chatbot 
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
            return (MyText)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
def speak(text):
   engine = pyttsx3.init()
   engine.say(text)
   engine.runAndWait()

def user_visual():
    chatbot()    
    
def user_auditory():
    SpeakText("Do you wish to speak or listen?")
    MyText = speech()
    speech_boolean= MyText.lower()
    from app import starter
    
    if speech_boolean == "listen":
        starter() 
        
    elif speech_boolean =="speak" or "pic":  
        from vtoswindow import root      
        root.mainloop()
    else:
        SpeakText("Invalid")
def VtoAmain(): 
    SpeakText("Please choose user type: 1 for visual impaired 2 for auditory impaired")
    Choice = speech()
    if Choice == 1 or 2 or "tu":
        if Choice==1:
            user_visual()
        elif Choice==2 or "tu":
            user_auditory()        
    else:
        SpeakText("Invalid Choice")
