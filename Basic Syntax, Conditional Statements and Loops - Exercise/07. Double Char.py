def double_char(string):

    result = "".join(x * 2 for x in string)
    print(result)


while True:

    command = input()

    if command == "End":
        break
    elif command == "SoftUni":
        continue
    else:
        double_char(command)