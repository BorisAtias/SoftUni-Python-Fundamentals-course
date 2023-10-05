keys = []
values = []
my_dict = {}
count = 0

while True:

    command = input()

    if command == "stop":
        break
    count += 1

    if count % 2 != 0:
        keys.append(command)

    if count % 2 == 0:
        values.append(command)
        for key in keys:
            for value in values:
                if key not in my_dict:
                    my_dict[key] = int(value)
                else:
                    my_dict[key] += int(value)
                keys.pop(0)
                values.pop(0)

for key, value in my_dict.items():
    print(f'{key} -> {value}')
