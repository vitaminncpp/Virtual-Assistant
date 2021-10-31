import web_access as wa
import wolframalpha
from open_app import open_application
import datetime
import assistant_speaks as ass
import date_access as da
import get_audio as ga
import wikipedia

def process_speak(text):
    # print(text)
    while True:
        if 'search' in text:
            wa.find_web(text)
            return
        elif 'today date' in text or 'date' in text:
            ass.assistant_speaks(da.get_date())
            return
        elif "who are you" in text or "define yourself" in text:
            speak = "Hello, I am Your Personal Assistant Mr. X"
            ass.assistant_speaks(speak)
            return
            
        elif "who made you" in text or "created you" in text:
            speak = "You. Akshay Parmar !"
            ass.assistant_speaks(speak)
            return
        elif 'time' in text:
            response=''
            now = datetime.datetime.now()
            meridian = ''
            if now.hour >= 12:
                meridian = 'PM'
                hour = now.hour - 12
            else:
                meridian = 'AM'
                hour = now.hour
            if now.minute < 10:
                minute = '0' + str(now.minute)
            else:
                minute = str(now.minute)
                response = response + ' ' + 'It is ' + str(hour) + ':' + minute + ' ' + meridian + '.'
            ass.assistant_speaks(response)
            return
        elif "calculate" in text:

            # write your wolframalpha app_id here
            app_id = "WOLFRAMALPHA_APP_ID"
            client = wolframalpha.Client(app_id)

            indx = text.lower().split().index('calculate')
            query = text.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            ass.assistant_speaks("The answer is " + answer)
            return

        elif 'open' in text:
            open_application(text)
            return
        elif 'who is' in text :
            wordList = text.split()
            p=''
            for i in range(0, len(wordList)):
                if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is':
                    p= wordList[i + 2] + ' ' + wordList[i + 3]
            try:
                wiki = wikipedia.summary(p, sentences=2)
                ass.assistant_speaks(wiki)
                return
            except:
                ass.assistant_speaks('could not search on wikipedia')
                return

        elif 'what is' in text:
            wordList = text.split()
            p = ''
            for i in range(0, len(wordList)):
                if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'what' and wordList[i + 1].lower() == 'is':
                    p = wordList[i + 2] + ' ' + wordList[i + 3]
            try:
                wiki = wikipedia.summary(p, sentences=2)
                ass.assistant_speaks(wiki)
                return
            except:
                ass.assistant_speaks('could not search on wikipedia')
                return
        elif 'play music' in text:
            ass.assistant_speaks('playing music')

            return
        elif ass.wishMe(text):
            return
        else:
            ass.assistant_speaks(r"i don't understand ! Please try again")
            return