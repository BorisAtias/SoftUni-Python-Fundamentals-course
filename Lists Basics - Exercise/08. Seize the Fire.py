import re

fire_range = {"Low": range(1, 51), "Medium": range(51, 81), "High": range(81, 126)}

info = input().split("#")
water = int(input())

effort = 0
total_fire = 0

print("Cells:")
for cell in info:

    text = re.findall(r"[A-Za-z]+", cell)
    num = re.findall(r"\d+", cell)
    intensity = text[0]
    value = int(num[0])

    if value in fire_range[intensity]:
        if water >= value:
            print(f" - {value}")
            water -= value
            effort += value * 0.25
            total_fire += value

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")