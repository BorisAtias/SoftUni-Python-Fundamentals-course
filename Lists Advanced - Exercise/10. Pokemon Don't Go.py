def lower_than_zero(sequence, discarded):
    first_el = sequence[0]
    last_el = sequence[-1]
    sequence.pop(0)
    sequence.insert(0, last_el)
    discarded.append(first_el)
    for value in range(len(sequence)):
        if sequence[value] <= first_el:
            sequence[value] += first_el
        else:
            sequence[value] -= first_el

    return sequence, discarded


def higher_than_len(sequence, discarded):
    last_el = sequence[-1]
    first_el = sequence[0]
    sequence.pop(-1)
    sequence.append(first_el)
    discarded.append(last_el)
    for value in range(len(sequence)):
        if sequence[value] <= last_el:
            sequence[value] += last_el
        else:
            sequence[value] -= last_el

    return sequence, discarded


def all_other_cases(index, sequence, discarded):
    elem = sequence[index]
    sequence.pop(index)
    discarded.append(elem)
    for value in range(len(sequence)):
        if sequence[value] <= elem:
            sequence[value] += elem
        else:
            sequence[value] -= elem

    return sequence, discarded


my_list = [int(x) for x in input().split()]
discarded = []

while len(my_list) > 0:

    positions = int(input())

    if positions < 0:
        my_list, discarded = lower_than_zero(my_list, discarded)
    elif positions >= len(my_list):
        my_list, discarded = higher_than_len(my_list, discarded)
    else:
        my_list, discarded = all_other_cases(positions, my_list, discarded)

print(sum(discarded))