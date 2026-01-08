from tkinter import Canvas, Tk
import random, time


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
    n = 0
    for y in range(sizey):
        a = field[y]
        for x in range(sizex):
            if a[x] == ".":
                pass
            else:
                n = int(a[x],16)
            c.create_text(
                x * s + s // 2,
                y * s + s // 2,
                text=n,
                font="Arial 20 bold",
                tags="num",
                fill=theme.fg[0],
            )


def load_nums():
    global sizex, sizey, number_count
    f = open("sik1.txt")
    a = f.readline().strip()
    sizex = len(a)
    while not a == "":
        field.append(a)
        sizey += 1
        a = f.readline().strip()

    for y in range(sizey):
        for x in range(sizex):
            if field[y][x] != ".":
                number_count += 1


def wrong_user_input(ylist,xlist):
    global s, c, w, first_click_registered
    c.create_rectangle(
        (
            xlist[0] * s + w // 2 + 1,
            ylist[0] * s + w // 2 + 1,
            xlist[1] * s + s - w // 2,
            ylist[1] * s + s - w // 2,
        ),
        tags="wrong",
        width=w,
        outline="#880000",
        fill="#AA0000"
    )

    first_click_registered = False
    c.delete("sel")

    c.create_text(W//2,H//2,text="Invalid Move, RTFM", tags="wrongtext", font="arial 60 bold", fill="#FF0000")

    c.update()
    time.sleep(3)
    c.delete("wrong")
    c.delete("wrongtext")
    c.update()


def check_win():
    global number_count, rects
    if number_count == len(rects):
        c.create_text(W//2,H//2,text="YOU WIN!", tags="wintext", font="arial 60 bold", fill="#00FF00")
        c.unbind("<1>")
        c.unbind("<3>")


def leftclick(e):
    global first_click_registered, last_x, last_y, rect_counter, rects
    x = (e.x - o) // s
    y = (e.y - o) // s
    xlist = sorted([x, last_x])
    ylist = sorted([y, last_y])

    if first_click_registered:

        # zistovanie cisel v obdlzniku a zapisanie do 1 stringu
        nums_in_sel = ""
        for y in range(ylist[0],ylist[1]+1):
            for x in range(xlist[0],xlist[1]+1):
                if field[y][x] != ".":
                    nums_in_sel += field[y][x]

        # check overlap
        x0, y0, x1, y1 = xlist[0]*s, ylist[0]*s, xlist[1]*s, ylist[1]*s
        for rect_id in rects:
            rx0, ry0, rx1, ry1 = c.coords(rect_id)

            # x/y 1/0   r x/y 0/1
            if not (x1 <= rx0 or rx1 <= x0 or y1 <= ry0 or ry1 <= y0):
                wrong_user_input(ylist,xlist)
                return

        # privela cisel v selection
        if len(nums_in_sel) != 1:
            c.delete("sel")
            wrong_user_input(ylist,xlist)
            return

        # iba jedno cislo v obdlzniku
        if len(nums_in_sel) == 1 and ((xlist[1]+1-xlist[0])*(ylist[1]+1-ylist[0])) != int(nums_in_sel,16):
            first_click_registered = False
            c.delete("sel")
            wrong_user_input(ylist,xlist)
            return


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

        check_win()
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


number_count = 0
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
