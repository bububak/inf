import random


def print_frogs():
    print(f"T{turn_counter}    ", end="")
    for num in frog_order:
        print(num, end=" ")
    print()


def check_sorted():
    p = frog_order.copy()
    if p[0] != "_" or p[-1] == "_":
        return False
    p.remove("_")
    return p == sorted(p)


def is_valid_input(num: str):
    if not num.isnumeric():
        print("input musi byt cislo")
        return False
    if int(num) > LIST_LENGTH or int(num) < 1:
        print(f"input musi byt v rozsahu 1 - {LIST_LENGTH}")
        return False
    if abs(frog_order.index("_") - frog_order.index(int(num))) > EXCHANGE_RADIUS:
        print("zadane cislo je pridaleko od _")
        return False
    return True


def get_user_input():
    print_frogs()
    user_input = input("ktore cislo vymenit s _?\n > ")
    print()
    return user_input


LIST_LENGTH = 6
EXCHANGE_RADIUS = 2
turn_counter = 0
frog_order = [n + 1 for n in range(LIST_LENGTH)] + ["_"]
while check_sorted():
    random.shuffle(frog_order)


while not check_sorted():
    turn_counter += 1

    user_input = get_user_input()
    while not is_valid_input(user_input):
        user_input = get_user_input()

    pos1 = frog_order.index(int(user_input))
    pos2 = frog_order.index("_")
    frog_order[pos1], frog_order[pos2] = frog_order[pos2], frog_order[pos1]

print(f"Vyhral si na {turn_counter} tahov!")
