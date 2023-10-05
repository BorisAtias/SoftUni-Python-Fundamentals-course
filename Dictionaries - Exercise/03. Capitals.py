country = input().split(", ")
capital = input().split(", ")

zipped = zip(country, capital)

for i in zipped:

    print(f"{i[0]} -> {i[1]}")