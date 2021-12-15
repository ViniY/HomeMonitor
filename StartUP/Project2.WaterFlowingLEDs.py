from machine import Pin
from time import sleep


Led_red = Pin(0, Pin.OUT)
Led_green = Pin(1, Pin.OUT)
Led_yewllow = Pin(2, Pin.OUT)

time_interval = 0.2

while True:
  Led_red.toggle()
  sleep(interval)
  
  Led_green.toggle()
  sleep(interval)
  
  Led_yellow.toggle()
  sleep(interval)
