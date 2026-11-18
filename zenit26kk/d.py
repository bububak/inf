import sys

vstup = sys.stdin.read()

w = 0
medzery = " \n"
p = " "
for c in vstup:
    if not c in medzery and p in medzery:
        w += 1
    p = c

print(w)
