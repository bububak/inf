n = int(input())
b = bin(n)[2:]
delenia = len(b[1:])

if b[0] == "1" and not "1" in b[1:]:
    print("ano")
    print(delenia)

else:
    print("nie")
