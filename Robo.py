import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser as web
import os
from wikipedia import wikipedia
import random
joo = random.randint(0,5)
e = pyttsx3.init('sapi5')
voices = e.getProperty('voices') 
e.setProperty('voice', voices[1].id)
def speak(audio):
    e.say(audio)
    e.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning Robo")
    elif hour>=12 and hour<16:
        speak("good afternoon Robo")
    elif hour>=16 and hour<=20:
        speak("good evevning Robo")
    else:
        speak("good night Robo")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Listnening...')
        print("Recognising....")
        speak("wait  a second")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as es:
        print(es)
        print("say that at again.......")
        return "None"
    return query
if __name__== "__main__":
    wishMe()
    #speak("Hii am your voice assistant")
    #speak("what can i do for you")
    while True:
       query = takecommand().lower()
       if "open youtube" in query:
           speak("opening youtube ")
           web.open("www.youtube.com")
       elif 'open google' in query:
           web.open("www.google.com")
           speak("opening google")
       elif "open facebook"  in query:
           web.open("www.facebook.com")
           speak("opening facebook")
       elif "what can you do" in query:
           speak("i can open facebook,google and also i can play music ")
           print("i can open facebook,google and also i can play music")
           print("i can open teamviewer and avast")
           speak("Still  a lot coming on my way")
       elif  "play music" in query:
           playlist="L:\songs"
           songs=os.listdir(playlist)
           os.startfile(os.path.join(playlist,songs[joo]))
           speak("playing music")
       elif "open avast" in query:
           py = "C:/Program Files/AVAST Software/Avast/AvastUI"
           speak("opening avast")
           speak("opening avast")
           os.startfile(py)
       elif "open teamviewer" in query:
           tv = "C:/Program Files (x86)/TeamViewer/TeamViewer"
           speak("opening teamviewer")
           os.startfile(tv)
       elif "wikipedia" in query:
           query = query.replace("wikipedia","")
           result = wikipedia.summary(query,sentences = 2)
           print(result)
           speak(result)
       elif "today headlines" in query:
          web.open("https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en")
       elif "play game" in query:
           speak("can we play guess the number game ")
           speak("type yes or no")
           i = input("type yes or no :")

           if i == "yes":
               print("you have three chance to guess the number")
               speak("you have three chance to guess the number")
               print("if you not guessed correctly it automatically exists from the game")
               speak("if you not guessed correctly it automatically exists from the game")
               secretnumber = random.randint(0, 8)
               for i in range(1, 4):
                   speak("guess a  number from  0 to 8")

                   guessnumber = int(input("guess a number from 1 to 8 = "))
                   if guessnumber < secretnumber:
                       speak("your guess is too low  ")
                       print("your guess is too low secret number is",secretnumber)
                       speak("secret number is ")
                       speak(secretnumber)
                   elif guessnumber > secretnumber:
                       speak("your guess is too high ")
                       speak("secret number is ")
                       print("your guess is too high secret number is :",secretnumber)
                       speak(secretnumber)
                   elif guessnumber == secretnumber:
                       speak("your guess is right ")
                       speak("secret number is ")
                       print("your guess is right secret number is: ",secretnumber)
                       speak(secretnumber)
                       break



