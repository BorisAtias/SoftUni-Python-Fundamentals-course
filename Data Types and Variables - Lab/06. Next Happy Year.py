def next_happy_year(year):

    while len(set(str(year))) != len(str(year)):
        year += 1
    print(year)

num = int(input()) + 1

next_happy_year(num)