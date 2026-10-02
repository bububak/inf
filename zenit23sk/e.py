l = int(input())
filmy = []
for i in range(l):
    filmy.append(int(input()))
filmy.sort()

if l <= 2:
    print(0)
else:
    druhy = filmy[-2]
    if l - 2 < druhy:
        print(l - 2)
    else:
        print(int(druhy) - 1)
