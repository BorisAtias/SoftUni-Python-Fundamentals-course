def rest(initial_energy, energy):
    initial_energy += energy
    if initial_energy > 100:
        energy = energy - (initial_energy - 100)
        initial_energy = 100

    print(f"You gained {energy} energy.\nCurrent energy: {initial_energy}.")
    return initial_energy

def order(coins, initial_coins, initial_energy):
    if initial_energy >= 30:
        initial_energy -= 30
        initial_coins += coins
        print(f"You earned {coins} coins.")
    else:
        initial_energy += 50
        print("You had to rest!")

    return initial_coins, initial_energy

def other(product, coins, initial_coins):
    initial_coins -= coins
    print(f"You bought {product}.")
    return initial_coins

initial_coins, initial_energy = 100, 100

text = [event.split("-") for event in input().split("|")]

all_done = True

for command, value in text:

    value = int(value)
    if command == "rest":
        initial_energy = rest(initial_energy, value)
    elif command == "order":
        initial_coins, initial_energy = order(value, initial_coins, initial_energy)
    else:
        product = command
        if initial_coins >= value:
            initial_coins = other(product, value, initial_coins)
        else:
            print(f"Closed! Cannot afford {product}.")
            all_done = False
            break

if all_done:
    print(f"Day completed!\nCoins: {initial_coins}\nEnergy: {initial_energy}")