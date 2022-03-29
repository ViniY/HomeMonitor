from playsound import playsound
import requests
import text_speechEngine as speech
import datetime
import geotext

def weatherReport(city):
    api_key = "1ada8f64926d58a8a31c7d92ec230faa7c462347a14269d45ba31d471b6f6aa6"  # Enter the API key you got from the OpenWeatherMap website
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # city_name = input("Enter city name : ")
    city_name = "Wellington"
    complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name  # This is to complete the base_url, you can also do this manually to checkout other weather data available
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"] - 273.15
        current_temperature = round(current_temperature,2)

        z = x["weather"]
        wind = x["wind"]
        windSpeed = wind['speed']

        print(wind)
        weather_description = z[0]["description"]

        h = y["humidity"]
        print()


        dTime = datetime.datetime.now()
        year = dTime.year
        month = dTime.month
        day = dTime.day
        dateText = "Today is "
        if day==1 :
            dateText += "first"
        elif day ==2:
            dateText += "second"
        elif day ==21:
            dateText += "twenty first"
        elif day == 22:
            dateText += "twenty second"
        elif day == 31:
            dateText += "thirty first"
        else:
            dateText += str(day) + "th"


        dateText += " of " + str(month)

        months = {1 : "January",
                  2 : "February",
                  3 : "March",
                  4 : "April",
                  5 : "May",
                  6 : "June",
                  7 : "July",
                  8 : "August",
                  9 : "September",
                  10: "October",
                  11: "November",
                  12 : "December"}

        date_today = "Sir, Today is " + dateText + " of " + months[month] + " Year " + str(year)
        speech.speak(date_today)
        detailedWeather = " The temprature today is " + str(current_temperature) + " degrees " +  " the humidity is " + str(h) + " the wind is " + str(windSpeed) + " metres per second"
        print(" Temperature (in Celsius unit) = " +
              str(current_temperature) +
              "\n Humidity = " + str(h) +
              "\n description = " +
              str(weather_description) +
              "\n Wind speed  = " + str(round(windSpeed,2)))
        speech.speak(detailedWeather)
    else:
        print(" City Not Found ")
