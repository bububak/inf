l = int(input())
kopky = []
for i in range(l):
    kopky.append(int(input()))
odpoved = ""
odpoved += str(max(kopky))
kopky.remove(int(odpoved))
odpoved += " "
odpoved += str(max(kopky))
print(odpoved)
