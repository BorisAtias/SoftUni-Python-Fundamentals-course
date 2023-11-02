words_to_ban = input().split(", ")
text = input()

for word in words_to_ban:
    while word in text:

        text = text.replace(word, "*" * len(word))

print(text)