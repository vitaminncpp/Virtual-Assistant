from selenium import webdriver
import assistant_speaks as ass
import webbrowser as wbb

def find_web(text):
    driver = webdriver.Chrome()
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in text:

        ass.assistant_speaks("Opening in youtube")
        indx = text.lower().split().index('youtube')
        query = text.split()[indx + 1:]
        wbb.open("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return

    elif 'wikipedia' in text.lower():

        ass.assistant_speaks("Opening Wikipedia")
        indx = text.lower().split().index('wikipedia')
        query = text.split()[indx + 1:]
        wbb.open("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return

    else:

        if 'google' in text:

            indx = text.lower().split().index('google')
            query = text.split()[indx + 1:]
            wbb.open("https://www.google.com/search?q =" + '+'.join(query))

        elif 'search' in text:

            indx = text.lower().split().index('google')
            query = text.split()[indx + 1:]
            wbb.open("https://www.google.com/search?q =" + '+'.join(query))

        else:

            wbb.open("https://www.google.com/search?q =" + '+'.join(text.split()))

        return

def playOnYoutube(tag):
    pass