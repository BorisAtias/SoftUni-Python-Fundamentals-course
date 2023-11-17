def take_odd(string):
    string = string[1::2]
    print(string)
    return string

def cut(index, length, string):
    substring = string[index: index + length]
    string = string.replace(substring, "", 1)
    print(string)

    return string

def substitute(old_el, new_el, string):
    if old_el in string:
        string = string.replace(old_el, new_el)
        print(string)
    else:
        print("Nothing to replace!")

    return string

def final_print(string):
    print(f"Your password is: {string}")



def password_reset(text):

    while True:
        command = input().split()
        if command[0] == "Done":
            final_print(text)
            break
        elif command[0] == "TakeOdd":
            text = take_odd(text)
        elif command[0] == "Cut":
            index, length = int(command[1]), int(command[2])
            text = cut(index, length, text)
        elif command[0] == "Substitute":
            old_el, new_el = command[1], command[2]
            text = substitute(old_el, new_el, text)

password = input()

password_reset(password)
