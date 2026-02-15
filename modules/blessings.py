def set_char(x,y,character):
    print(f"\x1b[{y};{x}f{character}", end="")


def clear():
    print("\x1b[2j", end="")
