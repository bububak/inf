import max7219, time
from machine import Pin, SPI


spi = SPI(1, baudrate=10000000, polarity=0, phase=0)
display = max7219.Matrix8x8(spi, Pin(15), 4)
display.brightness(0)
display.fill(0)
display.show()

time.sleep(0.1)
display.text("bapl", 0, 0, 1)
display.show()
time.sleep(2)
display.fill(0)
display.show()


W = 8
H = 8
FRAMERATE = 10
ms_per_frame = 1/FRAMERATE
ms_per_frame = 0

bytes_per_frame = (W*H)//8 + (0 if (W*H)%8 == 0 else 1)
f = open("badapple.bin", "rb")


chunk = f.read(bytes_per_frame)
while chunk:
    value = int.from_bytes(chunk, "little")

    b = str(bin(value))[2:]
    while len(b) < W*H:
        b = "0" + b

    
    for y in range(H):
        for x in range(W):
            c = int(b[y*H+x:y*H+x+1])
            display.pixel(x,y,c)


    display.show()
    time.sleep(ms_per_frame)
    chunk = f.read(bytes_per_frame)

f.close()
