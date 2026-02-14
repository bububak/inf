class Tile():

    character_dict = {
        ".":"blank",
        "~":"water"
    }

    def __init__(self,x,y,c) -> None:
        self.x = x
        self.y = y
        self.c = c



class Bot():
    def __init__(self) -> None:
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
        print(self.x_values,self.y_values)

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

        for y in range(len(self.field)):
            for x in range(len(self.field[y])):
                self.field[y][x] = Tile(x,y,self.field[y][x])

    def draw_field(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                print(self.field[y][x].c,end="")
            print()



game = Game()
game.draw_field()
