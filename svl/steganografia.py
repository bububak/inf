import tkinter


def dekoduj():
    for y in range(vyska):
        for x in range(sirka):
            if zakodovany.get(x, y)[2] % 2 == 1:
                sprava.put("#000000", (x, y))
            else:
                sprava.put("#FFFFFF", (x, y))
    c.create_image(sirka, 0, anchor="nw", image=sprava)


def enkoduj():
    novy = tkinter.PhotoImage(width=sirka, height=vyska)
    nezakodovany = tkinter.PhotoImage(file="zakodovanygjhnew.png")
    kod = tkinter.PhotoImage(file="template.png")
    for y in range(vyska):
        for x in range(sirka):
            if kod.get(x, y) == (00, 00, 00):
                if nezakodovany.get(x, y)[2] % 2 == 0:  # parne
                    novy.put(
                        f"#{nezakodovany.get(x, y)[0]:02x}{nezakodovany.get(x, y)[1]:02x}{((nezakodovany.get(x, y)[2] + 1) % 256):02x}",
                        (x, y),
                    )
            else:
                if nezakodovany.get(x, y)[2] % 2 == 1:  # neparne
                    novy.put(
                        f"#{nezakodovany.get(x, y)[0]:02x}{nezakodovany.get(x, y)[1]:02x}{((nezakodovany.get(x, y)[2] + 1) % 256):02x}",
                        (x, y),
                    )

    novy.write("sifra.png")


tkinter.Button(text="Dekoduj", command=dekoduj).pack(side="left")
tkinter.Button(text="Enkoduj", command=enkoduj).pack(side="left")
c = tkinter.Canvas(bg="white")
c.pack(side="left")

zakodovany = tkinter.PhotoImage(file="zakodovanygjh.png")
sirka, vyska = zakodovany.width(), zakodovany.height()
print(sirka, vyska)
c["width"], c["height"] = sirka * 2, vyska

sprava = tkinter.PhotoImage(width=sirka, height=vyska)


tkinter.mainloop()
