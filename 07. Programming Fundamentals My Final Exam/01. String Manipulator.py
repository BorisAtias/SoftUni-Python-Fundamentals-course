
my_string = input()


while True:

    command = input()

    if command == "End":
        break

    tokens = command.split()

    if tokens[0] == "Translate":
        old_char = tokens[1]
        new_char = tokens[2]
        my_string = my_string.replace(old_char, new_char)
        print(my_string)

    elif tokens[0] == "Includes":
        sub_string = tokens[1]
        if sub_string in my_string:
            print(True)
        else:
            print(False)

    elif tokens[0] == "Start":
        sub_string = tokens[1]
        part = len(sub_string)
        if sub_string == my_string[0:part]:
            print(True)
        else:
            print(False)

    elif tokens[0] == "Lowercase":
        my_string = my_string.lower()
        print(my_string)

    elif tokens[0] == "FindIndex":
        char = tokens[1]
        char_index = 0
        for index, character in enumerate(my_string):
            if character == char:
                char_index = index
        print(char_index)

    elif tokens[0] == "Remove":
        start_index = int(tokens[1])
        end_index = start_index + int(tokens[2])
        my_string = my_string[0:start_index] + my_string[end_index::]
        print(my_string)