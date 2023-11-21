def potion(hp_amount, health):
    curr_health = health
    health += hp_amount
    if health > 100:
        health = 100
        print(f"You healed for {100 - curr_health} hp.")
    else:
        print(f"You healed for {hp_amount} hp.")
    print(f"Current health: {health} hp.")

    return health


def chest(bit_amount, bitcoins):
    bitcoins += bit_amount
    print(f"You found {bit_amount} bitcoins.")

    return bitcoins


def any_other_case(damage, monster, counter, health):
    health -= damage
    if health > 0:
        print(f"You slayed {monster}.")
    else:
        print(f"You died! Killed by {monster}.\nBest room: {counter}")
        raise SystemExit

    return health


def win(counter, rooms, health):
    if counter == len(rooms):
        print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")

initial_health = 100
bitcoins = 0
counter = 0

rooms = [x.split() for x in input().split("|")]

for i in rooms:
    counter += 1
    if i[0] == "potion":
        hp_amount = int(i[1])
        initial_health = potion(hp_amount, initial_health)
    elif i[0] == "chest":
        amount = int(i[1])
        bitcoins = chest(amount, bitcoins)
    else:
        monster = i[0]
        damage = int(i[1])
        initial_health = any_other_case(damage, monster, counter, initial_health)

win(counter, rooms, initial_health)
