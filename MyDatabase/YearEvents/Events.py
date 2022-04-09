import datetime
import pyttsx3

def engine_speak(text):
    engine = pyttsx3.init('sapi5')
    text = str(text)
    engine.say(text)
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[7].id)
    engine.setProperty('rate',135)
    engine.runAndWait()
    
def YearEvents():
    now = datetime.datetime.now()
    Nmonth = now.month
    Nday = now.day

    #Birthday
    Pdate = 7
    Pmonth = 6

    if Pdate == Nday and Pmonth == Nmonth:
        engine_speak("Good Morning Sir, Today will be a great day for you, as It is your Birthday, A Very happy and delighted birthday to you. Yayyy,  Have a Great day.")

    #Christmas
    CmasDay = 25
    CmasMonth = 12

    if CmasDay == Nday and CmasMonth == Nmonth:
        engine_speak("Merry Christmas Sir, Hope You will Have a great Christmas day")