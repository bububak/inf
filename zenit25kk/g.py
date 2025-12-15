import re

l = int(input())
lines = []
for i in range(l):
    line = input().strip()
    line = re.sub("[^zenit]", "", line)
    lines.append(line)

nums_of_zenits = [0] * l
zenit = ["z", "e", "n", "i", "t"]
counter = [0] * l
for j in range(l):
    state = 0  # co teraz hladame, state-1 je posledne pismeno
    for c in lines[j]:
        if c == zenit[state]:
            state += 1
        if state == 5:
            state = 0
            counter[j] += 1

# printovanie vysledkov v slovencine

jednotky = [
    "",
    "jeden",
    "dva",
    "tri",
    "styri",
    "pat",
    "sest",
    "sedem",
    "osem",
    "devat",
    "desat",
]

desiatky = [
    "",
    "nast",
    "dvadsat",
    "tridsat",
    "styridsat",
    "patdesiat",
    "sestdesiat",
    "sedemdesiat",
    "osemdesiat",
    "devatdesiat",
]

# pozor na edge case nuly
for j in range(l):
    n = counter[j]
    s = str(n)
    # print(s)
    koniec = "zenitov"
    if 2 <= n <= 4:
        koniec = "zenity"
    elif n == 1:
        koniec = "zenit"

    if n == 0:
        print(f"nula {koniec}")
    elif 1 == len(s):
        print(f"{jednotky[n]} {koniec}")
    elif 2 == len(s):
        if s[0] == "1":  # nastky
            if s[1] == "1":
                print(f"{jednotky[int(s[1])]}{desiatky[1][1:]} {koniec}")
            elif s[1] == "0":
                print("desat zenitov")
            elif n == 14:
                print("strnast zenitov")
            else:
                print(f"{jednotky[int(s[1])]}{desiatky[1]} {koniec}")
        else:  # dvadsat tridsatat...
            print(f"{desiatky[int(s[0])]}{jednotky[int(s[1])]} {koniec}")
    elif len(s) == 3:
        print("sto zenitov")
