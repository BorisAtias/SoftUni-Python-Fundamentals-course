import re

def rage_quit(string):
    a = string
    result = ""
    curr_str = ""
    counter = 0
    index_count = 0
    for index, value in enumerate(string):
        if index < index_count:
            continue
        if not value.isnumeric():
            curr_str += value.upper()
        else:
            index += 1
            index_count = index
            if index in range(len(string)) and a[index].isnumeric():
                index += 1
                index_count += 1

            num = re.findall(r"\d+", a)
            result += curr_str * int(num[counter])
            curr_str = ""
            counter += 1
    return f"Unique symbols used: {len(set(result))}\n{result}"

text = input()

print(rage_quit(text))