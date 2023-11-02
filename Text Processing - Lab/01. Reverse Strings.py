while True:
    my_string = input()
    if my_string == 'end':
        break

    new_string = my_string[::-1]
    print(f'{my_string} = {new_string}')