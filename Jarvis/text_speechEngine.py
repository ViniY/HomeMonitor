import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 120)  # setting up new voice rate


def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    speak("Today is 25th of October, 2021")
