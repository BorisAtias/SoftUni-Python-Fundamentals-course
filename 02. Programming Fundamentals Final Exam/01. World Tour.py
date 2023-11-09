def add_stop(index, new_stop, string):
    if index in range(len(string)):
        string = string[:index] + new_stop + string[index:]
    print(string)

    return string


def remove_stop(start_index, end_index, string):
    if start_index in range(len(string)) and end_index in range(len(string)):
        string = string[:start_index] + string[end_index + 1:]
    print(string)

    return string


def switch(old_el, new_el, string):
    if old_el in string:
        string = string.replace(old_el, new_el)
    print(string)

    return string


stops = input()
command = input().split(":")

while command[0] != "Travel":

    if command[0] == "Add Stop":
        index, string = int(command[1]), command[2]
        stops = add_stop(index, string, stops)
    elif command[0] == "Remove Stop":
        start, stop, = int(command[1]), int(command[2])
        stops = remove_stop(start, stop, stops)
    elif command[0] == "Switch":
        old_str, new_str = command[1], command[2]
        stops = switch(old_str, new_str, stops)

    command = input().split(":")

print(f"Ready for world tour! Planned stops: {stops}")
