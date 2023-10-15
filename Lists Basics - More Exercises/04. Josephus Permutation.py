group = input().split()
sequence = int(input())

result = []
counter = 0
index = 0

while len(group) > 0:

    counter += 1

    if counter % sequence == 0:
        result.append(group.pop(index))

    else:
        index += 1

    if index >= len(group):
        index = 0

print(str(result).replace(' ', '').replace('\'', ''))