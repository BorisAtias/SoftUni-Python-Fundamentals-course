cities = int(input())

counter = 0
sunny_days = 0
total_profit = 0

for i in range(cities):

    city = input()
    money_earned = float(input())
    expenses = float(input())

    counter += 1
    sunny_days += 1

    if sunny_days % 5 == 0:
        money_earned *= 0.90
        sunny_days = 0

    elif counter % 3 == 0:
        expenses += (expenses * 0.50)
        counter = 0

    profit = money_earned - expenses
    total_profit += profit

    print(f"In {city} Burger Bus earned {money_earned - expenses:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")