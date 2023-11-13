import re
text = input()
pattern = r"(#|@)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"

matches = re.finditer(pattern, text)

counter = 0
mirror_words = ""

for match in matches:
    counter += 1
    a, b = match.group(2), match.group(3)
    if a == b[::-1]:
        mirror_words += a + " " + '<=>' + " " + b + ", "

mirror_words = mirror_words[:-2]

if counter == 0:
    print("No word pairs found!")
else:
    print(f"{counter} word pairs found!")
if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print(f"The mirror words are:\n{mirror_words}")

