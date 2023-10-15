num = input().split(' ')
given_string = input()

key = []

for _ in num:

    value = 0

    for i in _:
        value += int(i)

    value %= len(given_string)
    key.append(given_string[value])
    given_string = given_string.replace(given_string[value], '', 1)

print(''.join(key))