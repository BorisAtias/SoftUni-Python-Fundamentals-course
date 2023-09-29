beginning = int(input())
end = int(input())

my_string = ''

for i in range(beginning, end + 1):
    my_string += chr(i)

print(' '.join(my_string), end='')