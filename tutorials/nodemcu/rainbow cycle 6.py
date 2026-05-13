from machine import Pin
from neopixel import NeoPixel
from time import sleep


LIGHTS = 6
np = NeoPixel(Pin(4), LIGHTS)
BRIGHTNESS = 0.5
WAIT = 0
FULL = 255 * 6
STEP = 5

r = 4
g = 0
b = 2


i = 0
while True:
    state = i//255
    delta = i % 255
    colors = (delta,255,255,255-delta,0,0)    
    
    for light in range(LIGHTS):
        np[light] = (int(BRIGHTNESS*colors[(r+state+light)%6]), int(BRIGHTNESS*colors[(g+state+light)%6]), int(BRIGHTNESS*colors[(b+state+light)%6]))
    
    np.write()
    i += STEP
    i = i % FULL
    sleep(WAIT)