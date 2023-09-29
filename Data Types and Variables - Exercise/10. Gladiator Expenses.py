lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
counter = 0
for x in range(1, lost_fights + 1):

    if x % 2 == 0:
        expenses += helmet_price
    if x % 3 == 0:
        expenses += sword_price
        if x % 2 == 0:
            expenses += shield_price
            counter += 1
    if counter == 2:
        expenses += armor_price
        counter = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")
