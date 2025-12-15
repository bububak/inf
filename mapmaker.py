from tkinter import Canvas, Tk


def keyboard(e):
    key = e.keysym
    match key:
        case "s":
            save()
        case "l":
            load()


def save():
    f = open("map.txt", "w")
    print("saving...")
    for j in range(size):
        for i in range(size):
            f.write(f"{field[j][i]} ")
        f.write("\n")
    f.close()


def load():
    global field, counter
    field = []
    f = open("map.txt")
    print("loading...")

    a = list(map(int, f.readline().strip().split()))
    counter = 0
    while a != []:
        field.append(a)
        a = list(map(int, f.readline().strip().split()))
        counter += 1

    if counter != size:
        print(
            "WARNING: incompatible file size, could lead to data loss (close and adjust size variable)"
        )

    if counter < size:
        diff = size - counter
        # add white spaces to fill in gaps
        for j in range(counter):
            for i in range(diff):
                field[j].append(-1)
        for j in range(diff):
            field.append(list(-1 for i in range(size)).copy())

    vykresli_stvorce([0, size], [0, size])


def vykresli_ciary():
    for y in range(1, size):
        c.create_line(0, y * s, W, y * s)
    for x in range(1, size):
        c.create_line(x * s, 0, x * s, H)


def vykresli_stvorce(xlist, ylist):
    for j in range(size):
        for i in range(size):
            if j >= ylist[0] and j <= ylist[1] and i >= xlist[0] and i <= xlist[1]:
                if field[j][i] == 1:
                    c.create_rectangle(
                        (i * s + o, j * s + o, i * s + s + o, j * s + s + o),
                        fill="black",
                        tags=f"a{j}{i}",
                        outline="white",
                    )
                else:
                    c.delete(f"a{j}{i}")


def rightclick(e):
    global first_click_registered
    first_click_registered = False
    c.delete("sel")


def leftclick(e):
    global first_click_registered, last_x, last_y
    x = (e.x - o) // s
    y = (e.y - o) // s
    xlist = sorted([x, last_x])
    ylist = sorted([y, last_y])
    if first_click_registered:
        for j in range(size):
            for i in range(size):
                if j >= ylist[0] and j <= ylist[1] and i >= xlist[0] and i <= xlist[1]:
                    field[j][i] *= -1

        vykresli_stvorce(xlist, ylist)
        first_click_registered = False
        c.delete("sel")
    else:
        first_click_registered = True
        last_x, last_y = x, y
        c.create_rectangle(
            x * s + o, y * s + o, x * s + s + o, y * s + s + o, tags="sel", fill="gray"
        )


last_x, last_y = 0, 0
s, o = 150, 0

i = input("input field size: ")
while not i.isnumeric():
    i = input("input NUMERIC field size: ")
size = int(i)

W, H = size * s + 2 * o, size * s + 2 * o
counter = 0
first_click_registered = False
field = [[-1 for n in range(size)] for n in range(size)]

root = Tk()
c = Canvas(width=W, height=H)
c.pack()
c.focus_set()

vykresli_ciary()

c.bind("<1>", leftclick)
c.bind("<3>", rightclick)
c.bind("<Key>", keyboard)


root.mainloop()
