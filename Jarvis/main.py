import datetime
import os
import tkinter as tk
from tkinter import filedialog, Text
from playsound import playsound
import requests
from tkinter import *
from tkinter import messagebox
from geopy.geocoders import Nominatim
from geopy import geocoders
from bs4 import BeautifulSoup
import pyttsx3  # text to speech

import CommandControl
import text_speechEngine as speech
from datetime import date
import voiceRecognition as vr
from geopy.geocoders import Nominatim

'''
My Own Jarvis. Aiming great but currently is still quite basic. 
Currently writing as an small app using tkinter 
'''

city = 'Wellington'
country = 'nz'
RECONIZEDTEXT = ""


def welcome():
    playsound('S:\\Jarvais\SoundTracks\JarvisStartUp.mp3')


def getLocation():
    # importing geopy library

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
    timeNow = datetime.datetime.now()
    hour = timeNow.hour
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
