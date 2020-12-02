import datetime
import calendar
import pyttsx3

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print(voice)
engine.setProperty('voice',voice[1].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def dateT():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day
    meridiem = ''

    if now.hour >=12:
        meridiem = "P.M"
        hour = now.hour -12
    else:
        meridiem = "A.M"
        hour = now.hour
    if now.minute<10:
        minute = '0'+str(now.minute)
    else:
        minute = str(now.minute)

    month_names = ['January','February','March','April','May','June','July','August','September','Octuber','November','December']

    ordinalnumbers = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    
    r = 'Todays date is: '+weekday+' '+ordinalnumbers[dayNum -1]+'/'+month_names[monthNum -1]+'/'+str(now.year)+' '+'And'+' '+'Time is: '+str(now.hour)+ ':'+minute+' '+meridiem+'. ' 
    print(r)
    speak(r)