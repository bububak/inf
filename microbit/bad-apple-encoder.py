import cv2



def base_convert(original, base_input, base_output):

    # anything to decimal
    n = 0
    v = 1
    o = str(original)
    for i in range(len(o)):
        n += int(o[-(i+1)])*v
        v *= base_input

    # decimal to anything
    out = ""
    while n:
        rest = n % base_output
        n = n // base_output
        out = str(rest) + out
    return int(out)



TARGET_FRAMERATE = 30
THRESHHOLD = 128
TARGET_W, TARGET_H = 5, 5
INPUT_VIDEO = "badapple.mp4"
OUTPUT_FILE = "badapple.bin"


cap = cv2.VideoCapture(INPUT_VIDEO)
source_fps = cap.get(cv2.CAP_PROP_FPS)
frame_skip_amount = source_fps // TARGET_FRAMERATE
f = open(OUTPUT_FILE, "wb")



ret, frame = cap.read()
W, H = frame.shape[:2]
size = min(W, H)
x0 = (W - size) // 2
y0 = (H - size) // 2
bytes_per_frame = (H*W)//8+1

framei = 0

while ret:

    # only process every x frames
    if framei % frame_skip_amount == 0:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        square = gray[y0:y0+size, x0:x0+size]
        small = cv2.resize(square, (TARGET_W, TARGET_H), interpolation=cv2.INTER_AREA)
        radical = (small > THRESHHOLD).astype(int)
        print(radical)

        value = 0
        bit_index = 0

        for row in radical:
            for bit in row:
                value |= (bit << bit_index)
                bit_index += 1


        f.write(int(value).to_bytes(4, "little"))



    framei += 1
    ret, frame = cap.read()



f.close()
cap.release()
cv2.destroyAllWindows()
