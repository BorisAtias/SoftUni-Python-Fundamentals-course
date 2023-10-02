num = input().split()

def even_num():
    even_list = []

    for i in num:
        i = int(i)
        if i % 2 == 0:
            even_list.append(i)
    print(even_list)
even_num()
