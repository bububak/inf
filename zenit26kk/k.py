r = int(input())
cisla = list(map(int, input().strip().split()))
m = 0
s = 0
for i in range(r):
    n = cisla[i]
    print(n)
    if n > m:
        print("vacsie")
        s += n
        m = n
print(s)
