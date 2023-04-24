import tkinter as tk
from tkinter import messagebox
import pyttsx3
import speech_recognition as sr
import pyperclip
from tkinter import messagebox
from tkinter import simpledialog

def speak(text):
    """Uses text-to-speech to speak the given text."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_clipboard_text():
    """Returns the text currently on the clipboard."""
    return pyperclip.paste()


def set_clipboard_text(text):
    """Sets the clipboard text to the given text."""
    pyperclip.copy(text)


def stt():
    """Uses speech-to-text to recognize the user's speech."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening...")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio).lower()
        print("You said: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError as e:
        print("Sorry, an error occurred when requesting speech recognition results. ", e)


def tts(text):
    """Uses text-to-speech to read the given text."""
    speak("Reading text message.")
    speak(text)


def chatbot():
    """Asks the user if they want to speak or listen, and acts accordingly."""
    window = tk.Tk()
    window.geometry("400x300")
    window.title("Chatbot")

# Create a frame for the buttons
    button_frame = tk.Frame(window)
    button_frame.pack(pady=50)

    def speak_callback():
        speak("Please start speaking.")
        text = stt()
        set_clipboard_text(text)
        speak("Your message has been copied to the clipboard.")
        messagebox.showinfo("Success", "Your message has been copied to the clipboard.")

    def listen_callback():
        speak("Do you want me to read a text message for you?")
        response = stt()
        if response == "yes":
            text = get_clipboard_text()
            tts(text)
            messagebox.showinfo("Success", "The message has been read.")
        elif response=="manual":
            speak("Okay, please enter the message you want to listen.")
            window.withdraw()
            text = tk.simpledialog.askstring("Listen", "Enter the text message:")
            window.deiconify()
            set_clipboard_text(text)
            text = get_clipboard_text()
            tts(text)
            messagebox.showinfo("Success", "The message has been read.")
        else:
            speak("could not hear the choice")
    def exit():
        import Main
        exit=Main.py()
    
    speak_button = tk.Button(button_frame, text="Speak", command=speak_callback, font=("Arial", 20), bg="#0077be", fg="white")
    speak_button.pack(side="left", padx=10)

    listen_button = tk.Button(button_frame, text="Listen", command=listen_callback, font=("Arial", 20), bg="#00a859", fg="white")
    listen_button.pack(side="right", padx=10)
    
    
    window.config(bg="#f5f5f5")
    window.mainloop()


if __name__ == "__main__":
    chatbot()