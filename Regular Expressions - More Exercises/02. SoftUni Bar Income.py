import re

pattern = r"%([A-Z]{1}[a-z]+)%[^\|\$\.%]*<(\w+)>[^\|\$\.%]*\|[^\|\$\.%]*([1-9]+[0-9]*)[^\|\$\.%]*\|[^\|\$\.%]*([1-9]+[0-9]*\.?[0-9]*)[^\|\$\.%]*\$"
total_income = 0
while True:

    order = input()
    if order == "end of shift":
        print(f"Total income: {total_income:.2f}")
        break

    matches = re.finditer(pattern, order)

    for match in matches:
        client, drink = match.group(1), match.group(2)
        price = int(match.group(3)) * float(match.group(4))
        total_income += price
        print(f"{client}: {drink} - {price:.2f}")
