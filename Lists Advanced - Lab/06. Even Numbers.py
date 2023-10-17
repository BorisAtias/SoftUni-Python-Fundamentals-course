num_list = list(map(int, input().split(", ")))

even_or_not = map(lambda x: x if num_list[x] % 2 == 0 else 'no', range(len(num_list)))

even_nums_index = list(filter(lambda a: a != 'no', even_or_not))
print(even_nums_index)