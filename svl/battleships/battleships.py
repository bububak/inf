from blessings import set_char, clear_screen, hide_cursor


class Tile():

    character_dict = {
        ".":"blank",
        "~":"water",
        "<":"left",
        ">":"right",
        "A":"up",
        "V":"down",
        "#":"full",
        "o":"circle",
        "?":"ship"
    }

    def __init__(self,x,y,c) -> None:
        self.x = x
        self.y = y
        self.c = c



class Bot():
    def __init__(self) -> None:
        self.should_run = True


    def start_logic(self):
        while self.should_run:
            pass



class Game():
    def __init__(self) -> None:
        self.load_file()


    def load_file(self):
        file_id = 1
        f = open(f"battle{file_id}.txt")

        self.x_values = f.readline().strip().split()
        self.y_values = f.readline().strip().split()
        self.size_x = len(self.x_values)
        self.size_y = len(self.y_values)

        self.field = []
        temp_line = []
        for j in range(self.size_y):
            line = f.readline().strip()
            for i in range(self.size_x):
                temp_line.append(line[i])
            temp_line.append(".")
            self.field.append(temp_line.copy())
            temp_line = []
        self.field.append(["." for n in range(self.size_x+1)])
        f.close()

        for y in range(len(self.field)):
            for x in range(len(self.field[y])):
                self.field[y][x] = Tile(x,y,self.field[y][x])


    def draw_field(self):
        clear_screen()
        first_row = " |"
        second_row = "-+"
        for i in self.x_values:
            first_row += i
            second_row += "-"
        set_char(0,0,first_row)
        set_char(0,1,second_row)
        for i in range(len(self.y_values)):
            current_row = f"{self.y_values[i]}|"
            for j in range(len(self.x_values)):
                current_row += self.field[i][j].c
            set_char(0,i+2,current_row)
        hide_cursor()



game = Game()
bot = Bot()
game.draw_field()
bot.start_logic()
