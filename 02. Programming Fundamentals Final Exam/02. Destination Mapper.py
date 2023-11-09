import re
text = input()
dest_list = []
destinations = ""
pattern = r"(=|/)([A-Z][A-Za-z]{2,})\1"
matches = re.finditer(pattern, text)

for match in matches:
    destinations += match.group(2)
    dest_list.append(match.group(2))

print(f"Destinations: {', '.join(dest_list)}")
print(f"Travel Points: {len(destinations)}")
