n = int(input())
# sobdpq
hori = {
    "o": "o",
    "b": "d",
    "d": "b",
    "p": "q",
    "q": "p",
}

counter = 0
najdene = {}
for _ in range(n):
    p = input().strip()
    # if len(p) % 2 == 1 and not p[len(p) // 2] in "os":
    #     continue
    q = "".join(hori[p[-(i + 1)]] for i in range(len(p)))
    # b = "".join(vert[p[i]] for i in range(len(p)))

    if najdene.get(q, 0) > 0:
        najdene[q] -= 1
        counter += 1
    # elif najdene.get(b, 0) > 0:
    #     najdene[b] -= 1
    #     counter += 1
    else:
        najdene[p] = najdene.get(p, 0) + 1

print(counter)
