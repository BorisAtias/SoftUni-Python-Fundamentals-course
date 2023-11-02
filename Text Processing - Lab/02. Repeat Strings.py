text = input().split()

my_string = ""

for word in text:

    my_string += word * len(word)

print(my_string)