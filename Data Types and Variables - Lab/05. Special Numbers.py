def special_number(number):

    for i in range(1, number + 1):
        flag = False
        sum = 0
        for x in str(i):
            x = int(x)
            sum += x
        if sum == 5 or sum == 7 or sum == 11:
            flag = True

        print(f"{i} -> {flag}")

num = int(input())

special_number(num)
