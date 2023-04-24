import pyttsx3
import speech_recognition as sr
import tkinter as tk
from PIL import Image, ImageTk
from VtoIMP import chatbot
from tkinter import simpledialog
from VtoA import VtoAmain
from app import starter
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
            return int(MyText)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")

def nextPage():
    import Main
    Main()
    root.destroy()

def Visual_to_NonImpaired():
    import VtoIMP
    VtoIMP()
    
def Visual_to_Speech():
    from app import starter

def Visual_to_Auditory():
    from VtoA import VtoAmain
    
    
def Visual_to_Auditory_and_Speech():
    from vtoswindow import root

def next(Code):
    if Code == 1:    
        chatbot()           #speech to text and Text to speech 
    elif Code == 2:
        chatbot()      #speech to text and Text to speech 
    elif Code == 3:
        starter()           #speech to text 
    elif Code == 4:
        VtoAmain()         #sign language 
    elif Code == 5:
        root.mainloop()             #speech to sign language
    else:
        SpeakText("Invalid Choice")

def manual_input():
    global Code
    SpeakText("1 for non-impaired")
    SpeakText("2 for visual impairment")
    SpeakText("3 for speech impairment")
    SpeakText("4 for auditory impairment")
    SpeakText("5 for speech and auditory impairment")
    Code = simpledialog.askinteger("Input", "Please enter your choice:")
    next(Code)

def voice_input():
    global Code
    SpeakText("1 for non-impaired")
    SpeakText("2 for visual impairment")
    SpeakText("3 for speech impairment")
    SpeakText("4 for auditory impairment")
    SpeakText("5 for speech and auditory impairment")
    SpeakText("Please say your choice")
    Choice = speech()
    if Choice == 1 or 2 or 3 or 4 or 5:
        Code = Choice
        next(Code)
    else:
        SpeakText("Invalid Choice")
        Code = 0

# GUI code
def manual_button():
    manual_input()

def voice_button():
    voice_input()

root = tk.Tk()
root.title("Tech It Easy Menu")
root.geometry("600x600")
root.configure(bg="#FFFFFF")

# Add image
image = Image.open("C:/Users/DELL/Downloads/Tech-It-Easy-main/Tech-It-Easy-main/TIE2.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo, borderwidth=2, relief="solid")
label.pack(pady=10)

# Add buttons
font = ("Arial", 14)

manual_button = tk.Button(root, text="Enter Choice", font=font, command=manual_button)
manual_button.pack(pady=20)

voice_button = tk.Button(root, text="Voice Choice", font=font, command=voice_button)
voice_button.pack()

root.mainloop()