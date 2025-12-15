d = input()
n = sorted(list(map(int, input().split())))

ek = False
if n[-1] > 0:
    ek = True
ez = False
if n[0] < 1:
    ez = True


# najvacsi sucin vzdy posledne dve
if ek:
    print(f"{n[-2]} {n[-1]}")
else:
    print(f"{n[0]} {n[1]}")


# najmensi sucin
if ez and ek:
    print(f"{n[0]} {n[-1]}")
else:
    print(f"{n[0]} {n[1]}")

# najvacsi delitel posledne / najmensie kladne
if ez and ek:
    print(f"{n[-1]} {n[-2]}")  # nie
if ez and not ek:
    print(f"{n[1]} {n[0]}")
if ek and not ez:
    print(f"{n[-1]} {n[-2]}")

# najmensi delitel obe krajove jedno zaporne
print(f"{n[-1]} {n[0]}")
