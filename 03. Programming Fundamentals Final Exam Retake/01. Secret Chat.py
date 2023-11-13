def insert_space(index, string):
    string = string[:index] + " " + string[index:]
    print(string)

    return string


def reverse(substring, string):
    if substring in string:
        string = string.replace(substring, "", 1) + substring[::-1]
        print(string)
    else:
        print("error")
    return string

def change_all(old_el, new_el, string):
    if old_el in string:
        string = string.replace(old_el, new_el)
        print(string)

    return string


def final_print(string):
    print(f"You have a new text message: {string}")


text = input()

while True:

    command = input()
    if command == "Reveal":
        final_print(text)
        break

    tokens = command.split(":|:")

    if tokens[0] == "InsertSpace":
        index = int(tokens[1])
        text = insert_space(index, text)
    elif tokens[0] == "Reverse":
        substring = tokens[1]
        text = reverse(substring, text)
    elif tokens[0] == "ChangeAll":
        substring, replacement = tokens[1], tokens[2]
        text = change_all(substring, replacement, text)
