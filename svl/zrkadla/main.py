import curses
from time import sleep


class Ray:
    def __init__(self, x, y, dir) -> None:
        self.x = x
        self.y = y
        self.dir = dir

    def tick(self, stdscr):
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
            rays.remove(self)
            return

        # delete self if space traversed
        space = field[self.y][self.x]
        if (
            ((self.dir == RIGHT or self.dir == LEFT) and visited[self.y][self.x][0])
            or ((self.dir == UP or self.dir == DOWN) and visited[self.y][self.x][1])
        ) and not (space == "\\" or space == "/"):
            rays.remove(self)
            return

        # add coordinate to visited after moving - does not write outside play area because self deleting is before
        visited[self.y][self.x][0 if (self.dir == RIGHT or self.dir == LEFT) else 1] = (
            True
        )

        # direction change on special tiles
        # splitter:
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

        if SHOULD_ANIMATE:
            stdscr.addch(self.y, self.x, space)


def draw_mirrors_before(stdscr):
    for y in range(len(field)):
        for x in range(len(field[0])):
            print(field[y][x])
            stdscr.addch(y, x, field[y][x] if field[y][x] in "\\/-|" else " ")
    stdscr.refresh()


# mainloop
def mainloop(stdscr):
    if SHOULD_ANIMATE:
        curses.use_default_colors()

        draw_mirrors_before(stdscr)

    while len(rays) > 0:
        match SEARCH_TYPE:
            case "bfs":
                for ray in rays:
                    ray.tick(stdscr)
            case "first":
                rays[0].tick(stdscr)
            case "last":
                rays[-1].tick(stdscr)

        if SHOULD_ANIMATE:
            stdscr.refresh()
            sleep(DELAY)


# load file into field
with open("zrkadlaXXL.txt", "r") as f:
    field = f.read().splitlines()

# visited: mapa with [T/F, T/F] in order of "visited horizontally", "visited vertically"
visited = [[[False, False] for x in range(len(field[0]))] for y in range(len(field))]

# directions as (x,y)
UP, DOWN, RIGHT, LEFT = (0, -1), (0, 1), (1, 0), (-1, 0)
directions = {"/": (UP, DOWN, RIGHT, LEFT), "\\": (UP, DOWN, LEFT, RIGHT)}

# sets first ray to outside top left
rays = [
    Ray(-1, 0, RIGHT),
]


# code to execute
SHOULD_ANIMATE = True
SEARCH_TYPE = "last"

DELAY = 0.01
if SHOULD_ANIMATE:
    curses.wrapper(mainloop)
else:
    mainloop("")
print("finished")


# count visited
n = 0
for row in range(len(visited)):
    for column in range(len(visited[0])):
        if True in visited[row][column]:
            n += 1
print(f"visited {n} squares")
