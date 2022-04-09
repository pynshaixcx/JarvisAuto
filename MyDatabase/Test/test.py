import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name


def engine_speak(text):
    text = str(text)
    engine.say(text)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[7].id)
    engine.setProperty('rate',115)
    engine.runAndWait()


r = sr.Recognizer()
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

#Reminder
def Reminder():
    engine_speak("what's the reminder")
    rememberMsg = record_audio()
    remember = open('data.txt','w')
    remember.write(rememberMsg)
    engine_speak("Reminder set")
    remember.close()


person_obj = person()
asis_obj = asis()
asis_obj.name = 'JARVIS'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[7].id)
engine.setProperty('rate',115)
welcome = ["greetings sir","greetings","hello sir welcome back, how can I help you", "hey, what's up?", "I'm listening" , "how can I help you?" , "hello","online and ready sir","how may I be of help sir"]
greet = random.choice(welcome)
engine_speak(greet)

name = input("Set a reminder: ")
if name == 'y':
    Reminder()