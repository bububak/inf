max = int(input())
s = input()

l = len(s)
z = [0] * 2000001
ascii = [0] * 2000
temp = ""
for i in range(len(s)):
    n = s[i]
    if n.isnumeric():
        if z[int(n) + 1000000] < max:
            z[int(n) + 1000000] += 1
            print(temp, end=f"{n}")
            temp = " "

    else:
        if ascii[ord(n)] < max:
            ascii[ord(n)] += 1
            print(temp, end=f"{n}")
            temp = " "
print()
