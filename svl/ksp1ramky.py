skratky = (6, 3, 2, 0, -2, -3, -6)
get_index = ("M", "k", "h", "B", "c", "m", "u")
previous = 63

tens = 0
for c in input():
    i = get_index.index(c)
    if previous >= i:
        tens += skratky[i]
    else:
        tens -= skratky[i]
    previous = i


if tens >= 0:
    print("1" + "0" * tens)
else:
    print("0." + "0" * (-tens - 1) + "1")
