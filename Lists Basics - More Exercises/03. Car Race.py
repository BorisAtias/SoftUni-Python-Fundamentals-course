sequence = input().split()

finish_line = len(sequence) // 2

racer_left = sequence[:finish_line]
racer_right = sequence[finish_line + 1:][::-1]

total_time_left = 0
total_time_right = 0

for i in racer_left:
    total_time_left += int(i)
    if i == '0':
        total_time_left -= total_time_left * 0.20

for i in racer_right:
    total_time_right += int(i)
    if i == '0':
        total_time_right -= total_time_right * 0.20

if total_time_left < total_time_right:
    print(f'The winner is left with total time: {total_time_left:.1f}')
else:
    print(f'The winner is right with total time: {total_time_right:.1f}')