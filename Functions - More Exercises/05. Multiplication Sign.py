a = int(input())
b = int(input())
c = int(input())

def multiply():

    if a > 0 and b > 0 and c > 0 \
            or a < 0 and b < 0 and c > 0 \
            or a < 0 and b > 0 and c < 0 \
            or a > 0 and b < 0 and c < 0:
        print("positive")

    elif a == 0 or b == 0 or c == 0:
        print("zero")

    elif a < 0 or b < 0 or c < 0:
        print('negative')

multiply()