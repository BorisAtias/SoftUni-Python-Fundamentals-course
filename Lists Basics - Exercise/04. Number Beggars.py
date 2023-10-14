offers = [int(x) for x in input().split(", ")]
beggars_count = int(input())

beggars_list = [0] * beggars_count

for num in range(len(beggars_list)):

    current_beggar = num

    for n in range(len(offers)):
        current_num = n % beggars_count

        if current_num == current_beggar:
            if beggars_list[num] == 0:
                if offers[n] == 0:
                    beggars_list[current_num] = 0
                    break
                beggars_list[current_num] = offers[n]
            else:
                beggars_list[current_num] += offers[n]

print(beggars_list)
