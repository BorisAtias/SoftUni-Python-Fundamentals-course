import re
text = input()

pattern = r"(www.([A-Za-z0-9\-]+))(\.[a-z]+)+"

while text:

    matches = re.search(pattern, text)

    if matches:
        print(matches.group())

    text = input()
