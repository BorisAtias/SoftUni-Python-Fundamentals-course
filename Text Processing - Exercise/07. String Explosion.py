text = input()

expl_power = 0
i = 0
while i < len(text):
    if text[i] == '>':
        expl_power += int(text[i + 1])
    else:
        if expl_power > 0:
            text = text[:i] + text[i + 1:]
            expl_power -= 1
            i -= 1
    i += 1

print(text)