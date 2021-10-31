import os
import text_process as tp
import date_access as da
import assistant_speaks as ass
import get_audio as ga


def Main():
    ass.assistant_speaks("Hello, Akshay ! this is Mr. X. Your Personal Assistant...")
    n = "Akshay"

    ass.assistant_speaks("Today's date is " + da.get_date())

    while True:

        ass.assistant_speaks("Tell me What for today? Anything Special For me ...")
        text = ga.get_audio()
        # text=input('Please Enter Command : ')
        if text == '':
            continue

        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            ass.assistant_speaks("Ok bye, " + n + '.')
            break

        # calling process text to process the query
        tp.process_speak(text)


if __name__ == "__main__":
    Main()



