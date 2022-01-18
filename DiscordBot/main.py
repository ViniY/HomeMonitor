import os
import discord
import json
import requests
from replit import db
from keep_alive import keep_alive
from datetime import datetime
from geotext import GeoText
import random 
from discord.ext import commands,tasks
import os
from dotenv import load_dotenv
import youtube_dl
import re


client = discord.Client()
# intents = discord.Intents().all()
# client = discord.Client(intents=intents)
# bot = commands.Bot(command_prefix='!',intents=intents)

api_key="1ada8f64926d58a8a31c7d92ec230faa7c462347a14269d45ba31d471b6f6aa6"  
# Enter the API key you got from the OpenWeatherMap website
text_bobi = ["祖安大舞台 有妈你就来", "天工造物不测，怎么造出你这么个东西", "扔块肉在屏幕上，狗都比你会连招", "你脑子进水了吧，还是100°的那种沸水",
        "我终于知道你是一个什么怪物了，原来你是臭水沟里老鼠蜕变的呀，难怪浑身臭气熏天呢！"
        "别在卖萌嘟嘴剪到手了，都是被人叫做叔叔阿姨的人了", "其实我挺佩服你的，能长成这样，你长的比芙蓉姐还恶心，比凤姐还销魂。"]

def time_now():
  now = datetime.now()
  return now


def weatherToday(msg_in):
  insensitive_weather = re.compile(re.escape('weather'), re.IGNORECASE)
  msg_in = insensitive_weather.sub('', msg_in)
  msg_array = msg_in.split()
  msg_in_ = ""
  for ms in msg_array:
    msg_in_ += ms.title()
    msg_in_ += " "
  msg_in = msg_in_

  city_name = GeoText(msg_in).cities
  city_name = city_name[0]
    
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  complete_url = base_url + "appid=" +'d850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name

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
  weather=[]
  weather.append(weather_description)
  weather.append(current_temperature)
  weather.append(windSpeed)
  weather.append(h)
  weather.append(city_name)
  return weather

def addBobi(msg):
  msg_ = msg.replace("$添加:", "")
  text_bobi.append(msg)
  return (msg_ + " 已添加")



def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote
def update_encouragements(encouraging_msg):
  if "encouragements" in db.key():
    encouragemetns = db["encouragemetns"]
    encouragemetns.append(encouraging_msg)
  else: 
    db["encouragemetns"] = [encouraging_msg]  
    # options = options + db["encouragements"]

def delete_encouragment(index):
  encouragements = db['encouragements']
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

def zanghuabobi(duixiang):
  # print(text_bobi)
  index = random.randint(0,len(text_bobi)-1)
  words = text_bobi[index]
  return words
#=========================================Music=======================

def playMusic(url):
  return true


# @client.command(pass_context=True)
# async def yt(ctx, url):
#     author = ctx.message.author
#     voice_channel = author.voice_channel
#     vc = await client.join_voice_channel(voice_channel)

#     player = await vc.create_ytdl_player(url)
#     player.start()

#===========================================================================
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return # if the msg from the bot then just return

  if message.content == ('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  
  msg = message.content

  if ("time" in msg or "Time" in msg):
    msg_ = msg.lower()
    if "now" in msg_:
      timeNow = time_now()
      await message.channel.send(timeNow)
  
  if ("weather"  in msg) or ("Weather" in msg):
    weatherReport = weatherToday(msg)
    # await message.channel.send(weatherReport)

    weather = weatherReport[0]
    tempreture = weatherReport[1]
    wind = weatherReport[2]
    humidity = weatherReport[3]
    cityName = weatherReport[4]
    await message.channel.send("The weather today in " + cityName + " is " + weather
    + " the tempreture now is " + str(tempreture) + " and the wind is " + str(wind) + "m/s and the humidity is " + str(humidity))
  if "喷他" in msg:
    for i in range(5):
      zanghua = zanghuabobi("")
      await message.channel.send(zanghua)

  if "$添加:" in msg:
    returned = addBobi(msg)
    await message.channel.send(returned)

  if "$play" in msg: # fecth the url from the user input
    playing = playMusic("") 


my_secret = os.environ['dcrobotJarv1s']

keep_alive()
# bot.run(my_secret)
client.run(my_secret)