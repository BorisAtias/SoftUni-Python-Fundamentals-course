def perfect_num(a):

    perfect_num = []

    for i in range(1, a + 1):
        if a % i == 0 and i != a:
            perfect_num.append(i)

    if sum(perfect_num) == a:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")

number = int(input())
perfect_num(number)