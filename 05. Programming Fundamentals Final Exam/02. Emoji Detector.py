import re
text = input()

emoji_pattern = r"((?P<surround>[:]{2}|[\*]{2})(([A-Z])[a-z]{2,})(?P=surround))"
emoji_matches = re.finditer(emoji_pattern, text)

num_pattern = r"\d+"
num_matches = re.findall(num_pattern, text)

cool_threshold = 1
cool_emojis = []
emoji_count = 0
for i in num_matches:
    for text_emoji in i:
        text_emoji = int(text_emoji)

        cool_threshold = cool_threshold * text_emoji

for match in emoji_matches:
    emoji_count += 1
    full_emoji = match.group(1)
    text_emoji = match.group(3)
    sum = 0
    for i in text_emoji:

        value = ord(i)
        sum += value
    if sum >= cool_threshold:
        cool_emojis.append(full_emoji)

print(f"Cool threshold: {cool_threshold}\n{emoji_count} emojis found in the text. The cool ones are:")

for word in cool_emojis:
    print(f"{word}")