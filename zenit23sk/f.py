def main_f():
    if n < 5:
        return "WA"

    for y in range(n):
        for x in range(n):

            # check horizont
            if x < (n - len(WORD)+1):
                foo = boo = ""
                for i in range(len(WORD)):
                    foo += table[y][x+i]
                    boo = table[y][x+i] + boo
                if foo == WORD or boo == WORD:
                    return "OK"

            # check vert
            if y < (n - len(WORD)+1):
                foo = boo = ""
                for i in range(len(WORD)):
                    foo += table[y+i][x]
                    boo = table[y+i][x] + boo
                if foo == WORD or boo == WORD:
                    return "OK"

            # check diagonal top left to bottom right
            if x < (n - len(WORD)+1) and y < (n - len(WORD)+1):
                foo = boo = ""
                for i in range(len(WORD)):
                    foo += table[y+i][x+i]
                    boo = table[y+i][x+i] + boo
                if foo == WORD or boo == WORD:
                    return "OK"

                # diagonal top right to bottom left
                foo = boo = ""
                for i in range(len(WORD)):
                    foo += table[y+i][x+len(WORD)-i-1]
                    boo = table[y+i][x+len(WORD)-i-1] + boo
                if foo == WORD or boo == WORD:
                    return "OK"
    return "WA"


n = int(input())
WORD = "ZENIT"

table = []
for i in range(n):
    table.append(input())

print(main_f())
