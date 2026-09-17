l = int(input())
friends = input().strip().split()
sum = 0
for friend in friends:
    sum += int(friend)

for friend in friends:
    print(sum - int(friend))
