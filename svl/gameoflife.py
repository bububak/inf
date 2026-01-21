from tkinter import Tk, Canvas
import random



class Catppuccin:
    def __init__(self) -> None:
        pass

    bg = [
        "#11111b",
        "#181825",
        "#1e1e2e",
    ]
    surface = [
        "#313244",
        "#45475a",
        "#585b70",
    ]
    overlay = [
        "#6c7086",
        "#7f849c",
        "#9399b2",
    ]
    fg = [
        "#cdd6f4",
        "#bac2de",
        "#a6adc8",
    ]



class Tile:


    def __init__(self,y,x,) -> None:
        self.y = y
        self.x = x
        self.state = False
        self.new = False
        self.rect = c.create_rectangle(x*s+o+1,y*s+o+1,x*s+s-o,y*s+s-o,width=0,fill=tile_colors[0],tags=f"y{y}x{x}")


    def change_state(self):
        self.state = not self.state
        c.itemconfig(self.rect, fill=tile_colors[self.state])


    def logic(self):
        counter = 0
        if self.state:
            counter -= 1

        for y in range(self.y-1,self.y+2):
            for x in range(self.x-1,self.x+2):
                counter += int(field[y][x].state)

        if counter == 0:
            self.new = False
            return

        if self.state: # ak ziju
            if counter < 2:
                self.new = False
            elif counter > 3:
                self.new = False
            else:
                self.new = True

        else: # ak su sede
            if counter == 3:
                self.new = True
            else:
                self.new = False


    def update_rect(self):
        self.state = self.new
        c.itemconfig(self.rect, fill=tile_colors[self.state])



def leftclick(e):
    x = e.x//s
    y = e.y//s
    if 0 <= x < sizex*s and 0 <= y < sizey*s:
        field[y][x].change_state()


def draw_outlines():
    for i in range(sizex):
        c.create_line(0,i*s,WIDTH,i*s,fill=outline_colors[0],tags="line")
        c.create_line(i*s,0,i*s,HEIGHT,fill=outline_colors[0],tags="line")


def generate_field():
    f = []
    l = []
    for y in range(sizey+1):
        for x in range(sizex+1):
            l.append(Tile(y,x))
        f.append(l.copy())
        l = []
    return f.copy()


def toggle_running(e):
    global run
    run = not run
    c.itemconfig("line",fill=outline_colors[int(run)])
    if run:
        iterate_turn()


def iterate_turn():
    if run:
        c.after(turn_delay, iterate_turn)
    if run:
        for y in range(sizey):
            for x in range(sizex):
                field[y][x].logic()

        for y in range(sizey):
            for x in range(sizex):
                if field[y][x].state != field[y][x].new:
                    field[y][x].update_rect()


def keyboard_input(e):
    global turn_delay
    if e.char.isnumeric():
        n = int(e.char)
        if n == 0:
            n = 10
        turn_delay = 50*n


def randomize_field(e):
    for y in range(sizey):
        for x in range(sizex):
            if random.randrange(0,100) < chance:
                field[y][x].new = True
            else:
                field[y][x].new = False
            field[y][x].update_rect()



# changeable variables
wanted_window_size = 1000
s = 50
tile_color = "#89b4fa"


chance = 30
turn_delay = 500
tile_count = wanted_window_size//s
sizex, sizey = tile_count, tile_count
WIDTH, HEIGHT = sizex*s, sizey * s
run = False
o = 1

theme = Catppuccin()
root = Tk()
c = Canvas(bg=theme.bg[2],width=WIDTH,height=HEIGHT)
c.pack()
tile_colors = [theme.bg[2],tile_color]
field = generate_field()
outline_colors = [theme.surface[2],theme.surface[0]]

c.focus_set()
# neviem ako implementovat motion, musel by som dat key up key down eventy dva
# c.bind("<B1-Motion>",leftclick)
c.bind("<1>", leftclick)
c.bind("<space>", toggle_running)
c.bind("<Key>", keyboard_input)
c.bind("r",randomize_field)
draw_outlines()



root.mainloop()
