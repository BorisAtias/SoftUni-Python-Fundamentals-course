train_length = int(input())

train = [0] * train_length

while True:

    command = input().split()

    if command[0] == 'End':
        break

    elif command[0] == 'add':
        people_count = int(command[1])
        train[-1] += people_count

    elif command[0] == 'insert':
        wagon_num = int(command[1])
        people_count = int(command[2])
        train[wagon_num] += people_count

    elif command[0] == 'leave':
        wagon_num = int(command[1])
        people_count = int(command[2])
        train[wagon_num] -= people_count

print(train)