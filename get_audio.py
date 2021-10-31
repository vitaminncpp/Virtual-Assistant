from logging import root

import speech_recognition as sr
import assistant_speaks as ass
import tkinter as tk
import playsound as ps


def get_audio(limit=2):
    rObject = sr.Recognizer()
    audio = ''
    
    with sr.Microphone() as source:
        print("Please Ask What You Need")
    
        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit=2)
    print("Please Stop.")  # limit 5 secs

    try:
    
        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text.lower()
    
    except:
    
        ass.assistant_speaks("Could not understand your audio, PLease try again !")
        return ''
    # master = tk.Tk()
    # e = tk.Entry(master)
    # e.pack()
    # s = ''
    #
    # def callback():
    #     global s
    #     s = e.get()
    #     master.quit()
    #
    # e.focus_set()
    # b = tk.Button(master, text="OK", width=10, command=callback)
    # b.pack()
    # master.mainloop()
    # return s.lower()
    # return input("Enter Command : ").lower()
