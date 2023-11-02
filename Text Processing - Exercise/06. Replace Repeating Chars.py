text = input()

res = ""

for i in range(len(text)):

    if i + 1 == len(text) or text[i] != text[i + 1]:
        res += text[i]

print(res)
