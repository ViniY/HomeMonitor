from Jarvis.utils.CommandControl import recognized_text
from Jarvis.utils.Voice_Recognition import listening
import text_to_speech as speech
import datetime
from playsound import playsound
from geopy.geocoders import Nominatim


def greetings():
    time_Now = datetime.datetime.now()
    hour = time_Now.hour
    day_time = ""
    if 5 < hour <= 12:
        day_time = "Good Morning "
    elif 12 < hour <= 18:
        day_time = "Good Afternoon"
    elif hour <= 5 or hour > 22:
        day_time = "Good Night"
    else:
        day_time = "Good Evening"
    text_ = day_time + " sir " + " jarvis at your service as always. "
    speech.speak(text_)


def listen():
    text = listening()
    global RECONIZEDTEXT
    RECONIZEDTEXT = text
    recognized_text(RECONIZEDTEXT)


def welcome():
    playsound("../resource/tones/JARVIS_Wellcome.mp3")


def get_location(city="Wellington"): # if not specific the city then it will be WEllington
    # calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")
    # entering the location name
    getLoc = loc.geocode(city)
    # printing address
    print(getLoc.address)
    # printing latitude and longitude
    print("Latitude = ", getLoc.latitude, "\n")
    print("Longitude = ", getLoc.longitude)

