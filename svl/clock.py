import datetime
import math
import tkinter as tk


class Hand:
    def __init__(self, length, width, delay, offset) -> None:
        self.length = length
        self.pos = (270 + offset) % 360
        self.delay = delay

        self.item_id = c.create_line(
            SIZE // 2,
            SIZE // 2,
            SIZE // 2 + math.cos(math.radians(self.pos)) * self.length,
            SIZE // 2 + math.sin(math.radians(self.pos)) * self.length,
            fill="white",
            width=width,
        )
        c.after(self.delay // SPEED, self.tick)

    def tick(self):
        self.pos = (self.pos + 6) % 360
        c.coords(
            self.item_id,
            SIZE // 2,
            SIZE // 2,
            SIZE // 2 + math.cos(math.radians(self.pos)) * self.length,
            SIZE // 2 + math.sin(math.radians(self.pos)) * self.length,
        )
        c.after(self.delay // SPEED, self.tick)


SIZE = 500
SPEED = 1
CUSTOM_TIME = True
hands = {}
c = tk.Canvas(bg="black", width=SIZE, height=SIZE, highlightthickness=0)
c.pack()

now = datetime.datetime.now()  # noqa

if SPEED <= 600:
    hands["second"] = Hand(200, 5, 1000, now.second*6 if CUSTOM_TIME else 0)
hands["minute"] = Hand(180, 10, 60000, now.minute*6 if CUSTOM_TIME else 0)
hands["hour"] = Hand(150, 15, 360000, now.hour*30 if CUSTOM_TIME else 0)


c.mainloop()
