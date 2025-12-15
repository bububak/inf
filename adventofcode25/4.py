file = open("4.txt").read().split()
lines = []
lines.append("."*(len(file[0])+2))
for i in range(len(file)):
    lines.append(f".{file[i]}.")
lines.append("."*(len(file[0])+2))

counter = 0
for y in range(1,len(lines)-1):
    for x in range(1,len(lines[y])-1):
        if lines[y][x] == "@":
            availability_counter = -1
            for dy in range(-1,2):
                for dx in range(-1,2):
                    if lines[y+dy][x+dx] == "@":
                        availability_counter += 1
            if availability_counter < 4:
                counter += 1
print(counter)
