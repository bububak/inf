i = input().strip().split()
syr, diery = float(i[0]), float(i[1])
if syr == 0:
    print(0)
elif diery == 0:
    print(syr)
elif diery == 100:
    print(-1)
else:
    odpoved = syr / (1 - (diery / 100))
    print(f"{odpoved:.9f}")
