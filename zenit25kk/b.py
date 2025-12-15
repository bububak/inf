l = int(input())
nums = []
for n in range(l):
    nums.append(int(input().strip()))

sums = []
for j in range(l):
    for i in range(l):
        sums.append(nums[j] + nums[i])
sums.sort()
print(sums[len(sums) - l])
