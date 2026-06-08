import curses
from time import sleep


class Ray:
    def __init__(self, x, y, dir) -> None:
        self.x = x
        self.y = y
        self.dir = dir

    def tick(self):
        global field, visited

        # add coordinate to visited before moving - does not write outside play area
        visited[self.y][self.x][0 if (self.dir == RIGHT or self.dir == LEFT) else 1] = (
            True
        )

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
            self.dir = directions["/"][directions["/"].index(self.dir) - 2]
            rays.append(
                Ray(
                    self.x,
                    self.y,
                    directions["\\"][directions["\\"].index(self.dir) - 2],
                )
            )

        if space in "\\/":
            self.dir = directions[space][directions[space].index(self.dir) - 2]


# mainloop
def mainloop(stdscr):
    while rays:
        rays[-1].tick()
        sleep(0.01)


# directions as (x,y)
UP, DOWN, RIGHT, LEFT = (0, -1), (0, 1), (1, 0), (-1, 0)
directions = {"/": (UP, DOWN, RIGHT, LEFT), "\\": (UP, DOWN, LEFT, RIGHT)}
rays = [
    Ray(0, 0, RIGHT),
]

# load file into field
with open("zrkadla-nosplit.txt", "r") as f:
    field = f.read().split("\n")
# visited: mapa s [T/F, T/F] na kazdom mieste v poradi "navstivene horizontalne", "navstivene vertikalne"
visited = [[[False, False] for x in range(len(field[0]))] for y in range(len(field))]


# code to execute
curses.wrapper(mainloop)
print("finished")

n = 0
for row in range(len(visited)):
    for column in range(len(visited[0])):
        if True in visited[row][column]:
            n += 1
print(f"visited {n} squares")
