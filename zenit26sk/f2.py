kroky = input()

# new = [0, 0]  # r, s = y, x
# old1 = [0, 0]
# options = {"S": [-1, 0], "J": [1, 0], "V": [0, 1], "Z": [0, -1]}
# for krok in kroky:
#     old1 = new
#     new = [old1[0] + options[krok][0], old1[1] + options[krok][1]]


end_pos = [kroky.count("J")-kroky.count("S"), kroky.count("V") - kroky.count("Z")]


if kroky.count("V") < end_pos[1] or kroky.count("J") != end_pos[0] or kroky.count("Z")*(-1) != end_pos[1] or kroky.count("S")*(-1) != end_pos[0]:
    print("L")
else:
    print("W")
