from tkinter import Tk, Canvas
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


def load_field():
    global sizex, sizey
    f = open(f"0{file_id}.txt")
    field = []

    a = f.readline().strip().split()
    sizey, sizex = int(a[0]), int(a[1])

    a = f.readline().strip()
    for i in range(sizey):
        field.append(a)
        a = f.readline().strip()
    return field


def vykresli_ciary():
    for y in range(1, sizey):
        c.create_line(0, y * s, W, y * s, tags="liney", fill=theme.surface[2])
    for x in range(1, sizex):
        c.create_line(x * s, 0, x * s, H, tags="linex", fill=theme.surface[2])


def draw_rows():
    global font_size
    global sizex, sizey, c, nums
    for y in range(sizey):
        a = nums[y]
        for x in range(sizex):
            c.create_text(
                x * s + s // 2,
                y * s + s // 2,
                text=a[x : x + 1],
                font=f"Arial {font_size} bold",
                tags="num",
                fill=theme.fg[0] if nums[y][x] != "#" else "#ffaaaa",
            )


def find_k():
    for y in range(sizey):
        for x in range(sizex):
            if nums[y][x] == "K":
                q.append([y + 1, x + 1])

    for i in range(len(q)):
        field[q[i][0]][q[i][1]] = loopid


def pastel_color():
    r = random.randint(128, 255)
    g = random.randint(128, 255)
    b = random.randint(128, 255)
    return f"#{r:02x}{g:02x}{b:02x}"


def single_loop():
    global loopid, color
    loopid += 1
    color = pastel_color()

    for r in q.copy():
        draw_rect_with_field_coords(r[0], r[1])
        q.pop(0)

    d = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    for y in range(1, sizey + 1):
        for x in range(1, sizex + 1):
            if nums[y - 1][x - 1] != "#" and field[y][x] == loopid - 1:
                for i in range(len(d)):
                    if field[y + d[i][0]][x + d[i][1]] == 0:
                        field[y + d[i][0]][x + d[i][1]] = loopid
                        q.append([y + d[i][0], x + d[i][1]])
    if not len(q) == 0:
        c.after(speed, single_loop)
    else:
        return


def draw_rect_with_field_coords(y, x):
    global color
    c.create_rectangle(
        x * s - s + 2, y * s - s + 2, x * s - 1, y * s - 1, fill=color, width=0
    )


# SETTABLE VARIABLES
file_id = 6  # 10 nefunguje lebo neviem ako dat 0 pred to efektivne
s = 10
speed = 100  # ms

color = pastel_color()
sizex = 0
sizey = 0
loopid = 1
font_size = s // 2
nums = load_field()
field = [[0 for n in range(sizex + 2)] for n in range(sizey + 2)]
q = []
W, H = sizex * s, sizey * s
theme = Catppuccin()

find_k()

root = Tk()
c = Canvas(width=W, height=H, bg=theme.bg[2])
c.pack()
c.focus_set()
vykresli_ciary()
draw_rows()

single_loop()

root.mainloop()
