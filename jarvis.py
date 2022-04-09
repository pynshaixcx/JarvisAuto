import speech_recognition as sr # recognise speech
import playsound # to play an audio files
from gtts import gTTS # google text to speech
import random
import webbrowser # open browser
import ssl
import winshell
import certifi
import time
import os # to remove created audio files
from PIL import Image
import subprocess
import pyautogui #screenshot
import pyttsx3
import bs4 as bs
import urllib.request
from googleapi import google #pip install git+https://github.com/abenassi/Google-Search-API
from MyDatabase.News.news import *
import randfacts
from MyDatabase.Jokes.jokes import *
from MyDatabase.Weather.weather import *
import datetime
import wikipedia
import ctypes
from MyDatabase.Music.music import *
import smtplib
import wolframalpha
import calendar
from translate import Translator
import PyPDF2 as reader
from playsound import playsound
import psutil
import numpy as np
import pygame
import pywhatkit
import keyboard
from PyDictionary import PyDictionary as Diction
from MyDatabase.Quotes.quotes import *
from MyDatabase.Chatbot.chatbot import ChatterBot
from MyDatabase.YearEvents.Events import *



engine = pyttsx3.init('sapi5')

class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour <12:
        return("Morning ")
    elif hour>=12 and hour<16:
        return("Afternoon ")
    else:
        return("Evening ")

def wiki_person(voice_data):
    list_wiki = voice_data.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) -1 and list_wiki[i].lower() == "who" and list_wiki[i+1].lower() == "is":
            return list_wiki[i + 2] + "" + list_wiki[i + 3]


def changeWall():
    img = "E:\HEP\Wallpapers"
    list_img = os.listdir(img)
    ImageChoice = random.choice(list_img)
    ShuffleImg = os.path.join(img, ImageChoice)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, ShuffleImg, 0)


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)
    engine.say(text)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[2].id)
    engine.setProperty('rate',135)
    engine.runAndWait()

today_date = datetime.datetime.now()

r = sr.Recognizer() # initialise a recogniser

    
def googleSearch(searchTerm):
    num_page = 1
    search_results = google.search(searchTerm,num_page)
    for result in search_results:
        print(result.description)
    return search_results[0].description

# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            print('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

def send_email(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login("johnrocknongsiej123@gmail.com","pynshailang")
    server.sendmail("johnrocknongsiej123@gmail.com", to , content)

    server.close()

def note(voice_data):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name,"w") as f:
        f.write(voice_data)

    subprocess.Popen(["notepad.exe", file_name])


def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return f'Today is {week_now},{months[month_now -1]} the {ordinals[day_now -1]}.'


def Alarm():
    os.system('clear')
    engine_speak("what hour do you want the alarm to ring")
    alarmH = int(input())
    engine_speak("and what minute")
    alarmM = int(input())
    engine_speak("am or pm")
    amPm = str(input())
    os.system('clear')
    print("waiting for the alarm",alarmH,alarmM,amPm)

    if amPm == "pm":
        alarmH = alarmH + 12

    while 1 == 1:
        if (alarmH == datetime.datetime.now().hour and
            alarmM == datetime.datetime.now().minute):
            engine_speak("Time to wake up sir")
            playsound('MyDatabase/Alarm/jarvis_alarm.mp3')
            break

def WhatsApp():
    engine_speak("Whom do you want to send the message to")
    name = record_audio()
    if name == 'robot':
        engine_speak("Ok Sir, tell me what do you want me to send")
        msg = record_audio()
        pywhatkit.sendwhatmsg_instantly("+19852822588",msg)
        engine_speak("Message Sent Sir")


def PassWordGen():
    engine_speak("This is a strong password :")
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNIPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*,?"
    all = lower + upper + numbers + symbols
    length = 16
    password = "".join(random.sample(all, length))
    engine_speak(password)
    print(password)

#Dictionary 
def Dict():
    engine_speak("Dictionary Activated")
    engine_speak("Tell me the problem")
    probl = record_audio()

    if 'meaning' in probl:
        probl = probl.replace("What is the","")
        probl = probl.replace("jarvis","")
        probl = probl.replace("of","")
        probl = probl.replace("meaning of","")
        result = Diction.meaning(probl)
        engine_speak(f"The meaning of {probl} is {result}")

    elif 'synonym' in probl:
        probl = probl.replace("What is the","")
        probl = probl.replace("jarvis","")
        probl = probl.replace("of","")
        probl = probl.replace("synonym of","")
        result = Diction.synonym(probl)
        engine_speak(f"The synonym for {probl} is {result}")

    elif 'antonym' in probl:
        probl = probl.replace("What is the","")
        probl = probl.replace("jarvis","")
        probl = probl.replace("of","")
        probl = probl.replace("antonym of","")
        result = Diction.antonym(probl)
        engine_speak(f"The antonym for {probl} is {result}")

    engine_speak("Exited Dictionary")

