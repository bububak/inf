from math import ceil

l, a, b = list(map(int, input().split()))

if (a-1)//(l//2) != (b-1)//(l//2):
    print("To bude epicke!")
else:
    for i in range(l):
        a = ceil(a / 2)
        b = ceil(b / 2)
        if abs(a - b) == 0:
            print(i+1)
            break
