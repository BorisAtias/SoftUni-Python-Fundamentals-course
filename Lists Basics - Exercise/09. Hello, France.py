import re

market_cap = {"Clothes": 50.00, "Shoes": 35.00, "Accessories": 21.50}

items = input().split("|")
budget = float(input())

ticket_price = 150
selling_prices = []
profit = 0

for item in items:
    text = re.findall(r"[A-Za-z]+", item)
    num = re.findall(r"\d+.\d+|\d+", item)

    product = text[0]
    value = float(num[0])

    if product in market_cap and value <= market_cap[product]:
        if budget >= value:
            budget -= value
            selling_prices.append(f"{value * 1.40:.2f}")
            profit += (value * 1.40) - value

print(" ".join(selling_prices))
print(f"Profit: {profit:.2f}")
is_France = 0
for i in selling_prices:

    is_France += float(i)
if is_France + budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
