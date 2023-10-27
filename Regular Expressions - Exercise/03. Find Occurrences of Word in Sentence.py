import re

text = input()
word = input()

pattern = fr'\b{word}\b'

matches = len(re.findall(pattern, text, re.I))

print(matches)