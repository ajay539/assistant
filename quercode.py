import pyzbar.pyzbar as pyzbar
import cv2
import numpy
import pyttsx3

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print(voice)
engine.setProperty('voice',voice[1].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def scan():
    op = "Scaning QRcode"
    print(op)
    speak(op)
    i = 0
    cap = cv2.VideoCapture(0)
    while i<4:
        _,frame = cap.read()
        decoded = pyzbar.decode(frame)
        for obj in decoded:
            print(obj.data)
            i = i+1

        cv2.imshow("QRcode",frame)
        cv2.waitKey(5)
        cv2.destroyAllWindows