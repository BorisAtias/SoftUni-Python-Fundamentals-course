num1 = int(input())
num2 = int(input())
num3 = int(input())

def the_smallest(a, b, c):

    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

print(the_smallest(num1, num2, num3))