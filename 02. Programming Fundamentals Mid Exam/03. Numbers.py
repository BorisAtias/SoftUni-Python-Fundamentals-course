nums = list(map(int, input().split()))

average = sum(nums) // len(nums)
above_average = []

for num in nums:
    if num > average:
        above_average.append(num)

above_average.sort()
top_scores = above_average[::-1]

if len(above_average) == 0:
    print("No")
else:
    print(*top_scores[0:5])
