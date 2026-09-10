import random
import tkinter as tk


def vypis_poradie():
    c.delete("all")
    for i, num in enumerate(poradie):
        _ = c.create_text(SQUARE_SIZE * i + SQUARE_SIZE // 2, SQUARE_SIZE // 2, text=str(num), font=("Arial", 16), fill=colors["text"])
    c.update()


def check_sorted():
    p = poradie.copy()
    if p[0] != "_" and p[-1] != "_":
        return False
    p.remove("_")
    return p == sorted(p)


def is_valid_input(num: str):
    if not num.isnumeric():
        # print("input musi byt cislo")
        # vypis_error("input musi byt cislo")
        return False
    if int(num) > LIST_LENGTH or int(num) < 1:
        vypis_error(f"input musi byt v rozsahu 1 - {LIST_LENGTH}")
        return False
    if abs(poradie.index("_") - poradie.index(int(num))) > EXCHANGE_RADIUS:
        vypis_error("zadane cislo je pridaleko od _")
        return False
    return True


def get_user_input(e) -> None:
    global turn_counter
    x = e.x // SQUARE_SIZE

    if x < 0 or x > LIST_LENGTH:
        return

    clear_label()
    n = poradie[x]
    if not is_valid_input(str(n)):
        return

    pos1 = x
    pos2 = poradie.index("_")
    poradie[pos1], poradie[pos2] = poradie[pos2], poradie[pos1]

    vypis_poradie()
    turn_counter += 1

    if check_sorted():
        feedback_label.config(text=f"Vyhral si na {turn_counter} tahov!", font=("Arial", LABEL_FONT_SIZE, "bold"), fg=colors["green"])
        c.unbind("<1>")


def vypis_error(message: str):
    feedback_label.config(text=message, fg=colors["red"])


def clear_label():
    feedback_label.config(text="")


colors = {"text":"#cdd6f4", "bg":"#1e1e2e","red":"#f38ba8", "green":"#a6e3a1", "blue":"#89b4fa"}

LIST_LENGTH = 6
EXCHANGE_RADIUS = 2
turn_counter = 0
poradie = [n + 1 for n in range(LIST_LENGTH)] + ["_"]
while check_sorted():
    random.shuffle(poradie)

SQUARE_SIZE = 100
LABEL_FONT_SIZE = 20
root = tk.Tk()
root.configure(bg=colors["bg"])
feedback_label = tk.Label(root, text=f"Zorad cisla 1-{LIST_LENGTH} vymienanim s \"_\"", font=("Arial", LABEL_FONT_SIZE, "bold"),fg=colors["blue"], bg=colors["bg"])
feedback_label.pack(padx=10, pady=10)
c = tk.Canvas(root, width=SQUARE_SIZE * LIST_LENGTH + SQUARE_SIZE, height=SQUARE_SIZE, bg=colors["bg"], highlightthickness=0)
c.pack()



vypis_poradie()
_ = c.bind("<1>", get_user_input)
c.mainloop()
