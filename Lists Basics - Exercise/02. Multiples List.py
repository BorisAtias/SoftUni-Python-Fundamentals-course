start = int(input())
length = int(input())

my_list = []

for i in range(start, start * length + 1, start):
    my_list.append(i)

print(my_list)
