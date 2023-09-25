def find_the_largest(string):
    result = []
    for i in string:
        result.append(i)
    result = sorted(result)
    print("".join(result[::-1]))

text = input()

find_the_largest(text)


# Second version

num = input()

my_list = []

for i in num:
    my_list.append(int(i))

my_list.sort()
final_result = my_list[::-1]

for j in final_result:
    print(j, end="")