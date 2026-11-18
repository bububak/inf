n = int(input())
for _ in range(n):
    opp = sorted(map(int, input().strip().split()))
    co_treba = opp[3]
    if opp[2] == opp[3]:
        co_treba += 1

    if 4*co_treba+1 > sum(opp):
        print(-1)
    else:
        print(3*f"{co_treba} ", end="")
        print(f"{co_treba+1} ",end="")
        print(f"{sum(opp)-4*co_treba-1} ", end="")
        print("0")
