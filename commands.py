import webbrowser
import pyttsx3
from urllib.request import urlopen
from bs4 import BeautifulSoup

googleFlag =0

def addGoogle():
    if googleFlag is 0:
        chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('google-chrome', None, webbrowser.BackgroundBrowser(chrome_path), 1)

def openApplication(name):
    return 1

#open webpage
def searchWeb(webName):
    addGoogle()
    new =2 # new card
    webbrowser.get(using='google-chrome').open('www.'+webName+'.com',new=new)

def playSong(songName):
    try:
        page = urlopen('https://www.youtube.com/results?search_query='+songName)

    except:
        print("Error ocurred")

    try:
        soup = BeautifulSoup(page, "html.parser")
    except:
        print("Problem with soup")

    try:
        songs =soup.find("a", class_="yt-uix-tile-link")
    except:
        print("No video found")

    addGoogle()
    new =2 # new card
    webbrowser.get(using='google-chrome').open("https://www.youtube.com/"+songs.get('href'),new=new)



def analyzeString(command):
    #Devide string into list of words
    list_of_words = command.split()
    for index , word in enumerate(list_of_words):
        if word == 'open':
            application = index
            _application = list_of_words[application + 1]
            openApplication(_application)
            break

        if word == 'search':
            application = index
            _application = list_of_words[application + 1]
            searchWeb(_application)
            print('search')
            break

        if word == 'play':
            songName =''
            song = index
            for i in list_of_words[song+1:]:
                songName = songName+ '+'+ i

            playSong(songName)

