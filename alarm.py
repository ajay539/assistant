import datefinder
import datetime
import winsound
import os

def alarm(text):
    dTimeA = datefinder.find_dates(text)
    for mat in dTimeA:
        print(mat)
    stringA = str(mat)
    timeA = stringA[11:]
    hourA = timeA[:-6]
    hourA = int(hourA)
    minA = timeA[3:-3]
    minA = int(minA)


    while True:
        if hourA == datetime.datetime.now().hour:
            if minA == datetime.datetime.now().minute:
                print("Alarm is running")
                winsound.PlaySound('D:\\MOVIES\\python\\Assistant project\item\\audio.wav',winsound.SND_LOOP)
            elif minA<datetime.datetime.now().minute:
                break

#alarm("Set alarm at 1:17 pm")