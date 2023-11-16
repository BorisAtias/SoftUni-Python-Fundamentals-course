sequence = list(map(int, input().split()))

def shoot():

    index = int(command[1])
    power = int(command[2])

    if index in range(len(sequence)):
        new_value = sequence[index] - power
        sequence[index] = new_value

        if new_value <= 0:
            sequence.pop(index)

    return sequence

def add():

    index = int(command[1])
    value = int(command[2])

    if index in range(len(sequence)):
        sequence.insert(index, value)
    else:
        print("Invalid placement!")

    return sequence

def strike():

    index = int(command[1])
    extensions = int(command[2])
    radius = sequence[index - extensions:index + extensions + 1]

    if len(radius) < 1 + (extensions * 2):
        print("Strike missed!")
    else:
        del sequence[index - extensions:index + extensions + 1]
        return sequence

while True:

    command = input()

    if command == 'End':
        print("|".join(map(str, sequence)))
        break
    command = command.split()

    if command[0] == "Shoot":
        shoot()

    elif command[0] == 'Add':
        add()

    elif command[0] == 'Strike':
        strike()