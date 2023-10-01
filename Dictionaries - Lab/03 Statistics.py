def inventory(item, quantity, products):

    if item not in products:
        products[item] = 0

    products[item] += quantity

    return products


def statistics(products):

    for key, value in products.items():
        print(f"- {key}: {value}")

products = {}

while True:

    command = input()

    if command == 'statistics':
        print("Products in stock:")
        statistics(products)
        print(f'Total Products: {len(products.keys())}')
        print(f"Total Quantity: {sum(products.values())}")
        break
    tokens = command.split(": ")
    item = tokens[0]
    quantity = int(tokens[1])
    products = inventory(item, quantity, products)
