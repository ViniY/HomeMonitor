from machine import Pin
from time import sleep

Led_red = Pin(0, Pin.OUT)
Led_green = Pin(1, Pin.OUT)
Led_yewllow = Pin(2, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

interval = 2

while True:
  if button.value():
    interval = interval / 1.414
  if time_interval < 0.1:
    time_interval = 2 
  Led_red.toggle()
  sleep(interval)
  
  Led_green.toggle()
  sleep(interval)
  
  Led_yellow.toggle()
  sleep(interval)
