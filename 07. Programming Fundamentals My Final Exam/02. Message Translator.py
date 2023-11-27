import re

msg_count = int(input())
pattern = r"!([A-Z]{1}[a-z]{2,})!:\[([A-Za-z]{8,})\]"

for i in range(msg_count):

    message = input()

    matches = re.findall(pattern, message)
    if len(matches) == 0:
        print("The message is invalid")
        continue
    else:
        cipher = [ord(x) for x in matches[0][1]]
        result = ""
        for i in cipher:
            if i != ",":
                result += str(i)
                result += " "
        print(f"{matches[0][0]}: {result}")
