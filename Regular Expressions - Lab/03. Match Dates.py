import re
text = input()

regex = r"\b\d{2}/\b[A-Z]+[a-z]{2}/\d{4}|\d{2}-\b[A-Z]+[a-z]{2}-\d{4}|\d{2}.\b[A-Z]+[a-z]{2}.\d{4}"
matches = re.findall(regex,text)

for i in matches:

    if "/" in i and "-" in i:
        matches.remove(i)

for j in matches:

    print(f"Day: {j[0:2]}, Month: {j[3:6]}, Year: {j[7:11]}")