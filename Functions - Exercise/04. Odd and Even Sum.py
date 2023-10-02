num = input()

even_list = []
odd_list = []

def sum_even_odd():
    for i in str(num):
        if int(i) % 2 == 0:
            even_list.append(int(i))
        else:
            odd_list.append(int(i))

    return (f"Odd sum = {sum(odd_list)}, Even sum = {sum(even_list)}")

print(sum_even_odd())
