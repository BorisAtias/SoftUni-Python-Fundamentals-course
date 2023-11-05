def move(letter_count, string):

    string = string[letter_count:] + string[0:letter_count]

    return string


def insert(index, value, string):

    string = string[0:index] + value + string[index:]

    return string

def chageAll(old_el, new_el, string):

    string = string.replace(old_el, new_el)

    return string


text = input()


while True:

    command = input().split("|")

    if command[0] == "Decode":
        print(f"The decrypted message is: {text}")
        break

    elif command[0] == "Move":
        count = int(command[1])
        text = move(count, text)

    elif command[0] == "Insert":
        end_index = int(command[1])
        element = command[2]
        text = insert(end_index, element, text)

    elif command[0] == "ChangeAll":
        old = command[1]
        new = command[2]
        text = chageAll(old, new, text)
