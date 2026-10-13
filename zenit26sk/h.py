l = int(input())
riadok = input()

nor, rev = [], []
for i in range(l):
    nor.append(riadok[i::].count("p"))
    rev.append(riadok[:i:].count("p"))

print(nor)
print(rev)

# two pointers area
left = 0
right = 0
run = True
# while run:
    # area = nor[i] * rev[-i]
