with open("00.sample.a.txt") as f:
    r = int(f.readline())
    hodnoty = list(map(int, f.readline().strip().split()))
    uloha = int(f.readline())

heightmap = [0,]
current = 0
for i in range(r-1):
    current += hodnoty[i]
    heightmap.append(current)

print(heightmap)

# increnet n = n + n - 1 when seeing new
