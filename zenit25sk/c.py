l = int(input())
s = input().split()
k = list(map(int, s))


def find():
    for a in range(l):
        for b in range(l):
            for c in range(l):
                if a != b and a != c and b != c:
                    if (k[a] + k[b] + k[c]) % 3 == 0:
                        print(f"{k[a]} {k[b]} {k[c]}")
                        return


find()
