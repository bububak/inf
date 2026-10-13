l = int(input())
r1 = input().strip().split()
r2 = input().strip().split()

c1 = {}
c2 = {}
for i in range(l):
    c1[r1[i]] = c1.get(r1[i], 0) + 1
    c2[r2[i]] = c2.get(r2[i], 0) + 1

for j in range(2):
    for i in list(c1.keys()):
        c2[i] = c2.get(i, 0)
        smallest = min(c1[i], c2[i])
        c1[i] -= smallest
        c2[i] -= smallest
        if c1[i] == 0:
            c1.pop(i)
        else:
            c1[i] += 1
        if c2[i] == 0:
            c2.pop(i)


for key in list(c1.keys()):
    if c1[key] == 0:
        c1.pop(key)

if len(c1) == 0:
    print("Jednoduche")
else:
    print("Neda sa")
