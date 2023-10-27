import re

numbers = input()

pattern = r"[0-9]+"

result = []

while numbers:
    matches = re.findall(pattern, numbers)

    result.extend(matches)
    numbers = input()

print(" ".join(result))