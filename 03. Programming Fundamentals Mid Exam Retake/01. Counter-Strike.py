initial_energy = int(input())
distance = input()

wins = 0

while not distance == "End of battle":

    distance = int(distance)

    if initial_energy - distance < 0:
        print(f"Not enough energy! Game ends with {wins} won battles and {initial_energy} energy")
        break

    wins += 1
    initial_energy -= distance

    if wins % 3 == 0:
        initial_energy += wins

    distance = input()
if distance == 'End of battle':
    print(f"Won battles: {wins}. Energy left: {initial_energy}")
