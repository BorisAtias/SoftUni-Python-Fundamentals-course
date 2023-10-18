num = int(input())

cells = []
n = 1
while num > 0:

    res = 0
    filler = 2 * (n * n)

    if filler > num:
        cells.append(num)
        break

    cells.append(filler)
    n += 1
    num -= filler

print(cells)