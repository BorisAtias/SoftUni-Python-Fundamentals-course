n = int(input())

word = input()

my_list = []

for _ in range(n):

    current_word = input()
    my_list.append(current_word)

print(my_list)

for i in range(len(my_list) -1, -1, -1):
    element = my_list[i]

    if word not in element:
        my_list.remove(element)
print(my_list)