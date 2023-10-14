nums = input().split()

for index, value in enumerate(nums):
    value = int(value)
    if value == 0:
        nums[index] = 0
    elif int(value) > 0:
        nums[index] = -abs(value)
    else:
        nums[index] = abs(value)

print(nums)