import alarm
import music
import wolaph
import quercode
import asciis
import movies
import video
import dateT
import query
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import random
import getpass
import os

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print(voice)
engine.setProperty('voice',voice[1].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good morning")
        speak("Good morning")
    if hour>=12 and hour<18:
        print("Good afternoon")
        speak("Good afternoon")
    if hour>=18 and hour<24:
        print("Good evening")
        speak("Good evening")
      
wish()
speak("Type the password")
while True:
    Password = getpass.getpass(prompt="Type the password: ")
    if Password == "Forgot":
        print("Acess granted")
        break
    else:
        print("Acess denied")
print(" ")
print("WELCOME!!!!!!!")
print(" ")
print("* = recomended")
print('Now it will print and speak the current date and time')
print("*you can now ask for assistant's function if you are new, 'note:- to use this programme. type:- your features'*")

r = ("my following features are: ")
n = ("song 'note:- when this command starts it will show you the songs in my system'")
m = ("set alarm at (example:12:18 pm) 'note:- Type the time on which you want to set your alarm'")
q = ("QRCODE 'note:- this function can scan any qrcode'")
e = ("info 'note:- Can be used when internet connection is there'")
t = ("exit 'note:- this command will end the programme'")
s = ("shutdown 'note:- This command will shutdown your device in a minute or less'")
a = ("img2ascii 'note:- it will provide you with a image.txt and can convert any image picture")
w = ("movie 'note:- when this command starts it will show you the movies in my system'")
v = ("video 'note:- when this command starts it will show you the video in my system'")
g = ("game 'note:- This will start any game in my system'")

speak("Waiting for command")

dateT.dateT()
def main():
    print("Waiting for command")
    query = input(">>> ")
    if "your features" in query:
        speak(r)
        print(r)
        speak(n)
        print(n)
        speak(m)
        print(m)
        speak(q)
        print(q)
        speak(e)
        print(e)
        speak(t)
        print(t)
        speak(s)
        print(s)
        speak(a)
        print(a)
        speak(w)
        print(w)
        speak(g)
        print(g)
        return main()
    if "song" in query:
        print("TYPE 'music'")
        music.takecom()
        return main()
    if "movie" in query:
        movies.movies()
        return main()
    if "alarm" in query:
        print("Alarm is set at"+query[12:])
        speak("Alarm is set at"+query[12:])
        alarm.alarm(query)
        return main()
    if "QRCODE" in query:
        quercode.scan()
        return main()
    if "video" in query:
        video.videos()
        return main()
    if "info" in query:
        wolaph.woa()
        return main()
    if "img2ascii" in query:
        print("Put your image name with its extension")
        speak("Put your image name with its extension")
        query = input(">> ")
        asciis.start(query)
        return main()
    if "exit" in query:
        Hour = int(datetime.datetime.now().hour)
        if Hour>=0 and Hour<12:
            print("Good bye, Have a nice day")            
            speak("Good bye, Have a nice day")
        if Hour>=12 and Hour<18:
            print("Good bye, Have a nice day")
            speak("Good bye, Have a nice day")
        if Hour>=18 and Hour<24:
            print("Good Night")
            speak("Good Night")
        exit()
    if "shutdown" in query:
        HouT = int(datetime.datetime.now().hour)
        if HouT>=0 and HouT<12:
            print("Good bye, Have a nice day")            
            speak("Good bye, Have a nice day")
        if HouT>=12 and HouT<18:
            print("Good bye, Have a nice day")
            speak("Good bye, Have a nice day")
        if HouT>=18 and HouT<24:
            print("Good Night")
            speak("Good Night")
        os.system('shutdown -s')
main()