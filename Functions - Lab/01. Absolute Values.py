def rounding(values):

    res = []
    for i in values:
        res.append(abs(float(i)))
    return res

nums = input().split()

print(rounding(nums))