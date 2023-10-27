import re

total_price = 0
bought_furniture = []

while True:
    command = input()
    if command == "Purchase":
        break

    pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
    matches = re.search(pattern, command)

    if matches:
        product, price, quantity = matches.groups()
        bought_furniture.append(product)
        total_price += float(price) * int(quantity)

print("Bought furniture:")

for furniture in bought_furniture:
    print(furniture)

print(f'Total money spend: {total_price:.2f}')