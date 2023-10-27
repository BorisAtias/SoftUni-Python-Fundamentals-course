import re

text = input()

pattern = r'\s(([a-z]+[a-z\-\.\_]+)@([a-z\-]+)(\.[a-z]+)+)\b'

matches = re.findall(pattern, text)


for match in matches:
    print(match[0])