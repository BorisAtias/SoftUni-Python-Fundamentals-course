def max_multiple(num, boundary):
    max_mult = 0
    for i in range(1, boundary + 1):

        if i > 0 and i % num == 0:
            max_mult = i
    print(max_mult)

divisor = int(input())
count = int(input())

max_multiple(divisor, count)