def main_loop():
    kroky = input()
    navstivene = []
    new = [0, 0]  # r, s = y, x
    old1 = [0, 0]
    old2 = [0, 0]
    navstivene.append([0, 0])

    options = {"S": [-1, 0], "J": [1, 0], "V": [0, 1], "Z": [0, -1]}

    for krok in kroky:
        old2 = old1
        old1 = new
        new = [old1[0] + options[krok][0], old1[1] + options[krok][1]]
        for key in options:
            now_checked = [new[0] + options[key][0], new[1] + options[key][1]]
            if (now_checked in navstivene and now_checked != old1) or new == old2:
                return "L"
        navstivene.append(new.copy())
    return "W"


print(main_loop())
