import sys

s = ""
s0 = sys.stdin.read().split("\n")
for n in range(len(s0)):
    s += s0[n] + " f "


def find():
    koniec = len(s)
    for i in range(len(s)):
        if s[i - 5 : i] == "kod: ":
            zaciatok = i
            for j in range(zaciatok, len(s)):
                if s[j] == " ":
                    koniec = j
                    print(s[zaciatok:koniec])
                    return

    print(s[zaciatok:koniec])


find()
