# with open("04.txt") as f:
#     r = int(f.readline())
#     hodnoty = list(map(int, f.readline().strip().split()))
#     uloha = int(f.readline())
r = int(input())
hodnoty = list(map(int, input().strip().split()))
uloha = int(input())

heightmap = {}
# cislo: (pocet, kolko_ciest)

current = 0
for i in range(r - 1):
    # increnet n = n + n - 1 when seeing new
    current += hodnoty[i]
    foo = heightmap.get(current, (0, 0))
    boo = (foo[0] + 1, foo[1] + foo[0])
    heightmap[current] = boo

# print(heightmap)
match uloha:
    case 1:
        print(heightmap.get(1047, (0, 0))[0])
    case 2:
        end_sum = 0
        for height in heightmap:
            end_sum += heightmap[height][1]
        print(end_sum)
