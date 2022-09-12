import datetime
import tkinter as tk
from playsound import playsound
import text_speechEngine as speech
from geopy.geocoders import Nominatim
from Jarvis import CommandControl
import voiceRecognition as vr
import os
'''
This project is aiming to be a home monitor with voice control

# Currently available: 
    Voice to Text convert
    Weather check
    Text to Speech
# TODO: 
    0. Build a virtual Env and sort out all the libraries (on going) (22/5/2022)
    1. Connect the project with Mi Products using Access Token  (Done)
    2. Semantic Analysis (To get ric off stupid key word detection) (22/5/2022)
    3. Classify the text into tasks or just random talk (two weeks)
    4. Build the Sensors for Temperature, Moisture, Sound, Light intensity (done by July)
    5. Read info from surrounding env (...)
    6. Data Processing for the surrounding env data 
    7. Build House Model (IDK what to do with it but just list here first )
    8. Smart Control lights .... and other products based on the surrounding env (like turning on the light)
    9. Build Docker Image (This is aiming for make this project published)
    10. Image Processing
        a. Capture the front door visual
        b. Face detection and Recognising (simple classification should be fine)
        c. Height and weight prediction
    11. NLP:
        a. The system should be able to understand different languages
        b. Slice the voice into different layers (background sound, user voice) 
        c. Analysis the voice frequency of the users (To know who is controlling, better access control)
    More can be added later on 
          
'''

city = 'Wellington'
country = 'nz'
RECONIZEDTEXT = ""

# TODO The welcome song need to be conclude in the package
def welcome():
    playsound("../resource/tones/JARVIS_Wellcome.mp3")

def getLocation():
    # calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")
    # entering the location name
    getLoc = loc.geocode(city)
    # printing address
    print(getLoc.address)
    # printing latitude and longitude
    print("Latitude = ", getLoc.latitude, "\n")
    print("Longitude = ", getLoc.longitude)


def greetings():
    time_Now = datetime.datetime.now()
    hour = time_Now.hour
    dayTime = ""
    if 5 < hour <= 12:
        dayTime = "Good Morning "
    elif 12 < hour <= 18:
        dayTime = "Good Afternoon"
    elif hour <= 5 or hour > 22:
        dayTime = "Good Night"
    else:
        dayTime = "Good Evening"
    text_ = dayTime + " sir " + " jarvis at your service as always. "
    speech.speak(text_)


def listening():
    text = vr.listening()
    global RECONIZEDTEXT
    RECONIZEDTEXT = text
    CommandControl.recognizedText_(RECONIZEDTEXT)


if __name__ == '__main__':
    welcome()
    greetings()
    root = tk.Tk()
    root.title('Jarvis')
    canvas = tk.Canvas(root, height=600, width=900, bg="#263D42")
    canvas.pack()
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)  # adding a frame on the outside
    getLocation()
    listeningBut = tk.Button(root, text='Im here', padx=10, pady=5, fg='white', bg='#263D42', command=listening)
    listeningBut.pack()
    root.mainloop()
