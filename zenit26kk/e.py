vstup = list(map(int, input().strip().split()))

teror_counter = 0
s = 0
len_vstupu = len(vstup) - 1
for i, n in enumerate(vstup):
    end_char = " "
    if i == len_vstupu:
        end_char = "\n"

    if n % 2 == 1 and teror_counter == 0:
        teror_counter += 1

    if teror_counter > 10:
        print("TEROR", end=end_char)
        teror_counter += 1
    elif teror_counter > 0:
        print("ERROR", end=end_char)
        teror_counter += 1
    else:
        s += n
        print(s, end=end_char)
