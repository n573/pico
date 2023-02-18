from machine import Pin
from time import sleep
led = Pin(25, Pin.OUT)
button1 = Pin(2, Pin.IN)

while(True):
    if(button1.value == 1):
        led.value(1)
    else:
        led.value(0)
#    led.value(1)
#    sleep(2)
#    led.value(0)
    #sleep(1)