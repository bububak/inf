num_of_intervals = input().strip()
intervals = []
for n in range(int(num_of_intervals)):
    inp = input().strip().split()
    intervals.append([int(inp[0]), int(inp[1])])
# print(num_of_intervals, intervals)

# non = (1, 2, 3, 5, 6, 7, 10, 11, 14, 15, 19)
non = [4, 8, 9, 12, 13, 16, 17, 18]
non += [n + 20 for n in range(10000)]
for interval in intervals:
    counter = 0
    for n in non:
        if interval[1] >= n >= interval[0]:
            counter += 1
    print(counter)
