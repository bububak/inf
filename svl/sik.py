from tkinter import Canvas, Tk
import random


class Catppuccin:
    def __init__(self) -> None:
        pass

    bg = [
        "#11111b",
        "#181825",
        "#1e1e2e",
    ]
    surface = [
        "#313244",
        "#45475a",
        "#585b70",
    ]
    overlay = [
        "#6c7086",
        "#7f849c",
        "#9399b2",
    ]
    fg = [
        "#cdd6f4",
        "#bac2de",
        "#a6adc8",
    ]


def vykresli_ciary():
    for y in range(1, sizey):
        c.create_line(0, y * s, W, y * s, tags="liney", fill=theme.surface[2])
    for x in range(1, sizex):
        c.create_line(x * s, 0, x * s, H, tags="linex", fill=theme.surface[2])


def rightclick(e):
    global first_click_registered, rects
    for i in rects[:]:
        cor = c.coords(i)
        if cor[0] < e.x and cor[1] < e.y and cor[2] > e.x and cor[3] > e.y:
            c.delete(i)
            rects.remove(i)

    first_click_registered = False
    c.delete("sel")


def draw_rows():
    global sizex, sizey, c
    # urob pre vsetky pismenka
    n = 0
    for y in range(sizey):
        a = field[y]
        for x in range(sizex):
            if a[x] == ".":
                continue
            elif a[x].isnumeric():
                n = int(a[x])
            elif a[x] == "C":
                n = 12
            c.create_text(
                x * s + s // 2,
                y * s + s // 2,
                text=n,
                font="Arial 20 bold",
                tags="num",
                fill=theme.fg[0],
            )


def load_nums():
    f = open("sik1.txt")
    global sizex, sizey
    a = f.readline().strip()
    sizex = len(a)
    while not a == "":
        field.append(a)

        sizey += 1
        a = f.readline().strip()


def leftclick(e):
    global first_click_registered, last_x, last_y, rect_counter, rects
    x = (e.x - o) // s
    y = (e.y - o) // s
    xlist = sorted([x, last_x])
    ylist = sorted([y, last_y])
    if first_click_registered:
        rects.append(
            c.create_rectangle(
                (
                    xlist[0] * s + w // 2 + 1,
                    ylist[0] * s + w // 2 + 1,
                    xlist[1] * s + s - w // 2,
                    ylist[1] * s + s - w // 2,
                ),
                width=w,
                outline=pastel_color(),
            )
        )
        first_click_registered = False
        c.delete("sel")
    else:
        last_x = x
        last_y = y
        first_click_registered = True
        c.create_rectangle(
            x * s + o,
            y * s + o,
            x * s + s + o,
            y * s + s + o,
            tags="sel",
            fill=theme.overlay[0],
        )
        c.tag_lower("sel")


def pastel_color():
    r = random.randint(128, 255)
    g = random.randint(128, 255)
    b = random.randint(128, 255)
    return f"#{r:02x}{g:02x}{b:02x}"


last_x, last_y = 0, 0
s, o, w = 100, 0, 10
field = []
rects = []
theme = Catppuccin()

first_click_registered = False
sizex, sizey = 0, 0
load_nums()
W, H = sizex * s + 2 * o, sizey * s + 2 * o

root = Tk()
c = Canvas(width=W, height=H, bg=theme.bg[2])
c.pack()
c.focus_set()

draw_rows()
vykresli_ciary()

c.bind("<1>", leftclick)
c.bind("<3>", rightclick)


root.mainloop()
