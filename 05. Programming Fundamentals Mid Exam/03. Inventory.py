def collect(item, inventory):
    if item not in inventory:
        inventory.append(item)

    return inventory


def drop(item, inventory):
    if item in inventory:
        inventory.remove(item)

    return inventory


def combine(old_item, new_item, inventory):
    if old_item in inventory:
        index = inventory.index(old_item)
        inventory.insert(index + 1, new_item)

    return inventory


def renew(item, inventory):
    if item in inventory:
        inventory.remove(item)
        inventory.append(item)

    return inventory


def final_print(inventory):
    print(*inventory, sep=", ")

inventory = input().split(", ")

while True:

    command = input().split(" - ")

    if command[0] == "Craft!":
        final_print(inventory)
        break

    item = command[1]

    if command[0] == "Collect":
        inventory = collect(item, inventory)
    elif command[0] == "Drop":
        inventory = drop(item, inventory)
    elif command[0] == "Combine Items":
        x = command[1].split(":")
        old_item, new_item = x[0], x[1]
        inventory = combine(old_item, new_item, inventory)
    elif command[0] == "Renew":
        inventory = renew(item, inventory)