product = input()
quantity = int(input())

def calc_price(el, piece):

    if el == 'coffee':
        return piece * 1.50
    elif el == 'water':
        return piece * 1.00
    elif el == 'coke':
        return piece * 1.40
    elif el == 'snacks':
        return piece * 2.00
print(f'{calc_price(product, quantity):.2f}')