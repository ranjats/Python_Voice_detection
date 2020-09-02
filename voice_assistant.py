import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("Golu 2.0 ")
    speak("I am your Personal Assistant")
    speak(assname)


def usrname():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")


def takeCommand():
    r = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:

        print("Listening...")
        # r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source, duration=0.4)
        audio = r.listen(source, phrase_time_limit=5)
        # audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
        return query

    except:
        speak("Could not understand your audio, PLease try again ! Thank you")
        return 0

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email passowrd')
    server.sendmail('your email id', to, content)
    server.close()


def open_note(query):
    speak("What should i write, sir")
    note = takeCommand()
    file = open('F:\\ranjat.txt', 'w')
    speak("Sir, Should i include date and time")
    snfm = takeCommand()
    if 'yes' in snfm or 'sure' in snfm:
        strTime = datetime.datetime.now().strftime("% H:% M:% S")
        file.write(strTime)
        file.write(" :- ")
        file.write(note)
    else:
        print('hiiiiii')
        file.write(note)

if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    usrname()

    while True:


         try:
            query = takeCommand().lower()
            if query == 0:
                continue
            if "exit" in str(query) or "bye" in str(query) or "sleep" in str(query):
                speak("Ok bye, ")
                break
            # All the commands said by user will be
            # stored here in 'query' and will be
            # converted to lower case for easily
            # recognition of command

            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                speak("Here you go to Youtube\n")
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                speak("Here you go to Google\n")
                webbrowser.open("google.com")
            elif 'open chrome' in query:
                speak("Google Chrome")
                os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

            elif "firefox" in input or "mozilla" in input:
                speak("Opening Mozilla Firefox")
                os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')

            elif "notepad" in input:
                speak("Opening notepad ")
                os.startfile('C:\\Users\\ranjat\\Downloads\\Compressed\\notepad++.exe')

            elif 'open stackoverflow' in query:
                speak("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("stackoverflow.com")

            elif 'play music' in query or "play song" in query:
                speak("Here you go with music")
                playsound('C:\\Users\\ranjat\\Music\\Chaskay - Bilal Saeed.mp3')
                # music_dir = "G:\\Song"
                # music_dir = "C:\\Users\\ranjat\\Music"
                # songs = os.listdir(music_dir)
                # print(songs)
                # random = os.startfile(os.path.join(music_dir, songs[1]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'speak' in query:
                speak("O you are talking about Angel girl")
                speak("she is beautiful and her eyes are awesome.  and lovely")
                speak("Shubh you want to listen more!!, keep smile always")

            elif 'how are you' in query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif 'fine' in query or "good" in query:
                speak("It's good to know that your fine")

            elif "change my name to" in query:
                query = query.replace("change my name to", "")
                assname = query

            elif "change name" in query:
                speak("What would you like to call me, Sir ")
                assname = takeCommand()
                speak("Thanks for naming me")

            elif "what's your name" in query or "What is your name" in query:
                speak("My friends call me")
                speak(assname)
                print("My friends call me", assname)

            elif 'exit' in query:
                speak("Thanks for giving me your time")
                exit()

            elif "who made you" in query or "who created you" in query:
                speak("I have been created by Ranjat.")

            elif 'joke' in query:
                speak(pyjokes.get_joke())

            elif "calculate" in query:

                app_id = "7WVKRG-P78X9EH62A"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)

            elif 'search' in query or 'play' in query:

                query = query.replace("search", "")
                query = query.replace("play", "")
                webbrowser.open(query)

            elif "who i am" in query:
                speak("If you talk then definately your human.")

            elif "why you came to world" in query:
                speak("Thanks to Ranjat. further It's a secret")

            elif 'power point presentation' in query:
                speak("opening Power Point presentation")
                power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
                os.startfile(power)

            elif 'is love' in query:
                speak("It is 7th sense that destroy all other senses")

            elif "who are you" in query:
                speak("I am your virtual assistant created by Ranjat")

            elif 'reason for you' in query:
                speak("I was created as a Minor project by Mister Ranjat ")

            elif 'change background' in query:
                ctypes.windll.user32.SystemParametersInfoW(20,
                                                           0,
                                                           "Location of wallpaper",
                                                           0)
                speak("Background changed succesfully")

            elif 'open bluestack' in query:
                appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
                os.startfile(appli)

            elif 'news' in query:

                try:
                    jsonObj = urlopen(
                        '''https://newsapi.org/v2/top-headlines?country=in&apiKey=f909c25829c4439496465b9eda45bce3''')
                    data = json.load(jsonObj)
                    i = 1
