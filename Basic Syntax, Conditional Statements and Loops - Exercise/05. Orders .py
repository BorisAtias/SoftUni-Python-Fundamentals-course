def order(num):
    total = 0
    for i in range(num):

        price_per_capsule = float(input())
        days = int(input())
        capsules_per_day = int(input())
        price = (price_per_capsule * capsules_per_day) * days
        if price_per_capsule < 0.01 or price_per_capsule > 100:
            continue
        elif days not in range(1, 31 + 1):
            continue
        elif capsules_per_day not in range(1, 2000 + 1):
            continue
        else:
            total += price
            print(f"The price for the coffee is: ${price:.2f}")
    print(f"Total: ${total:.2f}")
count = int(input())
order(count)
