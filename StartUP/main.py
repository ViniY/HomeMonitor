from machine import Pin
from machine import Pin, Timer
import utime

led_red = Pin(15, Pin.OUT)
led_yellow = Pin(14, Pin.OUT)
#led_green = Pin(13, Pin.OUT)
timer = Timer()
counter = 0
def blink(timer):
    global counter
    counter +=1
    if counter >30:
        counter =0
    if counter%2 ==0:
        led_red.toggle()
    if counter%3 ==0:
        led_yellow.toggle()
    if counter%5 ==0:
        print("gre")
        #led_green.toggle()
timer.init(freq =2.5, mode = Timer.PERIODIC, callback =blink)