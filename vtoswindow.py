import tkinter as tk
from Speechinput import speech_to_text 
from Misc import speech_to_sign
def listen_clicked():
    speech_to_text()

def show_sign_language_clicked():
     speech_to_sign("Speech to sign.txt")
     

root = tk.Tk()
root.geometry("400x300")  # Set the size of the window
root.configure(bg='#F0F0F0')  # Set the background color

# Add an empty label to center the buttons
middle_label = tk.Label(root, text="", width=20, bg='#F0F0F0')
middle_label.pack(side=tk.LEFT)

# Add the Listen button

listen_button = tk.Button(root, text="Listen", command=listen_clicked, font=("Arial", 20), bg="#00a859", fg="white")
listen_button.pack(side="right", padx=10)
# Add the Show Sign Language button

show_sign_language_button = tk.Button(root, text="Speak", command=show_sign_language_clicked, font=("Arial", 20), bg="#0077be", fg="white")
show_sign_language_button.pack(side="left", padx=10)

root.mainloop()