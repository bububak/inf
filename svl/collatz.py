import tkinter as tk

W, H = 2000, 1000
LEN = 10000
STEP_W = W/LEN
STEP_H = 3
c = tk.Canvas(width=W, height=H, background="black")
c.pack()

m = 0
for n in range(1, LEN):
    original = n
    max_reached = 0
    turns = 0
    while n != 1:
        max_reached = max(max_reached,n)
        turns += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1

    to_display = turns
    c.create_rectangle(original*STEP_W,H-to_display*STEP_H,original*STEP_W+STEP_W,H-to_display*STEP_H+STEP_W,fill="white",width=0)
    c.update()

c.mainloop()
