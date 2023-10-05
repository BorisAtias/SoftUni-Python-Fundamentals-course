my_string = input().replace(" ", "")
my_dict = {}

for letter in my_string:
    count = 0
    if letter not in my_dict:
        my_dict[letter] = letter
    else:
        continue

    for i in my_string:
        if i == letter:
            count += 1
        my_dict[letter] = count

    print(f"{letter} -> {count}")

# Second way

from collections import defaultdict

my_string = input().replace(" ", "")
my_dict = defaultdict(int)
for letter in my_string:
    my_dict[letter] += 1

for key, value in my_dict.items():
    print(f'{key} -> {value}')