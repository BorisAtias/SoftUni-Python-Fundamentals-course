from math import floor
import re

text = input()
pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"

matches = re.finditer(pattern, text)
calories_needed = 2000
calories_total = 0
all_products = []
exp_dates = []
calories = []

for match in matches:

    all_products.append(match.group(2))
    exp_dates.append(match.group(3))
    calories.append(match.group(4))
    calories_total += int(match.group(4))

print(f"You have food to last you for: {floor(calories_total/calories_needed)} days!")

for element in range(len(all_products)):
    print(f"Item: {all_products[element]}, Best before: {exp_dates[element]}, Nutrition: {calories[element]}")