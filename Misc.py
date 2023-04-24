import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string

isl_gif = ['account closing', 'account currency', 'address', 'afternoon', 'ahemdabad', 'all', 'annually', 'any questions',
               'any', 'anyone', 'are you angry', 'are you busy', 'are you hungry', 'assam', 'assets', 'audit', 'august', 
               'automatic', 'balance', 'banana', 'banaras', 'banglore', 'be careful', 'black ice', 'blizzard', 'breezy',
               'bridge', 'card', 'cash', 'cat', 'christmas', 'church', 'cilinic', 'clear skies', 'cold', 'compound interest',
               'credit', 'current account', 'dasara', 'day', 'december', 'default', 'degrees', 'did you finish homework', 'direct', 
               'do you have money', 'do you want something to drink', 'do you watch tv', 'dont worry', 'dry', 'dusk', 'dust storm',
               'each', 'early', 'either', 'else', 'evening', 'every monday', 'every tuesday', 'every two months', 'every two weeks',
               'every two years', 'every wednesday', 'every week', 'everyday', 'everyone', 'everything', 'february', 'few', 'flower is beautiful',
               'fraud', 'friday', 'fund', 'good afternoon', 'good morning', 'good question', 'grapes', 'hail', 'he', 'heat wave', 'heavy rain',
               'hello', 'her', 'herself', 'him', 'himself', 'hindu', 'hot', 'hour', 'humid', 'hyderabad', 'i am a clerk', 'i am fine', 'i am sorry',
               'i am thinking', 'i am tired', 'i go to a theatre', 'i had to say something but i forgot', 'i like pink colour', 'i love to shop',
               'i', 'ice', 'interest rate', 'investment', 'it', 'itself', 'january', 'job', 'july', 'june', 'karnataka', 'kerala', 'krishna', 'late night',
               'late', 'lend', 'lets go for lunch', 'lightning', 'liquidation', 'loan', 'mango', 'many', 'march', 'may', 'me', 'midnight', 'mile', 'monday',
               'money', 'monthly', 'morning dew', 'morning', 'mortgage', 'mumbai', 'my', 'myself', 'nagpur', 'net profit', 'nice to meet you', 'night', 'none',
               'noon', 'nothing', 'november', 'open the door', 'our', 'ourselves', 'overdraft', 'pakistan', 'password', 'paying slip', 'please call me later',
               'please wait for sometime', 'police station', 'post office', 'pouring rain', 'principal', 'pune', 'punjab', 'rainbow', 'refinance', 'reserve fund', 
               'saturday', 'scattered rain', 'scattered snow', 'second', 'security collateral', 'security', 'shall i help you', 'shall we go together tommorow', 
               'share equity', 'shop', 'sign language interpreter', 'sit down', 'slippery walking', 'slippery', 'smog', 'snow', 'some', 'somebody', 'someone', 
               'something', 'soon', 'spring', 'stand up', 'statement of account', 'statement', 'stock', 'summer', 'sun', 'sunday', 'sunrise', 'sunset', 'take care', 'teller', 'temperature', 'temple', 'their', 'them', 'there was traffic jam', 'thunder', 'thursday', 'time', 'today', 'toilet', 'tomato', 'transaction', 'transfer', 'trust', 'tuesday', 'us', 'usa', 'village', 'visitor', 'we', 'weather', 'wednesday', 'weekend', 'what are you doing', 'what is the problem', "what is today's date", 'what is your father do', 'what is your mobile number', 'what is your name', 'what', 'whats up', 'where is the bathroom', 'where is the police station', 'which', 'who', 'windy', 'wintering', 'working hours', 'you are wrong', 'yourself']
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
import os

def user_input(input_text):  
    try:
        a = input_text.lower()
        for c in string.punctuation:
            a = a.replace(c, "")
        if (a.lower() in isl_gif):
            class ImageLabel(tk.Label):
                """a label that displays images, and plays them if they are gifs"""
                def load(self, im):
                    if isinstance(im, str):
                        im = Image.open(im)
                    self.loc = 0
                    self.frames = []
                    try:
                        for i in count(1):
                            self.frames.append(ImageTk.PhotoImage(im.copy()))
                            im.seek(i)
                    except EOFError:
                        pass
                    try:
                        self.delay = im.info['duration']
                    except:
                        self.delay = 100

                    if len(self.frames) == 1:
                        self.config(image=self.frames[0])
                    else:
                        self.next_frame()
                def unload(self):
                    self.config(image=None)
                    self.frames = None

                def next_frame(self):
                    if self.frames:
                        self.loc += 1
                        self.loc %= len(self.frames)
                        self.config(image=self.frames[self.loc])
                        self.after(self.delay, self.next_frame)
            root = tk.Tk()
            lbl = ImageLabel(root)
            lbl.pack()
            gif_path = 'C:/Users/DELL/Downloads/Tech-It-Easy-main/Tech-It-Easy-main/download/{}.gif'.format(a.lower())
            if os.path.exists(gif_path):
                lbl.load(gif_path)
                root.mainloop()
            else:
                print("GIF file not found.")
        else:
            word = input_text.split()
            for i in word:
                if (i.lower() in isl_gif):
                    gif_path = 'C:/Users/DELL/Downloads/Tech-It-Easy-main/Tech-It-Easy-main/download/{}.gif'.format(i.lower())
                    if os.path.exists(gif_path):
                        im = Image.open(gif_path)
                        im.show()
                    else:
                        print("GIF file not found.")
                else:
                    lst=[]
                    a = i
                    for letter in a:
                        lst.append(letter)
                    for k in lst:
                        if(k.lower() in arr):
                            img_path = 'C:/Users/DELL/Downloads/Tech-It-Easy-main/Tech-It-Easy-main/letters/{}.jpg'.format(k)
                            if os.path.exists(img_path):
                                im = Image.open(img_path)
                                im.show()
                            else:
                                print("Image file not found.")
                        else :
                            print("Word Not Found")      
    except Exception as e:
        print(f"Error: {e}")

path_to_file = "Speech to sign.txt"
    
def speech_to_sign(path_to_file):
    with open(path_to_file, "r") as file:
        content = file.read() 
    return user_input(content)