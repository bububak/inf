import tkinter as tk


def main_generation():
    S = int(s_entry.get())
    D = int(d_entry.get())
    WIDTH = (S - 1) * SIZE + 1
    HALF = WIDTH // 2
    HEIGHT = SIZE + 1
    c.config(width=WIDTH,height=HEIGHT)
    c.delete("all")
    c.update()
    prev = (S - 1) * [0] + [1] + [0] * (S - 1)
    turns = 0
    c.create_rectangle(HALF, 0, HALF + 1, 1, fill="white", width=0)
    while turns < SIZE:
        turns += 1

        new = []
        for i in range(len(prev) - (S - 1)):
            temp_sum = 0
            for j in range(S):
                temp_sum += prev[i + j]
            new.append(temp_sum)
        prev = (S - 1) * [0] + new + [0] * (S - 1)

        left = HALF - (S - 1) * turns // 2
        for i, n in enumerate(new):
            if n % D != 0:
                c.create_rectangle(
                    left + i - 1,
                    turns,
                    left + i,
                    turns + 1,
                    fill="white",
                    width=0,
                )
        c.update()


SIZE = 500
root = tk.Tk()
c = tk.Canvas(root, width=501, height=501, bg="black", highlightthickness=0)
c.grid(row=0, column=0, columnspan=3)
s_entry = tk.Entry(root, width=5, font="arial 20")
s_entry.grid(row=1, column=0)
d_entry = tk.Entry(root, width=5, font="arial 20")
d_entry.grid(row=1, column=2, pady=10)
main_button = tk.Button(text="Generate", command=main_generation, font="Arial 30 bold")
main_button.grid(row=1, column=1, columnspan=1, pady=10)



c.mainloop()
