import math
import random
import tkinter as tk
import turtle


def start_fractal():
    global should_stop, N
    should_stop = False
    t.teleport(0, 0)
    t.seth(0)
    t.width(int(w.get()))
    t.clear()
    t.speed(0)
    turtle.delay(0)
    turtle.tracer(0)
    t.penup()
    t.bk(math.sqrt(2 * (D / 2 * D / 2)) / 2)
    t.pendown()
    N = s.get()
    ciara(N, D)


def stop():
    global should_stop
    should_stop = True


def ciara(n, d):
    new_d = math.sqrt(2 * (d / 2 * d / 2))
    if should_stop:
        return
    elif n <= 0:
        t.color(f"#{random.randrange(256**3):06x}")
        t.fd(new_d)
    else:
        t.rt(45)
        ciara(n - 1, new_d)
        t.lt(45)
        t.lt(45)
        ciara(n - 1, new_d)
        t.rt(45)


N = 0
D = 600
PADDING = 10
should_stop = False

t = turtle.Turtle()
t.hideturtle()
start_button = tk.Button(
    command=start_fractal, text="start", font=f"arial {PADDING * 3} bold"
)
start_button.pack(side="right", padx=PADDING, pady=PADDING)
stop_button = tk.Button(command=stop, text="stop", font=f"arial {PADDING * 3} bold")
stop_button.pack(side="right", padx=PADDING, pady=PADDING)
s = tk.Scale(label="iterations",from_=0, to=15, orient="horizontal", length=200, width=2 * PADDING)
s.set(8)
s.pack(side="left", padx=PADDING, pady=PADDING)
w = tk.Scale(label="width",from_=0, to=15, orient="horizontal", length=200, width=2 * PADDING)
w.set(2)
w.pack(side="left", padx=PADDING, pady=PADDING)


tk.mainloop()
