start = input()
end = input()


def print_ascii(a, b):
    my_string = ''

    for i in range(ord(start) + 1, ord(end)):

        my_string += chr(i)


    print(' '.join(my_string))

print_ascii(start, end)
