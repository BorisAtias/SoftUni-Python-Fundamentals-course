num = int(input())

capacity = 255
water_filled = 0
leftover_capacity = capacity - water_filled

for i in range(num):
    leftover_capacity = capacity - water_filled

    water_income = int(input())

    if leftover_capacity < water_income:
        print("Insufficient capacity!")
        continue

    water_filled += water_income


print(water_filled)