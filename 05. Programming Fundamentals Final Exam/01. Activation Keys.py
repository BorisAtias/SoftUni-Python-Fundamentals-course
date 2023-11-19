def contains(substring, string):
    if substring in string:
        print(f"{string} contains {substring}")
    else:
        print("Substring not found!")


def flip_upper(start_index, end_index, string):
    string = string[:start_index] + string[start_index:end_index].upper() + string[end_index:]
    print(string)

    return string

def flip_lower(start_index, end_index, string):
    string = string[:start_index] + string[start_index:end_index].lower() + string[end_index:]
    print(string)

    return string

def slice(start_index, end_index, string):
    string = string[:start_index] + string[end_index:]
    print(string)

    return string

def final_print(string):
    print(f"Your activation key is: {string}")


def activation_keys(text):

    while True:

        command = input().split(">>>")
        if command[0] == "Generate":
            final_print(text)
            break
        elif command[0] == "Contains":
            substring = command[1]
            contains(substring, text)
        elif command[0] == "Flip":
            start_index, end_index = int(command[2]), int(command[3])
            if command[1] == "Upper":
                text = flip_upper(start_index, end_index, text)
            elif command[1] == "Lower":
                text = flip_lower(start_index, end_index, text)
        elif command[0] == "Slice":
            start_index, end_index = int(command[1]), int(command[2])
            text = slice(start_index, end_index, text)

text = input()

activation_keys(text)
