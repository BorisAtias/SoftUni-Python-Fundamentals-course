def tell_the_num(number):

    if number == 0:
        print("zero")
    elif number > 0:
        if number < 1:
            print("small positive")
        elif number > 1000000:
            print("large positive")
        else:
            print("positive")
    else:
        if number > -1:
            print("small negative")
        elif number < -1000000:
            print("large negative")
        else:
            print("negative")

num = float(input())

tell_the_num(num)