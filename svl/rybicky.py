with open("rybicky.txt", "r") as f:
    original_fish = list(map(int,f.read().split(",")))


TURNS = 256


# for turn in range(TURNS):
#     print(turn)
#     for i in range(len(fish)):
#         fish[i] -= 1
#         if fish[i] == -1:
#             fish[i] = 6
#             fish += [8]


fish = [0]*10
for f in original_fish:
    fish[f] += 1



for turn in range(TURNS):
    last_year = fish.copy()
    fish = [0]*9
    for age in range(len(fish)):

        if age == 0:
            fish[8] += last_year[0]
            fish[6] += last_year[0]
        else:
            fish[age-1] += last_year[age]



total = 0
for age in fish:
    total += age
print(total)


