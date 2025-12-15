max = int(input())
s = input().split()

l = len(s)
z = [0] * 2000001
temp = ""
for i in range(len(s)):
    n = int(s[i])
    if z[n + 1000000] < max:
        z[n + 1000000] += 1
        print(temp, end=f"{n}")
        temp = " "
print()
