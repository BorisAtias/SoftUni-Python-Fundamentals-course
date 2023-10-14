my_string = input().split()
to_discard = int(input())

my_list = []

for el in my_string:
    my_list.append(int(el))


for i in range(to_discard):

    my_list.remove(min(my_list))

print(*my_list, sep=", ")