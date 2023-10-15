my_string = input().split(", ")
my_list = []

for el in my_string:

    my_list.append(int(el))

for num in my_list:

    if num == 0:
        my_list.remove(num)
        my_list.append(num)

print(my_list)