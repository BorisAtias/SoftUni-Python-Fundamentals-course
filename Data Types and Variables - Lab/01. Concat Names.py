def contact_name(name, family_name, symbol):

    result = name + symbol + family_name

    print(result)

name = input()
last_name = input()
bond = input()

contact_name(name, last_name, bond)


# Second version

fist_name = input()
last_name = input()
delimiter = input()

print(f'{fist_name}{delimiter}{last_name}')