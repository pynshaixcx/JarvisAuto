import random
import pyttsx3
from pyttsx3 import engine

Hello = ('hello','hey','hi','hii','introduce yourself')

reply_Hello = ('Hello Sir , Hello I am Friday.',
            "Hey , What's Up ?",
            "Hey How Are You ?",
            "Hello Sir , Nice To Meet You Again .",
            "Of Course Sir , Hello .",
            "hello sir welcome back, how can I help you",
            "hey, what's up?",
            "I'm listening")

Bye = ('bye','sleep','go')

reply_Bye = ('Bye Sir.',
            "It's Okay .",
            "It Will Be Nice To Meet You Again.",
            "Bye.",
            "Thanks.",
            "Okay.")

How_Are_You = ('how are you','are you fine')

reply_how = ('I Am Fine.',
            "Excellent .",
            "Absolutely Fine.",
            "I'm Fine.",
            "Thanks For Asking.")

nice = ('nice','good','thanks')

reply_nice = ('Thanks .',
            "Ohh , It's Okay .",
            "Thanks To You.",
            "Your most welcome")

Functions = ('functions','abilities','what can you do','features','functions')

reply_Functions = ('I Can Perform Many Task Or Varieties Of Tasks , How Can I Help You ?',
            'I Can Call Your G.F .',
            'I Can Message Your Mom That You Are Not Studing..',
            'I Can Tell Your Class Teacher That You Had Attended All The Online Classes On Insta , Facebbook etc!',
            'Let Me Ask You First , How Can I Help You ?',
            'If You Want Me To Tell My Features , Call : Print Features !')


sorry_reply = ("Sorry , That's Beyond My Abilities .",
                "Sorry , I Can't Do That .",
                "Sorry , That's Above Me.")


def engine_speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[7].id)
    engine.setProperty('rate',135)
    engine.runAndWait()


def ChatterBot(Text):
    Text = str(Text)
    for word in Text:
        if word in Hello:
            reply = random.choice(reply_Hello)
            engine_speak(reply)

        elif word in Bye:
            reply = random.choice(reply_Bye)
            engine_speak(reply)

        elif word in How_Are_You:
            reply_ = random.choice(reply_how)
            engine_speak(reply_)

        elif word in Functions:
            reply___ = random.choice(reply_Functions)
            engine_speak(reply___)

