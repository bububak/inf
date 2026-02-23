f = open("airlines.txt")

airports = {}

r = f.readline().strip().split(";")
while r != [""]:

    for airport in r:
        if not airport in airports:
            airports[airport] = 1
        else:
            airports[airport] += 1

    r = f.readline().strip().split(";")

airports = sorted(airports.items(), key=lambda x:x[1], reverse=True)

for airport in airports:
    print(f"{airport[0]}: {airport[1]}")

f.close()
