def return_new_num(old):
    new = 0
    for i in old:
        new += int(i)*int(i)
    return str(new)


T = int(input())
for i in range(T):
    known = []
    n = input()
    counter = 0

    while True:
        known.append(n)

        n = return_new_num(n)
        counter += 1

        if n == str(1):
            print(counter)
            break
        if n in known:
            print(-1)
            break
