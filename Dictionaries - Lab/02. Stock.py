def create(item, product):

    for i in range(0, len(item), 2):

        key = item[i]
        value = item[i + 1]
        product[key] = int(value)

    return product

def search(item, product):

    for i in item:

        if i not in product:
            print(f"Sorry, we don't have {i}")
        else:
            print(f"We have {product[i]} of {i} left")

products = {}

inventory = input().split()
to_search = input().split()

create(inventory, products)
search(to_search, products)