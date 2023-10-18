nums = (input().split(", "))

positive = []
a = [positive.append(x) for x in nums if int(x) >= 0]

negative = []
b = [negative.append(x) for x in nums if int(x) < 0]

even = []
c = [even.append(x) for x in nums if int(x) % 2 == 0]

odd = []
d = [odd.append(x) for x in nums if int(x) % 2 != 0]

print(f'Positive: {", ".join(positive)}')
print(f'Negative: {", ".join(negative)}')
print(f'Even: {", ".join(even)}')
print(f'Odd: {", ".join(odd)}')