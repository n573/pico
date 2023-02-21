from machine import Pin
from time import sleep
led = Pin(25, Pin.OUT)
button1 = Pin(2, Pin.IN)
#vbus = Pin(40, Pin.OUT)
#vbus.value(1)

while(True):
    led.value(1)
    if button1.value(1) == True:
        led.value(1)
    else:
        led.value(0)
    
    sleep(1)
    led.value(0)
    sleep(1)
end