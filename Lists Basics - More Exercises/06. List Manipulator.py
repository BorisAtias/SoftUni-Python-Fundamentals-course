def exchange(index, my_list):
    if index in range(len(my_list)):
        my_list = my_list[index + 1::] + my_list[0:index + 1]
    else:
        print("Invalid index")

    return my_list

def max_even_odd(command, my_list):

    if command == "even":
        even_nums = [x for x in my_list if x % 2 == 0]
        if len(even_nums) == 0:
            print("No matches")
        else:
            res = max(even_nums)
            max_value = 0
            for index, value in enumerate(my_list):

                if value >= res and value % 2 == 0:
                    max_value = index
            print(max_value)

    elif command == "odd":
        odd_nums = [x for x in my_list if x % 2 != 0]
        if len(odd_nums) == 0:
            print("No matches")
        else:
            res = max(odd_nums)
            max_value = 0
            for index, value in enumerate(my_list):

                if value >= res and value % 2 != 0:
                    max_value = index
            print(max_value)

def min_even_odd(command, my_list):

    if command == "even":
        even_nums = [x for x in my_list if x % 2 == 0]
        if len(even_nums) == 0:
            print("No matches")
        else:
            res = min(even_nums)
            min_value = 0
            for index, value in enumerate(my_list):
                if value <= res and value % 2 == 0:
                    min_value = index
            print(min_value)

    elif command == "odd":
        odd_nums = [x for x in my_list if x % 2 != 0]
        if len(odd_nums) == 0:
            print("No matches")
        else:
            res = min(odd_nums)
            min_value = 0
            for index, value in enumerate(my_list):

                if value <= res and value % 2 != 0:
                    min_value = index
            print(min_value)

def first_even_odd(command, count, my_list):

    if command == "even":
        res = [x for x in my_list if x % 2 == 0]
        if count > len(my_list):
            print("Invalid count")
        else:
            print(res[0:count])
    elif command == "odd":
        res = [x for x in my_list if x % 2 != 0]
        if count > len(my_list):
            print("Invalid count")
        else:
            print(res[:count])

def last_even_odd(command, count, my_list):

    if command == "even":
        res = [x for x in my_list if x % 2 == 0]
        if count > len(my_list):
            print("Invalid count")
        else:
            print(res[-count::])
    elif command == "odd":
        res = [x for x in my_list if x % 2 != 0]
        if count > len(my_list):
            print("Invalid count")
        else:
            print(res[-count::])

my_list = [int(x) for x in input().split()]

breaker = input()

while breaker != "end":

    tokens = breaker.split()
    if tokens[0] == "exchange":
        index = int(tokens[1])
        my_list = exchange(index, my_list)

    elif tokens[0] == "max" and tokens[1] == "even" or tokens[0] == "max" and tokens[1] == "odd":
        command = tokens[1]
        max_even_odd(command, my_list)

    elif tokens[0] == "min" and tokens[1] == "even" or tokens[0] == "min" and tokens[1] == "odd":
        command = tokens[1]
        min_even_odd(command, my_list)

    elif tokens[0] == "first" and tokens[2] == "even" or tokens[0] == "first" and tokens[2] == "odd":
        count = int(tokens[1])
        command = tokens[2]
        first_even_odd(command, count, my_list)

    elif tokens[0] == "last" and tokens[2] == "even" or tokens[0] == "last" and tokens[2] == "odd":
        count = int(tokens[1])
        command = tokens[2]
        last_even_odd(command, count, my_list)

    breaker = input()
print(my_list)