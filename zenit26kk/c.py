diery = {
    "0": 1,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 1,
    "5": 0,
    "6": 1,
    "7": 0,
    "8": 2,
    "9": 1,
}
n = int(input())
s = 1
for _ in range(n):
    cisla = input()
    for c in cisla:
        s += diery[c]

print(s)
