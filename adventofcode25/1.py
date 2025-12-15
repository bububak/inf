movements = []
f = open("paper.txt")
line = f.readline().strip()
while line != "":
    movements.append(line)
    line = f.readline().strip()

current = 50
zero_count = 0

for i in range(len(movements)):
    line = movements[i]
    dir = line[:1:]
    n = int(line[1::])

    operator = 1
    if dir == "L":
        operator = -1

    for i in range(n):
        current += operator
        if current % 100 == 0:
            zero_count += 1

print(zero_count)
