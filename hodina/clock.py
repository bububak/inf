from math import sin, cos
from tkinter import Tk, Canvas
from datetime import datetime



class Clock():
    def __init__(self) -> None:
        self.draw_starting_clock()
        self.tick()


    def draw_starting_clock(self):
        c.create_oval(0,0,W,H,fill="#cdd6f4")
        c.create_oval(outline_width,outline_width,W-outline_width,H-outline_width,fill="#1e1e2e")


    def tick(self):
        self.hour, self.minute, self.second = list(map(int,str(datetime.now().strftime("%-H %-M %-S")).split()))
        hand_angles = [self.hour*30,self.minute*6,self.second*6]
        c.delete("hand")

        for angle in hand_angles:

            stage = angle//45
            if stage%2 != 0:
                d = 45 - angle % 45
            else:
                d = angle % 45

            # a - adjacent, o - opposite, r - hypotenuse (radius)
            a = r*cos(d)
            o = r*sin(d)

            match stage:
                case 0:
                    x = r + o
                    y = r - a
                case 1:
                    x = r + a
                    y = r - o
                case 2:
                    x = r + a
                    y = r + o
                case 3:
                    x = r + o
                    y = r + a
                case 4:
                    x = r - o
                    y = r + a
                case 5:
                    x = r - a
                    y = r + o
                case 6:
                    x = r - a
                    y = r - o
                case 7:
                    x = r - o
                    y = r - a


            c.create_line(r,r,x,y, fill="#cdd6f4", width=20, tags="hand")

        c.after(1000,self.tick)



outline_width = 10
W = H = 500 #clock size, use multiple of 2
r = W//2
root = Tk()
c = Canvas(root,bg="#1e1e2e",width=W,height=H)
c.pack()


clock = Clock()


root.mainloop()