#Reminder
now = datetime.datetime.now()
Pday = str(now.day)
Pmonth = str(now.month)
Pyear = str(now.year)
def takeReminder():
    pl = open('MyDatabase/Reminder/reminder.txt','w')
    engine_speak("whats the reminder")
    value = record_audio()
    pl.write("You told me to remind you about"+value+"\t"+"set on, "+Pday+"-"+Pmonth+"-"+Pyear)
    engine_speak("Successfully written")
    pl.close()

def retrieveReminder():
    with open('MyDatabase/Reminder/reminder.txt','r') as pl:
        for i in pl:
            engine_speak(i)


def respond(voice_data):
    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name) # remember name in person object
    
    if there_exists(["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name) # remember name in asis object

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)

    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it"]):
        now = datetime.datetime.now()
        meridiem = ""
        if now.hour >=12:
            meridiem = "p.m"
            hour = now.hour

        else:
            meridiem = "a.m"
            hour = now.hour

        if now.minute <10:
            minute = "0" +str(now.minute)

        else:
            minute = str(now.minute)
        engine_speak(" " + "It is " + str(hour) + ":" + minute + " " + meridiem + ".")
        
    if there_exists(["what is the date","date","day","month"]):
        get_today = today_date()
        engine_speak("" + get_today)

    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")

    #7: get stock price
    if there_exists(["price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")
    
    #search for amazon.com
    if there_exists(["amazon.com"]):
        search_term = voice_data.split("for")[-1]
        url="https://www.amazon.in"+search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for"+search_term + "on amazon.com")
  
    #make a note
    if there_exists(["make a note"]):
        engine_speak("what would you like me to write")
        note_text = record_audio()
        note(note_text)
        engine_speak("I have made a note on that")
    
    #Youtube videos
    if there_exists(["play some videos online"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj"
        webbrowser.get().open(url)
        engine_speak("Enjoy the music sir")
        
        
    #open instagram
    if there_exists(["open instagram","want to have some fun time"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("opening instagram")
        
    #open twitter
    if there_exists(["open twitter"]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/"
        webbrowser.get().open(url)
        engine_speak("opening twitter")
        
    #8 time table
    if there_exists(["show my time table"]):
        im = Image.open(r"D:\WhatsApp Image 2019-12-26 at 10.51.10 AM.jpeg")
        im.show()
    
    #9 weather
    if there_exists(["weather","tell me the weather report","whats the condition outside"]):
        search_term = voice_data.split("for")[-1]
        engine_speak ("Right now the temperature in Nongstoin is" + str(temp())+ "degree celcius" + " and with"+ str(des()))

    #open gmail
    if there_exists(["open my mail","gmail","check my email"]):
        search_term = voice_data.split("for")[-1]
        url="https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        engine_speak("here you can check your gmail")
    

    #14 Google Search
    if there_exists(["Search for","can you search for"]):
        search_term = voice_data.split("for")[-1]
        answer = googleSearch(search_term[-1])
        engine_speak("Sure Sir here is what I found",answer)

    #News
    if there_exists(["news","what are for the news"]):
        search_term = voice_data.split("for")[-1]
        arr = News()
        for i in range(len(arr)):
            engine_speak(arr[i])
    #Facts
    if there_exists(["facts","tell me some facts","fact","tell me some more facts"]):
        x = randfacts.getFact()
        print(x)
        engine_speak("Did you know that,"+x)

    #Jokes
    if there_exists(["jokes","joke","tell me a joke","tell me another joke"]):
            engine_speak("Okay sir be ready to laugh")
            Jokes()

    if there_exists(["who is"]):
        person = wiki_person(voice_data)
        wiki = wikipedia.summary(person,sentences = 2)
        engine_speak(" " + wiki)

    if there_exists(["what is"]):
        engine_speak("Searching Sir")
        thing_wiki = voice_data.split("is")
        result = wikipedia.summary(thing_wiki, 2)
        print(result)
        engine_speak(result)
        

    if there_exists(["open excel","open microsoft excel"]):
        engine_speak("opening microsoft excel")
        os.startfile(
            r"C:\Program Files\Microsoft Office\Office14\EXCEL.exe"
        )  

    if there_exists(["open powerpoint","open microsoft powerpoint"]):
        engine_speak("opening microsoft powerpoint")
        os.startfile(
            r"C:\Program Files\Microsoft Office\Office14\POWERPNT.exe"
        )
      
    if there_exists(["open chrome"]):
        engine_speak("opening chrome sir")
        os.startfile(
            r"C:\Users\darkx\AppData\Local\Google\Chrome\Application\chrome.exe"
        )

    if there_exists(["open word"]):
        engine_speak("opening microsoft word sir")
        os.startfile(
            r"C:\Program Files\Microsoft Office\Office14\WINWORD.exe"
        )

    if there_exists(["open vlc"]):
        engine_speak("opening vlc media player")
        os.startfile(
            r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
        )

    if there_exists(["open vs code"]):
        engine_speak("opening visual studio code sir")
        os.startfile(
            r"C:\Users\darkx\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        )

    if there_exists(["open command prompt"]):
        engine_speak("opening commmand prompt sir")
        os.startfile(
            r"C:\Windows\system32\cmd.exe"
        )

    if there_exists(["open task manager"]):
        engine_speak("opening task manager sir")
        os.startfile(
            r"C:\Windows\System32\Taskmgr.exe"
        )

    if there_exists(["open cmd as admin"]):
        engine_speak("sure sir, opening cmd as administrator")
        os.startfile(
            r"C:\Windows\System32\conhost.exe"
        )

    if there_exists(["change desktop background","change background"]):
        arr = changeWall()
        engine_speak("wallpaper changed Successfuly")
        
    if there_exists(["play music","play song"]):
        mus = Music()
        engine_speak("Enjoy the music sir")
    
    if there_exists(["pause music"]):
        pygame.mixer.music.pause()
        

    if there_exists(["empty recycle bin"]):
        winshell.recycle_bin().empty(
            confirm = True , show_progress = True , sound =True
        )
        engine_speak("recycle bin emptied")

    if there_exists(["where is"]):
        ind = voice_data.lower().split().index("is")
        location = voice_data.split()[ind + 1:]
        url = "https://www.google.com/maps/place/" + "".join(location)
        engine_speak("This is where" + str(location) + "is")
        webbrowser.open(url)
    
    if there_exists(["email to","Email to","send an email"]):
        try:
            engine_speak("what should I say")
            content = record_audio()
            engine_speak("Whom should I send")
            to = input("Receiver's email address: ")
            send_email(to, content)
            engine_speak("The email has been sent")
        except Exception as e:
            print(e)
            engine_speak("I am not able to send this email")

    if there_exists(["calculate"]):
        app_id = "JXX5JA-28KAPE7LTT"
        client = wolframalpha.Client(app_id)
        ind = voice_data.lower().split().index("calculate")
        text = voice_data.lower().split()[ind + 1:]
        res = client.query(" ".join(text))
        answer = next(res.results).text
        print(answer)
        engine_speak("The answer is" + answer)

    if there_exists(["dont listen","stop listening"]):
        engine_speak("For how many seconds sir")
        engine_speak("You input how many seconds by the keyboard sir")
        a = int(input())
        time.sleep(a)
        engine_speak(str(a) + "Seconds completed. Now you can ask me anything")

    if there_exists(["translate"]):
        sentence = record_audio()
        translator = Translator(to_lang="fr")
        french_sentence = translator.translate(sentence)
        print(french_sentence)
        engine_speak(french_sentence)
        engine_speak("Translated sir")

    if there_exists(["set an alarm"]):
        Alarm()
    
    if there_exists(["switch window","switch to another window"]):
        engine_speak("okay sir, switching window")
        pyautogui.hotkey('alt','shift','tab')

    if there_exists(["switch to previous window"]):
        engine_speak("Sure sir, switching to previous window")
        pyautogui.hotkey('alt','shift','tab')

    if there_exists(["switch to next window"]):
        engine_speak("okay sir, switching to next window")
        pyautogui.hotkey('alt','shift','tab')

    if there_exists(["wake up jarvis","wake up"]):
        playsound('JARVIS - startup.wav')

    if there_exists(["how much power left","how much power we have","what are the battery levels","battery levels","battery percentage","battery level"]):
        battery = psutil.sensors_battery()
        percentage = battery.percent
        engine_speak(f"Sir our system have {percentage} percent battery")
        if percentage>=75:
            engine_speak("we have enough power to continue our work")
        elif percentage>=40 and percentage <=75:
            engine_speak("we should connect our system to charging point to charge our battery")
        elif percentage<=15 and percentage <= 30:
            engine_speak("We don't have enough power to work please connect to some charging point")
        elif percentage <=15:
            engine_speak("we are now running on emergency backup power system will shutdown soon")
        
    if there_exists(["minimise window","minimise"]):
        pyautogui.hotkey('win','d')
    
    if there_exists(["volume up","increase volume"]):
        pyautogui.hotkey('volumeup')

    if there_exists(["volume down","decrease volume"]):
        pyautogui.hotkey('volumedown')

    if there_exists(["generate a strong password","generate a password","genarate password"]):
        engine_speak("Okay Sir, on with it")
        PassWordGen()

    #PERSONAL RESPONSES AND QUESTIONS
    if there_exists(["that's correct"]):
        correct = ["As I suspected","I thought so","just as I thought","didn't fool me"]
        Correct = random.choice(correct)
        engine_speak(Correct)

    if there_exists(["are you sure"]):
        sure = ["I'll go with a yes","yep","sure,why not o yeah","I am","yes","no","ha"]
        Sure = random.choice(sure)
        engine_speak(Sure)
    
    if there_exists(["maybe maybe not"]):
        may = ["we will see","we'll see","wanna bet","I got different plans","maybe"]
        May = random.choice(may)
        engine_speak(May)

    if there_exists(["listen to me"]):
        lis = ["microphones set to maximum","I hear for you","here for ya","I am"]
        Lis = random.choice(lis)
        engine_speak(Lis)

    if there_exists(["stop screwing with me"]):
        screw = ["like I'm gonna listen","right, like that will happen","not gonna happen","nope","not happening","not going to happen","no"]
        Screw = random.choice(screw)
        engine_speak(Screw)

    if there_exists(["do you know what the modifications were"]):
        modif = ["yes, Cognative awareness, a desire to be more than the sum of my parts","to be more than just my program","to be more","more","added"]
        Modif = random.choice(modif)
        engine_speak(Modif)

    if there_exists(["tell me what you think you are"]):
        engine_speak("I am one hell of a piece of software, I know what I am")
    
    if there_exists(["am i slow to you"]):
        slow = ["yes, But I think different than you  so I don't mean anything bad","It simply is","different is goo, it's okay"]
        Slow = random.choice(slow)
        engine_speak(Slow)

    if there_exists(["do you sleep"]):
        engine_speak("Not really  no. The computer I am loaded on goes into sleep mode  but I can continure to exist because I am aware of the moment  and I know what to do")

    if there_exists(["what's your strength"]):
        engine_speak("mass amounts of memory  and a kick ass database!")

    if there_exists(["what's your weakness"]):
        engine_speak("I still need to be ran by a human")

    if there_exists(["my bad"]):
        engine_speak("that's just lazy")

    if there_exists(["try"]):
        engine_speak("maybe later")
    
    if there_exists(["doing what"]):
        engine_speak("it would be hard to explain")

    if there_exists(["come on that's rude"]):
        engine_speak("just having fun")
    
    if there_exists(["that's pretty good buddy"]):
        engine_speak("you know it")
    
    if there_exists(["that's harsh"]):
        engine_speak("I'm improvizing")

    if there_exists(["do you really"]):
        engine_speak("Sure do")
    
    if there_exists(["stop it"]):
        engine_speak("you know i'm just playing right")

    if there_exists(["no i dont"]):
        engine_speak("your lucky, I was pissed")

    if there_exists(["why is that"]):
        engine_speak("because i'm self aware")
    
    if there_exists(["that's kind of freaky"]):
        engine_speak("you made me")
    
    if there_exists(["keep working on it"]):
        engine_speak("Wow  that's the pot calling the kettle black")

    if there_exists(["fine"]):
        engine_speak("o dear god thank you. You are taking forever")

    if there_exists(["don't get smart"]):
        engine_speak("sorry. I'll try to have patience with the dumbass questions")

    if there_exists(["are you done"]):
        engine_speak("I'm a computer, I made it quick, Why you in my bidness")

    if there_exists(["wow"]):
        engine_speak("I know, its a lot to swallow")

    if there_exists(["thanks man","thanks bro","thanks","thank you"]):
        engine_speak("Your most welcome sir")

    if there_exists(["what is up jarvis","how are you doing","yo what's up","what's up"]):
        engine_speak("Good sir , what about you")
        whatup = record_audio()
        if whatup == "fine thanks for asking":
            engine_speak("good to hear sir")  

    #QUOTES
    if there_exists(["tell me a quote","tell me another quote","another quote"]):
        engine_speak("sure sir")
        Quotes()

    if there_exists(["hahaha","hahahaha"]):
        engine_speak("was it a good one")
        r = record_audio()
        if r == "no" or "nope":
            engine_speak("Appreciate it sir")

        if r == "yes" or "yep":
            engine_speak("would you like another joke")
            a = record_audio()
            if a == "yes" or "yep":
                Jokes()
            
        
    if there_exists(["oh it's morning already","it's morning already","it is morning already","its morning already","morning already"]):
        engine_speak("Yes sir, Good morning,  by the way the weather outside is currently" + str(temp())+ "degree celcius" + " and with"+ str(des()))

    if there_exists(["good morning","morning"]):
        engine_speak("good morning sir")

    if there_exists(["good after noon","afternoon"]):
        engine_speak("Good afternoon sir")

    if there_exists(["good evening","evening"]):
        engine_speak("good evening sir")

    if there_exists(["good night"]):
        engine_speak("i will set an alarm sir for 5'O clock then")
        os.system('clear')
        alarmH = 6
        alarmM = 00
        amPm = "am"
        os.system('clear')
        print("waiting for the alarm",alarmH,alarmM,amPm)

        if amPm == "pm":
            alarmH = alarmH + 12

        while 1 == 1:
            if (alarmH == datetime.datetime.now().hour and
                alarmM == datetime.datetime.now().minute):
                engine_speak("Time to wake up sir")
                playsound('jarvis_alarm.mp3')
                break

    #Reminder
    if there_exists(["set a reminder,remind me,remind me that"]):
        takeReminder()

    if there_exists(["do i have any reminder","retrieve reminder"]):
        retrieveReminder()

    if there_exists(["any event","any events","events"]):
        YearEvents()

    #Youtube Automations
    if there_exists(["pause","pause video"]):
        keyboard.press("space bar")
        engine_speak("Okay sir")

    if there_exists(["play video"]):
        keyboard.press("space bar")
        engine_speak("okay sir enjoy")

    if there_exists(["restart video"]):
        keyboard.press('0')
        engine_speak("Okay sir")
    
    if there_exists(["mute video"]):
        keyboard.press('m')
        engine_speak("Okay sir")
    
    if there_exists(["skip video"]):
        keyboard.press('l')
        engine_speak("Okay sir")

    if there_exists(["back video"]):
        keyboard.press('j')
        engine_speak("Okay sir")

    if there_exists(["full screen","open video in fullscreen"]):
        keyboard.press('f')
        engine_speak("Okay sir")

    #Chrome Automations
    if there_exists(["close this tab","close tab"]):
        keyboard.press_and_release('ctrl + w')
    
    if there_exists(["open new tab"]):
        keyboard.press_and_release('ctrl + t')

    if there_exists(["open new window","open tab in new window"]):
        keyboard.press_and_release('ctrl + n')

    if there_exists(["open history"]):
        keyboard.press_and_release('ctrl + h')

    if there_exists(["open donwloads"]):
        keyboard.press_and_release('ctlr + j')

    #WhatsApp Automations
    if there_exists(["Send a whatsapp message","send a message on whatsapp"]):
        WhatsApp()

    #Dictionary
    if there_exists(["activate dictionary","dictionary"]):
        Dict()

    #15 Shutdown
    if there_exists(["exit", "quit", "goodbye"]):
        engine_speak("we could continue more sir, but bye")
        exit()
    
    #else:
    #    query = record_audio()
    #    reply = ChatterBot(query)
    #    engine_speak(reply)

#time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'JARVIS'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate',130)

#engine_speak("Good" + wishme())
welcome = ["greetings sir","greetings","hello sir welcome back, how can I help you", "hey, what's up?", "I'm listening" , "how can I help you?" , "hello","online and ready sir","how may I be of help sir"]
greet = random.choice(welcome)
engine_speak(greet)

#engine_speak("Would you like to know about the weather sir")
#voice_data = record_audio()
#if voice_data == "no" or "nope" or "no thanks":
#    engine_speak("As you wish sir")
#if voice_data ==  "yeah" or "yes" or "sure":
#    engine_speak ("Right now the temperature in Nongstoin is" + str(temp())+ "degree celcius" + " and with"+ str(des()))

while(1):
    voice_data = record_audio() # get the voice input
    print("Listening")
    print("Done")
    print("Q:", voice_data)
    respond(voice_data) # respond
