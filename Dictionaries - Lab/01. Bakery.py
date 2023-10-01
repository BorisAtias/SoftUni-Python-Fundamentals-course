def bakery(item, product):

    for i in range(0, len(item), 2):

        key = item[i]
        value = item[i + 1]
        product[key] = int(value)

    return product

items = input().split()

products = {}

print(bakery(items, products))