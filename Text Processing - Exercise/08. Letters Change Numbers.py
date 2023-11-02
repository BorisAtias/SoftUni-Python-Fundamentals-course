def first_letter(string):
    num = ""
    result = 0
    for i in string:
        if i.isnumeric():
            num += i
    if string[0].isupper():
        position = ord(string[0]) - 64
        result += int(num) / position

    elif string[0].islower():
        position = ord(string[0]) - 96
        result = int(num) * position
    result = last_letter(string, result)
    return result


def last_letter(string,result):


    if string[-1].isupper():
        position = ord(string[-1]) - 64
        result = result - position

    elif string[-1].islower():
        position = ord(string[-1]) - 96
        result = result + position

    return result


total = 0

text = [x for x in input().split()]

for word in text:
    total += first_letter(word)


print(f"{total:.2f}")
