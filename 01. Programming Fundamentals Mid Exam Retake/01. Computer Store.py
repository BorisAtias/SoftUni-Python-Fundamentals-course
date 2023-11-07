def sum_parts(parts_price, total, net_total):

    total += parts_price
    net_total += parts_price
    return total, net_total

def regular(total):

    tax = total * 0.20
    total = total + (total * 0.20)

    return final_print(total, tax, net_total)

def special(total):

    tax = total * 0.20
    total = (total + tax)
    total = total - (total * 0.10)

    return final_print(total, tax, net_total)

def final_print(final_price,tax,price):

    if final_price <= 0:
        print("Invalid order!")
    else:
        print(f"Congratulations you've just bought a new computer!"
              f"\nPrice without taxes: {price:.2f}$"
              f"\nTaxes: {tax:.2f}$"
              f"\n-----------"
              f"\nTotal price: {final_price:.2f}$")
        raise SystemExit


net_total = 0
total_bill = 0

while True:

    price = input().lower()
    if price == "regular":
        regular(net_total)
        break
    elif price == "special":
        special(total_bill)
        break

    price = float(price)
    if price < 0:
        print("Invalid price!")
        continue
    total_bill, net_total = sum_parts(price, total_bill,net_total)
