shopping_basket = {}

while True:

    command = input()

    if command == "buy":
        for key, value in shopping_basket.items():
            print(f'{key} -> {value[0] * value[1]:.2f}')
        break

    products = command.split()

    product = products[0]
    price = float(products[1])
    quantity = float(products[2])
    final_price = float(products[1]) * float(products[2])

    if product not in shopping_basket:
        shopping_basket[product] = product
        shopping_basket[product] = [price, quantity]
    else:
        shopping_basket[product][0] = price
        shopping_basket[product][1] += quantity
