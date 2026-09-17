import tkinter as tk

W, H = 2000, 1000
LEN = 10000
STEP_W = W/LEN
STEP_H = H/300
c = tk.Canvas(width=W, height=H, background="black")
c.pack()

m = 0
for n in range(1, LEN):
    original = n
    turns = 0
    while n != 1:
        turns += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
    c.create_rectangle(original*STEP_W,H-turns*STEP_H,original*STEP_W+STEP_W,H-turns*STEP_H+STEP_W,fill="white",width=0)
    c.update()

c.mainloop()
