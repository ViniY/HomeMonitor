"""This file is used as a main command controller, which will used  the reconized the text to match the implemented functions
    The ultimate goal of this is to automatically understand the word people saying and choose the right functionality
    But currently we donnt have Text segmentation on it and also blablabla
    so we basically using the most stupid way currently
"""
import functionalityPack as funcs
from geotext import GeoText


def recognizedText_(text):

    if "weather" and "today" in text:
        cityName = GeoText(text).cities
        if len(cityName) != 0 :
            cityName = cityName[0]
            funcs.weatherReport(cityName)
        else:
            funcs.weatherReport("Wellington")
    else:
        print("Currently I dont have that functionality")