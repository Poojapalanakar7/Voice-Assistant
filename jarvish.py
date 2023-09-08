import sys
import pyttsx3  # Import library for speak function
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
from requests import get  # pip install requests

import cv2
import requests
import instaloader  # pip install instaloader
import PyPDF2
import pyjokes  # pip install pyjokes
import pyautogui  # pip install pyautogui
import operator  # for calculation using voice
import smtplib
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jaevishUi import Ui_MainWindow


engine = pyttsx3.init('sapi5')  # sapie5 provides api from microsoft for Voice
voices = engine.getProperty('voices')

# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

# text to speech


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():

    hour = int(datetime.datetime.now().hour)

    tt = datetime.datetime.now().strftime("%H:%M:%S")
    if hour >= 0 and hour < 12:
        speak(f"Good Moring Team, it's {tt}")

    elif hour >= 12 and hour < 18:
        speak(f"Good Evening Team, it's {tt}")

    else:
        speak(f"Good Evening Team, it's {tt}")

    speak("Hellow Team i am jarvish 2 point O")
    speak("How may i help you")

# for news updates


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=83263a48521a48a797182dbc3926e513'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")


def pdf_reader():
    book = open('py3.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)  # pip install PyPDF2
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages} ")
    speak("sir please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def takeCommand(self):
        # It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            # Using google for voice recognition.
            self.query = r.recognize_google(audio, language='en-in')
            # User self.query will be printed.
            print(f"User said: {self.query}\n")

        except Exception as e:
            # print(e)
            # Say that again will be printed in case of improper voice
            print("Say that again please...")
            return "None"  # None string will be returned
        return self.query

    def run(self):
        self.taskExecution()
        speak("please say wakeup to continue")
        while True:
            self.query = self.takeCommand()
            if "wake up" in self.query or "are you there" in self.query or "hello" in self.query:
                self.taskExecution()

    # main function

    def taskExecution(self):
        wishme()
        while True:
            # if 1:
            # Converting user self.query into lower case
            self.query = self.takeCommand().lower()

            # Logic for executing tasks based on self.query
            # if wikipedia found in the self.query then this block will be executed

            # if 'wikipedia' in self.query or "who is" in self.query:
            #     speak('Searching Wikipedia...')
            #     self.query = self.query.replace("wikipedia", "")
            #     results = wikipedia.summary(self.query, sentences=2)
            #     speak("According to Wikipedia")
            #     print(results)
            #     speak(results)

            if "wikipedia" in self.query:
                speak("searching wikipedia....")
                Query = Query.replace("wikipedia", "")
                results = wikipedia.summary(Query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                print(results)

            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")

            elif 'how are you' in self.query:
                speak("i am fine team, what about you")

            elif 'open google' in self.query:
                webbrowser.open("google.com")

            elif 'open gfg' in self.query:
                webbrowser.open("https://www.geeksforgeeks.org/")

            elif 'play music' in self.query:
                # music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                music_dir = 'D:\\Mini_proj.voiceASS\\song'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in self.query:

                codePath = "C:\\Users\\91822\\Desktop\\Visual Studio Code.lnk"
                os.startfile(codePath)

            # elif 'open screenshot' in self.query:

            #     screenPath = "C:\Users\91822\Pictures\Saved Pictures"
            #     os.startfile(screenPath)

            elif 'internet speed' in self.query:
                webbrowser.open("https://fast.com/")

            elif "open notepad" in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open pdf reader" in self.query:
                apath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Adobe Acrobat.lnk"
                os.startfile(apath)

            elif "open cmd" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif "you can sleep" in self.query or "sleep now" in self.query:
                speak("okay sir, i am going to sleep you can call me anytime.")
                # sys.exit()
                # gifThread.exit()
                break

            # to close any application
            elif "close notepad" in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            # to set an alarm
            elif "set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn == 22:
                    music_dir = 'E:\\music'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

            # to find a joke
            elif "tell me a joke" in self.query or "joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "hello" in self.query or "hey" in self.query:
                speak("hello sir, may i help you with something.")

            elif "how are you" in self.query:
                speak("i am fine sir, what about you.")

            elif "thank you" in self.query or "thanks" in self.query:
                speak("it's my pleasure sir.")

            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me news" in self.query:
                speak("please wait sir, feteching the latest news")
                news()
# ---------------------
            elif "do some calculations" in self.query or "can you calculate" in self.query or "calculate" in self.query or "calculation" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Say what you want to calculate")
                    print("listening.....")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)
                # speak(my_string)

                def get_operator_fn(op):
                    return {
                        '+': operator.add,
                        '-': operator.sub,
                        'x': operator.mul,
                        'divided': operator.__truediv__,
                        'Mod': operator.mod,
                        'mod': operator.mod,
                        '^': operator.xor,
                    }[op]

                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                print(eval_binary_expr(*(my_string.split())))
                # speak(eval_binary_expr(*(my_string.split())))
                speak("I am calculating in your terminal ,please check their ")

            elif "where i am" in self.query or "where we are" in self.query:
                speak("wait sir, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    # print(geo_data)
                    city = geo_data['city']
                    # state = geo_data['state']
                    country = geo_data['country']
                    speak(
                        f"sir i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak(
                        "sorry sir, Due to network issue i am not able to find where we are.")
                    pass

            # -------------------To check a instagram profile----
            elif "instagram profile" in self.query or "profile on instagram" in self.query:
                speak("sir please enter the user name correctly.")
                name = input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"Sir here is the profile of the user {name}")
                time.sleep(5)
                speak("sir would you like to download profile picture of this account.")
                condition = self.takeCommand()
                if "yes" in condition:
                    mod = instaloader.Instaloader()  # pip install instadownloader
                    mod.download_profile(name, profile_pic_only=True)
                    speak(
                        "i am done sir, profile picture is saved in our main folder. now i am ready for next command")
                else:
                    pass

            # -------------------  To take screenshot -------------
            elif "take screenshot" in self.query or "take a screenshot" in self.query:
                speak("sir, please tell me the name for this screenshot file")
                name = self.takeCommand()
                speak(
                    "please sir hold the screen for few seconds, i am taking sreenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak(
                    "i am done sir, the screenshot is saved in our main folder. now i am ready for next command")

            # speak("sir, do you have any other work")

            # -------------------  To Read PDF file -------------
            elif "read pdf" in self.query:
                pdf_reader()

            # --------------------- To Hide files and folder ---------------
            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak(
                    "sir please tell me you want to hide this folder or make it visible for everyone")
                condition = self.takeCommand()
                if "hide" in condition:
                    os.system("attrib +h /s /d")  # os module
                    speak("sir, all the files in this folder are now hidden.")

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak(
                        "sir, all the files in this folder are now visible to everyone. i wish you are taking this decision in your own peace.")

                elif "leave it" in condition or "leave for now" in condition:
                    speak("Ok sir")

            elif "temperature" in self.query:
                search = "weather in TUMKURU bangluru"
                url = f"https://www.google.com/search?q={search}"
                req = requests.get(url)
                save = BeautifulSoup(req.text, "html.parser")
                tempp = save.find("div", class_="BNeawe").text
                speak(f"current {search} is {tempp}")


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:/Mini_proj.voiceASS/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:/Mini_proj.voiceASS/T8bahf.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()

        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)

        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvish = Main()
jarvish.show()
sys.exit(app.exec_())
