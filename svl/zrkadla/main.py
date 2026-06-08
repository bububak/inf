import curses
from time import sleep


class Ray:
    def __init__(self, x, y, dir) -> None:
        # sets first ray to outside top left
        self.x = x
        self.y = y
        self.dir = dir

    def tick(self):
        global field, visited

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

        # delete self if space traversed
        if ((self.dir == RIGHT or self.dir == LEFT) and visited[self.y][self.x][0]) or (
            (self.dir == UP or self.dir == DOWN) and visited[self.y][self.x][1]
        ):
            rays.pop()
            return

        # add coordinate to visited after moving - does not write outside play area because self deleting is before
        visited[self.y][self.x][0 if (self.dir == RIGHT or self.dir == LEFT) else 1] = (
            True
        )
        print(self.x, self.y, field[self.y][self.x], self.dir, self)

        # direction change on special tiles
        # splitter:
        space = field[self.y][self.x]
        if (space == "|" and (self.dir == RIGHT or self.dir == LEFT)) or (
            space == "-" and (self.dir == UP or self.dir == DOWN)
        ):
            rays.append(
                Ray(
                    self.x,
                    self.y,
                    directions["\\"][directions["\\"].index(self.dir) - 2],
                )
            )
            self.dir = directions["/"][directions["/"].index(self.dir) - 2]

        # corner
        elif space in "\\/":
            self.dir = directions[space][directions[space].index(self.dir) - 2]


# mainloop
def mainloop(stdscr):
    while len(rays) > 0:
        rays[-1].tick()
        sleep(0.01)


# load file into field
with open("zrkadla-custom.txt", "r") as f:
    field = f.read().split("\n")
    field.pop()
# visited: mapa with [T/F, T/F] in order of "visited horizontally", "visited vertically"
visited = [[[False, False] for x in range(len(field[0]))] for y in range(len(field))]

# directions as (x,y)
UP, DOWN, RIGHT, LEFT = (0, -1), (0, 1), (1, 0), (-1, 0)
directions = {"/": (UP, DOWN, RIGHT, LEFT), "\\": (UP, DOWN, LEFT, RIGHT)}
rays = [
    Ray(-1, 0, RIGHT),
]


# code to execute
SHOULD_ANIMATE = False
if SHOULD_ANIMATE:
    curses.wrapper(mainloop)
else:
    mainloop("a")
print("finished")


# count visited
n = 0
for row in range(len(visited)):
    for column in range(len(visited[0])):
        if True in visited[row][column]:
            n += 1
print(f"visited {n} squares")
