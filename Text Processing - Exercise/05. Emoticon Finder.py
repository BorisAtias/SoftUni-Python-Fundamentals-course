text = input()

res = ""
result = []
counter = 0

for i in text:
    if counter == 1:
        res += i
        res += " "
        counter = 0

    if i == ':':
        res += i
        counter += 1
res = res.split()

for i in res:
    result.append(i)

print(*result, sep="\n")
