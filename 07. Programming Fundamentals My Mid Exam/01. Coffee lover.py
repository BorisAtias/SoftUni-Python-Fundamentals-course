coffees = input().split()
num_commands = int(input())
counter = 0

while counter < num_commands:

    command = input().split()

    counter += 1

    if command[0] == "Include":
        coffees.append(command[1])

    if command[0] == "Remove":
        if int(command[2]) > len(coffees):
            continue
        if command[1] == 'first':
            del coffees[0:int(command[2])]
        if command[1] == 'last':
            coffees = coffees[::-1]
            del coffees[0:int(command[2])]
            coffees.reverse()

    if command[0] == "Prefer":
        if int(command[1]) not in range(len(coffees)) or int(command[2]) not in range(len(coffees)):
            continue
        else:
            product_1 = int(command[1])
            product_2 = int(command[2])

            x, y = coffees[product_1], coffees[product_2]
            i, j = coffees.index(x), coffees.index(y)
            coffees[i], coffees[j] = coffees[j], coffees[i]

    if command[0] == "Reverse":
        coffees.reverse()

print(f"Coffees:\n{' '.join(coffees)}")