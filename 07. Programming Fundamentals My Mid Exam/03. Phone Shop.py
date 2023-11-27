phones = input().split(", ")

while True:

    command = input()

    if command == "End":
        break
    command = command.split("- ")

    if 'Add ' in command:
        if command[1] in phones:
            continue
        else:
            phones.append(command[1])

    if "Remove " in command:
        if command[1] not in phones:
            continue
        else:
            phones.remove(command[1])

    if "Bonus phone " in command:
        text = list(command[-1])
        my_list = []
        res = ""

        for i in text:

            if i == ':':
                res += ''
                my_list.append(res)
                res = ''
                continue
            else:
                res += i
        my_list.append(res)
        old_phone = my_list[0]
        new_phone = my_list[1]

        if old_phone not in phones:
            continue
        else:
            x = phones.index(old_phone)
            phones.insert(x + 1, new_phone)

    if "Last " in command:
        if command[-1] not in phones:
            continue
        else:
            phones.remove(command[-1])
            phones.append(command[-1])

print(", ".join(phones))
