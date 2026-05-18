import cv2



TARGET_FRAMERATE = 30
THRESHHOLD = 128
TARGET_W = 8
TARGET_H = 8
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
bytes_per_frame = (TARGET_W*TARGET_H)//8 + (0 if (TARGET_W*TARGET_H)%8 == 0 else 1)
print(f"Encoding {INPUT_VIDEO} as {OUTPUT_FILE} with {bytes_per_frame} bytes ber frame at {TARGET_FRAMERATE}fps")
print(frame_skip_amount)

framei = 0

while ret:

    # only process every x frames
    if framei % frame_skip_amount == 0:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        square = gray[y0:y0+size, x0:x0+size]
        small = cv2.resize(square, (TARGET_W, TARGET_H), interpolation=cv2.INTER_AREA)
        radical = (small > THRESHHOLD).astype(int)
        # print(radical)

        value = 0
        bit_index = 0

        for row in radical:
            for bit in row:
                bit = int(bit)
                value |= (bit << bit_index)
                bit_index += 1


        f.write(value.to_bytes(bytes_per_frame,"little"))



    framei += 1
    ret, frame = cap.read()



f.close()
cap.release()
cv2.destroyAllWindows()
