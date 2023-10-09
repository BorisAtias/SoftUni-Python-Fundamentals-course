def rounding(values):

    res = []

    for i in values:

        i = float(i)
        res.append(round(i))
    return res

nums = input().split()

print(rounding(nums))