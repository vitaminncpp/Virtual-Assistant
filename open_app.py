import assistant_speaks as ass
import os
import web_access as wa
import webbrowser
def open_application(input):
    try:
        if "chrome" in input:
            ass.assistant_speaks("Google Chrome")
            os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
            return

        elif "firefox" in input or "mozilla" in input:
            ass.assistant_speaks("Opening Mozilla Firefox")
            os.startfile(r'C:\Program Files\Firefox Developer Edition\firefox.exe')
            return

        elif "code" in input:
            ass.assistant_speaks("Opening Microsoft visual Code")
            os.startfile(r'C:\Users\ashut\AppData\Local\Programs\Microsoft VS Code\Code.exe')
            return

        elif 'youtube' in input:
            ass.assistant_speaks("Google Chrome")
            webbrowser.open("http://www.youtube.com/")
            return

        elif 'facebook' in input:
            ass.assistant_speaks('Opening Facebook')
            webbrowser.open("http://www.facebook.com/")
            return
        elif 'notepad plus plus' in input:
            os.startfile(r'C:\Program Files\Notepad++\notepad++.exe')
            return
            #npp
        elif 'notepad' in input:
            os.startfile(r'C:\Windows\System32\notepad.exe')
            return
            #notepad
        elif 'paint' in input or 'mspaint' in input:
            os.startfile(r'C:\Windows\System32\mspaint.exe')
            return
            #paint
        elif 'net beans' or 'netbeans' in input:
            os.startfile(r'C:\Program Files\NetBeans 8.2\bin\netbeans64.exe')
            return
        elif 'sublime' in input:
            os.startfile(r'C:\Program Files\Sublime Text 3\sublime_text.exe')
            return
            #sublime
        elif 'music' in input:
            os.startfile(r'F:\Audio\english songs\Waving Flag.mp3')
            return
        elif 'explorer' in input:
            os.startfile(r'C:\Windows\explorer.exe')
            return
        elif 'calculator' in input:
            os.startfile(r'C:\Windows\System32\calc.exe')
            return
        elif 'media player' in input:
            os.startfile(r'C:\Program Files (x86)\Windows Media Player\wmplayer.exe')
            return
        elif 'vlc' in input or 'v l c' in input:
            os.startfile(r'C:\Program Files (x86)\VideoLAN\VLC\vlc.exe')
            return
        elif 'music' in input:
            os.startfile(r'F:\Audio\song\new songs\Blank+Space+(Taylor+Swift).mp3')
            return
    except Exception as e:
        print(e)
        ass.assistant_speaks("Appliation not available")
        return