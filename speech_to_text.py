# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:42:16 2023

@author: tjtej
"""
#prerequisites libraries required
#pip install SpeechRecognition
#if you encounter error while installing this library try
#pip install --upgrade pip
#pip install pyaudio

import speech_recognition as sr
import pyaudio


# Initialize the recognizer
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

# Convert speech to text
try:
    text = r.recognize_google(audio)
    print("You said: {}".format(text))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {}".format(e))