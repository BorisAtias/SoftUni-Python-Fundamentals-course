def fire(index, damage, war_ship):
    if index in range(len(war_ship)):
        war_ship[index] -= damage
        if war_ship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            raise SystemExit

    return war_ship


def defend(start_index, end_index, damage, pirate_ship):
    if start_index in range(len(pirate_ship)) and end_index in range(len(pirate_ship)):
        for section in range(start_index, end_index + 1):
            pirate_ship[section] -= damage
            if pirate_ship[section] <= 0:
                print("You lost! The pirate ship has sunken.")
                raise SystemExit

    return pirate_ship


def repair(index, health, max_health, pirate_ship):
    if index in range(len(pirate_ship)):
        pirate_ship[index] += health
        if pirate_ship[index] > max_health:
            pirate_ship[index] = max_health

    return pirate_ship, max_health


def status(pirate_ship, max_health):
    counter = 0
    for section in pirate_ship:
        if section < (max_health * 0.20):
            counter += 1
    print(f"{counter} sections need repair.")


def final_print(pirate_ship, war_ship):
    print(f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(war_ship)}")


pirate_ship = [int(x) for x in input().split(">")]
war_ship = [int(x) for x in input().split(">")]
max_health = int(input())


while True:

    command = input().split()

    if command[0] == "Retire":
        final_print(pirate_ship, war_ship)
        break
    elif command[0] == "Fire":
        index, damage = int(command[1]), int(command[2])
        war_ship = fire(index, damage, war_ship)
    elif command[0] == "Defend":
        start_index, end_index, damage = int(command[1]), int(command[2]), int(command[3])
        pirate_ship = defend(start_index, end_index, damage, pirate_ship)
    elif command[0] == "Repair":
        index, health = int(command[1]), int(command[2])
        pirate_ship, max_health = repair(index, health, max_health, pirate_ship)
    elif command[0] == "Status":
        status(pirate_ship, max_health)
