def urgent(item, my_list):
    if item not in my_list:
        my_list.insert(0, item)
    return my_list

def unnecessary(item, my_list):
    if item in my_list:
        my_list.remove(item)
    return my_list

def correct(old_item, new_item, my_list):
    if old_item in my_list:
        my_list = [item.replace(old_item, new_item) for item in my_list]
    return my_list

def rearrange(item, my_list):
    if item in my_list:
        my_list.remove(item)
        my_list.append(item)

    return my_list

def final_print(my_list):
    print(*my_list, sep=", ")

groceries = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        final_print(groceries)
        break
    command = command.split()
    if command[0] == "Urgent":
        item = command[1]
        groceries = urgent(item, groceries)
    elif command[0] == "Unnecessary":
        item = command[1]
        groceries = unnecessary(item, groceries)
    elif command[0] == "Correct":
        old_el, new_el = command[1], command[2]
        groceries = correct(old_el, new_el, groceries)
    elif command[0] == "Rearrange":
        item = command[1]
        groceries = rearrange(item, groceries)
