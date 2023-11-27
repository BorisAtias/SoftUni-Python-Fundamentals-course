zoo = {}

while True:

    command = input()

    if command == "EndDay":
        break

    tokens = command.split(": ")
    details = tokens[1].split("-")
    if tokens[0] == 'Add':

        animal, needed_food, area = details[0], int(details[1]), details[2]
        needed_food = int(needed_food)

        if animal in zoo:
            zoo[animal][0] += needed_food

        else:
            zoo[animal] = [needed_food, area]
    elif tokens[0] == 'Feed':

        animal, needed_food = details[0], int(details[1])
        needed_food = int(needed_food)
        if animal in zoo:
            zoo[animal][0] -= needed_food
            if zoo[animal][0] <= 0:
                print(f"{animal} was successfully fed")
                del zoo[animal]

print('Animals:')

for key, value in zoo.items():
    print(f' {key} -> {value[0]}g')

result = {}

print('Areas with hungry animals:')

for key, value in zoo.items():
    if value[1] in result:
        result[value[1]] += 1

    else:
        result[value[1]] = 1
for key, value in result.items():
    print(f'{key}: {value}')
