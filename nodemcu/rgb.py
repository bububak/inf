from machine import Pin
from neopixel import NeoPixel
from time import sleep
from os import urandom

np = NeoPixel(Pin(5),8)
# np[0] = (255, 0, 0)
# np[1] = (0, 255, 0)
# np[2] = (0, 0, 255)


for i in range(8):
    np[i] = (urandom(1)[0], urandom(1)[0], urandom(1)[0])
    sleep(0.5)
    np.write()
    
for i in range(8):
    np[i] = (0, 0, 0)
    sleep(0.5)
    np.write()
    
np.write()
    

