import speech_recognition as sr
import pyttsx3 as tts
import os, sys ,time

#Wgrać jakiś polski sensowny głos i poprawić ścieżkę


#Obiekty
r=sr.Recognizer()
engine =tts.init()
engine.setProperty('voice',engine.getProperty('voices')[0].id)


#wczytać chrome
chrome ='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

def speak(text):
    engine.say(text)
    engine.runAndWait()

def getText():
    try:
        with sr.Microphone() as source:
            print("Nasłuchuję...", end='\r')
            audio = r.listen(source)
            text = r.recognize_google(audio,language="pl-PL")
        if text =="":
            return None
        else:
            return text

    except:
        return None

def czy_zawiera(string, slowa):
	return [element for element in slowa if element in string.lower()]


WYKRYJ=['bot','robot','robocie']
DOWIDZENIA=['do widzenia','papa','żegnaj','dowidzenia']
SZUKAJ =['wyszukaj','szukaj','znajdź','google','googluj','pokaż']
print("Aby wyjść powiedz \"Do widzenia\"")
while True:
    time.sleep(0.5)
    cur =getText()
    print(cur)
    print(""*50, end="\r")
    if cur !=None:
        if len(czy_zawiera(cur, WYKRYJ)):
            if len(czy_zawiera(cur,DOWIDZENIA)):
                speak("Żegnaj.")
                break
            elif len(czy_zawiera(cur,SZUKAJ)):
                linczek=cur.lower().split('' + czy_zawiera(cur,SZUKAJ)[0] + '')[1]
                speak("Oto co udało mi się znaleźć.")
                url="https://www.google.com/search?q=" + linczek.replace("","+").replace("?","%3F")
                os.system(chrome+ "" + url)