# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:15:41 2023
@author: tjtej
"""
#prerequisites libraries required
#pip install pyttsx3
#pip install keyboard

import keyboard
import pyttsx3
import win32clipboard

# Initialize the pyttsx3 engine
engine = pyttsx3.init()
# Define a variable to store the speech status
is_speaking = False
# Define a function to convert the text to speech
def speak(text):
    global is_speaking
    is_speaking = True
    engine.say(text)
    engine.runAndWait()
    is_speaking = False
# Define a function to get the selected text from the clipboard
def get_clipboard_text():
    win32clipboard.OpenClipboard()
    text = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return text
# Define a function to handle the hotkeys
def on_start_hotkey():
    # Get the selected text from the clipboard
    text = get_clipboard_text()

    # Convert the text to speech
    speak(text)
def on_stop_hotkey():
    global is_speaking
    if is_speaking:
        # Stop the speech
        engine.stop()
# Register the hotkeys
keyboard.add_hotkey('ctrl+alt+s', on_start_hotkey)
keyboard.add_hotkey('ctrl+alt+x', on_stop_hotkey)
# Start the event loop
keyboard.wait()