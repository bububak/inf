import time, os


W = 8
H = 8
FRAMERATE = 30
ms_per_frame = 1/FRAMERATE


bytes_per_frame = (W*H)//8 + (0 if (W*H)%8 == 0 else 1)
f = open("badapple.bin", "rb")
translate = {"0":" ","1":"█"}

chunk = f.read(bytes_per_frame)
while chunk:
    value = int.from_bytes(chunk, "little")

    b = str(bin(value))[2:]
    while len(b) < W*H:
        b = "0" + b

    frame = ""
    for c in b:
        frame += translate[c]

    os.system("clear")
    for i in range(H):
        print(frame[i*W:(i+1)*W])
    time.sleep(0.016)

    chunk = f.read(bytes_per_frame)

f.close()
