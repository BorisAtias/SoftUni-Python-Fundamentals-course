import re
text = input()
pattern = r"((?<=^_)|(?<=\s_))(?P<name>[A-Za-z0-9]+)\b"

matches = re.findall(pattern, text)
result = []
for i in matches:
    i = list(i)
    for j in i:
        if j == "":
            continue
        else:
            result.append(j)

print(",".join(result))
