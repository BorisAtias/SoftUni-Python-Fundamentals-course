n = int(input())

nums = []
filtered_nums = []

for i in range(n):

    numbers = int(input())
    nums.append(numbers)

command  = input()
if command == 'even':
    for num in nums:
        if num % 2 == 0:
            filtered_nums.append(num)

elif command == 'odd':
    for num in nums:
        if num % 2 != 0:
            filtered_nums.append(num)

elif command == 'negative':
    for num in nums:
        if num < 0:
            filtered_nums.append(num)

elif command == 'positive':
    for num in nums:
        if num >= 0:
            filtered_nums.append(num)

print(filtered_nums)