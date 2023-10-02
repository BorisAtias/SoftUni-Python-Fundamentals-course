num = input().split(', ')

def check_palindrome():

    for i in num:
        if i == i[::-1]:
            print(True)
        else:
            print(False)

check_palindrome()
