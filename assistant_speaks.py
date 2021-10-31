import subprocess
import pyttsx3
import get_audio as ga
import random

# eng=pyttsx3.init()
# voices=eng.getProperty()
#
# print(voices[0].id)
#
# eng.setProperty('voice',voices[0].id)
#
# def speak(audio):
#     eng.say(audio)
#     eng.runAndWait()




def assistant_speaks(output):
    subprocess.call('espeak -g 3"'+output+'"',shell=True)

    # # num to rename every audio file
    # # with different name to remove ambiguity
    # num += 1
    # print("Seja : ", output)
    #
    # toSpeak = gTTS(text=output, lang='en', slow=False)
    # # saving the audio file given by google text to speech
    # file = str(num) + ".mp3"
    # toSpeak.save(file)
    #
    # # playsound package is used to play the same file.
    # playsound.playsound(file, True)
    # os.remove(file)

greet=['hi','hello','hey','how are you','who are you','what\'s up','good morning','good evening','good night']

glad=['glad','good','great','happy']
hereThat=['to here that','to here it']
def wishMe(text):
    if 'hi' in text or 'hello' in text or 'hey' in text :
        assistant_speaks('hi there ! how are you ?')
    if greet[4] in text:
        assistant_speaks('i am you perssonal assistant, Mr.X !')
    if greet[3] in text:
        assistant_speaks('i am fine ! what about you ?')
        res= ga.get_audio().lower()
        if 'bored' in res or 'not good' in res or 'bad' in res or 'not ok' in res:
            assistant_speaks('oh sorry !')
        elif 'fine' in res or 'good' in res:
            happ=random.choice(glad)+' '+random.choice(hereThat)
            assistant_speaks(happ)

def isWishWord(text):
    for i in greet:
        if i in text:
            wishMe(text)
            return True