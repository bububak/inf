l, a, b = list(map(int, input().split()))


if l // a >= 2 and l // b < 2:
    print("To bude epicke!")
else:
    for i in range(l):
        a = a//2
        b = b//2
        if abs(a-b) == 1 or abs(a-b) == 0:
            print(i+1)
            break
