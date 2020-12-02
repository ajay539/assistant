import os 
import query
import pyttsx3

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voices',voice[2])
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def movies():
    p1 = "pirate1"
    p2 = "pirate2"
    p3 = "pirate3"
    p4 = "pirate4"
    p5 = "pirate5"
    print("which movie you want me to play")
    speak("which movie you want me to play")
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(p5)
    query = input(">> ")
    if "pirate1" in query:
        print("playing your wished movie")
        speak("playing your wished movie")
        movie_dir = "D:\\MOVIES\\Pirates of Carbbean"
        movie = os.listdir(movie_dir)
        os.startfile(os.path.join(movie_dir,movie[1]))
    if "pirate2" in query:
        print("playing your wished movie")
        speak("playing your wished movie")
        movie_dir = "D:\\MOVIES\\Pirates of Carbbean"
        movie = os.listdir(movie_dir)
        os.startfile(os.path.join(movie_dir,movie[2]))
    if "pirate3" in query:
        print("playing your wished movie")
        speak("playing your wished movie")
        movie_dir = "D:\\MOVIES\\Pirates of Carbbean"
        movie = os.listdir(movie_dir)
        os.startfile(os.path.join(movie_dir,movie[3]))
    if "pirate4" in query:
        print("playing your wished movie")
        speak("playing your wished movie")
        movie_dir = "D:\\MOVIES\\Pirates of Carbbean"
        movie = os.listdir(movie_dir)
        os.startfile(os.path.join(movie_dir,movie[4]))
    if "pirate5" in query:
        print("playing your wished movie")
        speak("playing your wished movie")
        movie_dir = "D:\\MOVIES\\Pirates of Carbbean"
        movie = os.listdir(movie_dir)
        os.startfile(os.path.join(movie_dir,movie[5]))   