import tkinter



def kresli():
    for riadok in range(HEIGHT):
        for stlpec in range(WIDTH):
            r,g,b = obr.get(stlpec,riadok)
 

            r, g, b = ff-r, ff-g, ff-b


            obr.put('#{:02x}{:02x}{:02x}'.format(r, g, b),(stlpec,riadok))
        c.update()



while True:
    FILE = input("Enter file name without extension:\n") + ".png"
    try:
        with open(FILE) as f:
            pass
        break
    except:
        print("File not found. ", end="")

c = tkinter.Canvas(width=1, height=1, bg='white')
obr = tkinter.PhotoImage(file=FILE)
WIDTH, HEIGHT = obr.width(), obr.height()
ff = 255
c["width"], c["height"] = WIDTH, HEIGHT
c.grid(column=0,row=0)
c.create_image(1, 1, image=obr, anchor='nw')
button = tkinter.Button(text="Go", command=kresli).grid(column=0,row=1,sticky="NEWS")



tkinter.mainloop()
