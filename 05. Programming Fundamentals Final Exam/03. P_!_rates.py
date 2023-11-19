def plunder(town, people, gold, targets):
    targets[town]['People'] -= people
    targets[town]['Gold'] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if targets[town]['People'] <= 0 or targets[town]['Gold'] <= 0:
        print(f"{town} has been wiped off the map!")
        del targets[town]

    return targets


def prosper(town, gold, targets):
    targets[town]['Gold'] += gold
    print(f"{gold} gold added to the city treasury. {town} now has {targets[town]['Gold']} gold.")

    return targets


def final_print(targets):
    if len(targets) > 0:
        print(f"Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:")
        for town, value in targets.items():
            print(f"{town} -> Population: {targets[town]['People']} citizens, Gold: {targets[town]['Gold']} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


targets = {}

while True:
    targets_info = input().split("||")
    if targets_info[0] == "Sail":
        break
    town, people, gold = targets_info[0], int(targets_info[1]), int(targets_info[2])
    if town not in targets:
        targets[town] = {"People": people, "Gold": gold}
    else:
        targets[town]["People"] += people
        targets[town]["Gold"] += gold

while True:
    command = input().split("=>")
    if command[0] == "End":
        final_print(targets)
        break
    elif command[0] == "Plunder":
        town, people, gold = command[1], int(command[2]), int(command[3])
        targets = plunder(town, people, gold, targets)
    elif command[0] == "Prosper":
        town, gold = command[1], int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        else:
            targets = prosper(town, gold, targets)
