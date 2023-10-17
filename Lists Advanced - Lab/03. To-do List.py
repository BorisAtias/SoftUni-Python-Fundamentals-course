to_do_list = [0] * 10

while True:
    text = input()

    if text == 'End':
        break

    splitted_text = text.split("-")

    index = int(splitted_text[0]) - 1
    appointment = splitted_text[1]
    to_do_list.pop(index)
    to_do_list.insert(index,appointment)

result = [x for x in to_do_list if x != 0]
print(str(result))
