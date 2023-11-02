text = input().split()

line_1 = []
line_2 = []


for i in text[0]:
    line_1.append(ord(i))
for j in text[1]:
    line_2.append(ord(j))

result = 0

while True:

    if len(line_1) == 0 or len(line_2) == 0:
        break

    result += line_1[0] * line_2[0]
    line_1.pop(0)
    line_2.pop(0)

result += sum(line_1)
result += sum(line_2)

print(result)