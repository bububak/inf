def main_f():
    if r < 5:
        return "Chrrr"

    for y in range(r):
        for x in range(c):

            # check horizont
            if x < (c - len(KUBKO)+1):
                foo = boo = ""
                for i in range(len(KUBKO)):
                    foo += table[y][x+i]
                    boo = table[y][x+i] + boo
                if foo == KUBKO or boo == KUBKO:
                    return "Kubo je bozi!"
                if foo == MARIO or boo == MARIO:
                    return "JezisMario!"

            # check vert
            if y < (r - len(KUBKO)+1):
                foo = boo = ""
                for i in range(len(KUBKO)):
                    foo += table[y+i][x]
                    boo = table[y+i][x] + boo
                    if foo == KUBKO or boo == KUBKO:
                        return "Kubo je bozi!"
                    if foo == MARIO or boo == MARIO:
                        return "JezisMario!"

            # check diagonal top left to bottom right
            if x < (c - len(KUBKO)+1) and y < (r - len(KUBKO)+1):
                foo = boo = ""
                for i in range(len(KUBKO)):
                    foo += table[y+i][x+i]
                    boo = table[y+i][x+i] + boo
                    if foo == KUBKO or boo == KUBKO:
                        return "Kubo je bozi!"
                    if foo == MARIO or boo == MARIO:
                        return "JezisMario!"

                # diagonal top right to bottom left
                foo = boo = ""
                for i in range(len(KUBKO)):
                    foo += table[y+i][x+len(KUBKO)-i-1]
                    boo = table[y+i][x+len(KUBKO)-i-1] + boo
                    if foo == KUBKO or boo == KUBKO:
                        return "Kubo je bozi!"
                    if foo == MARIO or boo == MARIO:
                        return "JezisMario!"
    return "Chrrr"


r, c = list(map(int, input().strip().split()))
KUBKO = "OOOOO"
MARIO = "XXXXX"

table = []
for i in range(r):
    table.append(input())

print(main_f())