#https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8
                    speak('here are some top today news  of india by Golu version 2 point 0')
                    print('''=============== HELLO INDIA ============''' + '\n')

                    for item in data['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        speak(str(i) + '. ' + item['title'] + '\n')
                        i += 1
                        engine.runAndWait()
                        print("..............................................................")
                        time.sleep(2)
                except Exception as e:

                    print(str(e))


            elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

            elif 'empty recycle bin' in query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin Recycled")

            elif "don't listen" in query or "stop listening" in query:
                speak("for how much time you want to stop ranjat from listening commands")
                a = int(takeCommand())
                time.sleep(a)
                print(a)

            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.nl / maps / place/" + location + "")

            elif "camera" in query or "take a photo" in query:
                ec.capture(0, "Ranjat Camera ", "img.jpg")

            elif "restart" in query:
                subprocess.call(["shutdown", "/r"])

            elif "hibernate" in query or "sleep" in query:
                speak("Hibernating")
                subprocess.call("shutdown / h")

            elif "log off" in query or "sign out" in query:
                speak("Make sure all the application are closed before sign-out")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])

            elif "write a note" in query:
                open_note(query.lower())


            elif "show note" in query:
                speak("Showing Notes")
                file = open("F:\\ranjat.txt", "r")
                print(file.read())
                speak(file.read(6))

            elif "update assistant" in query:
                speak("After downloading file please replace this file with the downloaded one")
                url = '# url after uploading file'
                r = requests.get(url, stream=True)

                with open("Voice.py", "wb") as Pypdf:

                    total_length = int(r.headers.get('content-length'))

                    for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                           expected_size=(total_length / 1024) + 1):
                        if ch:
                            Pypdf.write(ch)

                            # NPPR9-FWDCX-D2C8J-H872K-2YT43
            elif "golu" in query:

                wishMe()
                speak("Golu 2 point o in your service Mister")
                speak(assname)
            elif "test" in query:
                speak('Ask what you want')
                question = takeCommand()
                app_id = '7WVKRG-P78X9EH62A'
                client = wolframalpha.Client(app_id)
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)

            elif "weather" in query:

                BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
                API_KEY = "b6e74869b4b15463c2f68a1eac96c8ea"

                speak(" for which city to want weather report ")
                print("City name : ")
                CITY = takeCommand()
                URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
                response = requests.get(URL)
                if response.status_code == 200:
                    data = response.json()
                    main = data['main']
                    temperature = main['temp']
                    humidity = main['humidity']
                    pressure = main['pressure']
                    report = data['weather']
                    weather_description = report[0]["description"]
                    summary = " welcome to  " + str(CITY) + "\n Now i will tell weather report for you "
                    speak(summary)
                    desc = " Temperature (in kelvin unit) = " + str(
                        temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                        pressure) + "\n humidity (in percentage) = " + str(
                        humidity) + "\n description = " + str(weather_description)
                    speak(desc)
                else:
                    # showing the error message
                    print("Error in the HTTP request")
            elif 'open opera' in query:
                codePath = r"C:\\Users\\GAURAV\\AppData\\Local\\Programs\\Opera\\launcher.exe"
                os.startfile(codePath)

            elif "wikipedia" in query:
                webbrowser.open("wikipedia.com")

            elif "Good Morning" in query:
                speak("A warm" + query)
                speak("How are you Mister")
                speak(assname)

                # most asked question from google Assistant
            elif "will you be my gf" in query or "will you be my bf" in query:
                speak("I'm not sure about, may be you should give me some time")

            elif "how are you" in query:
                speak("I'm fine, glad you me that")

            elif "i love you" in query:
                speak("It's hard to understand")

            elif "what is" in query or "who is" in query:

                # Use the same API key
                # that we have generated earlier
                client = wolframalpha.Client("API_ID")
                res = client.query(query)

                try:
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except StopIteration:
                    print("No results")

            elif 'email' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "ranjat.srivastava@gift.edu.in"
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif 'send a mail' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    speak("whome should i send")
                    to = input()
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")
            elif "send message " in query:
                # You need to create an account on Twilio to use this service
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                    body=takeCommand(),
                    from_='Sender No',
                    to='Receiver No'
                )

                print(message.sid)
                # elif "" in query:
                # Command go here
                # For adding more commands
        # except:
        #     speak("I don't understand, I can search the web for you, Do you want to continue?")
        #     ans = takeCommand()
        #     if 'yes' in str(ans) or 'yeah' in str(ans):
        #         speak("wait Ranjat for sometime , result will not display")

         except:
             print("Sorry could not recognize what you said")

