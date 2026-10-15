def find_biggest_overlap(l, normal, reverse):
    print(normal)
    print(reverse)
    biggest = 0
    current = 0
    for i in range(l):
        if normal[i] == "1" and reverse[i] == "1":
            current += 1
            biggest = max(current, biggest)
        else:
            current = 0

    return biggest


def return_overlap_map(l, riadok):
    left = 0
    output = ""
    while left < l:
        if riadok[left] == "p":
            # start counting
            counts = {"p":0, "j":0}
            while True and left < l:
                counts[riadok[left]] += 1
                left += 1
                if counts["j"] > counts["p"]:
                    output += "0"
                    break
                else:
                    output += "1"
        else:
            left += 1
            output += "0"
    return output


l = int(input())
riadok = input()
print(find_biggest_overlap(l, return_overlap_map(l, riadok), "".join(list(return_overlap_map(l, riadok[::-1]))[::-1])))
