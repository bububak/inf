import tkinter as tk

# ((S+1)%2+1) returns 2 if even, 1 if odd
# ((S+1)%2) returns 1 if even, 0 if odd

S = 3
D = 6
SIZE = 1000
WIDTH = (S - 1) * SIZE + 1
HALF = WIDTH // 2
HEIGHT = SIZE + 1

prev = (S - 1) * [0] + [1] + [0] * (S - 1)
new = []
turns = 0
c = tk.Canvas(width=WIDTH, height=HEIGHT, bg="black", highlightthickness=0)
c.pack()


c.create_rectangle(HALF, 0, HALF + 1, 1, fill="white", width=0)

while turns < SIZE:
    turns += 1

    # figure out next line
    new = []
    for i in range(len(prev) - (S - 1)):
        temp_sum = 0
        for j in range(S):
            temp_sum += prev[i + j]
        new.append(temp_sum)

    prev = (S - 1) * [0] + new + [0] * (S - 1)

    # draw the new line
    left = HALF - (len(new) - 1) // 2

    for i, n in enumerate(new):
        if n % D != 0:

            c.create_rectangle(
                left + i,
                turns,
                left + i + 1,
                turns + 1,
                fill="white",
                width=0,
            )
    c.update()


c.mainloop()
