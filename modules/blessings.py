def set_char(x,y,character):
    print(f"\x1b[{y+1};{x+1}f{character}")


def clear_screen():
    print("\x1b[2J")


def hide_cursor():
    print("\x1b[?25l")
