def outOfStock(inventory, gift):

    for index in range(len(inventory)):

        if inventory[index] == gift:
            inventory[index] = None

def required(gift, position, inventory):

    if position in range(len(inventory)):

        for index in range(len(inventory)):

            if index == position:
                inventory[index] = gift

def justInCase(gift, inventory):

    inventory.pop(-1)
    inventory.append(gift)

gift_list = input().split()

while True:

    command = input()
    if command == "No Money":
        print(" ".join(x for x in gift_list if x is not None))
        break

    tokens = command.split()

    if tokens[0] == "OutOfStock":
        gift = tokens[1]
        outOfStock(gift_list,gift)

    elif tokens[0] == "Required":
        gift = tokens[1]
        index = int(tokens[2])
        required(gift, index, gift_list)

    elif tokens[0] == "JustInCase":
        gift = tokens[1]
        justInCase(gift, gift_list)
