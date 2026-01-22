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
        self.rect = game.c.create_rectangle(x*game.s+game.o+1,y*game.s+game.o+1,x*game.s+game.s-game.o,y*game.s+game.s-game.o,width=0,fill=game.tile_colors[0],tags=f"y{y}x{x}")


    def change_state(self):
        self.state = not self.state
        game.c.itemconfig(self.rect, fill=game.tile_colors[self.state])


    def logic(self):
        counter = 0
        if self.state:
            counter -= 1

        for y in range(self.y-1,self.y+2):
            for x in range(self.x-1,self.x+2):
                counter += int(game.field[y][x].state)

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
        game.c.itemconfig(self.rect, fill=game.tile_colors[self.state])



class Game():

    def __init__(self) -> None:
        pass


    def intro_window(self):
        self.wanted_window_size = 1000
        self.s = 50
        self.tile_color = "#89b4fa"

        self.chance = 50
        self.turn_delay = 500
        self.tile_count = self.wanted_window_size//self.s
        self.sizex, self.sizey = self.tile_count, self.tile_count
        self.WIDTH, self.HEIGHT = self.sizex*self.s, self.sizey * self.s
        self.run = False
        self.o = 1

        self.tile_colors = [theme.bg[2],self.tile_color]
        self.outline_colors = [theme.surface[2],theme.surface[0]]

        self.draw_canvas_from_parameters()


    def draw_canvas_from_parameters(self):
        self.root = Tk()
        self.c = Canvas(bg=theme.bg[2],width=self.WIDTH,height=self.HEIGHT)
        self.c.pack()
        self.field = self.generate_field()

        self.c.focus_set()
        self.c.bind("<1>", self.leftclick)
        self.c.bind("<space>", self.toggle_running)
        self.c.bind("<Key>", self.keyboard_input)
        self.c.bind("r", self.randomize_field)
        self.draw_outlines()

        self.root.mainloop()

    def leftclick(self, e):
        x = e.x//self.s
        y = e.y//self.s
        if 0 <= x < self.sizex*self.s and 0 <= y < self.sizey*self.s:
            self.field[y][x].change_state()


    def draw_outlines(self):
        for i in range(self.sizex):
            self.c.create_line(0,i*self.s,self.WIDTH,i*self.s,fill=self.outline_colors[0],tags="line")
            self.c.create_line(i*self.s,0,i*self.s,self.HEIGHT,fill=self.outline_colors[0],tags="line")


    def generate_field(self):
        f = []
        l = []
        for y in range(self.sizey+1):
            for x in range(self.sizex+1):
                l.append(Tile(y,x))
            f.append(l.copy())
            l = []
        return f.copy()


    # tuto si skoncil
    def toggle_running(self, e):
        self.run = not self.run
        self.c.itemconfig("line",fill=self.outline_colors[int(self.run)])
        if self.run:
            self.iterate_turn()


    def iterate_turn(self):
        if self.run:
            for y in range(self.sizey):
                for x in range(self.sizex):
                    self.field[y][x].logic()

            for y in range(self.sizey):
                for x in range(self.sizex):
                    if self.field[y][x].state != self.field[y][x].new:
                        self.field[y][x].update_rect()
        if self.run:
            self.c.after(self.turn_delay, self.iterate_turn)


    def keyboard_input(self, e):
        if e.char.isnumeric():
            n = int(e.char)
            if n == 0:
                n = 10
            self.turn_delay = 50*n


    def randomize_field(self, e):
        for y in range(self.sizey):
            for x in range(self.sizex):
                if random.randrange(0,100) < self.chance:
                    self.field[y][x].new = True
                else:
                    self.field[y][x].new = False
                self.field[y][x].update_rect()



theme = Catppuccin()
game = Game()
game.intro_window()
