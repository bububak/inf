
# !! nenajde vert a horizont v dolnych pravych 5 riadkoch


n = int(input())

WORD = "ab"

table = []
for i in range(n):
    table.append(input())

answer = "WA"
for y in range(n - len(WORD)+1):
    for x in range(n - len(WORD)+1):

        # check horizont
        foo = boo = ""
        for i in range(len(WORD)):
            foo += table[y][x+i]
            boo = table[y][x+i] + boo
        if foo == WORD or boo == WORD:
            # print("horizont")
            answer = "OK"

        # check vert
        foo = boo = ""
        for i in range(len(WORD)):
            foo += table[y+i][x]
            boo = table[y+i][x] + boo
        if foo == WORD or boo == WORD:
            # print("vertical")
            answer = "OK"

        # check diagonal top left to bottom right
        foo = boo = ""
        for i in range(len(WORD)):
            foo += table[y+i][x+i]
            boo = table[y+i][x+i] + boo
        if foo == WORD or boo == WORD:
            # print("diag")
            answer = "OK"

        # diagonal top right to bottom left
        foo = boo = ""
        for i in range(len(WORD)):
            # print(x, len(WORD), i)
            # print(x+len(WORD)-i)
            # print(table[y+i][x+len(WORD)-i])
            foo += table[y+i][x+len(WORD)-i-1]
            boo = table[y+i][x+len(WORD)-i-1] + boo
        if foo == WORD or boo == WORD:
            # print("rdiag")
            answer = "OK"


for y in range(n - len(WORD)+1, n):
    for x in range(n - len(WORD)+1, n):

        # check horizont
        foo = boo = ""
        for i in range(len(WORD)):
            foo += table[y][x+i]
            boo = table[y][x+i] + boo
        if foo == WORD or boo == WORD:
            # print("horizont")
            answer = "OK"

        # check vert
        foo = boo = ""
        for i in range(len(WORD)):
            foo += table[y+i][x]
            boo = table[y+i][x] + boo
        if foo == WORD or boo == WORD:
            # print("vertical")
            answer = "OK"


print(answer)
