import random
import tkinter as tk


def first_draw():
    pictures = {}
    for i,n in enumerate(frog_order):
        current_image = tk.PhotoImage(file=f"zabka{n}.png")
        pictures[n] = current_image
        canvas_items[n] = c.create_image(SQUARE_SIZE * i + SQUARE_SIZE // 2, SQUARE_SIZE // 2, image=current_image)
    c.update()
    return pictures

def check_sorted():
    p = frog_order.copy()
    if p[0] != "_" and p[-1] != "_":
        return False
    p.remove("_")
    return p == sorted(p)


def is_valid_input(num: str):
    if not num.isnumeric():
        show_error("input musi byt cislo")
        return False
    if int(num) > LIST_LENGTH or int(num) < 1:
        show_error(f"input musi byt v rozsahu 1 - {LIST_LENGTH}")
        return False
    if abs(frog_order.index("_") - frog_order.index(int(num))) > EXCHANGE_RADIUS:
        show_error("zadane cislo je pridaleko od _")
        return False
    return True


def get_user_input(e) -> None:
    global turn_counter
    x = e.x // SQUARE_SIZE

    if x < 0 or x > LIST_LENGTH:
        return

    clear_label()
    n = frog_order[x]
    if not is_valid_input(str(n)):
        return

    swap_canvas_items(x, frog_order.index("_"))
    turn_counter += 1

    if check_sorted():
        feedback_label.config(text=f"Vyhral si na {turn_counter} tahov!", font=("Arial", LABEL_FONT_SIZE, "bold"), fg=colors["green"])
        c.unbind("<1>")


def swap_canvas_items(pos1, pos2):
    a = frog_order[pos1]
    b = frog_order[pos2]
    frog_order[pos1], frog_order[pos2] = b, a
    c.itemconfig(canvas_items[a], image=pictures[b])
    c.itemconfig(canvas_items[b], image=pictures[a])
    canvas_items[a], canvas_items[b] = canvas_items[b], canvas_items[a]
    c.update()


def show_error(message: str):
    feedback_label.config(text=message, fg=colors["red"])


def clear_label():
    feedback_label.config(text="")


colors = {"text":"#cdd6f4", "bg":"#1e1e2e","red":"#f38ba8", "green":"#a6e3a1", "blue":"#89b4fa"}

LIST_LENGTH = 6
EXCHANGE_RADIUS = 2
canvas_items = {}
turn_counter = 0
frog_order = [n + 1 for n in range(LIST_LENGTH)] + ["_"]
while check_sorted():
    random.shuffle(frog_order)

SQUARE_SIZE = 230
LABEL_FONT_SIZE = 20
root = tk.Tk()
root.configure(bg=colors["bg"])
feedback_label = tk.Label(root, text=f"Zorad cisla 1-{LIST_LENGTH} vymienanim s \"_\"", font=("Arial", LABEL_FONT_SIZE, "bold"),fg=colors["blue"], bg=colors["bg"])
feedback_label.pack(padx=10, pady=10)
c = tk.Canvas(root, width=SQUARE_SIZE * LIST_LENGTH + SQUARE_SIZE, height=SQUARE_SIZE, bg=colors["bg"], highlightthickness=0)
c.pack()



pictures = first_draw()
_ = c.bind("<1>", get_user_input)
c.mainloop()
