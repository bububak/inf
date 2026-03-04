NO_DUPLICATES = False
number = 5
nums = [1] * number
list_sum = number

while nums[0] != number:

    if NO_DUPLICATES:
        if sum(set(nums)) == number:
            print(nums)
    else:
        print(nums)

    list_sum -= nums.pop()
    nums[-1] += 1
    list_sum += 1

    while list_sum != number:
        nums.append(1)
        list_sum += 1
