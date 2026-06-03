import curses
from time import sleep


class Ray:
    def __init__(self, x, y, dir) -> None:
        self.x = x
        self.y = y
        self.dir = dir

    def tick(self):
        global field

        # move 1 space
        self.x, self.y = self.x + self.dir[0], self.y + self.dir[1]

        # delete and return if out of bounds
        if (
            self.x == -1
            or self.x == len(field[0])
            or self.y == -1
            or self.y == len(field)
        ):
            rays.pop()
            return

        # direction change on special tiles
        space = field[self.y][self.x]
        if space in "|-":  # splitter
            pass
        if space in "\\/":
            self.dir = directions[space][directions[space].index(self.dir) - 2]


# directions as (x,y)
UP, DOWN, RIGHT, LEFT = (0, -1), (0, 1), (1, 0), (-1, 0)
directions = {"/": (UP, DOWN, RIGHT, LEFT), "\\": (UP, DOWN, LEFT, RIGHT)}
rays = [
    Ray(0, 0, RIGHT),
]

# load file into field
with open("zrkadla-nosplit.txt", "r") as f:
    field = f.read().split("\n")
visited = [[[0, 0] for x in range(len(field[0]))] for y in range(len(field))]
print(visited)


# mainloop
while rays:
    rays[-1].tick()
    sleep(0.01)


# count visited
print("finishd")
