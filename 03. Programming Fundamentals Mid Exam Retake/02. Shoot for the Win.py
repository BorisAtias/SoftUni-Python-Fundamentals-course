sequence = list(map(int, input().split()))

while True:
    command = input()

    if command == 'End':
        break

    hits = int(command)

    if hits not in range(len(sequence)):
        continue

    precise_hit = sequence[hits]
    sequence[hits] = -1

    for i, value in enumerate(sequence):

        if value == - 1:
            continue

        if value > precise_hit:
            sequence[i] -= precise_hit

        elif value <= precise_hit:
            sequence[i] += precise_hit

        elif value == precise_hit:
            sequence[i] = -1

print(f"Shot targets: {sequence.count(-1)} -> {' '.join(map(str, sequence))}")
