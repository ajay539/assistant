import os
import pyttsx3
import query

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voices',voice[2].id)
engine.setProperty('rate',150)

def speaK(audio):
    engine.say(audio)
    engine.runAndWait()

def videos():
    print("Which video you want me to play")
    speaK("Which video you want me to play")
    print("Chamma Chamma")
    print("Dilbar")
    print("Garmi")
    print("O Saki Saki")
    print("Kamariya")
    print("Gali Gali")
    print("EK Toh Kum Zindagani")
    print("Odhani")
    print("Nari Nari")
    query = input(">> ")   
    if "Chamma Chamma" in query:
        print("Ok playing your wished video") 
        speaK("Ok playing your wished video") 
        video_dir = "./item v"
        video = os.listdir(video_dir)
        os.startfile(os.path.join(video_dir,video[0]))
    if "Dilbar" in query:
        print("Ok playing your wished video") 
        speaK("Ok playing your wished video") 
        video_dir = "./item v"
        video = os.listdir(video_dir)
        os.startfile(os.path.join(video_dir,video[1]))
    if "Garmi" in query:
        print("Ok playing your wished video") 
        speaK("Ok playing your wished video") 
        video_dir = "./item v"
        video = os.listdir(video_dir)
        os.startfile(os.path.join(video_dir,video[2]))
    if "O Saki Saki" in query:
        print("Ok playing your wished video") 
        speaK("Ok playing your wished video") 
        video_dir = "./item v"
        video = os.listdir(video_dir)
        os.startfile(os.path.join(video_dir,video[3]))
    if "Kamariya" in query:
        print("Ok playing your wished video") 
        speaK("Ok playing your wished video") 
        video_dir = "./item v"
        video = os.listdir(video_dir)
        os.startfile(os.path.join(video_dir,video[4]))
    if "Gali Gali" in query:
        print("Ok playing your wished video") 
        speaK("Ok playing your wished video") 
        video_dir = "./item v"
        video = os.listdir(video_dir)
        os.startfile(os.path.join(video_dir,video[5]))
    if "EK Toh Kum Zindagani" in query:
        print("Ok playing your wished video") 
        speaK("Ok playing your wished video") 
        video_dir = "./item v"
        video = os.listdir(video_dir)
        os.startfile(os.path.join(video_dir,video[6]))
    if "Odhani" in query:
        print("Ok playing your wished video") 
        speaK("Ok playing your wished video") 
        video_dir = "./item v"
        video = os.listdir(video_dir)
        os.startfile(os.path.join(video_dir,video[7]))
    if "Nari Nari" in query:
        print("Ok playing your wished video") 
        speaK("Ok playing your wished video") 
        video_dir = "./item v"
        video = os.listdir(video_dir)
        os.startfile(os.path.join(video_dir,video[8]))