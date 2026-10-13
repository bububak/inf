def find_biggest_overlap():
    pass



l = int(input())
riadok = input()

normals = []
reverses = []

# longest from left to right
left = 0
run = True
while left < l-1 and run:
    if riadok[left] != "J":
        # zisti ako dlho mozes ist a potom zmen pointer na koniec oznaceneho
        counts = {"P": 0, "J": 0}
        temp = left
        keep_going = True
        while keep_going:
            counts[riadok[temp]] += 1
            if counts["J"] > counts["P"] or temp == l-1:
                # cant continue - move left and write data

                normals.append([left, temp, temp-left])

                left = temp
                keep_going = False
            temp += 1
    else:
        left += 1


# longest from right
right = l-1
run = True
while right > 0 and run:
    if riadok[right] != "J":
        # zisti ako dlho mozes ist a potom zmen pointer na koniec oznaceneho
        counts = {"P": 0, "J": 0}
        temp = right
        keep_going = True
        while keep_going:
            counts[riadok[temp]] += 1
            if counts["J"] > counts["P"] or temp == 0:
                # cant continue - move left and write data

                reverses.append([temp, right, right-temp])

                right = temp
                keep_going = False
            temp -= 1
    else:
        right -= 1

print(normals)
print(reverses)
