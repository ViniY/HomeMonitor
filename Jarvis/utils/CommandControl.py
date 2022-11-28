"""This file is used as a main command controller, which will used  the reconized the text to match the implemented functions
    The ultimate goal of this is to automatically understand the word people saying and choose the right functionality
    But currently we donnt have Text segmentation on it and also blablabla
    so we are basically using the most stupid way currently
"""

from geotext import GeoText
from Jarvis.utils.WeatherReport import weather_report


def recognized_text(text):
    if "weather" and "today" in text:
        city_name = GeoText(text).cities
        if len(city_name) != 0:
            city_name = city_name[0]
            weather_report(city_name)
        else:
            weather_report("Wellington")
    else:
        print("Currently I dont have that functionality")

