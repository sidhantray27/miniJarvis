import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning  sir ")
    elif hour>=12 and hour<18:
        speak("good afternoon sir ")
    else:
        speak("good evening sir ")

    speak(" i am jarvis. please tell me how may i help you ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING........")
        r.energy_threshold = 1000
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("RECOGNIZING....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")
        speak(query)
        
    except Exception :
        print("say that again please....")
        return "none"
    return query

if __name__ == "__main__":
    c=1
    wishme()
    chrome="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    while c==1 :
        query=takeCommand().lower()
        print(query)

        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia..")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak('opening youtube for you sir')
            webbrowser.get(chrome).open("youtube.com")
        
        elif 'open google' in query:
            speak('opening google for you sir')
            webbrowser.get(chrome).open("google.com")
        
        elif 'open facebook' in query:
            speak('opening facebook for you sir')
            webbrowser.get(chrome).open("facebook.com")

        elif 'open hackerrank' in query:
            speak('opening hackerrank for you sir')
            webbrowser.get(chrome).open("hackerrank.com")

        elif 'open stackoverflow' in query:
            speak('opening stackoverflow for you sir')
            webbrowser.get(chrome).open("stackoverflow.com")

        elif 'play music' in query:
            music_dir='E:\\Music\\sidhu'  # music directory path in respective system
            songs=os.listdir(music_dir)
            r=random.randrange(0,len(songs)-1,1)
            speak('playing music for you sir')
            print(songs[r])
            os.startfile(os.path.join(music_dir,songs[r]))
    
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"sir , the time is {strTime}")
            speak(f"sir , the time is {strTime}")

        elif 'open code' in query:
            codePath="C:\\Program Files\\Microsoft VS Code\\Code.exe"   # vs code path in respective system
            speak('opening vs code for you sir')
            os.startfile(codePath)

        elif 'quit' in query:
            speak("quiting sir ")
            s="thank you  , have a nice day sir........ bye"
            print(s)
            speak(s)
            c=0       