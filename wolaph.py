import wolframalpha
import query
import pyttsx3
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print(voice)
engine.setProperty('voice',voice[1].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

try:
    app = wolframalpha.Client("V8UWVH-ETAT3T24AP")
except Exception:
    print("Check your network connection")

def woa():
    try:
        print("Type your question")
        query = (">> ")
        res = app.query(query)
        print(res)
        speak(res)
    except:
        print("Check your network connection")