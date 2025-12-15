import re

s = input().strip()
wordid = 0
small = [""] * 1000
big = [""] * 1000
nums = [""] * 1000

for n, c in enumerate(s):
    if c == " ":
        wordid += 1
        continue
    else:
        if c.isnumeric():
            nums[wordid] += c
        elif c.lower() == c:
            small[wordid] += c
        elif c.capitalize() == c:
            big[wordid] += c

out = ""
for i in range(len(small)):
    out += f" {small[i]} "
for i in range(len(big)):
    out += f" {big[i]} "
for i in range(len(nums)):
    out += f" {nums[i]} "
print(re.sub(" +", " ", out)[1:-1])
