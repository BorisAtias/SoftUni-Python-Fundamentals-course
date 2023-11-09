def rate(plant, rating, inventory):
    if plant in inventory:
        inventory[plant].append(rating)
    else:
        print("error")

    return inventory


def update(plant, new_rarity, inventory):
    if plant in inventory:
        inventory[plant].pop(0)
        inventory[plant].insert(0, new_rarity)
    else:
        print("error")

    return inventory


def reset(plant, inventory):
    if plant in inventory:
        del inventory[plant][1::]
    else:
        print("error")

    return inventory


def final_print(inventory):
    print("Plants for the exhibition:")
    for key, value in inventory.items():
        if len(value[1::]) > 0:
            print(f"- {key}; Rarity: {value[0]}; Rating: {sum(value[1::]) / len(value[1::]):.2f}")
        else:
            print(f"- {key}; Rarity: {value[0]}; Rating: {0:.2f}")


def plant_discovery(num):
    plant_collection = {}
    for i in range(num):
        plant, rarity = input().split("<->")
        plant_collection[plant] = [rarity]

    while True:
        command = input()
        if command == "Exhibition":
            final_print(plant_collection)
            break
        command = command.split()

        if command[0] == "Rate:":
            plant, rating = command[1], int(command[-1])
            plant_collection = rate(plant, rating, plant_collection)
        elif command[0] == "Update:":
            plant, new_rarity = command[1], int(command[-1])
            plant_collection = update(plant, new_rarity, plant_collection)
        elif command[0] == "Reset:":
            plant = command[1]
            plant_collection = reset(plant, plant_collection)

num = int(input())
plant_discovery(num)
