import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import random
import os

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print(voice)
engine.setProperty('voice',voice[1].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecom():
    sp = "Which music you want me to play"
    so = "Ok playing your wished music"
    W = "Welcome to my hell"
    D = "Dilbar"
    K = "Kamariya"
    G = "Gali Gali"
    Ga = "Garmi"
    O = "O Saki Saki"
    Od = "Odhani"
    N = "Nari Nari"
    Cc = "Chamma Chamma"
    Go = "Ghungaroo"
    A = "ACR"
    C = "MORIGAN"
    R = "I AM"
    query = input(">> ")
    if "music" in query:
        print(sp)
        speak(sp) 
        print(D)
        print(K)
        print(Cc)
        print(G)
        print(Ga)
        print(Go)
        print(O)
        print(Od)
        print(N)
        print(W)
        print("This is a offical game theme song:")
        print(R)  
        print(C)
        print(A)
        i = input(">> ")
        if "Dilbar" in i:
            print(so)
            speak(so)
            item_dir = "./item"
            item = os.listdir(item_dir)
            os.startfile(os.path.join(item_dir,item[0]))            
        if "Kamariya" in i:
            print(so)
            speak(so)
            item_dir = "./item"
            item = os.listdir(item_dir)
            os.startfile(os.path.join(item_dir,item[1]))  
        if "Chamma Chamma" in i:
            print(so)
            speak(so)
            item_dir = "./item"
            item = os.listdir(item_dir)
            os.startfile(os.path.join(item_dir,item[2]))  
        if "Gali Gali" in i:
            print(so)
            speak(so)
            item_dir = "./item"
            item = os.listdir(item_dir)
            os.startfile(os.path.join(item_dir,item[3]))  
        if "Garmi" in i:
            print(so)
            speak(so)
            item_dir = "./item"
            item = os.listdir(item_dir)
            os.startfile(os.path.join(item_dir,item[4]))  
        if "Ghungroo" in i:
            print(so)
            speak(so)
            item_dir = "./item"
            item = os.listdir(item_dir)
            os.startfile(os.path.join(item_dir,item[5]))  
        if "O Saki Saki" in i:
            print(so)
            speak(so)
            item_dir = "./item"
            item = os.listdir(item_dir)
            os.startfile(os.path.join(item_dir,item[6]))  
        if "Odhani" in i:
            print(so)
            speak(so)
            item_dir = "./item"
            item = os.listdir(item_dir)
            os.startfile(os.path.join(item_dir,item[7]))  
        if "Nari Nari" in i:
            print(so)
            speak(so)
            item_dir = "./item"
            item = os.listdir(item_dir)
            os.startfile(os.path.join(item_dir,item[8]))  
        if "Welcome to my hell" in i:
            print(so)
            speak(so)
            music_dir = "./music"
            music = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,music[0]))      
        if "I AM" in i:
            print(so)
            speak(so)
            theme_dir = "./theme"
            theme = os.listdir(theme_dir)
            os.startfile(os.path.join(theme_dir,theme[0])) 
        if "MORIGAN" in i:
            print(so)
            speak(so)
            theme_dir = "./theme"
            theme = os.listdir(theme_dir)
            os.startfile(os.path.join(theme_dir,theme[1]))  
        if "ACR" in i:
            print(so)
            speak(so)
            theme_dir = "./theme"
            theme = os.listdir(theme_dir)
            os.startfile(os.path.join(theme_dir,theme[2]))  