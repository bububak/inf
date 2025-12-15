import tkinter


def dekoduj():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if insecret.get(x, y)[2] % 2 == 1:  # 1 = cierna
                outsecret.put("#000000", (x, y))
            else:
                outsecret.put("#FFFFFF", (x, y))
    c.create_image(0, 0, anchor="nw", image=outsecret)


def change_pixel(x, y):
    global inkod, kod, outkod
    original_color = inkod.get(x, y)[2]
    original_is_black = bool(original_color % 2)

    change_variable = 1
    if original_color == 255:
        change_variable = -1

    pixel_should_change = False
    if y < kod.height() and x < kod.width():
        pixel_should_change = True

    cypher_is_black = False
    if pixel_should_change:
        if kod.get(x, y)[2] == 0:
            cypher_is_black = True

    if pixel_should_change:
        if cypher_is_black:
            if original_is_black:
                outkod.put(
                    f"#{inkod.get(x, y)[0]:02x}{inkod.get(x, y)[1]:02x}{inkod.get(x, y)[2]:02x}",
                    (x, y),
                )
            else:
                outkod.put(
                    f"#{inkod.get(x, y)[0]:02x}{inkod.get(x, y)[1]:02x}{(inkod.get(x, y)[2] + change_variable):02x}",
                    (x, y),
                )
        else:  # cypher je biely
            if original_is_black:
                outkod.put(
                    f"#{inkod.get(x, y)[0]:02x}{inkod.get(x, y)[1]:02x}{(inkod.get(x, y)[2] + change_variable):02x}",
                    (x, y),
                )
            else:
                outkod.put(
                    f"#{inkod.get(x, y)[0]:02x}{inkod.get(x, y)[1]:02x}{inkod.get(x, y)[2]:02x}",
                    (x, y),
                )
    else:
        outkod.put(
            f"#{inkod.get(x, y)[0]:02x}{inkod.get(x, y)[1]:02x}{inkod.get(x, y)[2]:02x}",
            (x, y),
        )


def enkoduj():
    for y in range(secret_height):
        for x in range(secret_width):
            change_pixel(x, y)
    outkod.write("output.png")


root = tkinter.Tk()
WIDTH, HEIGHT = 1000, 1000

tkinter.Button(text="Dekoduj", command=dekoduj).pack(side="bottom")
tkinter.Button(text="Enkoduj", command=enkoduj).pack(side="bottom")
c = tkinter.Canvas(bg="white")
c["width"], c["height"] = WIDTH, HEIGHT
c.pack(side="left")

try:
    insecret = tkinter.PhotoImage(file=input("png to decode (secret.png): "))
    WIDTH, HEIGHT = insecret.width(), insecret.height()
    outkod = tkinter.PhotoImage(width=WIDTH, height=HEIGHT)
    inkod = tkinter.PhotoImage(file=input("original file (input.png): "))
    kod = tkinter.PhotoImage(file=input("secret message file (cypher.png): "))
    secret_height, secret_width = inkod.height(), inkod.width()
    outsecret = tkinter.PhotoImage(width=WIDTH, height=HEIGHT)
except IOError as e:
    print(e)

c["width"], c["height"] = WIDTH, HEIGHT
c.update()


tkinter.mainloop()
