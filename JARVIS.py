
import pyautogui
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

from EDITH import cal_day, openApp


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss!")

    else:
        speak("Good Evening Boss!")

    speak("How may I help you ")

def schedule():
    day = cal_day().lower()
    speak("Boss today's schedule is ")
    week={
    "monday": "Boss, from 9:00 am to 10:10 am you have German class and then brakfast and at 12:00 pm to 12:30 pm you have exersize time and 4:00 pm to 6:00pm study science and mathematics, that is all boss",
    "tuesday": "Boss, from 9:00 am to 10:10 am you have German class and then brakfast and at 12:00 pm to 12:30 pm you have exersize time and 4:00 pm to 6:00pm study science and mathematics, that is all boss",
    "Wednesday": "Boss, from 9:00 am to 10:10 am you have German class. Then english class at 11:30 pm to 12:15 pm. Then you have exersize time from 12:30 pm to 1:00 pm and 4:00 pm to 6:00pm study science and mathematics, that is all boss",
    "thursday": "Boss, from 9:00 am to 10:10 am you have German class and then brakfast and at 12:00 pm to 12:30 pm you have exersize time and 4:00 pm to 6:00pm study science and mathematics, that is all boss",
    "friday": "Boss, from 9:00 am to 10:10 am you have German class. Then english class at 11:30 am to 12:15 pm. Then you have exersize time from 12:30 pm to 1:00 pm and 4:00 pm to 6:00pm study science and mathematics, that is all boss",
    "saturday": "Boss, from 9:00 am to 10:10 am you have German class and then brakfast and at 12:00 pm to 12:30 pm you have exersize time and 4:00 pm to 6:00pm study science and mathematics, that is all boss",
    "sunday": "Boss, today is holiday but just compleate your homework",
    }
    if day in week.keys():
        speak(week[day])

def openApp(command):
    if "calculator" in command:
        speak("opening calculator, boss")
        os.startfile('C:\\Windows\\System32\\calc.exe')
    elif "notepad" in command:
        speak("opening notepad, boss")
        os.startfile('C:\\Windows\\System32\\notepad.exe')


def closeApp(command):
    if "calculator" in command:
        speak("closing calculator, boss")
        os.system('taskkill /f /im calc.exe')
    elif "notepad" in command:
        speak("closing notepad, boss")
        os.system('taskkill /f /im notepad.exe')


def takeCommand():
    #It yakes microphone input from the user and returns string output

    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")   

    except Exception as e:
        # print(e)
        speak("Boss please repeat that for me")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
        
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searchin Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open gemini' in query:
            webbrowser.open("gemini.com")        
            
        elif 'open canva' in query:
            webbrowser.open("canva.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
 
        elif 'open music' in query:
            webbrowser.open("spotify.com")

        elif 'open meet' in query:
            webbrowser.open("meetgoogle.com")

        elif 'open chess' in query:
            webbrowser.open("chess.com")

 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Pranit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)   
        
            
        elif 'open google' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome_proxy.exe"              
            os.startfile(codePath)

        elif 'open remix' in query:
            codePath = "C:\\Program Files\\Audacity\\Audacity.exe"              
            os.startfile(codePath)    


        elif 'hi' in query:
            speak("What is my mission boss")
     
        elif 'how are you' in query:
            speak("Good, Boss. anything that I can do to help")
     
        elif 'who is your creator' in query:
            speak("My creator is Mr. Pranit Jain. Boss started creating me on eleventh november 2024 at 2pm")

        elif ("today timtable" in query) or ("schedule" in query):
            schedule()

        elif ("volume up" in query) or ("increase volume" in query):
            pyautogui.press("volumeup")
            speak("Volume increased")

        elif ("volume down" in query) or ("decrease volume" in query):
            pyautogui.press("volumedown")
            speak("Volume decreased")

        elif ("volume mute" in query) or ("Silence" in query):
            pyautogui.press("volumemute")
            speak("Volume muted")

        elif ("open calculator"in query) or ("open notepad" in query):
            openApp(query)

        elif ("close calculator"in query) or ("close notepad"):
            closeApp(query)             

        elif 'sleep' in query:
          speak("Okay, going to sleep now.")
          break
