l = int(input())
filmy = []
for i in range(l):
    filmy.append(int(input()))
filmy.sort()
s = sum(filmy)
filmy.pop(0)
filmy.pop(0)

print(s - len(filmy))
