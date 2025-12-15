from tkinter import Tk, Canvas
import random


def update_num():
    font = "arial 20"
    c.delete(f"n{last_y}{last_x}")
    if sudoku[last_y][last_x] < 0:
        c.create_text(
            last_x * s + 0.5 * s,
            last_y * s + 0.5 * s,
            font=font,
            text=abs(sudoku[last_y][last_x]),
            tags=f"n{last_y}{last_x}",
        )
    check()


def draw_sudoku_from_list():
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] > 0:
                font = "arial 20 bold"
                c.create_text(
                    x * s + 0.5 * s, y * s + 0.5 * s, font=font, text=abs(sudoku[y][x])
                )
            elif sudoku[y][x] < 0:
                font = "arial 20"
                c.create_text(
                    x * s + 0.5 * s,
                    y * s + 0.5 * s,
                    font=font,
                    text=abs(sudoku[y][x]),
                    tags=f"n{y}{x}",
                )
    draw_square_lines()
    check()


def draw_square_lines():
    for i in range(1, 9):
        w = 1
        if i % 3 == 0:
            w = 3
        c.create_line((0, i * s, WIDTH, i * s), width=w)
        c.create_line((i * s, 0, i * s, HEIGHT), width=w)


def leftclick(e):
    c.focus_set()
    global last_y, last_x
    x, y = e.x // s, e.y // s
    if sudoku[y][x] <= 0:
        last_x, last_y = x, y
        c.delete("sel")
        c.create_rectangle(
            last_x * s,
            last_y * s,
            last_x * s + s,
            last_y * s + s,
            tags="sel",
            fill="gray",
        )
        c.tag_lower("sel")
    else:
        c.delete("sel")


def keyboard(e):
    num = e.keysym
    if num in "123456789":
        sudoku[last_y][last_x] = (-1) * int(num)
        update_num()


def read_text_file(file_name):
    f = open(file_name)
    for i in range(9):
        sudoku.append(list(map(int, list(f.readline().strip()))))
    f.close()
    randomize_sudoku()


def randomize_sudoku():
    for y in range(9):
        for x in range(9):
            roll = random.randrange(0, 100)
            if roll < difficulty:
                sudoku[y][x] = 0


def check_old():
    for y in sudoku:
        if sum(abs(n) for n in y) != 45:
            return
    for y in range(9):
        if sum(abs(sudoku[y][x]) for x in range(9)) != 45:
            return

    for y0 in range(0, 9, 3):
        for x0 in range(0, 9, 3):
            square_sum = 0
            for y in range(3):
                for x in range(3):
                    square_sum += abs(sudoku[y + y0][x + x0])

            if square_sum != 45:
                return

    c.delete("all")
    c.create_text(
        WIDTH // 2, HEIGHT // 2, text="YOU WIN!", font="arial 60 bold", fill="green"
    )

    # //TODO nefunguje


def check():  # v skutocnosti nefunkcny (neviem preco) ale hra funguje
    for j in range(9):
        print(set(list(abs(sudoku[n][j]) for n in range(9))))
        if not set(sudoku[j]) == set(range(1, 10)):
            return

        if not set(list(abs(sudoku[n][j]) for n in range(9))) == set(range(1, 10)):
            return

    c.delete("all")
    c.create_text(
        WIDTH // 2, HEIGHT // 2, text="YOU WIN!", font="arial 60 bold", fill="green"
    )


last_x, last_y = None, None
difficulty = 5  # 0 - ~50
s = 100
sudoku = []
WIDTH, HEIGHT = s * 9, s * 9
root = Tk()
root.title("Sudoku")
c = Canvas(width=WIDTH, height=HEIGHT)
c.pack()
c.bind("<1>", leftclick)
c.bind("<Key>", keyboard)  #!!!!!

read_text_file("sudoku.txt")
draw_sudoku_from_list()


root.mainloop()
