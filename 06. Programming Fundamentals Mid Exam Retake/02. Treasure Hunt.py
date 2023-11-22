def loot(elements, initial_loot):
    for element in elements:
        if element in initial_loot:
            continue
        else:
            initial_loot.insert(0, element)

    return initial_loot


def drop(index, initial_loot):
    if index in range(len(initial_loot)):
        loot = initial_loot.pop(index)
        initial_loot.append(loot)

    return initial_loot


def steal(count, initial_loot):
    if count > 0:
        section = initial_loot[-count::]
        if count >= len(initial_loot):
            del initial_loot
            print(*section, sep=", ")
        else:
            del initial_loot[-count::]
            print(*section, sep=", ")
            return initial_loot


def final_print(initial_loot):

    if initial_loot is None:
        print("Failed treasure hunt.")
    else:
        words_len = 0
        for word in initial_loot:
            words_len += len(word)
        if len(initial_loot) > 0:
            print(f"Average treasure gain: {(words_len / len(initial_loot)):.2f} pirate credits.")



initial_loot = input().split("|")


while True:

    command = input().split()

    if command[0] == "Yohoho!":
        final_print(initial_loot)
        break
    elif command[0] == "Loot":
        elements = command[1::]
        initial_loot = loot(elements, initial_loot)
    elif command[0] == "Drop":
        index = int(command[1])
        initial_loot = drop(index, initial_loot)
    elif command[0] == "Steal":
        count = int(command[1])
        initial_loot = steal(count, initial_loot)
