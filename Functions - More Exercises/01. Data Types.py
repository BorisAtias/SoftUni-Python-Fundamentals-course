def data_types():

    command = input()
    variable = input()

    if command == 'int':
        variable = int(variable)
        return variable * 2

    if command == 'real':
        variable = float(variable)
        return (f'{variable * 1.5:.2f}')

    if command == 'string':
        return (f'${variable}$')

print(data_types())